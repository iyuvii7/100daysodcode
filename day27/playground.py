# unlimited positional arguments
# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)
#
# add(10,20,40,50,50)


# unlimited keyword arguments
# def add(n, **kw):
#     # print(kw)
#     # for key, value in kw.items():
#     #     print(value)
#     n += kw["add"]
#     n *= kw["multi"]
#     print(n)
#
# add(2, add=10, multi=120)

# class with unlimited keyword arguments
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")

car = Car(make="Nissan")
print(car.make)