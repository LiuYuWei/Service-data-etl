"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import FastAPI

# import project package.
from config.config_setting import ConfigSetting
from src.blueprint.api_router import create_api_router

def create_app(unittest=False):
    """The function to creates the fastapi service."""
    # Initial config and log
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_app]")
    config = config_setting.yaml_parser()
    
    app = FastAPI()

    api_router = create_api_router()
    app.include_router(api_router, prefix="/api", tags=["api"])

    log.info("Start the fastapi service.")
    return app