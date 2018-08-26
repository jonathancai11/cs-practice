# Jonathan Cai
# May 13, 2018

################ MERGE SORT ################

def mergeSort(lst):
    """
    Sorts the given nonempty list, lst.
    """
    # Base Case: list with single element
    if len(lst) == 1:
        return lst
    # Recursive Case: sort left and right halves
    else:
        middle = len(lst) / 2
        left = mergeSort(lst[0: middle])
        right = mergeSort(lst[middle: len(lst)])
        # Construct result based on sorted halves
        result = []
        i = j = 0
        while i + j < len(lst):
            if i == len(left):
                result.append(right[j])
                j += 1
            elif j == len(right):
                result.append(left[i])
                i += 1
            elif left[i] <= right[j]:
                result.append(left[i])
                i += 1
            elif right[j] < left[i]:
                result.append(right[j])
                j += 1
        return result

### Testing:
# print mergeSort([1, 0])
# print mergeSort([1, 4, 3, 0, 10, 5])
# print mergeSort([1, 4, 3, 0, 10, 51, 4, 3, 0, 10, 5])


################ BINARY SEARCH ################

def binarySearch(lst, num):
    """
    Given a sorted list (ascending), and a given number, returns True if
    the number is in the list. Returns False otherwise.
    """
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        if lst[0] == num:
            return True
        return False
    else:
        middle = len(lst) / 2
        if lst[middle] == num:
            return True
        elif lst[middle] < num:
            return binarySearch(lst[middle: len(lst)], num)
        elif lst[middle] > num:
            return binarySearch(lst[0: middle], num)

# print binarySearch([0, 0, 1, 3, 3, 4, 4, 5, 10, 10, 51], 7)
# print binarySearch([0, 0, 1, 3, 3, 4, 4, 5, 10, 10, 51], 51)
# print binarySearch([], 3)

def listSearch(lst, num):
    """
    Combines mergeSort and binarySearch to search lst for element num.
    """
    sorted = mergeSort(lst)
    return binarySearch(sorted, num)


################ GRAPH SEARCH ################

class Queue:
    """
    Represents a FIFO queue.
    """
    def __init__(self, lst=None):
        """
        Constructs a queue.
        If no lst is given, creates an empty queue.
        """
        self.__list = lst
    def __str__(self):
        """
        Prints the queue.
        """
        print (self.__list)

    def push(self, elem):
        """
        Pushes element elemn onto queue.
        """
        self.__list.append(elem)
    def pop(self):
        """
        Pops an element from the queue.
        """
        return self.__list.pop(0)
    def len(self):
        return len(self.__list)


def bfs(g, i):
    """
    Takes in a graph in adjacency list form, and a starting node i.
    Runs BFS on the graph g.
    Returns a dictionary mapping all nodes to True if visited, False otherwise.
    """
    seen = {}
    for node in g:
        seen[node] = False
    q = Queue
    q.push(i)
    while len(q) > 0:
        currentnode = q.pop()
        for nbr in g[currentnode]:
            seen[nbr] = True
            q.push(nbr)
    return seen


### Testing:
def testSort():
    num = int(input())

    array = []
    for x in range(num):
        array.append(int(input()))

    x = mergeSort(array)
    for i in x:
        print (i)

    
# testSort()