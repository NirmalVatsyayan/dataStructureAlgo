
'''
The program is to find is there any combination 2 numbers in an array
with sum equals to any given sum

It will print all combinations

'''

CONST_MAX = 10000

def find_val(arr, size, sum_req):
    bitmap = [0]*CONST_MAX
    found = False
    for i in range(0, size):
        temp = sum_req - arr[i]

        if temp >= 0 and bitmap[temp] == 1:
            print("[PAIR] ",temp, "  >>> ", arr[i])
            found = True
            
        bitmap[arr[i]] = 1
    
    if not found:
        print("No pair found")



data = [1,5,7,33,11,0,99,443, 20, 24]
sum_req = 44

find_val(data, len(data), sum_req)

