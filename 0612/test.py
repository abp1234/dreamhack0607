N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1],x[0]),reverse=True)

time=arr[0][1]
for i in range(N):
    if time>=0:
        if time<=arr[i][1]:
            time=time-arr[i][0]
        else:
            time=arr[i][1]-arr[i][0]
        if time<0:
            time=-1
            break
    else:
        time=-1
        break
print(time)
