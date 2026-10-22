


def verify_list_is_sorted(list_to_sort: list, reverse_order: bool) -> bool:
    return list_to_sort == sorted(list_to_sort, reverse=reverse_order)

def create_list_of_matching_values_ordered(list1: list, list2: list) -> list:
    first_index, second_index = 0, 0
    matching_values_first_list = []
    matching_values_second_list = []

    while first_index < len(list1) and second_index < len(list2):
        if list1[first_index] != list2[second_index]:
            matching_values_first_list.append(list1[first_index])
            matching_values_second_list.append(list2[second_index])
            first_index += 1
            second_index += 1
        else:
            first_index += 1
            second_index += 1
    return [matching_values_first_list, matching_values_second_list]