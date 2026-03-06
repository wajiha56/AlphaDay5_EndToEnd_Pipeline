"""
Alpha Day 5: End-to-End Automated Data Pipeline
Author: Wajiha
Description:
This script builds a complete automated pipeline that:
1. Reads raw CSV data
2. Cleans missing values and outliers
3. Stores the cleaned data in an SQLite database
4. Queries insights using SQL
5. Generates an automated BI chart
"""

# ==========================
# Import Required Libraries
# ==========================
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================
# Pipeline Start Message
# ==========================
print("\n--- Starting Alpha Automated Pipeline ---\n")


# =====================================================
# STEP 1: DATA INGESTION & CLEANING (The Data Surgeon)
# =====================================================
print("1. Ingesting and Cleaning Data...")

# Load the raw CSV dataset
df = pd.read_csv("broken_sales_data.csv")

# ------------------------------
# Handle Missing Sales Values
# ------------------------------
# Calculate median sales for Electronics category
electronics_median = df[df["Category"] == "Electronics"]["Sales"].median()

# Fill missing sales with median value
df["Sales"] = df["Sales"].fillna(electronics_median)

# ------------------------------
# Handle Missing Quantity Values
# ------------------------------
# Replace missing quantity with 1
df["Quantity"] = df["Quantity"].fillna(1)

# ------------------------------
# Fix Quantity Outliers
# ------------------------------
# If quantity is greater than 100, replace with Office category mean
office_mean_quantity = df[df["Category"] == "Office"]["Quantity"].mean()

df.loc[df["Quantity"] > 100, "Quantity"] = office_mean_quantity


# ==========================================
# STEP 2: DATABASE STORAGE (The Architect)
# ==========================================
print("2. Pushing Data to SQLite Database...")

# Create SQLite database connection
conn = sqlite3.connect("Alpha_Data_Warehouse.db")

# Store cleaned dataframe into SQL table
df.to_sql(
    "Cleaned_Sales",
    conn,
    if_exists="replace",   # Replace table if it already exists
    index=False
)


# ===============================================
# STEP 3: QUERY & VISUALIZATION (The Translator)
# ===============================================
print("3. Querying Insights and Generating Report...")

# SQL query to calculate total profit by category
query = """
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM Cleaned_Sales
GROUP BY Category
"""

# Execute query and load results into dataframe
profit_df = pd.read_sql_query(query, conn)

# Close database connection
conn.close()


# ===============================================
# STEP 4: CREATE EXECUTIVE BUSINESS CHART
# ===============================================

# Set seaborn theme
sns.set_theme(style="whitegrid")

# Create figure
plt.figure(figsize=(8, 5))

# Create bar chart
sns.barplot(
    data=profit_df,
    x="Category",
    y="Total_Profit",
    palette="magma"
)

# Chart title
plt.title(
    "Automated Report: Total Net Profit by Category",
    fontweight="bold"
)

# Y-axis label
plt.ylabel("Net Profit (PKR)")

# Zero baseline
plt.axhline(0, color="black", linewidth=1)


# ===============================================
# STEP 5: SAVE FINAL REPORT
# ===============================================
plt.savefig(
    "Automated_Profit_Report.png",
    dpi=300,
    bbox_inches="tight"
)

# Close plot
plt.close()


# ===============================================
# PIPELINE COMPLETE MESSAGE
# ===============================================
print("\n--- Pipeline Complete! ---")
print("Check your folder for the following outputs:")
print("1. Alpha_Data_Warehouse.db")
print("2. Automated_Profit_Report.png\n")