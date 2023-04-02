import duckdb
from {{cookiecutter.project_slug}}.app import get_data


def test_get_data():
    duckdb_conn = duckdb.connect()
    df = get_data(duckdb_conn)
    assert df.count() == 2
