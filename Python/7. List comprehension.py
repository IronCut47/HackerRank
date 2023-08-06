if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    main = []
    
#Multiple loops solution 
    # for i in range(0, x+1):
    #     for j in range(0, y+1):
    #         for k in range(0, z+1):
    #             temp = [i, j, k]
    #             if temp[0] + temp[1] + temp[2] != n:
    #                 main.append(temp)
    # print(main)

#List Comprehension 
    main = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(main)