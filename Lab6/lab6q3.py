def sum_even_numbers(start,end):
    return sum(num for num in range(start,end+1) if num%2==0)
start=1
end=10
result=sum_even_numbers(start,end)
print(f"Sum of even numbers between {start} and {end} : {result}")
