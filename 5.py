#kataryal tiv
nums = []
for i in range(1, 10000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        nums.append(i)
print(nums)


#with comprehension



#print([i for i in range(2, 10000) if i == sum(j for j in range(1, i) if i % j == 0)])
