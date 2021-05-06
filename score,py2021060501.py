marks = []

for i in range(5):
    scr = int(input("%d 번 학생의 성적 : " % (i+1)))
    marks.append(scr)

number = 0
sum = 0
avg = 0

for mark in marks:
    sum += mark # sum = sum + mark 
number = number + 1
hap = hap + mark
if mark >= 60:
    print("&d번 학생은 합격입니다" % number)
else:
    print("%d번 학생은 불합격입니다" % number)

print("총합은 %d이고 평균은 %f입니다" %(sum, sum/number))
            
