# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:18:33 2022

@author: Reza
"""

import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="total_bill",data=data)
plt.show()