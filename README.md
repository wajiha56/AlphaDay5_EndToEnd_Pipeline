# Automated Sales Intelligence Pipeline

Author: Wajiha  
Role: Data Analyst & Junior AI Engineer  
Location: Pakistan

## Executive Summary

This project demonstrates an automated end-to-end data pipeline built in Python.  
The system ingests messy raw sales data, performs automated data cleaning and imputation, stores the processed data inside a local SQLite database, and generates business intelligence visualizations.

The entire workflow runs automatically using a single Python script.

## Tech Stack

Python  
Pandas  
SQLite  
Matplotlib  
Seaborn

## Pipeline Workflow

1. Raw CSV data is ingested.
2. Missing values are automatically cleaned and imputed.
3. Data is stored inside an SQLite data warehouse.
4. SQL queries extract business insights.
5. Seaborn generates automated visual reports.

## Business Impact

This pipeline helps organizations:

• eliminate manual Excel reporting  
• reduce human error  
• generate insights instantly

## How to Run

Install dependencies

pip install pandas matplotlib seaborn

Run the pipeline

python AlphaDay5_MasterPipeline.py
