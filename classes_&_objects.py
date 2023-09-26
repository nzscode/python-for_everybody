class name_of_class:
    var1 = 0

    def method1(self):
        self.var1 = self.var1 + 1
        print("so far: ", self.var1)

object1 = name_of_class()

object1.method1()
object1.method1()
object1.method1()
object1.method1()

print("Type Object1: ", type(object1))
print("Dir Object1: ", dir(object1))
