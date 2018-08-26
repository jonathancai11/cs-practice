# Jonathan Cai
# August 26, 2018

def numsteps(n):
    """
    Recursive, returns the number of paths for a child to step up n steps.
    Child can step 1, 2 or 3 steps at a time.
    """
    # Base Cases
    if n == 0 or n == 1 or n == 2:
        return n
    return numsteps(n-1) + numsteps(n-2) + numsteps(n-3) + 3


# TESTING
print(numsteps(5), "Expected: idk")
print(numsteps(10), "Expected: idk")
print(numsteps(0), "Expected: 0")

