from datetime import datetime

def linear_search(array, query):
    position = 0
    while position < len(array):
          if array[position] == query:
             return "the number is found in the array at index : {}".format(position)
          position +=1
    return "the number is not in the array"

start_time = datetime.now()
arr = [i for i in range(0, 50)] 
Query = input("Enter the Number you want to check in the array :")
try:
    Query = int(Query)
except ValueError:
    print("Invalid input. Please enter an integer")
print(linear_search(arr, Query))
end_time = datetime.now()
print('Execution time : {}'.format(end_time - start_time))