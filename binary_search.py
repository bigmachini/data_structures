def binary_search_recursive(_list, search_value, l, h):
    if l >= h:
        return -1
    else:
        mid = (l + h) // 2
        if _list[mid] == search_value:
            return mid
        elif _list[mid] > search_value:
            h = mid - 1
        else:
            l = mid + 1

        return binary_search_recursive(_list, search_value, l, h)


def binary_search_iterative(_list, search_value):
    l = 1
    h = len(_list)
    while l < h:
        mid = (l + h) // 2
        if _list[mid] == search_value:
            return mid
        elif _list[mid] > search_value:
            h = mid - 1
        else:
            l = mid + 1
    return -1


x = range(0, 100, 7)

y = binary_search_recursive(list(x), 777, 0, len(x))
z = binary_search_iterative(list(x), 777)

print(list(x)[y])
print(list(x)[z])
