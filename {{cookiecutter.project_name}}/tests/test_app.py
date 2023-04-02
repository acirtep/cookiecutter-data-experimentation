import duckdb
from {{cookiecutter.project_slug}}.app import get_data
from {{cookiecutter.project_slug}}.settings import DATA_LOCATION


def test_get_data():
    duckdb_conn = duckdb.connect()
    df = get_data(duckdb_conn, file=f'{DATA_LOCATION}/example_data.csv')
    assert df.shape[0] == 2
