#打印1～20

for i in range(1,21):
    print(i)


#创建一个1-100的列表，在使用for循环打印
one_hundred_list = list(range(1,101))
for i in one_hundred_list:
    print(i)


heji_sum = sum(one_hundred_list)
print(heji_sum)


#只有奇数1-20
for i in range(1,21,2):
    print(i)

#只有3的倍数3-30
for i in range(3,31,3):
    print(i)