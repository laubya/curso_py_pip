import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_list():
    return [1,2,3]

@app.get("/contact", response_class=HTMLResponse)
def list():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Estoy en una página con HTML</h1>
            <p> En algun momento aprenderé a pasarle los datos de la API</p>
        </body>
    </html>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()