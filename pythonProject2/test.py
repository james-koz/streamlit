
import pandas as pd
import numpy as np
file_path = r'C:\Users\James\Desktop\pythonProject2\赛宁机器信息.xlsx'   # r对路径进行转义，windows需要
raw_data = pd.read_excel(file_path, header=0)  # header=0表示第一行是表头，就自动去除了
random_data = np.random.rand(100, 10)

print(random_data)
print(raw_data)
