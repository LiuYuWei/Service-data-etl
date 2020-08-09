"""Confusion matrix calculation service."""
# coding=utf-8
# import relation package.
import pandas as pd
import datetime
import json
import sqlite3
from sklearn.metrics import confusion_matrix

# import project package.
from config.config_setting import ConfigSetting
from src.dao.confusion_matrix_record_dao import ConfusionMatrixRecordDao


class ConfusionMatrixCalculationService:
    """Confusion matrix calculation service."""

    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger(
            "[Confusion_matrix_calculation_service]")
        self.config = config_setting.yaml_parser()
        self.confusion_matrix_record_dao = ConfusionMatrixRecordDao()
        self.confusion_matrix_record_dao.setting_confusion_matrix_database()

    def confusion_matrix_calculation(self, y_true, y_pred):
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        payload = {"number_data": len(y_true), "tp": int(tp), "fp": int(
            fp), "tn": int(tn), "fn": int(fn), "timestamp": datetime.datetime.now().isoformat()}
        self.confusion_matrix_record_dao.save_data(payload, "confusion_matrix")
        return payload
    
    def confusion_matrix_calculation_html(self, y_true, y_pred):
        y_true = pd.Series(y_true, name='Actual')
        y_pred = pd.Series(y_pred, name='Predicted')
        df_confusion = pd.crosstab(y_true, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)
        html = df_confusion.to_html()
        return html

    def accuracy_calculation(self, confusion_matrix):
        total_number = (confusion_matrix['tp'] + confusion_matrix['tn'] +
                        confusion_matrix['fp'] + confusion_matrix['fn'])
        accuracy = (confusion_matrix['tp'] +
                    confusion_matrix['tn']) / total_number
        payload = {"number_data": total_number, "accuracy_score": accuracy,
                   "cm_timestamp": confusion_matrix["timestamp"], "timestamp": datetime.datetime.now().isoformat()}
        self.confusion_matrix_record_dao.save_data(payload, "accuracy_score")
        return payload

    def precision_recall_calculation(self, confusion_matrix):
        total_number = (confusion_matrix['tp'] + confusion_matrix['tn'] +
                        confusion_matrix['fp'] + confusion_matrix['fn'])
        if (confusion_matrix['tp'] + confusion_matrix['fp']) != 0:
            precision = confusion_matrix['tp'] / \
                (confusion_matrix['tp'] + confusion_matrix['fp'])
        else:
            precision = -1

        if (confusion_matrix['tp'] + confusion_matrix['fn']) != 0:
            recall = confusion_matrix['tp'] / \
                (confusion_matrix['tp'] + confusion_matrix['fn'])
        else:
            recall = -1

        payload = {"number_data": total_number, "precision_score": precision, "recall_score": recall,
                   "cm_timestamp": confusion_matrix["timestamp"], "timestamp": datetime.datetime.now().isoformat()}
        self.confusion_matrix_record_dao.save_data(payload, "precision_recall_score")
        return payload
