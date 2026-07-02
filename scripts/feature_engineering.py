from pathlib import Path
import pandas as pd

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "Sample_Superstore_Cleaned.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "Sample_Superstore_Featured.csv"

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

print("\nDataset Loaded Successfully.")
print(f"Shape : {df.shape}")

# =====================================================
# Date Features
# =====================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Month Number"] = df["Order Date"].dt.month
df["Quarter"] = df["Order Date"].dt.quarter
df["Day"] = df["Order Date"].dt.day
df["Day Name"] = df["Order Date"].dt.day_name()

print("\nDate Features Created.")

# =====================================================
# Profit Margin
# =====================================================

df["Profit Margin (%)"] = (
    (df["Profit"] / df["Sales"]) * 100
).round(2)

print("Profit Margin Created.")

# =====================================================
# Sales Category
# =====================================================

def sales_category(value):
    if value < 100:
        return "Low"
    elif value < 500:
        return "Medium"
    else:
        return "High"

df["Sales Category"] = df["Sales"].apply(sales_category)

print("Sales Category Created.")

# =====================================================
# Discount Category
# =====================================================

def discount_category(value):
    if value == 0:
        return "No Discount"
    elif value <= 0.2:
        return "Low Discount"
    else:
        return "High Discount"

df["Discount Category"] = df["Discount"].apply(discount_category)

print("Discount Category Created.")

# =====================================================
# Save Dataset
# =====================================================

df.to_csv(OUTPUT_FILE, index=False)

print("\nFeature Engineered Dataset Saved Successfully.")

print(OUTPUT_FILE)

print("\nFinal Shape :", df.shape)

print("\nFeature Engineering Completed Successfully.")