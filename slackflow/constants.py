import os

AIRFLOWHOST = os.environ.get("AIRFLOW_HOST", "http://0.0.0.0:8080")
SLACKTOKEN = os.environ.get("SLACK_TOKEN")
if SLACKTOKEN is None:
    raise EnvironmentError(
        "Environment missing slack token, it can be set with `SLACK_TOKEN`"
    )
SLACKCHANNEL = os.environ.get("SLACK_CHANNEL")
if SLACKCHANNEL is None:
    raise EnvironmentError(
        "Environment missing slack channel, it can be set with `SLACK_CHANNEL`"
    )
