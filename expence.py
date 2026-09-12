"""
models/expense.py
Models for the expense request being evaluated.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ExpenseRequest(BaseModel):
    """The purchase a user wants to evaluate."""
    item_name: str
    amount: float
    category: str = "discretionary"     # essential | discretionary | luxury
    is_urgent: bool = False
    notes: Optional[str] = None
    image_path: Optional[str] = None    # path to receipt/screenshot image
    requested_at: datetime = None

    def __init__(self, **data):
        if "requested_at" not in data or data["requested_at"] is None:
            data["requested_at"] = datetime.now()
        super().__init__(**data)
