"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# import project package.
from config.config_setting import ConfigSetting
from src.blueprint.api_router import create_api_router
from src.blueprint.confusion_matrix_router import create_confusion_matrix_router

def create_app(unittest=False):
    """The function to creates the fastapi service."""
    # Initial config and log
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_app]")
    config = config_setting.yaml_parser()
    
    app = FastAPI()

    api_router = create_api_router()
    app.include_router(api_router, prefix="/api", tags=["api"])

    confusion_matrix_router = create_confusion_matrix_router()
    app.include_router(confusion_matrix_router, prefix="/confusion_matrix", tags=["confusion_matrix"])

    log.info("Start the fastapi service.")
    return app