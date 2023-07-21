

start = int(input ('Enter first number'))
end = int(input ('Enter second number'))

def multiplication(start,end):
    for x in range (start,end+1):
        for y in range (1,11):
            print(f"{x} X {y} = {x*y}")

        print ('---------')

multiplication(start,end)
