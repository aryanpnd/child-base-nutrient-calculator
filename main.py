import os  # Importing

# Initialize the CBNC class
class CBNC:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

        # Define a dictionary to store the calorie content of different foods
        self.food_calories = {
            "Milk": 100,
            "Egg": 155,
            "Rice": 130,
            "Lentils": 113,
            "Vegetable": 85,
            "Meat": 143
        }

    # Calculate BMI 
    def calculateBmi(self):
        try:
            bmi = self.weight / (self.height ** 2) * 703
            return round(bmi, 2)
        except ZeroDivisionError:
            return "Error: Height cannot be zero."


    # Calculate the minimum calorie requirement 
    def minimunCalReq(self):
        try:
            if self.age > 0 and self.age <= 3:
                return 800
            elif self.age >= 2 and self.age <= 4:
                return 1400
            elif self.age >= 4 and self.age <= 8:
                return 1800
            else:
                return "You're not a child"
        except e:
            return e

    # Calculate the total calories consumed 
    def dailyCalConsumption(self, meals):
        total_calories = 0
        for food, quantity in meals.items():
            if food in self.food_calories:
                calories_per_100g = self.food_calories[food]
                calories_eaten = quantity / 100 * calories_per_100g
                total_calories += calories_eaten
            else:
                return f"{food} not available in datalist"
        return total_calories

    # Check if the child is undernourished based on BMI
    def isChildUndernourished(self):
        bmi = self.calculateBmi()
        if bmi < 16:
            return "Severely Underweight"
        elif 16 <= bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Healthy"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif bmi >= 30:
            return "Obese"
        else:
            return "Wrong BMI value"


# driver code
if __name__ == "__main__":
    print("\t\t\t\tChild Nutrients Calculator\n\n")

    # taking child's information from the user
    cName = input("Enter your child's name: ")
    while True:
        cAge = int(input("Enter your child's age: "))
        if 0 <= cAge <= 8:
            break
        else:
            print("The age must be between 0-8 years")
            continue
    cGender = input("Enter your child's gender: ")
    cHeight = int(input("Enter your child's Height (in inches): "))
    cWeight = int(input("Enter your child's weight (in pounds): "))

    # Create an instance of CBNC class with the given child's information
    childBaseNutrientsCalculator = CBNC(cName, cAge, cGender, cHeight, cWeight)

    # Gather meal data from the user
    print("\n\n")
    print("\t\tWhat number of times the child has eaten during the day")
    mealCount = int(input("Enter meal counts: "))
    print("\n\n")

    meal_data = {
        input(f"Enter the meal name: ").capitalize(): float(input("Enter the quantity in grams(g): "))
        for _ in range(mealCount)
    }

    # Clear the terminal screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("\t\t\t\tChild Nutrients and Data\n\n")

    # Print the child's information and meal data
    print(f"Your child's name: {cName}")
    print(f"Your child's age: {cAge}")
    print(f"Your child's gender: {cGender}")
    print(f"Your child's Height: {cHeight} inches")
    print(f"Your child's weight: {cWeight} lbs")

    print("\n\nChild's daily meal------\n")
    tempMealCount = 1
    for food, quantity in meal_data.items():
        print(f"Meal {tempMealCount}: {food} {quantity}g")
        tempMealCount += 1
    print("--------------\n\n")

    # Calculate and display the child's BMI and calorie-related information
    print(f"Child's BMI: {childBaseNutrientsCalculator.calculateBmi()}\n")
    print(f"Your Child's calories intake: {childBaseNutrientsCalculator.calculateBmi()}\n")
    print(f"Calories intake for a {cAge}yo Child's: {childBaseNutrientsCalculator.minimunCalReq()} or higher\n")
    print(f"Your Child is: {childBaseNutrientsCalculator.isChildUndernourished()}\n")
