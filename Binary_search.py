def Binary_search(array, query):
    low = 0 
    high = len(array) - 1
    while low <= high:
          mid = (low + high) // 2
          if array[mid] == query:
             return "the number is found in the array at index : {}".format(mid)
          elif array[mid] < query:
              low = mid + 1
          elif array[mid] > query:
              high = mid -1
    return "the number is not in the array"
arr = [i for i in range(0, 10000000)] 
Query = input("Enter the Number you want to check in the array :")
try:
    Query = int(Query)
except ValueError:
    print("Invalid input. Please enter an integer")
print(Binary_search(arr, Query))
