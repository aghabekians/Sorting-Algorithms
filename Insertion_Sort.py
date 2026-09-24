def Insertion_sort(lst1):
    lst=lst1.copy()

    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1

        while j>=0 and lst[j]>key:
            lst[j+1]=lst[j]
            j-=1

        lst[j+1]=key

    return lst

        

lst = [8,2,4,9,3,6]
l = Insertion_sort(lst)
print(f"{lst} -> {l}")

lst1=[36,45,-9,0,65,100,3,10]
l1=Insertion_sort(lst1)
print(f"{lst1} -> {l1}")