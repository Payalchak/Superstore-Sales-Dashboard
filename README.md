# 📊 Superstore Sales Dashboard with Python & Power BI

An end-to-end Data Analytics project that combines **Python** and **Power BI** to analyze Superstore sales data, perform data preprocessing, generate business insights, create visualizations, and build an interactive dashboard.

---

# 📌 Project Overview

This project demonstrates a complete Data Analytics workflow using Python for data preparation and Power BI for interactive dashboard development.

The project focuses on analyzing Superstore sales performance, identifying business trends, and generating meaningful insights to support business decision-making.

---

# 🎯 Business Objectives

- Analyze sales and profit performance.
- Identify high-performing products and categories.
- Compare regional performance.
- Track monthly sales trends.
- Understand customer segments.
- Improve business decision-making using data.

---

# 🚀 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Power BI
- DAX
- Microsoft Excel

---

# 📂 Project Structure

```text
Superstore-Sales-Dashboard
│
├── data
│   ├── raw
│   │   └── Sample_Superstore.csv
│   │
│   └── processed
│       ├── Sample_Superstore_Cleaned.csv
│       ├── Sample_Superstore_Featured.csv
│       └── Sample_Superstore_Export.xlsx
│
├── notebooks
│
├── powerbi
│   └── Superstore Sales Dashboard.pbix
│
├── scripts
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   └── export_data.py
│
├── visualizations
│   ├── sales_distribution.png
│   ├── profit_distribution.png
│   ├── region_profit.png
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── heatmap.png
│   └── boxplot.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Dashboard KPIs

- Total Sales
- Total Profit
- Profit Margin (%)
- Month-over-Month (MoM) Growth

---

# 📈 Dashboard Features

- Monthly Sales Trend
- Profit Margin by Region
- Sales by Category
- Top Products Analysis
- Interactive Filters (Slicers)
- Business Insights
- Dynamic Dashboard

---

# 🐍 Python Workflow

The Python pipeline performs the following tasks before loading data into Power BI:

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Visualization
5. Excel Export
6. Power BI Dashboard Integration

---

# 📜 Python Scripts

| Script | Description |
|---------|-------------|
| data_cleaning.py | Cleans and preprocesses the raw dataset |
| eda.py | Performs Exploratory Data Analysis |
| feature_engineering.py | Creates additional business features |
| visualization.py | Generates charts automatically |
| export_data.py | Exports processed dataset to Excel |

---

# 🧹 Data Cleaning

The dataset is processed using Python to perform:

- Missing Value Analysis
- Duplicate Record Analysis
- Date Conversion
- Data Validation
- Data Type Verification

---

# 📊 Exploratory Data Analysis (EDA)

Python performs analysis on:

- Sales Performance
- Profit Performance
- Region-wise Sales
- Category-wise Sales
- Customer Segment Analysis
- Monthly Sales Trend

---

# ⚙ Feature Engineering

Additional business features created:

- Year
- Month
- Month Number
- Quarter
- Day
- Day Name
- Profit Margin (%)
- Sales Category
- Discount Category

---

# 📉 Generated Visualizations

Python automatically generates the following charts:

- Sales Distribution
- Profit Distribution
- Region-wise Profit
- Monthly Sales Trend
- Category-wise Sales
- Correlation Heatmap
- Sales Boxplot

All charts are stored inside the **visualizations/** folder.

---

# 📦 Output Files

Python generates:

- Sample_Superstore_Cleaned.csv
- Sample_Superstore_Featured.csv
- Sample_Superstore_Export.xlsx

---

# 💼 Business Insights

The analysis provides insights such as:

- High sales do not always generate high profit.
- Technology is the highest revenue-generating category.
- Regional sales performance varies significantly.
- Consumer segment contributes the highest revenue.
- Monthly sales fluctuate throughout the year.

---

# ▶ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python scripts/data_cleaning.py
python scripts/eda.py
python scripts/feature_engineering.py
python scripts/visualization.py
python scripts/export_data.py
```

---

# 📁 Dataset

Sample Superstore Dataset

---

# 🔮 Future Improvements

- Sales Forecasting
- Customer Segmentation
- SQL Database Integration
- Machine Learning Models
- Interactive Web Dashboard
- Real-Time Analytics

---

# 👨‍💻 Author

**Payal Chak**

MCA Student | Data Analytics Enthusiast

**Skills**

- Python
- Power BI
- Pandas
- Matplotlib
- Seaborn
- Microsoft Excel
- Data Cleaning
- Data Visualization
- Exploratory Data Analysis (EDA)

---

# ⭐ Project Highlights

- End-to-End Data Analytics Project
- Python + Power BI Integration
- Professional Folder Structure
- Automated Data Processing
- Automated Visualizations
- Business-Oriented Insights
- GitHub Portfolio Ready
- Data Analyst Interview Ready
