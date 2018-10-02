#!/usr/bin/env python
class BinarySearch(object):
    def __init__(self,data):
        if len(data) > 0:
            if sorted(data) == data:
                print 'Not Sorted Sorted'
            else:
                print'Sorting the list...\n'
                data= sorted(data)
            self.data = data
        else:
            raise ValueError("The List is empty")

    def search(self,ele):
        print 'Binary Search In progess...\n'
        m = (len(self.data)/2)
        if data[m] == ele:
            print 'Found the search element: {} \nAt index: {}'.format(data[m],m)
        elif ele < data[m]:
            for i in range(0,m):
                if ele == self.data[i]:
                    print 'Found the search element: {} \nAt index: {}'.format(data[i], i)
        elif ele > data[m]:
            for i in range(m,len(self.data)):
                print self.data[i]
                if ele == self.data[i]:
                    print 'Found the search element: {} \nAt index: {}'.format(data[i], i)






data = [1,11,3,4,5]
obj = BinarySearch(data)
obj.search(11)
