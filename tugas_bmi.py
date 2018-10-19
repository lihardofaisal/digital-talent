weight = eval(input('masukkan berat badan anda '))
height = eval(input('masukkan tinggi badan anda (dalam cm) '))
height = height/100
bmi = weight/(height*height)
print(bmi)

if bmi<15:
    print('Very severely underweight')
elif 15<=bmi and bmi<16:
    print('Severely underweight')
elif 16<=bmi and bmi<18.5:
    print('Underweight')
elif 18.5<=bmi and bmi<25:
    print("Normal (healthy weight)")
elif 25<=bmi and bmi<30:
    print('Overweight')
elif 30<=bmi and bmi<35:
    print('Moderately obese')
elif 35<=bmi and bmi<40:
    print('Severely obese')
else :
    print('Very severely obese')
