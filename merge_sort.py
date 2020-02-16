def merge(list_a, list_b):
    """
    merge 2 sorted list into single sorted list
    """
    result = []
    for k in range(len(list_a) + len(list_b)):
        if len(list_a) > 0 and len(list_b) > 0:
            # append the smallest item among input lists to result
            if list_a[0] <= list_b[0]:
                result.append(list_a.pop(0))
            else:
                result.append(list_b.pop(0))
        elif len(list_a) == 0:
            # list_a used up, attach remaining items in list_b to result
            result += list_b
            break
        elif len(list_b) == 0:
            # list_b used up, attach remaining items in list_a to result
            result += list_a
            break
    return result


def merge_sort(input_list):
    # base case
    if len(input_list) <= 1:
        return input_list
    else:
        # split in half
        a = input_list[0 : len(input_list) // 2]
        b = input_list[len(input_list) // 2 : len(input_list)]

        # recursive calls
        sorted_a = merge_sort(a)
        sorted_b = merge_sort(b)

        # merge
        return merge(sorted_a, sorted_b)


def test1():
    assert merge_sort([5, 4, 1, 8, 7, 2, 6, 3]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test2():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
