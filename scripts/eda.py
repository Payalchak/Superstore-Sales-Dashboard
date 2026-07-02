from pathlib import Path
import pandas as pd

# =====================================================
# Load Clean Dataset
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN_DATA = BASE_DIR / "data" / "processed" / "Sample_Superstore_Cleaned.csv"

df = pd.read_csv(CLEAN_DATA)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# =====================================================
# Basic Statistics
# =====================================================

print("\nDataset Shape")
print(df.shape)

print("\nNumerical Summary")
print(df.describe())

# =====================================================
# Total Sales
# =====================================================

print("\n" + "=" * 60)
print("TOTAL SALES")
print("=" * 60)

total_sales = df["Sales"].sum()

print(f"Total Sales : ${total_sales:,.2f}")

# =====================================================
# Total Profit
# =====================================================

print("\n" + "=" * 60)
print("TOTAL PROFIT")
print("=" * 60)

total_profit = df["Profit"].sum()

print(f"Total Profit : ${total_profit:,.2f}")

# =====================================================
# Region-wise Sales
# =====================================================

print("\n" + "=" * 60)
print("REGION WISE SALES")
print("=" * 60)

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)

# =====================================================
# Category-wise Sales
# =====================================================

print("\n" + "=" * 60)
print("CATEGORY WISE SALES")
print("=" * 60)

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print(category_sales)

# =====================================================
# Customer Segment Sales
# =====================================================

print("\n" + "=" * 60)
print("SEGMENT WISE SALES")
print("=" * 60)

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print(segment_sales)

# =====================================================
# Monthly Sales
# =====================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n" + "=" * 60)
print("MONTHLY SALES")
print("=" * 60)

print(monthly_sales)

# =====================================================
# Business Insights
# =====================================================

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(f"Highest Sales Region : {region_sales.idxmax()}")

print(f"Highest Sales Category : {category_sales.idxmax()}")

print(f"Highest Revenue Segment : {segment_sales.idxmax()}")

print(f"Average Profit : ${df['Profit'].mean():,.2f}")

print(f"Average Discount : {df['Discount'].mean():.2%}")

print("\nEDA Completed Successfully.")