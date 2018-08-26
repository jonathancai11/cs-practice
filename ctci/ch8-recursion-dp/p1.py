# Jonathan Cai
# August 26, 2018

def numsteps(n):
    """
    Recursive, returns lowest number of steps needed for a child to step up n steps.
    Child can step 1, 2 or 3 steps at a time.
    """
    # Base Cases
    if n == 0:
        return 0
    if n == 1 or n == 2 or n == 3:
        return 1
    return min(numsteps(n-1), numsteps(n-2), numsteps(n-3)) + 1


# TESTING
print(numsteps(5), "Expected: 2")
print(numsteps(10), "Expected: 4")
print(numsteps(0), "Expected: 0")
print(numsteps(20), "Expected: 7")

