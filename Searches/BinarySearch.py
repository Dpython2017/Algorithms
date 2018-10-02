#!/usr/bin/env python
"""
Binary Search works on sorted array. Once the array is sorted in ascending order, then the mid point of
the list is calculated. If the value of search element is less than the mid-point the search is done within the
index [0:mid-pint] if the search element is greater than the mid in that case search is done within[m:len(data)]
"""
class BinarySearch(object):
    def __init__(self,data):
        if len(data) > 0:
            if sorted(data) == data:
                print 'Sorted List'
            else:
                print'Sorting the list...\n'
                data= sorted(data)
            self.data = data
        else:
            raise ValueError("The List is empty")

    def search(self,ele):
        """
        Calulating the mid element: if the search element is less than the mid element
        in that case the search will be within data[0]:data[m]{ where 'm'  is the index of middle element }

        """
        m = (len(self.data)/2)
        if data[m] == ele:
            print 'Found the search element: {} \nAt index: {}'.format(self.data[m],m)
        elif ele < data[m]:
           index = self.found(0,m,ele)
           if index > 0:
               print 'Found the search element: {} \nAt index: {}'.format(self.data[index], index)
           else:
               print 'Search element: {} not found in the list.'.format(ele)
        elif ele > data[m]:
            index = self.found(m,len(self.data),ele)
            if index > 0:
                print 'Found the search element: {} \nAt index: {}'.format(self.data[index], index)
            else:
                print 'Search element: {} not found in the list.'.format(ele)

    def found(self,start, end, ele):
        for i in range(start, end):
            if ele == self.data[i]:
                return i


data = [1,11,3,4,5]
obj = BinarySearch(data)
ele =11
obj.search(ele)
