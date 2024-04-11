# sum all the integers from 1 to 20 except 10 and 11
s = 0
for i in range(1,21):
    if i == 10 or i == 11:
        continue
    s = s + i
print("sum is",s)