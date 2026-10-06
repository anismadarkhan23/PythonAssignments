import numpy as np

data_set = np.array([6, 7, 8, 9, 10, 11, 12])

mean_of_data_set = np.mean(data_set)

print("Data set is : ", data_set)
print("Mean of the data set is : ", mean_of_data_set)
print("-" * 50)

sum_squared_deviations = 0

for value in data_set:
    deviation_value = value - mean_of_data_set
    print(f"Deviation from mean for value {value} is : {deviation_value}")

    squared_deviation = deviation_value ** 2
    print(f"Squared deviation from mean for value {value} is : {squared_deviation}")

    print("-" * 50)
    sum_squared_deviations = sum_squared_deviations + squared_deviation

print("Sum of squared deviations from mean is : ", sum_squared_deviations)
print("-" * 50)

variance_of_data_set = sum_squared_deviations / len(data_set)
print("Variance of the data set is : ", variance_of_data_set)
print("-" * 50)

standard_deviation_of_data_set = np.sqrt(variance_of_data_set)
print("Standard deviation of the data set is : ", standard_deviation_of_data_set)
print("-" * 50)


