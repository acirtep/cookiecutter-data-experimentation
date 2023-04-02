import streamlit as st
import duckdb
import plotly.express as px


def get_data(duckdb_conn):
    df = duckdb_conn.read_csv("/app/data/example_data.csv").df()
    return df


def get_bar_graph(df):
    fig = px.bar(df, x="x", y="y", title="Example of plotly chart")
    return fig


if __name__ == "__main__":
    st.title("Hello world!")
    session_duckdb_conn = duckdb.connect()
    df_data = get_data(duckdb_conn=session_duckdb_conn)
    st.text("Some example data")
    st.dataframe(df_data)
    px_fig = get_bar_graph(df=df_data)
    st.plotly_chart(px_fig)
