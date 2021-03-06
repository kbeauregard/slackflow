# SlackFlow
[![Generic badge](https://img.shields.io/badge/python-3.7+-blue.svg)](https://shields.io/)
[![codecov](https://codecov.io/gh/kbeauregard/slackflow/branch/master/graph/badge.svg)](https://codecov.io/gh/kbeauregard/slackflow)
[![Generic badge](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)
![PyPI - Downloads](https://img.shields.io/pypi/dm/slackflow)


An airflow slack notification app

<img src="https://user-images.githubusercontent.com/38864919/86988569-888d2d80-c166-11ea-897e-24afbb263ec3.png" alt="example" width="300"/>

## Install
```
pip install slackflow
AIRFLOW_HOST=<host> SLACK_TOKEN=<your_token> SLACK_CHANNEL=<channel_id> slackflow-run
```

## Development

#### Setup

[Pip-tools](https://github.com/jazzband/pip-tools) is used to manage dependencies.

```
pip install pip-tools
pip-sync requirements.txt dev-requirements.txt
```

#### Codestyle and Linting

This project uses [Black](https://github.com/psf/black) to auto format code using [pre-commit](https://github.com/pre-commit/pre-commit) to enforce format before committing. [Flake8](https://gitlab.com/pycqa/flake8) is used for linting.
```
pre-commit install
```

#### Changing Requirements

production
1. update `setup.py`
2. run `pip-compile`

development
1. update `dev-requirements.in`
2. run `pip-compile dev-requirements.in`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
