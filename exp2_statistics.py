import statistics
data = [1, 5, 2, 8, 3, 3]
mean_value = statistics.mean(data)
print(f"Mean: {mean_value}")
median_value =statistics.median(data)
print(f"median: {median_value}")
mode_value = statistics.mode(data)
print(f"Mode: {mode_value}")
standard_dev_value =statistics.stdev(data)
print(f"standard deviation:{standard_dev_value}")

OUTPUT:
Mean: 3.6666666666666665
median: 3.0
Mode: 3
standard deviation:2.503331114069145
