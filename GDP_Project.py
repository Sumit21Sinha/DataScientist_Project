import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
current_gdp=pd.read_csv("Current_GDP.csv", sep=",", on_bad_lines="skip")
inflation=pd.read_csv("Inflation.csv", sep=",", on_bad_lines="skip")
unemployment=pd.read_csv("Unemployment.csv", sep=",", on_bad_lines="skip")
population=pd.read_csv("Population.csv", sep=",", on_bad_lines="skip")
growth_gdp=pd.read_csv("GDP_growth.csv", sep=",", on_bad_lines="skip")
print("\nThe inflation dataset/table looks like this :\n", inflation.head())
print("\nThe inflation dataset/table looks like this :\n", unemployment.head())
print("\nThe inflation dataset/table looks like this :\n", population.head())
print("\nThe inflation dataset/table looks like this :\n", current_gdp.head())
print("\nThe inflation dataset/table looks like this :\n", growth_gdp.head())
