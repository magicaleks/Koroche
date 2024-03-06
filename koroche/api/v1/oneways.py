from fastapi import APIRouter, Response
from koroche.api.v1.validation.oneway import CreateOneWay, UpdateOneWay
from koroche.oneway.manager import OneWayManager
from koroche.oneway.model import OneWay
import starlette.status as status

router = APIRouter(prefix="/oneways", tags=["oneways"])


@router.post("/create", response_model=OneWay, response_description="Create oneway")
def create_oneway(schema: CreateOneWay):
    """Create oneway"""

    way = OneWayManager.create(
        target=schema.target,
        is_temporary=schema.is_temporary,
        lifetime=schema.lifetime,
        user_uid=schema.user_uid,
        only_numbers=schema.only_numbers,
    )

    return way


@router.post("/update", response_description="Update oneway")
def update_oneway(schema: UpdateOneWay):
    """Update oneway"""

    OneWayManager.update(uid=schema.uid, alias=schema.alias)

    return Response(status_code=status.HTTP_200_OK)

@router.get("/{alias}", response_description="Redirect oneway")
def redirect_oneway(alias: str):
    """Redirect oneway"""

    link = OneWayManager.redirect(alias=alias)

    return {"url": link}
