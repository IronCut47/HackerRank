n,m = map(int, input().split())

def worker(n, m):
    for i in range(n // 2):    
        print((".|." * (2 * i + 1)).center(m, '-'))
    print(("WELCOME").center(m, '-'))
    for i in range((n // 2) - 1, -1, -1): #range(start(n//2)-1, stop(-1), step(-1))
        print((".|." * (2 * i + 1)).center(m, '-'))
        
worker(n,m)