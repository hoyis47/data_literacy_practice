import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset("tips")

plt.figure(figsize=(4,3))
sns.barplot(tips_df, x='day', y='total_bill')
plt.show()