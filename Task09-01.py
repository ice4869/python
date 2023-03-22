#def f(a, b):
#    if a > b:
#        return a
#    return b


#def max_value(*args):
#    max_val = args[0]
#    for val in args:
#        max_val = f(val , max_val)
#    return max_val


#print(max_value(3,5))
#print(max_value(3,4,5))
#print(max_value(3,4,5,6,7))



a = 'A'

def f(b):
    a = 'AAA'
    c = 'C'
    print(a)
    print(b)
    print(c)
    return b

print(a)
print(f('B'))
print(a)
