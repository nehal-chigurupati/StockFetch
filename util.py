def selection_sort(nums):
    for i in range(len(nums)):
        index_current_min = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index_current_min]:
                index_current_min = j
        nums[i], nums[index_current_min] = nums[index_current_min], nums[i]
    return nums

def clean_list(list):
    return_list = []
    for item in list:
        try:
            floated_item = float(item)
            return_list.append(floated_item)
        except ValueError:
            print(str(item + " is not a double"))

    return return_list
