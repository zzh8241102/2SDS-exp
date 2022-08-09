# Data segmentation
def segementation(input_data, segement_size):
    for i in range(0, len(input_data), segement_size):
    	yield input_data[i:i+segement_size]

# Length Weighted Average Pooling, a more agressive way is Stochastic-pooling
def length_weighted_average_pooling(input_list):
	avg_len = sum(len(i) * len(i) * 0.1 for i in input_list) / sum(len(i) * 0.1 for i in input_list)
	mini = min(abs(len(i) - avg_len) for i in input_list)
	return [i for i in input_list if abs(len(i) - avg_len) == mini][0]

# Feature Max Pooling
def feature_max_pooling(input_list):
	maxi = max(len(set(i)) for i in input_list)
	candidate_list = [i for i in input_list if len(set(i)) == maxi]
	return max((len(i), i) for i in candidate_list)[1]

# Feature Weighted Average Pooling
def feature_weighted_average_pooling(input_list):
	avg_feat_num = sum(len(set(i)) * len(set(i)) * 0.1 for i in input_list) / sum(len(set(i)) * 0.1 for i in input_list)
	mini = min(abs(len(set(i)) - avg_feat_num) for i in input_list)
	candidate_list = [i for i in input_list if abs(len(set(i)) - avg_feat_num) == mini]
	return max((len(set(i)), i) for i in candidate_list)[1]