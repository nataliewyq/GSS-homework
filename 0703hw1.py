print('enter your score:')
score=int(input())
if score >=0 and score<=100:
    print('score valid')
    if score>=91 and score <=100:
        print('your letter grade is A')
    if score>=81 and score<=90:
        print ('your letter grade is B')
    if score>=71 and score<=80:
        print('your letter grade is C')
    if score>=61 and score<=70:
        print('your letter grade is D')
    if score<=60 and score>=0:
        print('your letter grade is F')
else:
    print('score invalid')