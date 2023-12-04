from fastapi import APIRouter

from .oneways import router as oneways_router

# from .users import router as users_router


router = APIRouter(prefix="/v1", tags=["api"])

# Temporary deprecated
# router.include_router(users_router)
router.include_router(oneways_router)
