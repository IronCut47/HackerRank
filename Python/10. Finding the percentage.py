if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    named = student_marks[query_name]
    temp = 0
    for i in range(0, len(named)):
        temp = temp + named[i]
    avg = temp/len(named)
    print('%.2f' % avg)