# SlackFlow
[![Generic badge](https://img.shields.io/badge/python-3.7+-blue.svg)](https://shields.io/)
[![codecov](https://codecov.io/gh/kbeauregard/slackflow/branch/master/graph/badge.svg)](https://codecov.io/gh/kbeauregard/slackflow)
[![Generic badge](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)


An airflow slack notification app

<img src="https://user-images.githubusercontent.com/38864919/86988569-888d2d80-c166-11ea-897e-24afbb263ec3.png" alt="example" width="300"/>

## Install
```
pip install slackflow
AIRFLOW_HOST=<host> SLACK_TOKEN=<your_token> SLACK_CHANNEL=<channel_id> slackflow-run
```

## Development

#### Setup

```
pip install -r requirements
pre-commit install
```
