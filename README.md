
# OSP graphs

Graph visualizations for fields, schools, departments.

## Installation (OSX)

1. Install [brew](https://brew.sh/).

1. Install Postgres:

    `brew install postgres`

1. Start Postgres:

    `brew services start postgresql`

1. Create a Postgres database to house the OSP dump:

    `createdb osp_graphs`

1. Download a database dump of the V1 data. Source it in with:

    `pg_restore -d osp_graphs <path to dump> -vvv`

    This will take ~10 minutes. Ignore warnings about the "osp" role not existing, they don't matter.

1. Install pipenv:

    `brew install pipenv`

1. Clone this repo, change into the root directory, and create a virtual environment / install the dependencies:

    `pipenv install`

    (The first time, it might have to download a new version of Python, which could take a minute or two.)

## Run Jupyter notebooks

1. Install the local package:

    `pipenv install -e .`

1. Then, start the Jupyter notebook server with:

    `pipenv run jupyter notebook`

    This should automatically open a browser tab with the Jupyter interface, pointed at the project root. Click down into `notebooks`, and then open / create a notebook.
