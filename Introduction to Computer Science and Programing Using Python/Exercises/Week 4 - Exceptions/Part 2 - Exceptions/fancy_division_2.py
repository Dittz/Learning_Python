def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        result = item / denom
        return result
    except ZeroDivisionError:
        return 0
