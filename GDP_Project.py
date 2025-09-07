import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def clean_dataset(df, name):
    df = df.drop(df.columns[1:24], axis=1)
    if df.columns[-1].startswith("Unnamed"):
        df = df.drop(df.columns[-1], axis=1)
    df.iloc[:, 1:] = df.iloc[:, 1:].interpolate(method="linear", axis=1)
    df.iloc[:, 1:] = df.iloc[:, 1:].bfill(axis=1).ffill(axis=1)
    print(f"\n{name} dataset after cleaning:\n", df.head())
    return df
current_gdp = pd.read_csv("Current_GDP.csv", sep=",", on_bad_lines="skip")
inflation = pd.read_csv("Inflation.csv", sep=",", on_bad_lines="skip")
unemployment = pd.read_csv("Unemployment.csv", sep=",", on_bad_lines="skip")
population = pd.read_csv("Population.csv", sep=",", on_bad_lines="skip")
growth_gdp = pd.read_csv("GDP_growth.csv", sep=",", on_bad_lines="skip")
current_gdp = clean_dataset(current_gdp, "Current GDP")
inflation = clean_dataset(inflation, "Inflation")
unemployment = clean_dataset(unemployment, "Unemployment")
population = clean_dataset(population, "Population")
growth_gdp = clean_dataset(growth_gdp, "GDP Growth")