from _7_10_BMIClass import BMI
def main():
    bmi1=BMI("doe",18,145,70)
    print("the BMI for",bmi1.getName(),"is",bmi1.getBMI(),bmi1.getStatus())
    bmi2=BMI("anna",50,215,70)
    print("the BMI for",bmi2.getName(),"is",bmi2.getBMI(),bmi2.getStatus())

main()