import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
matplotlib inline
import seaborn as sns
print("Setup Complete")

import os
for dirname, _, filenames in os.walk('D:/Github/Python_learning/kaggle/input/test.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))