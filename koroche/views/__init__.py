from fastapi import APIRouter
from .oneways import router as oneways_router

router = APIRouter()

router.include_router(oneways_router)
