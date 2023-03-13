L, N = list(map(int, input().split()))
lst = list(map(int, input().split()))
def length(n, lst, lst0, dist0, N, m):
    if n > N-1:
        return 0
    else:
        if n == 0:
            m += 1
        for i in range(len(lst0)-1):
            lst0[i+1] += lst0[i]
        num = lst0[-1]
        dist1 = [0]*num
        dist1[0] = -(num - 1)
        for i in range(1, num):
            dist1[i] = dist1[i-1] + 2
        lst1 = [0]*num
        for i in range(num):
            j = m%L
            lst1[i] = lst[j]
            m += 1
        sum_distance = 0
        for i in range(len(lst0)):
            if i == 0:
                for j in range(lst0[i]):
                    if lst0[i] == 0:
                        continue
                    else:
                        sum_distance += ((dist1[j] - dist0[i])**2 + 4)**(0.5)
            else:
                for j in range(lst0[i-1], lst0[i]):
                    if lst0[i-1] == lst0[i]:
                        continue
                    else:
                        sum_distance += ((dist1[j] - dist0[i])**2 + 4)**(0.5)
    return sum_distance + length(n+1, lst, lst1, dist1, N, m)
value = (length(0, lst, [lst[0]], [0], N, 0))
print(int(value) + 1)

        

        


            

