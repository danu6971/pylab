def find_largest(lst):
    if not lst:  
        return None  
    largest = lst[0]  


    for number in lst:
        if number > largest:
            largest = number  

    return largest  


numbers = [10, 20, 5, 8, 25, 3]
largest_number = find_largest(numbers)
print(f"The largest number is: {largest_number}")
