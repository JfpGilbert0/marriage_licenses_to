import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
data = pd.read_csv("data/analysis_data/cleaned_marriage_data.csv")

df = pd.DataFrame(data)

# Plotting the average marriage licenses by month
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='TIME_PERIOD', y='MARRIAGE_LICENSES', marker='o')
plt.title('Average Marriage Licenses by Month')
plt.xlabel('Month-Year')
plt.ylabel('Average Number of Licenses')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()