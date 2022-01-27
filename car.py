class Car (object):
    def __init__ (self,model,color,speed_limit,company):
        self.model=model
        self.color=color
        self.speed_limit=speed_limit
        self.company=company
    def Start (self):
        print("Started")
    def Stop (self):
        print("Stopped")
    def Accelerate (self):
        print("Accelerated")
    def Change_Gear (self):
        print("Gear Changed")
Audi=Car("A6","Red","Audi","80")
print(Audi.color)
