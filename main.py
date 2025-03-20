numra1 = [1,2,3,4,4,5,6,7,7,7,7,8]

unique_list = list(set(numra1)) #kthen kllapat ne liste ne terminal

print(unique_list)

#for loop

numra = [1,2,3,4,5,6,7,8,9]

for num in numra:
    if num %2 == 0:
        print(num)

for num in numra:
    if num %2 == 1:
        print(num)


first_name = "Blend"

for char in first_name:
    print(char)


dictionary_names = {
    "Blend" : 4,
    "Suela" : 5,
    "Darsej": 1,
    "Leoni" : 3
}

total_sum = 0



for val in dictionary_names.values():
    print(val)
    total_sum += val
    print("Shuma totale eshte:", total_sum)

for value in dictionary_names.keys():
    print(value)

for i in range(1,10):
    print(i)


numrat = [1,42,5,21,4,5,67,12,0,-5,10]

largest_number = numrat[0] #1

for nums in numrat:
    #42 > #1
    if nums>largest_number:
        largest_number = nums
        print(nums)


smallest_number = numrat[6]

for number in numrat:
    if number<smallest_number:
        smallest_number = number
        print(number)


#while loop

count = 0

while count <= 5:
    print(count)
    count += 1