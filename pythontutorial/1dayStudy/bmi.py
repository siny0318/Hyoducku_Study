tall = input("키를 입력해주세요:  ")
tall = int(tall)

weight = input("몸무게를 입력해주세요:  ")
weight = float(weight)

print("키 : {} , 몸무게: {}".format(tall,weight))

bmi = weight/(tall/100)**2
print("bmi 지수는 {0:.2f} 입니다.".format(bmi))
