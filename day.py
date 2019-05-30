import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('entry.csv',error_bad_lines=False)
print('Total Transfer Amount:',data['Amounts'].sum())
rem=pd.DataFrame(data.groupby('Date').sum())
rem.index
plt.pie(rem['Amounts'],labels=rem.index,autopct='%1.1f%%',radius=1)
plt.legend(data.Date,loc='best')
plt.title('Total Spending According To Date')
