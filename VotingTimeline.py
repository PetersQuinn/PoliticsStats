import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Event': ['Primary Election', 'General Election'],
    'Date': ['2026-08-18', '2026-11-03']
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
plt.figure(figsize=(10, 2))
plt.hlines(1, df['Date'].min(), df['Date'].max(), colors='lightgray', linestyles='dashed')
plt.plot(df['Date'], [1]*len(df), 'o', markersize=10, color='skyblue')
for idx, row in df.iterrows():
    plt.text(row['Date'], 1.02, row['Event'], rotation=45, ha='right')
plt.yticks([])
plt.title('Florida 2026 State Elections Timeline')
plt.tight_layout()
plt.show()
