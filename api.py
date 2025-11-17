from fastapi import FastAPI

# import controllers here
from students.controller import router as table_name_router

#


def register_routes(app: FastAPI):
    # register controllers here
    app.include_router(prefix="/api/v1", tags=["table_name"], router=table_name_router)
