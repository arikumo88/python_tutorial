import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータの作成
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Sales': [30500, 35600, 28300, 33900, 42300]
}

# データフレームの作成
df = pd.DataFrame(data)

# データの表示
print(df)

# グラフの作成
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
