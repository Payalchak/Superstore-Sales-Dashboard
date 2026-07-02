from pathlib import Path
import pandas as pd

# =====================================================
# Project Paths
# =====================================================
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "Sample_Superstore.csv"
PROCESSED_FOLDER = BASE_DIR / "data" / "processed"
PROCESSED_FOLDER.mkdir(exist_ok=True)

OUTPUT_FILE = PROCESSED_FOLDER / "Sample_Superstore_Cleaned.csv"



# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(RAW_FILE)

# =====================================================
# Basic Information
# =====================================================

print(f"\nRows, Columns : {df.shape}")

print("\nColumn Names:")
print(df.columns.tolist())

# =====================================================
# Missing Values
# =====================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(df.isnull().sum())

# =====================================================
# Duplicate Records
# =====================================================

duplicates = df.duplicated().sum()

print("\nDuplicate Records :", duplicates)
print("Duplicate removal skipped.")

# =====================================================
# Date Conversion
# =====================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDate Conversion Completed.")

# =====================================================
# Data Types
# =====================================================

print("\nData Types")

print(df.dtypes)

# =====================================================
# Save Clean Dataset
# =====================================================

df.to_csv(OUTPUT_FILE, index=False)

print("\nClean Dataset Saved Successfully.")

print(OUTPUT_FILE)

print("\nCleaning Completed Successfully.")