from random import shuffle
from heapq import heappop, heappush
import csv
from datetime import datetime, timedelta

mdma = ["Max", "Dom", "Miles", "Avi"]
today = datetime.now() # this was written on a Sunday morning
start_monday = today + timedelta(days=1) # person gets spot for full weekend if weeks start on Mon

all_equal = False
while(not all_equal):
    mdma_heap = [(0, person) for person in mdma]
    biweeks = [["Week","Spot 1","Spot 2"]] # first row is column headers
    for i in range(int((52 - 4)/2)): # 4 weeks since move-in, generate for biweeks starting 9/13/21
        shuffle(mdma_heap) # reorder heap every 4 weeks, more random
        biweek = [(start_monday+timedelta(days=(i*14))).strftime("%m/%d/%Y")] # first col is week
        for j in range(2):
            (sum_biweeks, person) = heappop(mdma_heap)
            biweek.append(person)
            heappush(mdma_heap, (sum_biweeks+1, person))
        biweeks.append(biweek)
    all_equal = True # assume True until one value is False
    for k in range(4):
        all_equal = all_equal and (mdma_heap[k][0] == 12)

with open("schedule.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(biweeks)

