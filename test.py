import unittest

import demographic_data_analyzer

import pandas as pd


df = pd.read_csv("adult.data.csv")

min_work_hours = df["hours-per-week"].min()
print(min_work_hours)