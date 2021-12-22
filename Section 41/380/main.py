activites = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9]
]

def printMaxActivites(activites):
    activites.sort(key=lambda x: x[2])
    i = 0
    firstA = activites[i][0]
    print(firstA)
    for j in range(len(activites)):
        # if start time of next activity that is j is greater
        # than end time of previous selected activity that is i
        if activites[j][1] > activites[i][2]:
            print(activites[j][0])
            i = j

printMaxActivites(activites)