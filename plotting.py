import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from midterm_starter import flawed_benchmark, find_duplicates_fast, find_duplicates_slow

data = flawed_benchmark()
df = pd.DataFrame(data)
df.head()

plt.figure(figsize = (4,5))
sns.lineplot(data = df, x = 'size', y = 'Time', hue = 'Algorithm')
plt.xscale('log')
plt.xlabel('Duplicates')
plt.tight_layout
plt.savefig('results.png')
plt.show()