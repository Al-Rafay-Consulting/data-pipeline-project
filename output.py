import json

def save_output(total_sales, category_sales, monthly_sales, top_products, profit_by_category, region_sales):

    result = {
        "total_sales": float(total_sales),
        "category_sales": category_sales.to_dict(),
        "monthly_sales": {str(k): v for k, v in monthly_sales.items()},
        "top_products": top_products.to_dict(),
        "region_sales": region_sales.to_dict()
    }

    if profit_by_category is not None:
        result["profit_by_category"] = profit_by_category.to_dict()

    with open("output/result.json", "w") as f:
        json.dump(result, f, indent=4)