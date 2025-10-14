def search(lst):
    counter = {} # create a dictionary to keep track of the frequency of each integer
    for num in lst:
        counter[num] = counter.get(num, 0) + 1 # count the number of times each integer appears in the list
    candidates = [num for num in counter if num == counter[num] and num > 0] # create a list of integers with frequency greater than or equal to the integer itself and greater than zero
    if candidates:
        return max(candidates) # return the greatest integer from the list of candidates
    else:
        return -1 # if no such a value exists, return -1
