from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index(q: str = None):
    return {
        'id': 1,
        'message': 'a pretty message',
        'q': q
    }