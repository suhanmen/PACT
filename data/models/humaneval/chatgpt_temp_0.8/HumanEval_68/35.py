python
def pluck(arr):
    even_nodes = [node for node in arr if node % 2 == 0] # filter even nodes
    if not even_nodes: # if no even nodes, return empty list
        return []
    else:
        smallest_even = min(even_nodes) # get smallest even node
        smallest_even_index = arr.index(smallest_even) # get index of smallest even node
        return [smallest_even, smallest_even_index] # return smallest even node and its index
