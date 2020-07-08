from slack import WebClient
from datetime import datetime

from .constants import SLACKCHANNEL, SLACKTOKEN

client = WebClient(token=SLACKTOKEN)


class Colors:
    success = "#22bb33"
    running = "#f2c744"
    failure = "#ff0033"


def build_message(dag_id: str, status: str, start: str):
    if status == "success":
        color = Colors.success
    elif status == "failed":
        color = Colors.failure
    else:
        color = Colors.running

    attachments = [
        {
            "mrkdwn_in": ["text"],
            "color": color,
            "title": dag_id,
            "text": status,
            "footer": "Started:",
            "ts": datetime.fromisoformat(start).timestamp(),
        }
    ]

    return {
        "text": "New DAG run started",
        "channel": SLACKCHANNEL,
        "attachments": attachments,
        "username": "Airflow",
        "icon_url": "https://airflow.apache.org/docs/stable/_images/pin_large.png",
    }


def post_message(dag_id: str, status: str, start: str):
    blocks = build_message(dag_id, status, start)

    response = client.api_call("chat.postMessage", data=blocks)

    return response["ts"]


def update_message(dag_id: str, ts: str, status: str, start: str):
    blocks = build_message(dag_id, status, start)

    client.api_call(
        "chat.update", data=blocks, params={"channel": SLACKCHANNEL, "ts": ts}
    )
