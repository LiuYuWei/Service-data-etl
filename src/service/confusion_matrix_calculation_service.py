"""Confusion matrix calculation service."""
# coding=utf-8
# import relation package.
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
        self.setting_database()

    def setting_database(self):
        self.confusion_matrix_record_dao.create_connection()
        create_table_sql = """ CREATE TABLE IF NOT EXISTS confusion_matrix (
                                timestamp datetime PRIMARY KEY NOT NULL,
                                number_data integer NOT NULL,
                                tp integer NOT NULL,
                                fp integer NOT NULL,
                                tn integer NOT NULL,
                                fn integer NOT NULL);
                           """
        self.confusion_matrix_record_dao.create_table(create_table_sql)

    def confusion_matrix_calculation(self, y_true, y_pred):
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
        payload = {"number_data": len(y_true), "tp": int(tp), "fp": int(
            fp), "tn": int(tn), "fn": int(fn), "timestamp": datetime.datetime.now().isoformat()}
        self.confusion_matrix_record_dao.save_data(payload, "confusion_matrix")
        return payload
