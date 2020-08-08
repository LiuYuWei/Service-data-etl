"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import APIRouter

# import project package.
from config.config_setting import ConfigSetting
from src.util.health_check_information import HealthCheckInformation
from src.util.api_router_base_model import HealthCheckBaseModel

def create_api_router():
    """The function to creates the fastapi api router service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_api_router]")
    config = config_setting.yaml_parser()

    user_router = APIRouter()
    health_check_information = HealthCheckInformation()

    @user_router.get("/health_check", response_model=HealthCheckBaseModel)
    def health_check():
        """health_check: Check the service is working.
        Returns:
            json format: the health check content.
        """
        return health_check_information.get_health_check_content()
    
    log.info("Successfully setting the api router.")
    return user_router
