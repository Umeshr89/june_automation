import numpy as np
import pandas as pd

from pandasql import sqldf

arr = np.array([1,2,3,3.4,'str', True])

print("arr is", arr)
print('arr type is', type(arr))

print("arr[0] type", arr[0], type(arr[0]))
print("arr[3] type", arr[0], type(arr[0]))

print("dimention", arr)

