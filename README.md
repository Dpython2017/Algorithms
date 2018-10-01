# Algorithms
This Repo contains solutions to various Algorithms in python     
#SEARCH
##Linear Search
Let there be a given list called as list1. The ist contains elements, let them be integer by default.
 list1 = [1,2,3,4,5]
 let there be a search element called as ele. Let ele be assigned to some value
 
###***Working of linear search***

Search        | List 
------------- | -------------
ele=3         | list1[0] = 1
 
 The first value of the list if checked with the search element value if it matches it returns the position at which the value is found else goes to the next index of the list__

  Search        | List 
------------- | -------------
ele=3         | list1[1] = 2
 ...
 Ans so on until the value is found. If the value is not present in the list. It displays Value not found in the list.
 
 ###Code:
 ```buildoutcfg
    found = [i for i in range(len(data)) if data[i] == ele]
```
 
