import pandas as pd
series = pd.series([1,2,3,4,5], index=['a','b','c','d','e'])
print(series)


print("series[a]", series['a'])
print("series['e']", series['e'])