"""This file creates the fastapi service."""
# coding=utf-8
# import relation package.
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

# import project package.
from config.config_setting import ConfigSetting
from src.app.confusion_matrix_calculation_app import ConfusionMatrixCalculationApp
from src.util.confusion_matrix_router_base_model import ConfusionMatrixBaseModel

def create_confusion_matrix_router():
    """The function to creates the fastapi api router service."""5
    config_setting = ConfigSetting()
    log = config_setting.set_logger("[create_confusion_matrix_router]")
    config = config_setting.yaml_parser()

    user_router = APIRouter()
    confusion_matrix_calculation_app = ConfusionMatrixCalculationApp()

    @user_router.post("/json/confusion_matrix")
    def calculate_confusion_matrix(y_true: list, y_pred: list):
        if len(y_true) > 0 and len(y_pred) > 0 and len(y_true) == len(y_pred):
            payload = confusion_matrix_calculation_app.get_confusion_matrix(y_true, y_pred)
        else:
            payload = {"message": "Length error."}
        return payload
    
    @user_router.post("/html/confusion_matrix", response_class=HTMLResponse)
    def calculate_confusion_matrix_html(y_true: list, y_pred: list):
        if len(y_true) > 0 and len(y_pred) > 0 and len(y_true) == len(y_pred):
            confusion_matrix_calculation_app.get_confusion_matrix(y_true, y_pred)
            html = confusion_matrix_calculation_app.get_confusion_matrix_html(y_true, y_pred)
        else:
            html = {"message": "Length error."}
        return html

    @user_router.post("/json/accuracy_score")
    def calculate_accuracy_score(confusion_matrix: ConfusionMatrixBaseModel):
        payload = confusion_matrix_calculation_app.confusion_matrix_to_accuracy_value(confusion_matrix.dict())
        return payload
    
    @user_router.post("/json/prediction_accuracy")
    def calculate_prediction_accuracy(y_true: list, y_pred: list):
        if len(y_true) > 0 and len(y_pred) > 0 and len(y_true) == len(y_pred):
            payload = confusion_matrix_calculation_app.prediction_to_accuracy_value(y_true, y_pred)
        else:
            payload = {"message": "Length error."}
        return payload
    
    @user_router.post("/json/precision_recall_score")
    def calculate_precision_recall_value(confusion_matrix: ConfusionMatrixBaseModel):
        payload = confusion_matrix_calculation_app.confusion_matrix_to_precision_recall_value(confusion_matrix.dict())
        return payload
    
    @user_router.post("/json/prediction_precision_recall")
    def calculate_prediction_precision_recall(y_true: list, y_pred: list):
        if len(y_true) > 0 and len(y_pred) > 0 and len(y_true) == len(y_pred):
            payload = confusion_matrix_calculation_app.prediction_to_precision_recall_value(y_true, y_pred)
        else:
            payload = {"message": "Length error."}
        return payload

    log.info("Successfully setting the api router.")
    return user_router
