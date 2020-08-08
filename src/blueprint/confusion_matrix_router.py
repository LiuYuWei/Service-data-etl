"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import APIRouter

# import project package.
from config.config_setting import ConfigSetting
from src.app.confusion_matrix_calculation_app import ConfusionMatrixCalculationApp


def create_confusion_matrix_router():
    """The function to creates the fastapi api router service."""
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_confusion_matrix_router]")
    config = config_setting.yaml_parser()

    user_router = APIRouter()
    confusion_matrix_calculation_app = ConfusionMatrixCalculationApp()

    @user_router.get("/json/confusion_matrix")
    def get_confusion_matrix():
        y_true = [1,1,0,0]
        y_pred = [1,0,1,0]
        payload = confusion_matrix_calculation_app.get_confusion_matrix(y_true, y_pred)
        return payload

    
    log.info("Successfully setting the api router.")
    return user_router
