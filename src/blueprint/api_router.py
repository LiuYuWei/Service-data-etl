"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
# from fastapi import FastAPI
from fastapi import APIRouter

# import project package.
from config.config_setting import ConfigSetting
from src.util.health_check_information import HealthCheckInformation
from src.util.api_router_base_model import HealthCheckBaseModel

def create_api_router():
    """The function to creates the fastapi api router service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_app]")
    config = config_setting.yaml_parser()

    api_router = APIRouter()

    @api_router.get("/health_check", response_model=HealthCheckBaseModel)
    def health_check():
        """health_check: Check the service is working.
        Returns:
            json format: the health check content.
        """
        health_check_information = HealthCheckInformation()
        return health_check_information.get_health_check_content()
    
    return api_router
