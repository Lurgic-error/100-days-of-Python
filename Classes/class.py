
class Lurgic: 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("lurge created")    
    
    def displayAge(self):
        print(self.name + " is " + str(self.age) + " years old")
        
    def canJump(self):
        if(self.age <= 18): 
            print(self.name + ' can not jump')
        else:
            print(self.name + " can jump")
    
        

lurge = Lurgic("Captain", 12)

print(lurge.age)

lurge.displayAge()

lurge.canJump()