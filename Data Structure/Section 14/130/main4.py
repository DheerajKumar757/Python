class send:
    def __iter__(self):
        #lst = ['a', 'b', 'c', 'd']
        lst = ['a', 'b', 'c', 'd', None, 'e', 'f']
        i = 0
        while lst[i]:
            yield lst[i]
            i+=1
            if i==7:
                break

send1 = send()
i = 10
for item in send1:
    i = i-1
    if i == 0:
        break
    print(item)