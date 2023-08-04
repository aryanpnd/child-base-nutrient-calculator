class CBNC:
    def __init__(self,name,age,gender,height,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def calculateBmi(self):
        try:
            bmi = self.weight / (self.height ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return "Error: Height cannot be zero."
    
    def minimunCalReq(self):
        try:
            if(self.age>0 and self.age<=3):
                return 800
            elif(self.age>=2 and self.age<=4):
                return 1400
            elif(self.age>=4 and self.age<=8):
                return 1800
            else:
                return "You're not a child"
        except e:
            return e                
    
    def dailyCalConsumption(self):

# driver code
if __name__ == "__main__":
    childBaseNutrientsCalculator = CBNC("Junior Aryan",5,"male",10,20)
    print(childBaseNutrientsCalculator.calculateBmi())