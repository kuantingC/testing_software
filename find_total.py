
def parser(f):
    ret = []
    for line in f:
        # text = line.read()
        nums = line.split()  
        for n in nums:
            assert int(n), f'invalid literal for int() with base 10: {n}'
        ret.append(nums)
    return ret

def calculate_total(nums):
    ret = 0
    for n in nums:
        ret += int(n)
    return ret

