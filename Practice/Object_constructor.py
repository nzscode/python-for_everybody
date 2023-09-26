class name_of_class:
    var1 = 0

    def __init__(self):
        print("initializing object")

    def add(self):
        self.var1 = self.var1 + 1
        print("var1 value: ", self.var1)

    def __del__(self):
        print("destructuring var1", self.var1)


object1 = name_of_class()
object1.add()
object1.add()
object1.add()
object1 = 15
print('object1 contains', object1)