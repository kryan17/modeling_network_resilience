import networks as nw
import config as config

import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy as np

results = pd.read_csv(r'C:\Users\Public\DAEN690\Model_Cellular_Network\SimResults\NetworkRun-baseline.csv')
df_summary = results.groupby(["tower_range", "connection_check", "run_type"], as_index=False).count()

df_true = df_summary["connection_check"]==True
df_false = df_summary["connection_check"]==False

plt.plot(df_summary[df_true]["tower_range"], df_summary[df_true]["cell_id"], 'g')
plt.plot(df_summary[df_false]["tower_range"], df_summary[df_false]["cell_id"], 'r')
plt.ylabel('Number of Device Connections')
plt.xlabel('Tower Range')
plt.suptitle('Simulation Results')
plt.show()
