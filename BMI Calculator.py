
def usr_weight():
    while True:
        try:
            weight=float(input('Enter your weight: '))

        except ValueError:
            print('Incorrect Value, please try again')
            continue
        else:
            break
    return weight

def usr_height():
    while True:
        print('Enter your Height:')
        try:
            feet=float(input('Feet: '))
            inches=float(input('Inches: '))

        except ValueError:
            print('Incorrect Value, please try again')
            continue
        else:
            break
    Height = feet*12 + inches
    return Height

def calculation(): 
    weight=usr_weight()
    height=usr_height()
    BMI = float(703*weight/(height**2))
    return BMI


def BMI_output():
    BMI=calculation()
    if BMI < 18.5:
        print('Your BMI is %.1f' %BMI)
        print('You are considered underweight')
    elif BMI >= 18.5 and BMI < 25:
        print('Your BMI is %.1f ' %BMI)
        print('You are considered a Normal Weight')
    elif BMI >= 25 and BMI < 30:
        print('Your BMI is %.1f' %BMI)
        print('You are considered overweight')
    elif BMI >= 30:
        print('Your BMI is %.1f ' %BMI)
        print('You are considered Obese')

BMI_output()