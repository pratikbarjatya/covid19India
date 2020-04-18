import papermill as pm

pm.execute_notebook(
   'Covid19India.ipynb',
   'Covid19IndiaOutput.ipynb',
   parameters = dict(alpha=0.1, ratio=0.1)
)
