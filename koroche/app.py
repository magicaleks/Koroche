import os
import pathlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from koroche.api.v1 import router
from koroche.applogger import AppLogger
from koroche.config import ConfigManager
from koroche.data import AppHttpClient
from koroche.oneway.manager import OneWayManager, RedirectManager
from koroche.user.manager import UserManager
from uvicorn import run

fpath = pathlib.Path(__file__)
path = os.path.join(fpath.parent, "configs", "config.yml")
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

app.include_router(router, prefix="/api")


@app.on_event("startup")
def startup():
    """Startup function"""

    # user_logger = AppLogger("User", ConfigManager.applog)
    # UserManager.init(user_logger)

    # redirect_logger = AppLogger("Redirect", ConfigManager.applog)
    # RedirectManager.init(redirect_logger)
    api_client_logger = AppLogger("ApiClient", ConfigManager.applog)

    client = AppHttpClient(api_client_logger)

    way_logger = AppLogger("OneWay", ConfigManager.applog)
    OneWayManager.init(way_logger, client)


if __name__ == "__main__":
    run("app:app", host=ConfigManager.app.host, port=ConfigManager.app.port, reload=True)
