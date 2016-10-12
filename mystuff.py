test_list = [1, 2, 3, 4]


def reverse_list(input_list):
    return list(reversed(input_list))


def reverse_list2(input_list):
    return input_list[::-1]


def reverse_list3(input_list):
    return input_list.reverse()


if __name__ == '__main__':
    import timeit

    print(timeit.timeit('reverse_list(test_list)', setup="from __main__ import reverse_list,test_list"))
    print(timeit.timeit('reverse_list2(test_list)', setup="from __main__ import reverse_list2,test_list"))
    print(timeit.timeit('reverse_list3(test_list)', setup="from __main__ import reverse_list3,test_list"))
