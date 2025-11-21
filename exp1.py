import math
from collections import Counter
def mean(data):
    return sum(data) / len(data) if data else 0
def median(data):
    if not data:
        return 0
    s = sorted(data)
    n = len(s)
    return (s[n//2 - 1] + s[n//2]) / 2 if n % 2 == 0 else s[n//2]
def mode(data):
    return [k for k, v in Counter(data).items() if v == max(Counter(data).values())] if data else []
def variance(data, m=None):
    if len(data) <= 1:
        return 0
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)
def std_dev(v):
    return math.sqrt(v) if v else 0
def main():
    data = [3, 4, 4, 5, 6, 7]
    print(f"Data: {data}")
    m = mean(data)
    print(f"Mean: {m}")
    print(f"Median: {median(data)}")
    print(f"Mode(s): {mode(data)}")
    v = variance(data, m)
    print(f"Variance: {v}")
    print(f"Standard Deviation: {std_dev(v)}")
if __name__ == "__main__":
    main()

OUTPUT:
Data: [3, 4, 4, 5, 6, 7]
Mean: 4.833333333333333
Median: 4.5
Mode(s): [4]
Variance: 2.1666666666666665
Standard Deviation: 1.4719601443879744
