import os
import pathlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from koroche.api import router
from koroche.applogger import AppLogger
from koroche.config import ConfigManager
from koroche.oneway.manager import OneWayManager, RedirectManager
from koroche.oneway.model import OneWay, Redirect
from koroche.user.manager import UserManager
from koroche.user.model import User
from uvicorn import run

fpath = pathlib.Path(__file__)
path = os.path.join(fpath.parent.parent, "configs", "test_config.yml")
ConfigManager.load_config(path)

app = FastAPI(
    debug=ConfigManager.app.debug,
    title="Koroche",
    version=ConfigManager.app.version,
    openapi_url=f"/api/{ConfigManager.app.api_version}/openapi.json",
    docs_url=f"/api/{ConfigManager.app.api_version}/docs",
)

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(router)


@app.on_event("startup")
def startup():
    """Startup function"""

    user_logger = AppLogger("User", ConfigManager.applog)
    UserManager.init(user_logger, User)

    redirect_logger = AppLogger("Redirect", ConfigManager.applog)
    RedirectManager.init(redirect_logger, Redirect)

    way_logger = AppLogger("OneWay", ConfigManager.applog)
    OneWayManager.init(way_logger, OneWay)


if __name__ == "__main__":
    run("app:app", host=ConfigManager.app.host, port=ConfigManager.app.port, reload=True)
