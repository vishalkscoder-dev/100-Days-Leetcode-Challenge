import os
os.system('cls')


def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
        
    petrol = 0
    start = 0

    for i in range(len(gas)):
        petrol += gas[i]
        petrol -= cost[i]

        if petrol < 0:
            petrol = 0
            start = i + 1

    return start

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(canCompleteCircuit(gas, cost))