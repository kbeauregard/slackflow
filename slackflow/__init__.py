import time

from .airflow import get_latest_runs, get_dag_run_status
from .models import (
    create_dag_run,
    update_dag_run_status,
    update_dag_run_slack,
    get_running_dags,
    DuplicateResourceError,
)
from .slack import post_message, update_message


def run_service():
    try:
        while True:
            dags = get_latest_runs()

            for dag in dags:
                dag_runs = get_dag_run_status(dag["dag_id"])
                for run in dag_runs[-1 * min(len(dag_runs), 10) :]:
                    try:
                        create_dag_run(
                            run["dag_id"],
                            run["dag_run_url"],
                            run["state"],
                            run["start_date"],
                        )
                        print(
                            f"Created dag run {run['dag_run_url']} with status {run['state']}"
                        )
                    except DuplicateResourceError:
                        update_dag_run_status(run["dag_run_url"], run["state"])
                        print(
                            f"Updated dag run {run['dag_run_url']} with status {run['state']}"
                        )

            dags = get_running_dags()
            for dag in dags:
                if dag["slack_id"]:
                    if dag["status"] != dag["notified_status"]:
                        update_message(
                            dag["dag_id"],
                            dag["slack_id"],
                            dag["status"],
                            dag["start_time"],
                        )
                        update_dag_run_slack(
                            dag["dag_run_url"], dag["slack_id"], dag["status"]
                        )
                        print(f"Updated slack message {dag['dag_id']}")
                else:
                    ts = post_message(dag["dag_id"], dag["status"], dag["start_time"])
                    update_dag_run_slack(dag["dag_run_url"], ts, dag["status"])
                    print(f"Created slack message {dag['dag_id']}")

            time.sleep(5)

    except KeyboardInterrupt:
        print("Good bye!")
