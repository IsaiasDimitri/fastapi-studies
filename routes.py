from fastapi import APIRouter

motorcycle_routes = APIRouter(prefix='/motorcycles')
client_routes = APIRouter(prefix='/clients')
mechanic_routes = APIRouter(prefix='/mechanics')
service_routes = APIRouter(prefix='/services')
quote_routes = APIRouter(prefix='/quotes') # TODO improve that name
service_order_routes = APIRouter(prefix='/service_orders')

@motorcycle_routes.get('/')
def get_all_motorcycles():
    return { 'motorcycles': 'a lot of motorcycles to repair...'}
