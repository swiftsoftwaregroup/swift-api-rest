from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

origins = [
    # local testing with Angular
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Web API
@app.get("/", tags=["Root"])
async def get_root():
    return {"message": "Swift API REST"}


@app.get("/ping", tags=["Root"])
async def ping():
    return "PONG"


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'ping' and 'root'


use_route_names_as_operation_ids(app)
