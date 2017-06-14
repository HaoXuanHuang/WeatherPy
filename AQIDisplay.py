import codecs
from xlrd import open_workbook
import pandas
import json
import numpy as np
import matplotlib as plt

path="C:\\Users\\Joyce\\Documents\\BeijingAQI.xlsx"
df =pandas.read_excel(path)
frame =pandas.DataFrame(df)
Beijing=pandas.Series(frame['Beijing'])
frame2=pandas.DataFrame(df, index=frame.index, columns=['Beijing', 'Tianjing', 'shijiazhuang'])
#print(frame2)
print("mean:", np.mean(Beijing, axis=0), np.median(Beijing), np.max(Beijing), np.min(Beijing), np.std(Beijing))
print(frame2.describe())
frame2.plot(kind="line")
plt.pyplot.show()

