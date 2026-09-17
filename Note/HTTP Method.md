# HTTP METHODS IN FASTAPI

In FastAPI, you can define routes that respond to different HTTP methods such as GET, POST, PUT, DELETE, etc. Each method corresponds to a specific type of operation that you want to perform on the server.

Here are some common HTTP methods and how to use them in FastAPI:

1. **GET**: Used to retrieve data from the server.

```pythonfrom fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
2. **POST**: Used to create new resources on the server.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```
3. **PUT**: Used to update existing resources on the server.

```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```
4. **DELETE**: Used to delete resources from the server.

```python
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id}
```
5. **PATCH**: Used to partially update existing resources on the server.

```python
@app.patch("/items/{item_id}")
async def patch_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```
In FastAPI, you can also use the `@app.api_route` decorator to define routes that can handle multiple HTTP methods. For example:

```python
@app.api_route("/items/{item_id}", methods=["GET", "PUT", "DELETE"])
async def item_handler(item_id: int):
    return {"item_id": item_id}
```
This allows you to handle different HTTP methods for the same endpoint, making your API more flexible and easier to maintain.

In summary, FastAPI provides a straightforward way to define routes for various HTTP methods, allowing you to create a robust and efficient API. You can use the appropriate method for each operation, ensuring that your API follows RESTful principles and is easy to understand for clients.

