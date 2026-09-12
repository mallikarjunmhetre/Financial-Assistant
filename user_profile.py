"""
models/user_profile.py
User financial profile — balance, income, expenses, preferences.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class RecurringExpense(BaseModel):
    """A bill or subscription paid regularly."""
    name: str                        # e.g. "Netflix", "Rent"
    amount: float
    due_day: int                     # day of month (1-31)
    category: str                    # "essential" | "flexible"
    description: Optional[str] = None


class PendingPayment(BaseModel):
    """A one-time upcoming payment."""
    name: str
    amount: float
    due_date: date
    is_essential: bool = True


class IncomeEntry(BaseModel):
    """A confirmed income event."""
    source: str                      # e.g. "Salary", "Freelance"
    amount: float
    expected_date: date
    is_confirmed: bool = True


class PaymentPreference(BaseModel):
    """User's preferences for payments."""
    preferred_method: str = "FULL"   # FULL | INSTALLMENTS | PARTIAL
    max_installments: int = 3
    min_balance_buffer: float = 500  # minimum cash to keep at all times
    risk_tolerance: str = "LOW"      # LOW | MEDIUM | HIGH


class UserProfile(BaseModel):
    """Complete financial profile of a user."""
    user_id: str
    name: str
    current_balance: float
    currency: str = "INR"
    recurring_expenses: List[RecurringExpense] = Field(default_factory=list)
    pending_payments: List[PendingPayment] = Field(default_factory=list)
    income_schedule: List[IncomeEntry] = Field(default_factory=list)
    preferences: PaymentPreference = Field(default_factory=PaymentPreference)
    monthly_essential_spend: float = 0.0   # avg essential (groceries, bills)
    monthly_flexible_spend: float = 0.0    # avg flexible (dining, shopping)

    def total_monthly_fixed_outflow(self) -> float:
        """Sum of all recurring expenses per month."""
        return sum(e.amount for e in self.recurring_expenses)

    def upcoming_essential_outflow(self, days: int = 30) -> float:
        """Essential outflows due in next `days` days."""
        from datetime import datetime, timedelta
        today = datetime.today().date()
        cutoff = today + timedelta(days=days)
        total = 0.0
        for p in self.pending_payments:
            if p.is_essential and today <= p.due_date <= cutoff:
                total += p.amount
        # Add essential recurring (pro-rata not needed, add all for month)
        total += sum(
            e.amount for e in self.recurring_expenses
            if e.category == "essential"
        )
        total += self.monthly_essential_spend
        return total

    def confirmed_income_next_days(self, days: int = 30) -> float:
        """Sum of confirmed income arriving in next `days` days."""
        from datetime import datetime, timedelta
        today = datetime.today().date()
        cutoff = today + timedelta(days=days)
        return sum(
            i.amount for i in self.income_schedule
            if i.is_confirmed and today <= i.expected_date <= cutoff
        )
