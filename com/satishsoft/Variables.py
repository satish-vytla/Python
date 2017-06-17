#global myvar = 'something'
class Variables:
    #pass
    #global gc
    temp=5

    def __init__(self):
        self.object_elem = 456


    #global myvar = 'something'
    def m1(self):
        gc="cddcdcdcdcdcdcdcdcd"
        print("M1 Methode Dude")
        print(self.temp)
        global b
        b=10
        print(b)
        c=12
        print(c)
        self.object_elem=10000
        print(self.object_elem)

    def m2(self):
        print("M2 Methode Dude")
        print(b)
       # print(c)
        self.object_elem = 45622222
        print(self.object_elem)



obj1=Variables()
obj1.m1()
obj1.m2()


