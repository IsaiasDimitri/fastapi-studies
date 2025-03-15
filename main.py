from fastapi import FastAPI
from routes import (
    motorcycle_routes,
    mechanic_routes,
    client_routes,
    quote_routes,
    service_order_routes,
    service_routes
)

app = FastAPI()

app.include_router(motorcycle_routes)
app.include_router(mechanic_routes)
app.include_router(client_routes)
app.include_router(quote_routes)
app.include_router(service_order_routes)
app.include_router(service_routes)

@app.get("/")
def index(q: str = None):
    return {
        'id': 1,
        'message': 'a pretty message',
        'q': q
    }