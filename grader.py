f = open("sample_input.txt", "r")
#print(f.readline())
T = f.readline()
for i in range(int(T)):
    b = f.readline()
    students, questions = map(int,b.split())
    ans = f.readline()
    ans = [int(i) for i in ans.split()]
    scores = []
    for i in range(students):
        student = f.readline()
        student = [int(i) for i in student.split()]
        score = 0
        temp = 0
        for question in range(questions):
            if student[question] == ans[question]:
                temp += 1
                score += temp
            else:
                temp = 0

        scores.append(score)
    fin = max(scores) - min(scores)
    print(fin)