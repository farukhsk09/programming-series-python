# bubble search works on sorted arrays by repeatedly splitting into two
# and searching them until the item is found


def bubble_sort(arr, l, r, item):
    # after l passes r we can conclude we didnt find the item
    if(r >= l):
        mid = int(l+(r-l)/2)
        if(arr[mid] < item):
            return bubble_sort(arr, mid+1, r, item)
        elif(arr[mid] == item):
            return mid
        else:
            return bubble_sort(arr, l, mid-1, item)
    return -1


print(bubble_sort([1, 2, 3, 5, 8, 9, 21, 23, 24, 25], 0, 9, 21))
