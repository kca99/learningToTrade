from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np

start_date= datetime.datetime(2016,1,1)
end_date = datetime.date.today()

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
df = data.DataReader({'V', 'SQ', 'MA'}, 'morningstar', start_date, end_date)
# df = data.DataReader('IQ', 'morningstar', start_date, end_date)

this = df.index.get_level_values('Date')
df = df.unstack(level=0)['Close']
# print(this[0])
print(df)

# df.plot(secondary_y = ["V", "SQ"], grid = True)
# plt.title('Close Price of V MA and SQ (scaled)')
# plt.show()

# stock_return =  df.apply(lambda x: x / x[0])
# stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
# plt.title('Return Price of V MA and SQ')
# plt.show()

# stock_change = df.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
# stock_change.plot(grid = True).axhline(y = 0, color = "black", lw = 2)
# plt.title('Percentage Change in Price of V MA and SQ (scaled)')
# plt.show()

plt.plot(df['SQ'],label= 'Close')
plt.plot(df['SQ'].rolling(20).mean(),label= 'MA 20 days')
plt.plot(df['SQ'].rolling(50).mean(),label= 'MA 50 days')
plt.plot(df['SQ'].rolling(100).mean(),label= 'MA 100 days')
plt.legend(loc='best')
plt.title('SQ \n 10D AND 20D MA')


# plt.plot(df['MA'],label= 'Close')
# plt.plot(df['MA'].rolling(10).mean(),label= 'MA 10 days')
# plt.plot(df['MA'].rolling(20).mean(),label= 'MA 20 days')
plt.show()