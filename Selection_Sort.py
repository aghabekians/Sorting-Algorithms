def Selection_Sort(lst1):
    lst=lst1.copy()

    for j in range(len(lst)-1):
        minn=lst[j]
        min_index=j
        for i in range (j+1,len(lst)):
            if lst[i]<minn:
                minn=lst[i]
                min_index=i

        if minn!=lst[j]:
            lst[j],lst[min_index]=minn, lst[j]

    return lst

lst=[9,66,57,57,-6,-78,0]
lst_sorted=Selection_Sort(lst)
print(f"{lst} -> {lst_sorted}")