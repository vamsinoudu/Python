class Dog():
    def bark(self):
        height = 10
        weight = 20
        print("Dog height and weight:", height, weight)

    def run(self):
        print("dog can eat NV ")


obj = Dog()

obj.bark()
obj.run()


# with constructor

class myDog():
    def __init__(self, sound):
        self.sound = sound

    def run(self):
        pace = "Runs faster like Cheetah and "
        print(pace + self.sound)


obj = myDog("Barks louder")
obj.run()
