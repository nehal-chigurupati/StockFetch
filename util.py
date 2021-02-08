import datetime

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

def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
    return None

def get_day_of_week(datetime_date_object):
    #To get today's datetime date object: datetime.date.today()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_num = datetime_date_object.weekday()
    return week_days[week_num]

def is_weekday(datetime_date_object):
    day_of_week = get_day_of_week(datetime_date_object)
    return (day_of_week != "Saturday" and day_of_week != "Sunday")

def get_properly_formatted_date(datetime_date_object):
    return_time = datetime_date_object.strftime('%Y-%m-%d')
    return return_time
