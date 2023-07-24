### Fastapi 

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



