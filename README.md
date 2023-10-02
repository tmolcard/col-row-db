# Database use case optimization

The objective of this project is to propose a use case illustrating some choices that a user can make in order to adapt a database to a specific use case.

The main themes addressed are:

- Indexing
- Partitioning
- Database orientation (Rows/Columns)

#### Setup Databases

Launch a local postgres and clickhouse database using environment variables as config.

```bash
cp .env_example .env
export $(grep -v '^#' .env | xargs)
make local_db_up
```

#### Setup Python

Create a new virtual environment.

```bash
virtualenv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

#### Initialize and make sure tables initialize properly

Run alembic migration.

```bash
alembic upgrade b1fe2784ca6f
```

Upload datasets

```bash
make upload_datasets_to_pg
make upload_datasets_to_ch
```

## Compare query executions

#### Measure query on Postgres execution time

Update and run ./source/usecase/time_query_pg.py

#### Add index

Run the following command in order to add index on title_basics(primary_title) and title_akas(title) and try to time queries again.

```bash
alembic upgrade ba3f0e134532
```

#### Measure query on Clickhouse execution time

Update and run ./source/usecase/time_query_ch.py