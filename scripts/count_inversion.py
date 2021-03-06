def merge_and_count_split_inversion(sorted_left, sorted_right):
    """
    merge and count split inversion given 2 sorted lists as inputs
    """
    count = 0
    result = []
    for k in range(len(sorted_left) + len(sorted_right)):
        if len(sorted_left) > 0 and len(sorted_right) > 0:
            # append the smallest item among input lists to result
            if sorted_left[0] <= sorted_right[0]:
                result.append(sorted_left.pop(0))
            else:
                result.append(sorted_right.pop(0))
                count += len(sorted_left)  # inversion spotted
        elif len(sorted_left) == 0:
            # sorted_left used up, attach remaining items in sorted_right to result
            result += sorted_right
            break
        elif len(sorted_right) == 0:
            # sorted_right used up, attach remaining items in sorted_left to result
            result += sorted_left
            break
    return result, count


def sort_and_count_inversion(input_list):
    # base case
    if len(input_list) <= 1:
        return (input_list, 0)
    else:
        # split input list in 2 parts
        left = input_list[0 : len(input_list) // 2]
        right = input_list[len(input_list) // 2 : len(input_list)]

        # recursively sort and count left inversion
        (sorted_left, left_inversion) = sort_and_count_inversion(left)

        # recursively sort and count right inversion
        (sorted_right, right_inversion) = sort_and_count_inversion(right)

        # merge and count split inversion
        (sorted_all, split_inversion) = merge_and_count_split_inversion(
            sorted_left, sorted_right
        )

        return (
            sorted_all,  # sorted list
            left_inversion + right_inversion + split_inversion,  # number of inversion
        )


def test_count_inversion_1():
    assert sort_and_count_inversion([1, 3, 5, 2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)


def test_count_inversion_2():
    assert sort_and_count_inversion([6, 5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5, 6], 15)


def test_split_inversion():
    assert merge_and_count_split_inversion([1, 3, 5], [2, 4, 6]) == (
        [1, 2, 3, 4, 5, 6],
        3,
    )


def test_count_inversion_in_file():
    # read file
    with open("../data/IntegerArray.txt", "r") as f:
        input_list = f.read().splitlines()
    # convert all str into int
    input_list = [int(x) for x in input_list]

    # count inversion
    assert sort_and_count_inversion(input_list)[1] == 2407905288
