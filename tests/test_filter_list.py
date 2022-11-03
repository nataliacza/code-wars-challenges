from challenges.list_filtering import filter_list

def tests_list1():
    result = filter_list([1, 2, 'a', 'b'])
    expected = [1, 2]
    assert result == expected

def tests_list2():
    result = filter_list([1, 'a', 'b', 0, 15])
    expected = [1, 0, 15]
    assert result == expected

def tests_list3():
    result = filter_list([1, 2, 'aasf', '1', '123', 123])
    expected = [1, 2, 123]
    assert result == expected
