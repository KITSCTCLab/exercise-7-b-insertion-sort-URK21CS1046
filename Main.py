from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  in = 0
  for(int i = 1;i<array.length;i++): 
    for(int j = in;arr.length;j++):
      if arra[i] > array[j]:
        temp = array[j]
        array[j] = array[i]
        array[i] = temp
      else:
        continue
    return array
  

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
