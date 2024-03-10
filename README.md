# Fetch Rewards Coding Exercise

## Submission
Please find the complete solution for the challenge in [submission.ipynb](submission.ipynb).

## Steps to load data in PostgreSQL database

Install psycopg2 for PostgreSQL using the following command:

```
pip install psycopg2
```
or
```
python -m pip install psycopg2
```

Create a database called `fetch_rewards` in PostgreSQL and update the credentials in [scripts/constants.py](scripts/constants.py).

Run the following script to create tables and load data:
```
cd scripts
python main.py
```

All creation and insertion scripts can be found at [scripts/sql/create](scripts/sql/create) and [scripts/sql/insert](scripts/sql/insert).