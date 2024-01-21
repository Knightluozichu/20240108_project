# lst1 = [3, 1, 2], lst2 = [4, 5, 6], 程序实现: 把lst2中的元素添加到lst1中, 并对lst1进行降序排序
lst1 = [3, 1, 2]
lst2 = [4, 5, 6]
lst1.extend(lst2)
lst1.sort(reverse=True)
print(f"降序后的lst1 : {lst1}")


# lst1 = [1, 2], lst2 = [3, 4], lst3 = [5, 6], 程序实现: 把lst1, lst2作为元素添加到lst3中, 并求lst3的长度

lst1 = [1, 2]
lst2 = [3, 4]
lst3 = [5, 6]
lst3.extend([lst1, lst2])
print(f"lst3 : {lst3},\nlst3的长度: {len(lst3)}")

# lst = [1, 3, 2, 6, 4], 程序实现: 删除lst元素中的中位数（只考虑列表中元素个数为奇数的情况）

lst = [1, 3, 2, 6, 4]
lst.sort()
print(f"排序后的lst : {lst}")
lst.pop(int(len(lst) / 2))
print(f"删除中位数后的lst : {lst}")

# lst = [1, 3, 2, 6, 1, 1, 41], 程序实现: 求lst最后一个元素1的索引


lst = [1, 3, 2, 6, 1, 1, 41]


def lst_rIndex(lst, value):
    lst.reverse()
    return len(lst) - lst.index(value) - 1


print(f"lst最后一个元素1的索引 : {lst_rIndex(lst, 1)}")
