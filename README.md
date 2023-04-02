# cookiecutter-data-experimentation
Base repo for data experimentation with streamlit, plotly and duckdb

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
6. `docker compose up`
7. Go to http://0.0.0.0:port of choice 
8. A "hello world" Streamlit app is running ![hello_world_streamlit.png](hello_world_streamlit.png)

# How to link to git repo
``` 
echo "# demo-cookiecutter-data-experimentation" >> README.md
git init -b main
git add .
git commit -m "feat: initial setup from cookiecutter"
git remote add origin **git https link**
git push -u origin main
```
