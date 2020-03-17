# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    arrCopy = arr[:]

    for i in range(0, len(arrCopy) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i, len(arrCopy)):
            if arrCopy[j] < arrCopy[smallest_index]:
                smallest_index = j
        arrCopy[i], arrCopy[smallest_index] = arrCopy[smallest_index], arrCopy[i]

    return arrCopy


# TO-DO:  implement the Bubble Sort function below

# go through list

def bubble_sort(arr):
    # for i in range(0, len(arr) - 1):
    #     if arr[i] > arr[i + 1]:
    #         arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #         bubble_sort(arr)
    arrCopy = arr[:]
    for i in range(0, len(arrCopy) - 1):
      for j in range(0, len(arrCopy) - 1 - i):
        if arrCopy[j] > arrCopy[j + 1]:
          arrCopy[j], arrCopy[j + 1] = arrCopy[j + 1], arrCopy[j]
          


    return arrCopy

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) < 2:
      return arr
    if maximum < 0:
      maximum = max(arr)
    # Take a count array to store the count of each unique object.
    count = [0] * (maximum + 1)
    for i in arr:
      if i < 0:
        return 'Error, negative numbers not allowed in Count Sort'
      count[i] += 1
    # Modify the count array such that each element at each index stores the sum of previous counts.
    for i in range(0, len(count)):
      if i:
        count[i] += count[i - 1]

    # Output each object from the input sequence followed by decreasing its count by 1.
    output = [0] * len(arr)
    for i in arr:
      output[count[i] - 1] = i
      count[i] -= 1
    return output

print(count_sort([1, 5, 4, 4, 7, 9, 2, 3, 3]))