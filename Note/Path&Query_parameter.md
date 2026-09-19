# Path & Query parameter in FastAPI

In FastAPI, you can define path parameters and query parameters to handle dynamic data in your API endpoints.

## Path Parameters
Path parameters are defined in the URL path and are used to capture values from the URL. They are specified using curly braces `{}` in the route definition.

For example, if you want to capture an `item_id` from the URL, you can define a path parameter like this:

```pythonfrom fastapi import FastAPI
app = FastAPI()
```
```python   
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
``` 
In this example, `{item_id}` is a path parameter that will capture the value from the URL. The `item_id` parameter in the function will be automatically converted to an integer.


# Path() 

In FastAPI, you can use the `Path()` function from the `fastapi` module to add additional validation and metadata to path parameters. This allows you to specify constraints such as minimum and maximum values, as well as provide descriptions for better documentation.

```python
from fastapi import FastAPI, Path
app = FastAPI()


@app.get("/items/{item_id}")

def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=1, le=100)):
    return {"item_id": item_id}
```


# HttpException 

In FastAPI, you can raise HTTP exceptions to return specific HTTP status codes and error messages when certain conditions are not met. This is done using the `HTTPException` class from the `fastapi` module.

```python
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 1 or item_id > 100:
        raise HTTPException(status_code=400, detail="Item ID must be between 1 and 100")
    return {"item_id": item_id}
```


# Query Parameters

Query parameters are defined in the URL after the `?` symbol and are used to capture additional data that is not part of the path. They are specified as key-value pairs in the URL.

For example, if you want to capture a `q` query parameter from the URL, you can define it like this:

```pythonfrom fastapi import FastAPI
app = FastAPI() 
@app.get("/items/")
def read_items(q: str = None):
    return {"q": q}
```
In this example, `q` is a query parameter that will capture the value from the URL. The `q` parameter in the function is optional and will default to `None` if not provided in the URL. You can access the query parameter by appending it to the URL like this: `/items/?q=searchterm`.
You can also define multiple query parameters in the same endpoint. For example:

```python
@app.get("/items/")
def read_items(q: str = None, limit: int = 10):
    return {"q": q, "limit": limit}
```
In this example, `q` is a query parameter for the search term, and `limit` is a query parameter that specifies the maximum number of items to return. Both parameters are optional, and you can access them in the URL like this: `/items/?q=searchterm&limit=5`.

# Query()
In FastAPI, you can use the `Query()` function from the `fastapi` module to add additional validation and metadata to query parameters. This allows you to specify constraints such as minimum and maximum values, as well as provide descriptions for better documentation.

```python
from fastapi import FastAPI, Query
app = FastAPI()         
@app.get("/items/")
def read_items(q: str = Query(None, title="Search query", min_length=3, max_length=50)):
    return {"q": q}
```