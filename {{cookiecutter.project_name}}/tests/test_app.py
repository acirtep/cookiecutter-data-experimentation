import os

import duckdb
from {{cookiecutter.project_slug}}.app import get_data


def test_get_data():
    path = os.path.dirname(os.path.realpath(__file__))
    duckdb_conn = duckdb.connect()
    df = get_data(duckdb_conn, file=f'{path}/../data/example_data.csv')
    assert df.shape[0] == 2