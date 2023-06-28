import pymssql
from addict import Dict


def read(db: Dict, query: str):
    with pymssql.connect(f'{db.server}:{db.port}', db.user, db.password, db.database) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(query)
            return [row for row in cursor]