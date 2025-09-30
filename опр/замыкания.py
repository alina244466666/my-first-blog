'''def outer():
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)
    return inner
fn= outer()
fn()
fn()
fn()

def inner():
    nonlocal n
    n += 1
    print(n)
return inner
fn = outer()
fn()
fn()
fn()'''

def multiply(n):
    def inner(m): return n * m
    return inner
fn = multiply(1)
print(fn(5))
print(fn(8))
print(fn(5))

def multiply(n): return lambda m: n * m
fn = multiply(1)
print(fn(8))
print(fn(5))
print(fn(8))

