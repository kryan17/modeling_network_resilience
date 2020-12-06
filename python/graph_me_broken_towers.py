import networks as nw
import config as config

import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy as np

results = pd.read_csv(r'C:\Users\Public\DAEN690\Model_Cellular_Network\SimResults\NetworkRun-breaktowers.csv')
df_summary = results.groupby(["tower_range", "connection_check", "run_type"], as_index=False).count()

# print(df_summary.run_type.unique())
# ['Break Tower: Aquia_Creek Ln' 'Break Tower: Chesapeak River Ln'
#  'Break Tower: Nguyen Engineering' 'Break Tower: Patriot Cir'
#  'Break Tower: Rivanna River Way']

run = 'Break Tower: Patriot Cir'

df_true = df_summary["connection_check"]==True
df_false = df_summary["connection_check"]==False

df_break = df_summary["run_type"] == run

df_Aquia = df_summary["run_type"] == 'Break Tower: Aquia_Creek Ln'
df_Chesapeak = df_summary["run_type"] == 'Break Tower: Chesapeak River Ln'
df_Nguyen = df_summary["run_type"] == 'Break Tower: Nguyen Engineering'
df_Patriot = df_summary["run_type"] == 'Break Tower: Patriot Cir'
df_Rivanna = df_summary["run_type"] == 'Break Tower: Rivanna River Way'

"""
plt.plot(df_summary[df_true][df_break]["tower_range"]
         , df_summary[df_true][df_break]["cell_id"]
         , 'g'
         , label='Can Connect')
plt.plot(df_summary[df_false][df_break]["tower_range"]
         , df_summary[df_false][df_break]["cell_id"]
         , 'r'
         , label='Cannot Connect')
plt.legend()
plt.ylabel('Number of Device Connections')
plt.xlabel('Tower Range')
plt.suptitle('Simulation Results {run}'.format(run=run))
plt.show()
"""

plt.plot(df_summary[df_Aquia][df_true]["tower_range"]
         , df_summary[df_Aquia][df_true]["cell_id"]
         , color='green'
         , label='Aquia Break')
plt.plot(df_summary[df_Chesapeak][df_true]["tower_range"]
         , df_summary[df_Chesapeak][df_true]["cell_id"]
         , color='yellow'
         , label='Chesapeak Break')
plt.plot(df_summary[df_Nguyen][df_true]["tower_range"]
         , df_summary[df_Nguyen][df_true]["cell_id"]
         , color='red'
         , label='Nguyen Break')
plt.plot(df_summary[df_Patriot][df_true]["tower_range"]
         , df_summary[df_Patriot][df_true]["cell_id"]
         , color='purple'
         , label='Patriot Break')
plt.plot(df_summary[df_Rivanna][df_true]["tower_range"]
         , df_summary[df_Rivanna][df_true]["cell_id"]
         , color='orange'
         , label='Rivanna Break')

plt.legend()
plt.ylabel('Number of Device Connections')
plt.xlabel('Tower Range')
plt.suptitle('Comparing Tower Breaks')
plt.show()
