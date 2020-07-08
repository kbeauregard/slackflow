from pymongo import MongoClient
from dataclasses import dataclass, asdict

db_name = "airflow_slacker"
dag_run_collection = "dag_runs"

db = MongoClient()[db_name]


@dataclass
class DAGRun:
    dag_id: str
    dag_run_url: str
    status: str
    start_time: str
    notified_status: str = ""
    slack_id: str = ""


class DuplicateResourceError(Exception):
    pass


def create_dag_run(dag_id, dag_run_url, status, start):
    col = db[dag_run_collection]
    dag_run = DAGRun(dag_id, dag_run_url, status, start)
    if not col.find_one({"dag_run_url": dag_run_url}):
        col.insert_one(asdict(dag_run))
    else:
        raise DuplicateResourceError("Duplicate dag run id.")


def update_dag_run_status(dag_run_url, status):
    col = db[dag_run_collection]
    col.update_one({"dag_run_url": dag_run_url}, {"$set": {"status": status}})


def update_dag_run_slack(dag_run_url, slack_id, slack_status):
    col = db[dag_run_collection]
    col.update_one(
        {"dag_run_url": dag_run_url},
        {"$set": {"slack_id": slack_id, "notified_status": slack_status}},
    )


def get_running_dags():
    col = db[dag_run_collection]
    return [
        dag_run
        for dag_run in col.find()
        if dag_run["notified_status"] not in ["success", "failed"]
    ]
