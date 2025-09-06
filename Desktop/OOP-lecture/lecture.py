class employee:
    def __init__(self,name,surname,age):
        print("__init__ is working...  ")
        self.name = name
        self.surname = surname
        self.age = age
    def __init__(self,Color,height):
        print("Seccond __init__ is working...  ")
        self.Color = Color 
        self.height = height

employee1 = employee("Ali","Veli","20")
print(employee1.name,employee1.surname,employee1.age)