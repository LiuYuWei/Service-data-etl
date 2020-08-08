"""Record confusion matrix dao"""
# coding=utf-8
# import relation package.
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# import project package.
from config.config_setting import ConfigSetting

class ConfusionMatrixRecordDao:
    """Record confusion matrix dao"""
    
    def __init__(self):
        """Initial variable and module"""
        config_setting = ConfigSetting()
        self.log = config_setting.set_logger("[Confusion_matrix_record_dao]")
        self.config = config_setting.yaml_parser()
        self.sqlite_engine = None
    
    def create_connection(self):
        """create a database connection to the SQLite database
        Returns:
            Successfully create connection or not.
        """
        result = False
        try:
            self.sqlite_engine = create_engine('sqlite:///{}'.format(self.config['sqlite']['file_path']), echo=False)
            result = True
        except Exception as e:
            self.log.error("Create conntection error: {}".format(e))
        return result

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        Arguments:
            create_table_sql: str, sql string.
        Returns:
            Successfully create table or not.
        """
        result = False
        try:
            result = True
            self.sqlite_engine.execute(create_table_sql)
        except Exception as e:
            self.log.error("Create table error: {}".format(e))
        return result
    
    def save_data(self, data_dict, table_name):
        df = pd.DataFrame.from_dict(data_dict, orient = 'index').T
        df.columns = data_dict.keys()
        df.to_sql(table_name, con=self.sqlite_engine, if_exists='append', index=False)