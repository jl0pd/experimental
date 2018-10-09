def return_hi():
    return "hi"

def return_hello():
    return "hello"


def fib(n):
    a = 1
    b = 1

    yield b
    yield b

    for _ in range(n - 2):
        a, b = b, a+b
        yield b