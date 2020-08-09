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
        self.log = config_setting.set_logger(
            "[Confusion_matrix_calculation_app]")
        self.config = config_setting.yaml_parser()
        self.confusion_matrix_calculation_service = ConfusionMatrixCalculationService()

    def get_confusion_matrix(self, y_true, y_pred):
        payload = self.confusion_matrix_calculation_service.confusion_matrix_calculation(
            y_true, y_pred)
        return payload
    
    def get_confusion_matrix_html(self, y_true, y_pred):
        html = self.confusion_matrix_calculation_service.confusion_matrix_calculation_html(
            y_true, y_pred)
        return html

    def confusion_matrix_to_accuracy_value(self, confusion_matrix):
        payload = self.confusion_matrix_calculation_service.accuracy_calculation(
            confusion_matrix=confusion_matrix)
        return payload

    def prediction_to_accuracy_value(self, y_true, y_pred):
        confusion_matrix = self.get_confusion_matrix(y_true, y_pred)
        payload = self.confusion_matrix_to_accuracy_value(confusion_matrix)
        return payload

    def confusion_matrix_to_precision_recall_value(self, confusion_matrix):
        payload = self.confusion_matrix_calculation_service.precision_recall_calculation(
            confusion_matrix=confusion_matrix)
        return payload

    def prediction_to_precision_recall_value(self, y_true, y_pred):
        confusion_matrix = self.get_confusion_matrix(y_true, y_pred)
        payload = self.confusion_matrix_to_precision_recall_value(
            confusion_matrix)
        return payload
