import pandas as pd


def transform_data(df):
    # 1. Total sales
    total_sales = df['Sales'].sum()

    # 2. Sales grouped by Category
    category_sales = df.groupby('Category')['Sales'].sum()

    # 3. Sales grouped by Order Date month
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

    # 4. Top 5 products by total sales
    top_products = df.groupby('Product Name')['Sales'].sum().nlargest(5)

    # 5. Total profit by Category
    profit_by_category = df.groupby('Category')['Profit'].sum()

    # 6. Total sales by Region
    region_sales = df.groupby('Region')['Sales'].sum()

    return total_sales, category_sales, monthly_sales, top_products, profit_by_category, region_sales
