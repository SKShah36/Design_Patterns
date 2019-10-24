import copy
import pandas as pd

df1 = pd.read_csv('datasets/electric-motor-temperature/pmsm_temperature_data.csv', usecols=[4, 5], nrows=1000)
df2 = pd.read_csv('datasets/one-year-industrial-component-degradation/01-04T184148_000_mode1.csv', usecols=[0, 3],
                  nrows=1000)
df3 = pd.read_csv('datasets/hourly-energy-consumption/AEP_hourly.csv', usecols=[1], nrows=1000)

df1_header_list = list(df1.columns)
df2_header_list = list(df2.columns)
df3_header_list = list(df3.columns)

df4 = copy.deepcopy(df2)

for i in range(len(df1.columns)):
    df4.insert(len(df4.columns), df1_header_list[i], df1.iloc[:, i])

for i in range(len(df3.columns)):
    df4.insert(len(df4.columns), df3_header_list[i], df3.iloc[:, i])

df4.columns = ['Timestamp', 'Actual_position', 'Motor_speed', 'Torque', 'Energy_Consumption']
print(df4)
df4.to_csv('combo.csv', index=False)



