# def sumofarray(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# numberslist = [1,2,3,4,5,6]
# print(sumofarray(numberslist))


#Largest numbers in array

def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    
    return largest

number_list = [1,2,56,78,90]
print(find_largest_number(number_list))
