# lst = ['a', 'b', 'c', None, 'd', 'e']
# for item in lst:
#     print(item)

class send:
    def __iter__(self):
        lst = ['a', 'b', 'c', 'd']
        for item in lst:
            yield item

send1 = send()
i = 10
for item in send1:
    i = i-1
    if i == 0:
        break
    print(item)