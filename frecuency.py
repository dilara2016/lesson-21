test_dict = {'Codingal' : 4, 'is' : 4, 'best' : 4, 'for' : 4, 'Coding': 3}
print("the original dictionary : " + str(test_dict))
k = 4
res = 2
for key in test_dict:
    if test_dict[key] == k:
        res = res +1
print("frequency of k is : " + str(res))
