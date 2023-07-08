# Operations that aren't built-in for in-built types. Non-business logic.

def get_list_differences(list_a, list_b):
	list_a_only = list(set(list_a) - set(list_b))
	list_b_only = list(set(list_b) - set(list_a))
	return list_a_only, list_b_only


def get_dict_differences(dict1, dict2):
	dict_1_only = {k: dict1[k] for k in set(dict1) - set(dict2)}
	dict_2_only = {k: dict2[k] for k in set(dict2) - set(dict1)}
	return dict_1_only, dict_2_only


def get_dict_intersecting_keys(dict1, dict2):
	intersecting_keys = list(set(dict1.keys()) & set(dict2.keys()))
	return intersecting_keys


def get_dict_where_value_differs(dict1, dict2):
	intersecting_keys = get_dict_intersecting_keys(dict1, dict2)
	different_values = {key: (dict1[key], dict2[key]) for key in intersecting_keys if dict1[key] != dict2[key]}
	return different_values
