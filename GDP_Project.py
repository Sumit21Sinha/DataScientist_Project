import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def clean_dataset(df, name):
    df = df.drop(df.columns[1:24], axis=1)
    if df.columns[-1].startswith("Unnamed"):
        df = df.drop(df.columns[-1], axis=1)
    df.iloc[:, 1:] = df.iloc[:, 1:].interpolate(method="linear", axis=1)
    df.iloc[:, 1:] = df.iloc[:, 1:].bfill(axis=1).ffill(axis=1)
    df = df.dropna(how="all", subset=df.columns[1:])
    print(f"\n{name} dataset after cleaning:\n", df.head())
    return df

current_gdp = pd.read_csv("Current_GDP.csv", sep=",", on_bad_lines="skip")
inflation = pd.read_csv("Inflation.csv", sep=",", on_bad_lines="skip")
unemployment = pd.read_csv("Unemployment.csv", sep=",", on_bad_lines="skip")
population = pd.read_csv("Population.csv", sep=",", on_bad_lines="skip")
growth_gdp = pd.read_csv("GDP_growth.csv", sep=",", on_bad_lines="skip")

print(growth_gdp.info())
print(inflation.columns)
print(current_gdp.isnull().sum())

current_gdp = clean_dataset(current_gdp, "Current GDP")
inflation = clean_dataset(inflation, "Inflation")
unemployment = clean_dataset(unemployment, "Unemployment")
population = clean_dataset(population, "Population")
growth_gdp = clean_dataset(growth_gdp, "GDP Growth")

current_gdp = current_gdp.melt(id_vars=["Country Name"], var_name="Year", value_name="Current GDP")
inflation = inflation.melt(id_vars=["Country Name"], var_name="Year", value_name="Inflation")
unemployment = unemployment.melt(id_vars=["Country Name"], var_name="Year", value_name="Unemployment")
population = population.melt(id_vars=["Country Name"], var_name="Year", value_name="Population")
growth_gdp = growth_gdp.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP Growth")

final_df = current_gdp.merge(inflation, on=["Country Name", "Year"], how="inner")
final_df = final_df.merge(unemployment, on=["Country Name", "Year"], how="inner")
final_df = final_df.merge(population, on=["Country Name", "Year"], how="inner")
final_df = final_df.merge(growth_gdp, on=["Country Name", "Year"], how="inner")

print("\nFinal merged dataset:\n", final_df.head())
final_df["Year"] = final_df["Year"].astype(int)
print(final_df.info())
print(final_df)

# sns.heatmap(final_df[["Current GDP", "Inflation", "Unemployment", "Population", "GDP Growth"]].corr(),
#             annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Correlation between Economic Indicators")
# plt.show()
#
# countries = ["India", "United States", "China", "Japan", "Germany", "Pakistan"]
# for country in countries:
#     countryData = final_df[final_df["Country Name"] == country]
#     plt.plot(countryData["Year"], countryData["Current GDP"]/1e12, label=country)
# plt.title("GDP Trends for Selected Countries")
# plt.xlabel("Year"); plt.ylabel("GDP (Trillions USD)")
# plt.legend()
# plt.show()
#
# countries = ["India", "United States", "China", "Japan", "Germany", "Pakistan"]
# for country in countries:
#     countryData = final_df[final_df["Country Name"] == country]
#     plt.plot(countryData["Year"], countryData["Inflation"], label=country)
# plt.title("Inflation Trends for Selected Countries")
# plt.xlabel("Year"); plt.ylabel("Inflation Rate")
# plt.legend()
# plt.show()
#
# countries = ["India", "United States", "China", "Japan", "Germany", "Pakistan"]
# for country in countries:
#     countryData = final_df[final_df["Country Name"] == country]
#     plt.plot(countryData["Year"], countryData["Unemployment"], label=country)
# plt.title("Unemployment Trends for Selected Countries")
# plt.xlabel("Year"); plt.ylabel("Unemployment Rate")
# plt.legend()
# plt.show()
#
# sns.histplot(final_df[(final_df["Inflation"] >= -20) & (final_df["Inflation"] <= 30)]["Inflation"], bins=30, kde=True, color="blue")
# plt.title("Distribution of Inflation (–20% to 30%)")
# plt.show()
#
# sns.scatterplot(x="Population", y="Current GDP", data=final_df, alpha=0.5)
# plt.title("GDP vs Population")
# plt.xscale("log")
# plt.yscale("log")
# plt.show()
#
# sns.boxplot(x="Year", y="Unemployment", data=final_df[final_df["Year"] >= 2000])
# plt.xticks(rotation=90)
# plt.title("Unemployment Distribution (2000 onwards)")
# plt.show()

print("Mean Inflation:", final_df["Inflation"].mean())
print("Median Unemployment:", final_df["Unemployment"].median())
print("Mode of Current GDP:", final_df["Current GDP"].mode())
print("Earliest Year:", final_df["Year"].min())
print("Maximum GDP Growth:", final_df["GDP Growth"].max())

