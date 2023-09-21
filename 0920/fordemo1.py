# count, line = 0, 1
# for i in range(65, 91) :
#     if line % 2 == 1 :print(chr(i), end = '\t')
#     else : print(chr(i+32), end = '\t')
#     count += 1
#     if count % 5 == 0 :
#          print()
#          line += 1
# print()

scores = [70, 65, 55, 75, 85, 90, 90, 80, 80, 45]
total_score = 0
for score in scores :
    total_score += score
    
num_students = len(scores)
average_score = total_score / num_students
print('평균점수는', average_score)