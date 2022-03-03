import sys
sys.path.append('~/projects/testing_software')
import find_total

def test_parser():
    with open('test_data/test.txt', 'r') as reader:
        nums = find_total.parser(reader)
    return nums

def test_calculate_total():
    # expected_result = 10
    with open('test_data/test.txt', 'r') as reader:
        inputs_list = find_total.parser(reader)
        for inputs in inputs_list:
            nums, expected_result = inputs[:-1], int(inputs[-1])
            print(nums, expected_result)
            actual_result = find_total.calculate_total(nums)
        assert actual_result == expected_result, 'wrong answer'
