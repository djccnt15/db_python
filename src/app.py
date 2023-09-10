from pathlib import Path
import json

from addict import Dict

from settings.config import get_config

paths = get_config()["DIR"]


def get_db(db_info: str):
    with open(file=Path(paths.get("db_info")) / db_info) as f:
        db = Dict(json.load(f))
    return db


def get_query(query: str):
    with open(file=Path(paths.get("query")) / query) as f:
        q = f.read()
    return q
