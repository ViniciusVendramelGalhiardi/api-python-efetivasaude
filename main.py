from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from fastapi.openapi.utils import get_openapi 
from app.router import web, pgtoIugu, tokbox
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI(title='Efetiva Saúde')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Home"])
async def redirect():
    response = RedirectResponse(url='/docs')
    return response

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Efetiva Saúde V.10",
        version="2.5.0",
        description="",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(web.router_web)
app.include_router(pgtoIugu.router_pgto)
app.include_router(tokbox.router_tokbox)