import random

print("로또 번호를 추첨하겠다.")

for i in range(5):
    lotto = random.sample(range(1,46),6)
    print(lotto)

y =  input ("y를 입력하시면 한번더 추첨")
if y == "y" :
    lotto = random.sample(range(1,46),6)
    print(lotto)


