import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\Kenzo\Documents\Visual Studio Code\Retail sales Data cleaning\retail_store_sales.csv")

category_to_item = (
    df.dropna(subset=["Item"])
      .groupby("Category")["Item"]
      .first()
)
mask = df["Item"].isna()
df.loc[mask, "Item"] = df.loc[mask, "Category"].map(category_to_item)


item_price_per_item= (
    df.dropna(subset=["Price Per Unit"])
    .groupby("Item")["Price Per Unit"]
    .first()
)
mask = df["Price Per Unit"].isna()
df.loc[mask, "Price Per Unit"] = df.loc[mask, "Item"].map(item_price_per_item)


df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
df["Transaction Year"] = df["Transaction Date"].dt.year
df["Transaction Month"] = df["Transaction Date"].dt.month_name().str[:3]
df["Transaction day"] = df["Transaction Date"].dt.day


df["Total"] = df["Price Per Unit"] * df["Quantity"]
mask_error = ~np.isclose(df["Total Spent"], df["Total"], atol=0.01)
df.loc[mask_error, "Total Spent"] = df.loc[mask_error, "Total"]

df = df.dropna(subset=["Total Spent"])

df.to_csv("corregido.csv", index=False)
