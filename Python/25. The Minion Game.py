def minion_game(string):
    s = ['A', 'E', 'I', 'O', 'U']
    
    def main(string):
        kevin_score, stuart_score = 0, 0

        for i in range(len(string)):
            if string[i] in s:
                kevin_score += len(string) - i
            else:
                stuart_score += len(string) - i
    
        return kevin_score, stuart_score
    
    kevin_score, stuart_score = main(string)
    
    if stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif kevin_score > stuart_score:
        print('Kevin', kevin_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)