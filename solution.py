def findMin(queue, start, finish):
    minimum = pow(10,9)
    for i in range(n, numOfCom):
        if queue[i] and queue[i] <= minimum:
            minimum = queue[i]
    return minimum


fi = open('./input.txt', 'r')
numOfCom = int(fi.readline().split()[0])

com = []

for line in fi:
    com.append(line.split())

queue = [None] * numOfCom
poped = [None] * numOfCom

j = 0
k = 0
n = 0

minimums = []

for i in range(0, numOfCom):
    if com[i][0] == "+":
        queue[j] = int(com[i][1])
        j += 1
    elif com[i][0] == "-":
        poped[k] = queue[n]
        n += 1
        k += 1
    else:
        minimums.append(findMin(queue, n, numOfCom))

fo = open('./output.txt', 'w')

for element in minimums:
    fo.write(str(element)+'\n')
