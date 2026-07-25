## Architecture

                 Shopify Admin API
                         │
                         ▼
                Python EL Pipeline
                         │
                         ▼
                DuckDB Data Warehouse
                         │
                         ▼
                dbt Transformations
         (Staging → Dimensions → Facts)
                         │
                         ▼
                 Power BI Dashboard
## Tech Stacks

Tool
and
Purpose

Python
for
Data ingestion from Shopify API

Shopify Admin API
for
Source system

DuckDB
for
Analytical database

dbt
for
Data transformation and modeling

Power BI
for
Dashboarding and visualization

Git
For 
Version control

## Project Structure
shopify-analytical-engineering/
│
├── ingestion/
│   ├── config.py
│   ├── shopify_client.py
│   ├── extract_products.py
│   ├── extract_customers.py
│   ├── extract_orders.py
│   └── load_duckdb.py
│
├── database/
│   └── shopify.duckdb
│
├── dbt_shopify/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   │       ├── dimensions/
│   │       └── facts/
│   └── dbt_project.yml
│
├── dashboards/
├── sql/
├── run_pipeline.py
├── requirements.txt
└── README.md

Data Pipeline

1. Extract

Python connects to the Shopify Admin API and extracts:

* Products
* Customers
* Orders

2. Load

The extracted data is loaded into DuckDB as raw tables:

* raw_products
* raw_customers
* raw_orders

3. Transform

dbt transforms the raw data into analytics-ready models.

Staging Layer

* stg_products
* stg_customers
* stg_orders

This layer:

* Renames columns
* Applies data types
* Standardizes field names
* Removes unnecessary API fields

Mart Layer

Dimension tables:

* dim_products
* dim_customers

Fact table:

* fct_orders

## Data Model
                 dim_customers
                        │
                        │
                        ▼
                  fct_orders
                        ▲
                        │
                        │
                  dim_products

## Features

* Shopify Admin API integration
* Modular Python ingestion pipeline
* DuckDB analytical warehouse
* dbt staging and mart models
* Analytics-ready star schema
* Automated data quality testing with dbt
* Power BI reporting layer

## Getting Started
git clone https://github.com/yourusername/shopify-analytical-engineering.git

cd shopify-analytical-engineering

### Create a virtual environment
python -m venv venv

source venv/bin/activate      # macOS/Linux

venv\Scripts\activate         # Windows

### Install dependencies
pip install -r requirements.txt

### Environmental files:
SHOP_NAME=your-shop-name
ACCESS_TOKEN=your-admin-api-token
API_VERSION=2025-01

### Run ingestion pipelines
python run_pipeline.py

### Run dbt
Navigate to dbt project
cd dbt_shopify

### Build all models
dbt run

### Run data quality tests
dbt test

### Generate documentations
dbt docs generate

## Launch documentation site
dbt docs serve

### Example Analytics

This project supports analyses such as:

* Total Revenue
* Revenue by Customer
* Orders Over Time
* Average Order Value (AOV)
* Customer Lifetime Value (CLV)
* Product Performance
* Revenue by Product Type
* Revenue by Vendor

### Author

<b>Samin C</b>

<i>GitHub</i>: https://github.com/saminyc

<i>LinkedIn</i>: https://linkedin.com/in/sychowdhury