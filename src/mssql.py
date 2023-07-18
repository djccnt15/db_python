import pymssql
from addict import Dict


def read(db: Dict, query: str):
    with pymssql.connect(f'{db.server}:{db.port}', db.user, db.password, db.database) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(query)
            return [row for row in cursor]


def db_commit(query: str, host: str, port: str, user: str, pw: str, db: str):
    with pymssql.connect(f'{host}:{port}', user, pw, db) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()