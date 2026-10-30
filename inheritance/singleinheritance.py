
class Father:
    def show(self):
        print("This is Father class")

class Son(Father):
    def display(self):
        print("This is Son class")

obj = Son()
obj.show()
obj.display()
