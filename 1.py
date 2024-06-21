import heapq
diry=[0,0,-1,1]
dirx=[1,-1,0,0]
MAX_SIZE=65536
t=int(input())
while t:
    t-=1
    n=int(input())
    map_arr=[[0]*MAX_SIZE for _ in range(MAX_SIZE)]
    start=None
    for i in range(n+2):
        temp=map(int,input().split())
        if i==0:
            start=temp
        elif i==n+1:
            map_arr[temp[1]+32768][temp[0]+32768]='E'
        else:
            map_arr[temp[1]+32768][temp[0]+32768]='S'
    q=[]
    heapq.heappush(q,[0,start[0]*100000+start[1]])
    flag=0
    while q:
        
        temp=heapq.heappop(q)
        # if temp[0]<=0 and temp[2]>=49:continue
        for i in range(4):
            dy=diry[i]+temp[1]//100000
            dx=dirx[i]+temp[1]%100000
            if dy<0 or dx<0 or dy>=100000 or dx>=100000: continue
            if map_arr[dy][dx]=='S':
                flag=1
                print('happy')
                break
            elif map_arr[dy][dx]=='E':
                pass
            else:
                if temp[0]+1==50:
                    if map_arr[temp[1]//100000][temp[1]%100000]=='E':
                        if map_arr[dy][dx]>=19:continue
                        map_arr[dy][dx]=19
                    else:
                        if map_arr[dy][dx]>=map_arr[temp[1]//100000][temp[1]%100000]-1:continue
                        map_arr[dy][dx]=map_arr[temp[1]//100000][temp[1]%100000]-1
                else:
                    temp[0]+=1
            if map_arr[dy][dx]<0 and map_arr[dy][dx]!='E':continue
            heapq.heappush(q,[temp[0],dy*100000+dx])

            
        if flag==1:break
    if flag==0:
        print('sad')
