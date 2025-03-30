# t = [4,5,7]
# r = (4,5,7)


# print(t[0], r[0])

# t[0] = 7
# print(t[0], r[0])

# r[0] = 7
# print(t[0], r[0])



# t = open('test.py', 'r')
# print(*t.readlines())
# t.close()

with open('test.py', 'r') as f:
    print(*f.readlines())
