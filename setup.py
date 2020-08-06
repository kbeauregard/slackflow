import setuptools
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="slackflow",
    version="1.0.0",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="Slack notifications for airflow dags.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbeauregard/slackflow",
    packages=setuptools.find_packages(include=["slackflow*"]),
    py_modules=["slackflow.__init__"],
    keywords=["slack", "airflow"],
    scripts=["slackflow-run"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests==2.23.0", "slackclient==2.7.2", "pymongo==3.9.0"],
)
