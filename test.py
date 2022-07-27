import time

def delay_dec(function):
    time.sleep(2)
    function()


@delay_dec
def say_hello():
    print("hello")


print('wait')
say_hello()