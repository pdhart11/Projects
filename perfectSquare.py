import math
value = input("Enter N: ")
n_array = list(range(1,int(value)+1))
new_array = [math.ceil(((int(value))+1)/2)]
n_array.pop(new_array[0]-1)

new_array = [math.ceil(((int(value))+1)/2)]
n_array.pop(new_array[0]-1)
k = 0
counter = 0
while k < int(value) -1:
    counter += 1
    if counter > int(value):
        print("No solution found")
        print("Remaining numbers: " + str(n_array))
        break

    for j in range(len(n_array)-1, -1, -1):
        
        if (math.sqrt(new_array[k] + n_array[j])) - math.floor(math.sqrt(new_array[k] + n_array[j])) == 0:
            
            new_array.append(n_array[j])
            n_array.pop(j)
            k+=1
            break

print("Final result: " + str(new_array))
