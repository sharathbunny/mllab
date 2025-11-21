import pandas as pd
df = pd.DataFrame({
    'Hours_Studied': [1, 2, 3, 4, 5],
    'Test_Score': [50, 55, 65, 70, 80]
})
print("1.original df\n",df)
print("2.Shape:\n", df.shape)
print("3.Missing(isnull):\n", df.isnull().sum())
print("4.basic Stats(describe):\n", df.describe())
print("5.Correlation:\n", df.corr())
print("6.dataframe Info\n",df.info())
print("7.head\n",df.head(3))
print("8.tail\n",df.tail(2))
print("9.row with index 2\n",df.loc[2])
OUTPUT:
1.original df
    Hours_Studied  Test_Score
0              1          50
1              2          55
2              3          65
3              4          70
4              5          80
2.Shape:
 (5, 2)
3.Missing(isnull):
 Hours_Studied    0
Test_Score       0
dtype: int64
4.basic Stats(describe):
        Hours_Studied  Test_Score
count       5.000000    5.000000
mean        3.000000   64.000000
std         1.581139   11.937336
min         1.000000   50.000000
25%         2.000000   55.000000
50%         3.000000   65.000000
75%         4.000000   70.000000
max         5.000000   80.000000
5.Correlation:
                Hours_Studied  Test_Score
Hours_Studied       1.000000    0.993399
Test_Score          0.993399    1.000000
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Hours_Studied  5 non-null      int64
 1   Test_Score     5 non-null      int64
dtypes: int64(2)
memory usage: 212.0 bytes
6.dataframe Info
 None
7.head
    Hours_Studied  Test_Score
0              1          50
1              2          55
2              3          65
8.tail
    Hours_Studied  Test_Score
3              4          70
4              5          80
9.row with index 2
 Hours_Studied     3
Test_Score       65
Name: 2, dtype: int64
