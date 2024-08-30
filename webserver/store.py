import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')

    print(r.status_code)
    print(r.text)
    print(type(r.text))
    print('Categorías:')  # Imprimir título de categorías
    categories = r.json()
    for category in categories:
        print(category['name'])