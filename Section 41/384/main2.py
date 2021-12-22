class Item:
    def __init__(self, name, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
        self.name = name
        self.req = None

    

def knapsackProblem(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    print(items, [x.ratio for x in items])
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight 
            totalValue += i.value
            i.req = i.value
        else: 
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            i.req = value
            usedCapacity += unusedWeight
            totalValue += value
        if usedCapacity == capacity:
            break

    print("Total value obtained : " + str(totalValue))
    print([(x.name, x. req) for x in items])
    print(usedCapacity)

item1 = Item("A", 20, 100)
item2 = Item("B", 30, 120)
item3 = Item("C", 10, 60)
cList = [item1, item2, item3] # list of objects of same class

knapsackProblem(cList, 50)