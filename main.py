import os
class CBNC:
    def __init__(self,name,age,gender,height,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

        self.food_calories = {
            "Milk": 100,
            "Egg": 155,
            "Rice": 130,
            "Lentils": 113,
            "Vegetable": 85,
            "Meat": 143
        }
    
    def calculateBmi(self):
        try:
            bmi = self.weight / (self.height ** 2)*703
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

    def dailyCalConsumption(self,meals):
        total_calories = 0
        for food, quantity in meals.items():
            if food in self.food_calories:
                calories_per_100g = self.food_calories[food]
                calories_eaten = quantity / 100 * calories_per_100g
                total_calories += calories_eaten
            else:
                return f"{food} not available in datalist"
        return total_calories
    
    def isChildUndernourished (self):
        bmi = self.calculateBmi()
        if(bmi<16):
            return "Severely Underweight" 
        elif(bmi>=16 and bmi<18.5):
            return "Underweight"
        elif(bmi>=18.5 and bmi<25):
            return "Healthy"
        elif(bmi>=25 and bmi<30):
            return "Overweight"
        elif(bmi>=30):
            return "Obese"
        else:
            return "Wrong BMI value"



# driver code
if __name__ == "__main__":
    print("\t\t\t\tChild Nutrients Calculator\n\n")

    cName = input("Enter your child's name : ")
    while True:
        cAge = int(input("Enter your child's age : "))
        if(cAge>=0 and cAge<=8):
            break
        else:
            print("The age must be between 0-8 years")
            continue
    cGender = input("Enter your child's gender : ")
    cHeight = int(input("Enter your child's Height (in inches): "))
    cWeight = int(input("Enter your child's weight (in pounds): "))

    childBaseNutrientsCalculator = CBNC(cName,cAge,cGender,cHeight,cWeight)

    print("\n\n")
    print("\t\tWhat number of times the child has eaten durnig the day")
    mealCount = int(input("Enter meal counts :  "))
    print("\n\n")

    meal_data = {
        input(f"Enter the meal name : ").capitalize(): float(input("Enter the quantity in grams(g): "))
        for _ in range(mealCount)
    }

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("\t\t\t\tChild Nutrients and Data\n\n")

    print(f"Your child's name : {cName}")
    print(f"Your child's age : {cAge}")
    print(f"Your child's gender : {cGender}")
    print(f"Your child's Height : {cHeight}inches")
    print(f"Your child's weight : {cWeight}lbs")

    print("\n\nChild's dail meal------\n")
    tempMealCount=1
    for food,quantity in meal_data.items():
        print(f"Meal {tempMealCount} : {food} {quantity}g")
        tempMealCount+=1
    print("--------------\n\n")

    print(f"Child's BMI : {childBaseNutrientsCalculator.calculateBmi()} \n")
    print(f"Your Child's calories intake : {childBaseNutrientsCalculator.calculateBmi()} \n")
    print(f"Calories intake for a {cAge}yo Child's : {childBaseNutrientsCalculator.minimunCalReq()} or higher\n")
    print(f"Your Child is : {childBaseNutrientsCalculator.isChildUndernourished()} \n")