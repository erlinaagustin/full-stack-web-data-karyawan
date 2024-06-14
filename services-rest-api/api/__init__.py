from fastapi import APIRouter

# import modul api
from .api import *

api_router = APIRouter()

api_router.include_router(api.router, prefix="/data-karyawan", tags=["Data Karyawan"])