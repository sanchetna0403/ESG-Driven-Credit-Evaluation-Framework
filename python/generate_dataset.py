import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

states = [
    "Texas", "California", "Florida", "New York", "Ohio",
    "Illinois", "Georgia", "Arizona", "Washington", "Colorado"
]

data = []

for i in range(1, 501):

    revenue = random.randint(500000, 5000000)

    profit_margin = round(random.uniform(2, 25), 2)

    debt_to_equity = round(random.uniform(0.1, 1.2), 2)

    cash_flow = random.randint(-100000, 1000000)

    loan_amount = random.randint(100000, 1000000)

    recycling_volume = random.randint(100, 2000)

    utilization = random.randint(45, 95)

    collection_efficiency = random.randint(60, 98)

    co2_saved = random.randint(500, 8000)

    operational_cost = random.randint(
        int(revenue * 0.5),
        int(revenue * 0.95)
    )

    compliance = random.randint(60, 100)

    previous_default = random.choice(["Yes", "No"])

    score = (
        (100 - debt_to_equity * 50) * 0.4
        + (profit_margin * 3) * 0.3
        + (compliance) * 0.3
    )

    score = round(min(max(score, 20), 95), 0)

    if score >= 80:
        risk = "Low"
    elif score >= 60:
        risk = "Medium"
    else:
        risk = "High"

    data.append([
        f"C{i:03}",
        fake.company(),
        random.choice(states),
        random.randint(2, 20),
        random.randint(15, 250),
        revenue,
        profit_margin,
        debt_to_equity,
        cash_flow,
        loan_amount,
        recycling_volume,
        utilization,
        collection_efficiency,
        co2_saved,
        operational_cost,
        compliance,
        previous_default,
        score,
        risk
    ])

columns = [
    "Company_ID",
    "Company_Name",
    "State",
    "Years_Operation",
    "Employees",
    "Annual_Revenue_USD",
    "Profit_Margin_Pct",
    "Debt_to_Equity",
    "Cash_Flow_USD",
    "Loan_Amount_Requested_USD",
    "Monthly_Recycling_Tons",
    "Plant_Utilization_Pct",
    "Collection_Efficiency_Pct",
    "CO2_Saved_Tons",
    "Operational_Cost_USD",
    "Regulatory_Compliance_Score",
    "Previous_Default",
    "Credit_Score",
    "Risk_Category"
]

df = pd.DataFrame(data, columns=columns)

os.makedirs("../data", exist_ok=True)

df.to_excel(
    "data/recycling_credit_data.xlsx",
    index=False
)

print("Dataset created successfully!")
print("Rows:", len(df))
import pandas as pd

df = pd.read_excel("data/recycling_credit_data.xlsx")
print(df.shape)
