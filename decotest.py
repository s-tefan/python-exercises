def my_decorator(func):
    def mupp():
        print("Start!")
        func()
        print("Mål!")
    return mupp

def sägnåt():
    print("Raj!")

sägnåt()
sägnåt = my_decorator(sägnåt)
sägnåt()

@my_decorator
def sägnåtannat():
    print("Nåt annat!")

sägnåtannat()

