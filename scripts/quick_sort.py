# helper function - choose pivot subroutine
def choose_first(A, l, r):
    """
    Choose the first element as pivot
    """
    return l


def choose_last(A, l, r):
    """
    Choose the last element as pivot
    """
    return r


def choose_mid(A, l, r):
    """
    Choose the median of first, middle, and last elements as pivot
    """
    length = r - l + 1
    if l >= r:
        pass
    else:
        first = l
        last = r
        if length % 2 == 0:
            center = l + ((length // 2) - 1)
        else:
            center = l + ((length - 1) // 2)
        median_value = sorted([A[first], A[center], A[last]])[1]
        median_index = [A[first], A[center], A[last]].index(median_value)

        if median_index == 0:
            return first
        elif median_index == 1:
            return center
        elif median_index == 2:
            return last


# helper function - partition subroutine
def partition(A, l, r):
    """
    Partiaion around the chosen pivot.
    Keep track of 2 boundaries:
       (1) i: within checked items, where should the pivot locates
       (2) j: next checking location
    """
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:  # if A[i] > pivot, do nothing
            A[i], A[j] = A[j], A[i]
            i += 1
    # put pivot to its final correct location
    A[l], A[i - 1] = A[i - 1], A[l]

    return i - 1  # return pivot's final location


# main quick sort algorithm function
def quick_sort(A, l, r, choose_pivot):
    comparison = 0  # keep track of comparisons performed
    if l >= r:
        return 0
    else:
        # count comparisons during the quick sort process
        comparison += r - l

        # choose pivot
        pivot_index = choose_pivot(A, l, r)
        # swap before partition
        A[l], A[pivot_index] = A[pivot_index], A[l]
        # partition around pivot
        pivot_loc = partition(A, l, r)

        # recursively sort left part (< pivot)
        comparison_left = quick_sort(A, l, pivot_loc - 1, choose_pivot)
        # recursively sort right part (> pivot)
        comparison_right = quick_sort(A, pivot_loc + 1, r, choose_pivot)

        return comparison + comparison_left + comparison_right


def read_data(path):
    """
    Read in data (txt) and return a list.
    Each element in the returned list is a line in the input file
    """
    # read file
    with open(path, "r") as f:
        data = f.read().splitlines()
    # convert all str into int
    data = [int(x) for x in data]

    return data


# Test cases
def test_quick_sort_pivot_first():
    data = read_data("../data/QuickSort.txt")
    assert quick_sort(data, 0, len(data) - 1, choose_first) == 162085


def test_quick_sort_pivot_last():
    data = read_data("../data/QuickSort.txt")
    assert quick_sort(data, 0, len(data) - 1, choose_last) == 164123


def test_quick_sort_pivot_mid():
    data = read_data("../data/QuickSort.txt")
    assert quick_sort(data, 0, len(data) - 1, choose_mid) == 138382
