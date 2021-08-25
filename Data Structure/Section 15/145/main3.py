lst = [1, 2, 3, 4, 5, 6, 7]

def returnchck():
    for item in lst:
        if item == 5:
            return 'hi'
        print(item)

print(returnchck())