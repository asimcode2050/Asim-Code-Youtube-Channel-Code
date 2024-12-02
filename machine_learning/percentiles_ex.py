import numpy as np
scores = [60, 75, 80, 85, 90, 92, 95, 98, 99, 100]
scores_array = np.array(scores)


def calculate_percentiles(data, percentiles):
    return np.percentile(data, percentiles)


percentile_values = calculate_percentiles(scores_array, [25, 50, 75])
print(f"25th percentile: {percentile_values[0]}")
print(f"50th percentile (Median): {percentile_values[1]}")
print(f"75th percentile: {percentile_values[2]}")
outlier_thresholds = calculate_percentiles(scores_array, [5, 95])
print(f"5th percentile (Lower outlier threshold): {outlier_thresholds[0]}")
print(f"95th percentile (Upper outlier threshold): {outlier_thresholds[1]}")
lower_outlier = [score for score in scores if score < outlier_thresholds[0]]
upper_outlier = [score for score in scores if score > outlier_thresholds[1]]
print(f"Scores lower than the 5th percentile: {lower_outlier}")
print(f"Scores higher than the 95th percentile: {upper_outlier}")
