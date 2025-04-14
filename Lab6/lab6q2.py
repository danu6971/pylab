def count_even_odd(numbers):
    even_count=sum(1 for num in numbers if num %2==0)
    odd_count=len(numbers)- even_count
    return even_count,odd_count
num_list=[1,2,3,4,5,6]
evens,odds=count_even_odd(num_list)
print(f"Even numbers:{evens},Odd numbers:{odds}")
