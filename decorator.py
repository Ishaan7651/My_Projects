def greet(fx):
    def mfx(*args):
        print("Hello")
        fx(*args)
        print("Goodbye")

    return mfx


@greet
def say_hello():
    print("Hello World")

@greet
def add(x,y):
    print (x+y)

say_hello()
add(2,5)