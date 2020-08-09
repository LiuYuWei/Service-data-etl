"""Define fastapi input variable type."""
# import relation package.
from pydantic import BaseModel

# import project package.


class ConfusionMatrixBaseModel(BaseModel):
    """The input of change direction"""
    tp: int
    tn: int
    fp: int
    fn: int
    number_data: int
    timestamp: str

class YValueBaseModel(BaseModel):
    """The input of change direction"""
    y_true: list
    y_pred: list