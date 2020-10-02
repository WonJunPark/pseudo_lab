import random

questions = [
    '좋아하는 동물은? : ',
    '좋아하는 음식은? : ',
    '좋아하는 노래는? : ',
    '최근에 본 영화는? : ',
    '카레맛 똥 vs 똥맛 카레 :',
    '토마토맛 토 vs 토맛 토마토 :',
]

result = {}
count = 0

while count < 11: #11
    print('********** pseudo lab **********')
    print(count+1,'/ 11')
    name = input('이름을 입력해주세요 : ')

    count += 1

    ques = random.choice(questions)
#    k = input(ques)

    while 1:
        ran_num = random.randint(2,12)

        if ran_num not in result.keys():
            result[ran_num] = name
            break

    print('''
            . 　。　　　　•　 　ﾟ　　。
        　　.　　　.　　　 　　.　　　　　。　　
        　.　　 。　 ඞ 。　 . •
        • . {}님은 {}번째 발표입니다. 　 。　.
        　 　　。　　　　　　ﾟ　　　.　　　.
        ,　　　　.　 .　　 . 。
    '''.format(name,ran_num))


result = sorted(result.items())

print('********** pseudo lab **********')
print('1주차 - 오정환님')
for a,b in result:
    print(str(a)+'주차 - '+str(b)+'님')


