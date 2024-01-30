from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from koroche.oneway.manager import OneWayManager

router = APIRouter()

@router.get("/{alias}")
def redirect(alias: str):
    link = OneWayManager.redirect(alias)
    return RedirectResponse(link)
