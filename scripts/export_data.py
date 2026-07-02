from pathlib import Path
import pandas as pd

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "Sample_Superstore_Featured.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "Sample_Superstore_Export.xlsx"

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("EXPORT DATA")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

# =====================================================
# Export to Excel
# =====================================================

df.to_excel(OUTPUT_FILE, index=False)

print("\nExcel Export Completed Successfully.")
print(OUTPUT_FILE)

print("\nRows :", len(df))
print("Columns :", len(df.columns))