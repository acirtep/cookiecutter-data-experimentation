# cookiecutter-data-experimentation
Base repo for data experimentation with streamlit, plotly and duckdb

## what does it generate
Will generate the needed setup for fast data experimentation:
1. Poetry configuration
2. Installation of streamlit, plotly and duckdb
3. In docker and with docker-compose
4. A simple app as an example
5. Pre-commit
6. Pytest

## for whom and why?
This cookie-cutter is intended to be the starting point for data experimentation.
The main use-case is focused on working with non-private data, which can easily be worked
with on local systems, for example data from the space, weather data and the likes.

If your use-case is about private data, I recommend avoid using the `data` folder the cookiecutter comes with.

## streamlit
Easy, out of the box, web application for data analytics: https://docs.streamlit.io/
Alternative:
- dash, https://dash.plotly.com/

## plotly
Graphing library, with better graphs than streamlit: https://plotly.com/python/

## duckdb
In-memory OLAP database: https://duckdb.org/docs/

# Acknowledgements
This cookiecutter is inspired from https://github.com/fpgmaas/cookiecutter-poetry .

# How to use
1. `pip install cookiecutter`
2. Inside the repository directory execute
```
cookiecutter https://github.com/acirtep/cookiecutter-data-experimentation.git
```
3. Go through the questions and add the port of choice for your application
4. Inside the repository directory make sure to use python > 3.11 `poetry env use ...`
5. Run `poetry install`
6. `docker compose up` or `streamlit run ./demo_cookiecutter_data_experimentation/app.py`
7. Go to http://0.0.0.0:port of choice 
8. A "hello world" Streamlit app is running ![hello_world_streamlit.png](hello_world_streamlit.png)

- for tests run locally `pytest -v`

# How to link to git repo
1. Create an empty repository on your git hosting, preferably with the same name as the project_name used above.
2. Follow the steps for an empty repository, from within the above directory
``` 
git init -b main
git add .
git commit -m "feat: initial setup from cookiecutter"
git remote add origin **git https link**
git branch --set-upstream-to=origin/main main
git push -u origin main
```

# To run pre-commit (after link to git)
1. `git remote set-head origin main`
2. `pre-commit install --hook-type commit-msg --hook-type pre-push`
3. `pre-commit run --all-files`
