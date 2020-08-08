"""Confusion matrix calculation app."""
# coding=utf-8
# import relation package.

# import project package.
from config.config_setting import ConfigSetting
from src.service.confusion_matrix_calculation_service import ConfusionMatrixCalculationService

class ConfusionMatrixCalculationApp:
    """Confusion matrix calculation app."""
    
    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger("[Confusion_matrix_calculation_app]")
        self.config = config_setting.yaml_parser()
        self.confusion_matrix_calculation_service = ConfusionMatrixCalculationService()
    
    def get_confusion_matrix(self, y_true, y_pred):
        payload = self.confusion_matrix_calculation_service.confusion_matrix_calculation(y_true, y_pred)
        return payload