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


print(bubble_sort([1, 5, 2, 7, 6, 3]))
# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
