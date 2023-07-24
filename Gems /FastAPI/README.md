### Fastapi 

Uvicorn is a fast ASGI server, built on uvloop and httptools. It currently supports HTTP/1.1 and WebSockets.

```
sudo apt-get update
sudo apt-get -y install uvicorn
```

```
pip install fastapi
```

```
pip install "uvicorn[standard]"
```

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

```
uvicorn main:app --reload
```

```
Go to http://localhost:8000/
```

### References:

https://realpython.com/fastapi-python-web-apis/



