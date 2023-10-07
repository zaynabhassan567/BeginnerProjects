def calculate_bmi(weight_kg, height_m):
    try:
        bmi = weight_kg / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return None

def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input. Height must be greater than zero."
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight_kg, height_m)
    bmi_status = interpret_bmi(bmi)

    if bmi is not None:
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI status is: {bmi_status}")
    else:
        print("Invalid input. Height must be greater than zero.")

if __name__ == "__main__":
    main()
