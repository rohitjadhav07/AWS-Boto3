rollnos={32,42,23,432,232,1}
print("initial: ",rollnos)
rollnos.add(65)
print("add: ",rollnos)
rollnos.remove(23)
print("remove: ",rollnos)
rollnos.discard(432)
print("discarded: ",rollnos)
sorted_rollnos=sorted(rollnos)
print("sorted: ",sorted_rollnos)    
for i in rollnos:
    if i%2==0:
        print(i)
    else:        
        print(i,"is odd")