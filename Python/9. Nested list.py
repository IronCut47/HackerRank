if __name__ == '__main__':
    names = []
    scores = []
    new = []
    for i in range(int(input())):
        name = input()
        score = float(input())

        names.append(name)
        scores.append(score)
    
    [new.append([names[i], scores[i]]) for i in range(0, len(names))]

    new.sort()

    score_new = list(set(scores))
    score_new.sort()

    for i in range(0, len(new)):
        temp = new[i]
        if temp[1] == score_new[1]:
            print(temp[0])