from fastapi import APIRouter
from koroche.config import ConfigManager

from .oneways import router as oneways_router

# from .users import router as users_router


router = APIRouter(prefix=f"/api/{ConfigManager.app.api_version}", tags=["api"])

# Temporary deprecated
# router.include_router(users_router)
router.include_router(oneways_router)
