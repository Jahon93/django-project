from fastapi import FastAPI, Response
import random
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 699},
    {"id": 3, "name": "iWatch", "price": 799},
]


@app.get("/")
def get_products():
    return products


@app.get('/search')
def get_by_category(name: str, response: Response):
    founded_products = [
        product for product in products if name.lower() in product['name'].lower()]

    if not founded_products:
        response.status_code = 404
        return "No Products Found"
    return founded_products if len(founded_products) > 1 else founded_products[0]
# http://127.0.0.1:8000/search?name=iWatch


@app.get("/{id}")
def get_by_id(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            return product
    # returns 404 if not found, if it isn't written it returns 200
    response.status_code = 404
    return "Product Not Found"


@app.post('/')
def create_product(new_product: Product, response: Response):
    product = new_product.dict()
    product['id'] = random.random()
    products.append(product)
    response.status_code = 201
    return product


@app.put('/{id}')
def edit_product(id: int, edited_product: Product, response: Response):
    for product in products:
        if product['id'] == id:
            product['name'] == edited_product.name
            product['price'] == edited_product.price
            response.status_code = 200
            return product
        else:
            response.status_code = 404
            return "Product Not Found"


@app.delete('/{id}')
def delete_product(id: int, response: Response):
    for product in products:
        if product['id'] == id:
            products.remove(product)
            response.status_code = 204
            return 'Product Successfully Deleted'
        else:
            response.status_code = 404
            return "Product Not Found"
