import requests
from slackflow.constants import AIRFLOWHOST

latest_runs = "/api/experimental/latest_runs"
dag_runs = "/api/experimental/dags/{dag_id}/dag_runs"

headers = {"Cache-Control": "no-cache", "Content-Type": "application/json"}


def get_latest_runs():
    resp = requests.get(AIRFLOWHOST + latest_runs, headers=headers, timeout=5)
    return resp.json()["items"]


def get_dag_run_status(dag_id):
    resp = requests.get(
        AIRFLOWHOST + dag_runs.format(dag_id=dag_id), headers=headers, timeout=5
    )
    return resp.json()
