from geopy.distance import geodesic

def calculate_distance(row, sorted_data_stops):
    distances = []
    for i in range(len(row['planned_route_craft'])-1):
        coords_1 = (sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['planned_route_craft'][i], ['current_lat']].values[0][0],
                     sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['planned_route_craft'][i], ['current_lng']].values[0][0])
        coords_2 = (sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['planned_route_craft'][i+1], ['current_lat']].values[0][0],
                     sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['planned_route_craft'][i+1], ['current_lng']].values[0][0])
        distances.append(geodesic(coords_1, coords_2).miles)
    return distances

def calculate_distance_actual(row, sorted_data_stops):
    distances = []
    for i in range(len(row['actual_route_location'])-1):
        coords_1 = (sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['actual_route_location'][i], ['current_lat']].values[0][0],
                     sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['actual_route_location'][i], ['current_lng']].values[0][0])
        coords_2 = (sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['actual_route_location'][i+1], ['current_lat']].values[0][0],
                     sorted_data_stops.loc[sorted_data_stops['location_id_craft'] == row['actual_route_location'][i+1], ['current_lng']].values[0][0])
        distances.append(geodesic(coords_1, coords_2).miles)
    return distances


from collections import defaultdict

def analyze_routes(df):
    rows = []

    for idx, row in df.iterrows():
        route_id = idx
        driver_id = row['driver_id_sorted']
        planned_real = row['planned_route_location']
        actual_real = row['actual_route_unique']
        arriving_times = row['arriving_time']
        planned_distances = row['distance_route']
        actual_distances = row['distance_actual_route']
        country_flag = row['country_flag']
        day_of_week = row['day_of_week']
        date = row['date']
        experience = row['last_two_weeks_count']
        is_depot = row['location_is_depot']
        is_pickup = row['location_type_id']
        craft_id = row['routes']

        #times
        arr_times = [pd.to_datetime(ts) for ts in arriving_times]
        earliest_times = [pd.to_datetime(ts) for ts in row['stop_earliest']]
        latest_times = [pd.to_datetime(ts) for ts in row['stop_latest']]
        earliest_timestamp = min(min(arr_times), min(earliest_times), min(latest_times))

        arr_durations = [(t - earliest_timestamp).total_seconds()  for t in arr_times]
        earliest_durations = [(t - earliest_timestamp).total_seconds()  for t in earliest_times]
        latest_durations = [(t - earliest_timestamp).total_seconds()  for t in latest_times]
        #indexes
        map = defaultdict(lambda: [])
        for i in range(len(planned_real)):
            map[planned_real[i]].append(i)

        map_index = defaultdict(lambda: 0)

        for (idx, stop) in enumerate(actual_real):
            planned_index = idx
            planned_distance = 0 if planned_index == 0 else planned_distances[planned_index - 1]
            if stop in map:
                actual_index = map[stop][map_index[stop]]
                map_index[stop] += 1
            else:
                actual_index = planned_real.index(stop)
            actual_distance = 0 if actual_index == 0 else actual_distances[actual_index - 1]

            rows.append({
                'Route ID': route_id,
                'Driver ID': driver_id,
                'Country': country_flag,
                'Day of Week': day_of_week,
                'Stop ID': stop-1,
                'Location ID': craft_id[idx],
                'IndexP': planned_index,
                'IndexA': actual_index,
                'Arrived Time': round(arr_durations[idx]/60, 3),
                'Time Earliest': round(earliest_durations[idx]/60, 3),
                'Time Latest': round(latest_durations[idx]/60, 3),
                # 'Arrived Time_c': arriving_times[idx],
                # 'Time Earliest_c': row['stop_earliest'][idx],
                # 'Time Latest_c': row['stop_latest'][idx],
                'DistanceP': planned_distance,
                'DistanceA': actual_distance,
                'Depot': is_depot[idx],
                'Delivery': is_pickup[idx],
            })

    return pd.DataFrame(rows)