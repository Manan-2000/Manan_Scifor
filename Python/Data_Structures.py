#Even elements in single list without repeatition
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
res=[]
for i in l1:
    if i%2==0:
        res.append(i)
for i in l2:
    if i%2==0:
        res.append(i)
res=set(res)
print(list(res))

#Occurance of each element
l = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for i in l:
    d[i]=l.count(i)
print(d)

#Elements and their Squares tigether
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = zip(first_list, second_list)
result_set = set(result)
print(result_set)