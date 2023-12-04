import numpy as np
import pandas as pd
from Model_1 import *
import ast

df = pd.read_excel('encoding_results.xlsx')

df['Encoding'] = df['Encoding'].apply(ast.literal_eval)
# Assuming the column you want to print is named 'Encoding'
column_values_encoding = df['Encoding'].tolist()
column_values_status = df['Status'].tolist()

# print(column_values_encoding, column_values_status)
# training_model(np.array(column_values_encoding), np.array(column_values_status))
weight = np.random.uniform(-0.5, 0.5, features)

# print("start before")
# logistic_model(encoding=column_values_encoding, target=column_values_status, weight=weight)
print("Training")
weight = training_model(encoding=column_values_encoding, weight= weight, target=column_values_status, epoch=500, alpha=0.01)
# print("After")
# logistic_model(encoding=column_values_encoding, target=column_values_status, weight=weight)


