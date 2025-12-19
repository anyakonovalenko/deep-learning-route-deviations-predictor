def minDistance(word1, word2) -> int:
    m = len(word1)
    n = len(word2)
    # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
      dp[i][0] = i

    for j in range(1, n + 1):
      dp[0][j] = j

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


def calculate_route_quality_score(planned_ranks, actual_ranks):
    # Calculate sum of absolute differences in ranks
    sum_of_differences = sum(abs(actual_ranks.index(x) - planned_ranks.index(x)) for x in planned_ranks)

    # Calculate max possible difference
    max_possible_difference = sum([abs(2 * i - (len(planned_ranks) + 1)) for i in range(1, len(planned_ranks) + 1)])

    # Calculate route quality score
    route_quality_score = 1 - (sum_of_differences / max_possible_difference)

    return route_quality_score


#%%
# drivers_dic = {}
# k = 1
# for driver in final_routes_split['driver_id_sorted']:
#     if driver not in drivers_dic:
#         drivers_dic[driver] = k
#         k += 1
# print('Total number of drivers', len(drivers_dic))
# total_drivers = len(drivers_dic)
# encoding_drivers = []
# for driver in final_routes_split['driver_id_sorted']:
#     encoding_drivers.append(drivers_dic[driver])
# #
# final_routes_split['driver_id_sorted'] = encoding_drivers
#
# locations_dic = {}
# location_count = {}
# k = 1
# for row in final_routes_split['routes']:
#    for location in row:
#        if location not in locations_dic:
#            locations_dic[location] = k
#            k += 1
# k = 1
# print(len(locations_dic))
#
# for row in final_routes_split['routes']:
#    for location in row:
#        if location not in location_count:
#             location_count[location] = 1
#        else:
#             location_count[location] += 1
# encoding_routes = []
# for row in final_routes_split['routes']:
#     encoding_route = []
#     for location in row:
#         encoding_route.append(locations_dic[location])
#     encoding_routes.append(encoding_route)
# final_routes_split['routes'] = encoding_routes

# def split_group(group):
#     n = len(group)
#     global extra_to_val
#     if n < 4:  # Ensure at least 1 sample for train and 2 each for val and test
#         return pd.DataFrame()
#
#     # Calculate sizes for each split
#     train_size = max(int(n * 0.8), n - 4)  # Ensure at least 2 samples each for val and test
#     val_test_size = n - train_size
#     if val_test_size % 2 == 1:
#         if extra_to_val:
#             val_size = val_test_size // 2 + 1
#             test_size = val_test_size // 2
#         else:
#             val_size = val_test_size // 2
#             test_size = val_test_size // 2 + 1
#         extra_to_val = not extra_to_val  # Flip for next time
#     else:
#         val_size = test_size = val_test_size // 2
#
#     return pd.concat([
#         group.iloc[:train_size].assign(split='train'),
#         group.iloc[train_size:train_size+val_size].assign(split='val'),
#         group.iloc[train_size+val_size:].assign(split='test')
#     ])
