c.Spawner.args = [f'--NotebookApp.allow_origin={"*"}']
c.JupyterHub.tornado_settings = {
    'headers': {
        'Access-Control-Allow-Origin': '*',
    },
}



