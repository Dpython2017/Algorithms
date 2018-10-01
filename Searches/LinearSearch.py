#!/usr/bin/env python
"""
Implementing Linear Search: In this search the search element is checked
with each element of the list.

"""
class LinearSearch:
    """
    :param data: An itearble list for searching the values in
            ele: The search element

    :return : Position if the element is found
    """

    def __init__(self,data = []):
        if len(data) <= 0:
            raise ValueError('List is empty')
        self.data = data

    def searchData(self,ele):
        found = [i for i in range(len(data)) if data[i] == ele]
        if found:
            print 'Found at position: {}'.format(found)
        else:
            print'Not Found'

data = [1,2,3,4]
obj = LinearSearch(data)
obj.searchData(1)