import geopy

# set variables for event generation
center = geopy.point.Point(38.830114, -77.307079, 0)
bearing_min = 0
bearing_max = 360
distance_min = 0.1
distance_max = 1
events_generated = 1000


# consider multiple ranges
vary_tower_range = True
min_range = 0.1
max_range = 1.0
increase_incr = 0.1

# Break Towers
break_towers = True
