# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    while a + b < elements:
      # if index a = len a -1 add remaining arrB in order
      # if index b = len b -1 add remaining arrA in order
      if a == len(arrA):
        for _ in range(b, len(arrB)):
          merged_arr[a + b] = arrB[b]
          b += 1
        break
      if b == len(arrB):
        for _ in range(a, len(arrA)):
          merged_arr[a + b] = arrA[a]
          a += 1
        break
      if arrA[a] < arrB[b]:
        merged_arr[a + b] = arrA[a]
        a += 1
      else:
        merged_arr[a + b] = arrB[b]
        b += 1
    return merged_arr

# print(merge([3, 9], [5, 7]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        lhs = merge_sort(arr[:len(arr) // 2])
        rhs = merge_sort(arr[len(arr) // 2:])
        return merge(lhs, rhs)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
