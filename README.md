# Algorithms
This Repo contains solutions to various Algorithms in python     
# SEARCH  
## Linear Search  

Let there be a iterable list called as **list1**.let them be integer by default.  
let there be a search element called as **ele**. Let ele be assigned to some value 
>list1 = [ 1, 2, 3, 4, 5 ]  
>ele = 3 
 
***Working of linear search***

Search        | List 
------------- | -------------
ele=3         | list1[0] = 1
 
 The first value of the list if checked with the search element value if it matches it returns the position at which the value is found else goes to the next index of the list  

  Search        | List 
------------- | -------------
ele=3         | list1[1] = 2  
  
  
 Ans so on until the value is found. If the value is not present in the list. It displays Value not found in the list.
 
 ### Code:
 ```buildoutcfg
    found = [i for i in range(len(data)) if data[i] == ele]
```
 ### Time Complexity  
   
 ***Best Case*** : O(1)  
 ***Average Case*** : O(N/2)  
 ***Worst Case*** : O(N)  
   
     
     
## Binary Search  
Binary Search works on sorted arrays. The sorted array is divided into half and based on value of search element the values is searched in one of the two halves.  
 Mind point is calulated m = len(data)/2  
 >if data[m] > ele  
 >if data[m] < ele  
 >if data[m] == ele  
 
###Code
```buildoutcfg
    def found(self,start, end, ele):
        for i in range(start, end):
            if ele == self.data[i]:
                return i
```  
 ### Time Complexity  
   
 ***Best Case*** : O(1)  
 ***Average Case*** : O(log n)  
 ***Worst Case*** : O(log n)