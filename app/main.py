from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.db import init_db, get_session
from app.routes.motorcycles import motorcycle_routes
from app.routes.mechanics import mechanic_routes
from app.routes.clients import client_routes
from app.routes.quotes import quote_routes
from app.routes.service_orders import service_order_routes
from app.routes.services import service_routes


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=db_lifespan)

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