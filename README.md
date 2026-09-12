# Financial-Assistant
Buy or Wait? — Alice's Financial Assistant
# 💰 Buy or Wait? — AI-Powered Financial Decision Agent

An AI-powered financial agent that decides whether a user can safely afford a requested expense — considering balance, recurring costs, income, payment plans, and personal spending habits.

---

## 🚀 Features

- ✅ Analyzes current balance vs. requested expense
- ✅ Accounts for recurring bills, pending payments, essential spending
- ✅ Considers confirmed income schedule
- ✅ Suggests installment/partial payment plans
- ✅ Identifies flexible expenses that can be reduced
- ✅ Personalized recommendations per user
- ✅ Supports text + image inputs (receipts, bank screenshots)
- ✅ Multi-turn conversational agent via Google Gemini

---

## 📁 Project Structure

```
buy-or-wait-agent/
├── README.md
├── requirements.txt
├── .env.example
├── main.py                    # Entry point (CLI interface)
├── app.py                     # Streamlit web UI
├── agent/
│   ├── __init__.py
│   ├── financial_agent.py     # Core AI agent logic
│   ├── decision_engine.py     # Affordability decision engine
│   ├── payment_planner.py     # Payment plan generator
│   └── prompt_templates.py    # Gemini prompt templates
├── models/
│   ├── __init__.py
│   ├── user_profile.py        # User financial profile
│   ├── expense.py             # Expense & transaction models
│   └── recommendation.py     # Output recommendation model
├── tools/
│   ├── __init__.py
│   ├── balance_tool.py        # Get current balance
│   ├── expense_tool.py        # Fetch recurring/pending expenses
│   ├── income_tool.py         # Fetch income schedule
│   ├── spending_analyzer.py   # Analyze spending patterns
│   └── image_parser.py        # Parse receipts/images via Gemini Vision
├── data/
│   ├── sample_user_alice.json # Sample user: careful saver
│   ├── sample_user_bob.json   # Sample user: spender
│   └── sample_user_carol.json # Sample user: installment-friendly
└── tests/
    ├── test_decision_engine.py
    ├── test_payment_planner.py
    └── test_agent.py
```

---

## ⚙️ Setup

### 1. Clone & Install

```bash
cd buy-or-wait-agent
pip install -r requirements.txt
```

### 2. Set API Key

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

Get a free key at: https://aistudio.google.com/app/apikey

### 3. Run CLI

```bash
python main.py
```

### 4. Run Web App

```bash
streamlit run app.py
```

---

## 📊 Output Fields Explained

| Field | Description |
|-------|-------------|
| `amount_safe_to_pay` | Max amount payable today without risk |
| `affordability_status` | `AFFORDABLE` / `AFFORDABLE_WITH_PLAN` / `WAIT` / `NOT_AFFORDABLE` |
| `recommended_payment_method` | `FULL` / `PARTIAL` / `INSTALLMENTS` / `WAIT` / `DO_NOT_PROCEED` |
| `payment_plan` | List of `{date, amount}` payment steps |
| `earliest_date_for_full_payment` | Earliest safe date to pay full amount |
| `spending_changes_needed` | Flexible expenses to cut/reduce |
| `decision_explanation` | Human-readable reasoning |

---

## 🧠 How the AI Agent Works

1. **User Input** → Parse expense amount + context
2. **Profile Load** → Load user's balance, bills, income, preferences
3. **Image Parsing** (optional) → Extract data from receipt/screenshot
4. **Forecast Engine** → Project cash flow for next 90 days
5. **Safety Check** → Ensure minimum balance is maintained
6. **Gemini AI** → Generate personalized explanation + payment plan
7. **Output** → Structured JSON recommendation

---

## 🎯 Interview Talking Points

- Agent uses **function calling** (tool use) pattern
- Decisions are **rule-based + AI-enhanced** (hybrid)
- **Personalization** via user profiles
- **Multi-modal** input (text + images)
- Handles **edge cases**: no income, negative balance, large purchase
