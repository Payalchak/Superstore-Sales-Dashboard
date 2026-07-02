from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "processed" / "Sample_Superstore_Featured.csv"

OUTPUT_DIR = BASE_DIR / "visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("VISUALIZATION")
print("=" * 60)

df = pd.read_csv(DATA_FILE)

# =====================================================
# Sales Distribution
# =====================================================

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_distribution.png")
plt.close()

# =====================================================
# Profit Distribution
# =====================================================

plt.figure(figsize=(8,5))
plt.hist(df["Profit"], bins=30)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_distribution.png")
plt.close()

# =====================================================
# Region Wise Profit
# =====================================================

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar")
plt.title("Region Wise Profit")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "region_profit.png")
plt.close()

# =====================================================
# Monthly Sales
# =====================================================

monthly_sales = df.groupby("Month Number")["Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales.png")
plt.close()

# =====================================================
# Category Sales
# =====================================================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "category_sales.png")
plt.close()

# =====================================================
# Correlation Heatmap
# =====================================================

plt.figure(figsize=(8,6))
sns.heatmap(
    df[["Sales","Profit","Quantity","Discount"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "heatmap.png")
plt.close()

# =====================================================
# Sales Boxplot
# =====================================================

plt.figure(figsize=(6,5))
sns.boxplot(y=df["Sales"])
plt.title("Sales Boxplot")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "boxplot.png")
plt.close()

print("\nVisualizations Generated Successfully.")
print(OUTPUT_DIR)