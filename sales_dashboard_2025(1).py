import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_2025_data.csv')
plt.plot(df['date'], df['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time (2025)')
plt.show()
