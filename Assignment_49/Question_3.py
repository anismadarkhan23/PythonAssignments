import pandas as pd
from sklearn.preprocessing import StandardScaler

data_set = pd.DataFrame({
    "Age": [25, 30, 35],
    "Salary": [20000, 40000, 80000]
})

print("Data set is : ")
print(data_set)
print("-" * 50)

scaler = StandardScaler()

scaled_data_set = scaler.fit_transform(data_set)
scaled_data_set = pd.DataFrame(scaled_data_set, columns = data_set.columns)
print("Scaled data set is : ")
print(scaled_data_set)
print("-" * 50)