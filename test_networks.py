import networks as nw
import config as config

import geopy
import random
import pandas as pd
import time
import numpy as np


timestr = time.strftime("%Y%m%d-%H%M%S")
filename = r'C:\Users\Public\DAEN690\Model_Cellular_Network\SimResults\NetworkRun-{time}.csv'.format(time=timestr)


# parameters for generating events
bearing_min = config.bearing_min
bearing_max = config.bearing_max
distance_min = config.distance_min
distance_max = config.distance_max

towers = []
df = pd.read_csv('Towers.csv')

if config.vary_tower_range and config.break_towers:
    current_range = config.min_range
    while current_range <= config.max_range:
        for ind in df.index:
            ii = 0
            dfc = len(df.index)
            while ii < dfc:
                if ind == ii:
                    tw = nw.Tower("".join((df['Tower_ID'][ind], str(current_range)))
                                  , df['Tower_Lat'][ind]
                                  , df['Tower_Lon'][ind]
                                  , 0)
                else:
                    tw = nw.Tower("".join((df['Tower_ID'][ind], str(current_range)))
                                  , df['Tower_Lat'][ind]
                                  , df['Tower_Lon'][ind]
                                  , current_range)
                towers.append([tw, current_range, 'Break Tower: ' + str(df['Tower_ID'][ii])])
                ii += 1
        current_range = current_range + config.increase_incr

elif config.vary_tower_range and not config.break_towers:
    current_range = config.min_range
    while current_range <= config.max_range:
        for ind in df.index:
            tw = nw.Tower("".join((df['Tower_ID'][ind], str(current_range)))
                          , df['Tower_Lat'][ind]
                          , df['Tower_Lon'][ind]
                          , current_range)
            towers.append([tw, current_range])
        current_range = current_range + config.increase_incr
else:
    for ind in df.index:
        tw = nw.Tower(df['Tower_ID'][ind]
                      , df['Tower_Lat'][ind]
                      , df['Tower_Lon'][ind]
                      , df['Tower_Range'][ind])
        towers.append(tw)

calls = []
i = 0

while i < config.events_generated:
    ds = random.uniform(distance_min, distance_max)
    d = geopy.distance.distance(kilometers=ds)
    br = random.uniform(bearing_min, bearing_max)

    call_point = d.destination(point=config.center, bearing=br)
    dv = nw.Device(i, 'cellphone', call_point.latitude, call_point.longitude)
    i += 1
    calls.append(dv)

output_detail = []
output_summary = []

print(len(calls))
print(len(towers))

if config.vary_tower_range and not config.break_towers:
    lat_dict = {}
    lon_dict = {}
    for cl in calls:
        can_connect = False
        for tw in towers:
            a = cl.check_connection(tw[0])
            output_detail.append([cl.id, tw[0].id, a, tw[1]])
            if a:
                can_connect = True
    df_details = pd.DataFrame(output_detail, columns=['cell_id', 'tower', 'connection_check', 'tower_range'])
    df_summary = df_details.groupby(["cell_id", "tower_range"], as_index=False)["connection_check"].max()
    df_summary["run_type"] = 'Baseline Variable Range'

elif not config.vary_tower_range and not config.break_towers:
    for cl in calls:
        can_connect = False
        for tw in towers:
            a = cl.check_connection(tw)
            output_detail.append([cl.id, tw.id, a, tw.range])
            if a:
                can_connect = True
        output_summary.append([cl.id, can_connect, tw.range])

    df_details = pd.DataFrame(output_detail, columns=['cell_id', 'tower', 'connection_check', 'tower_range'])
    df_summary = pd.DataFrame(output_summary, columns=['cell_id', 'connection_check', 'tower_range'])
    df_summary["run_type"] = 'Baseline'

elif config.vary_tower_range and config.break_towers:
    lat_dict = {}
    lon_dict = {}
    run_desc = []
    for cl in calls:
        can_connect = False
        for tw in towers:
            a = cl.check_connection(tw[0])
            output_detail.append([cl.id, tw[0].id, a, tw[0].range])
            run_desc.append(tw[2])
            if a:
                can_connect = True
    df_details = pd.DataFrame(output_detail, columns=['cell_id', 'tower', 'connection_check', 'tower_range'])
    df_details["run_type"] = run_desc
    df_summary = df_details.groupby(["cell_id", "tower_range", "run_type"], as_index=False)["connection_check"].max()

else :
    print("Something Is Wrong")

df_summary.to_csv(filename, index = False)