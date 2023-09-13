#Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

def multiply_list(numbers):
    result = 1
    for num in numbers :
        result *=num
    return result
list =( 8,2,3,-1,7)
result= multiply_list(list)
print( f"Output {result}")