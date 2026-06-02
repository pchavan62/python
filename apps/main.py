from fastapi import FastAPI, Request
from apps.mockdata import products

app = FastAPI()

@app.get("/")
def home():
    return 'Welcome to fastapi!'

@app.get("/contact")
def contact():
    return 'you can connect with us anytime.'


@app.get("/products")
def get_products():
    return products

### path param

@app.get("/product/{product_id}/{count}")
def get_product(product_id:int, count:int):

    print("URL Values:", product_id, count)
    for product in products:
        if product.get("id") == product_id and product.get("count") == count:
            return product
        
    return {
        "Error":"Product not found for this id."
    }

## Query Param

@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet": f"Hello {name}, Your age is {age}"
    }


## Query Param : if we have 100 params

@app.get("/greets")
def greet_users(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet": f"Hello {query_params.get("name")}, Your age is {query_params.get("age")} "
    }