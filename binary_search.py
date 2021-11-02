def binary_search_recursive(_list, search_value, l, h):
    if h - l == 1:
        if _list[l] == search_value:
            return l
        elif _list[h] == search_value:
            return h
        else:
            return -1
    else:
        mid = (l + h) // 2
        if _list[mid] > search_value:
            h = mid
        else:
            l = mid

        return binary_search_recursive(_list, search_value, l, h)


def binary_search_iterative(_list, search_value):
    l = 0
    h = len(_list)-1
    while h - l > 0:
        if h - l == 1:
            if _list[l] == search_value:
                return l
            elif _list[h] == search_value:
                return h
            else:
                return -1
        else:
            mid = (l + h) // 2
            if _list[mid] > search_value:
                h = mid
            else:
                l = mid


x = range(0, 100, 7)

y = binary_search_recursive(list(x), 777, 0, len(x) - 1)
z = binary_search_iterative(list(x), 777)

print(list(x)[y])
print(list(x)[z])

