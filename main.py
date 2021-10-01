"""
CMPS 2200  Assignment 1. Marisa Long
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if (x <= 1):
        return x
    else:
        return foo(x-1)+foo(x-2)

def longest_run(mylist, key):
    max = 0
    for i in range(len(myarray)):
        if myarray[i] == key:
            count +=1
            if count > max:
                max = count
        else:
            count = 0
    return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def combine_results(left_result, right_result):
    #cases where the left is entirely comprised of the key
    if(left_result.is_entire_range == True):
        if(right_result.is_entire_range == True):
            combined_size = left_result.left_size + right_result.left_size
            return Result(combined_size, combined_size, combined_size, True)
        else:
            left = left_result.left_size + right_result.left_size
            right = right_result.right_size
    #cases where the left is not entirely comprised of the key
    else:
        left = left_result.left_size
        if(right_result.is_entire_range == True):
            right = left_result.right_size + right_result.left_size
        else:
            right = right_result.right_size

    #dealing with cases that span partially on the left and partially on the right
    center = left_result.right_size + right_result.left_size
    if left_result.longest_size > right_result.longest_size:
        longest = left_result.longest_size
    else:
        longest = right_result.longest_size
    #case if longest spans the center
    if center > longest:
        return Result(left, right, center, False)
    else:
        return Result(left, right, longest, False)


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if (mylist[0] == key):
            element_value = Result(1, 1, 1, True)
        else:
            element_value = Result(0, 0, 0, False)
        return element_value
    else:
        left = longest_run_recursive(mylist[:len(mylist)//2], key)
        right = longest_run_recursive(mylist[len(mylist)//2:], key)
        return combine_results(left, right)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

## Feel free to add your own tests here.
def test_longest_run_recursive():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,12,12,12,12,0,12,1], 12) == 3

print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))
print(longest_run_recursive([2,12,12,12,12,12,12,0,12,1], 12))
