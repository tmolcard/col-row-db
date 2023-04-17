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
alembic upgrade head
```

Reverse migration.

```bash
alembic downgrade -1
```
