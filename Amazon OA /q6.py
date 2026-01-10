numOfPoints=6
points=['green', 'yellow', 'red', 'blue', 'grey', 'pink'] 
xCoordinates=[10, 20, 15, 30, 10, 15]
yCoordinates=[30, 25, 30, 40, 25, 25] 
numOfQueriedPoints=4
queriedPoints=['grey', 'blue', 'red', 'pink']
ans=[]
for i in queriedPoints:
    print(i)
    index = points.index(i)
    x=[]
    if index==0:
        x = xCoordinates[index+1:]
        y = yCoordinates[index+1:]
        p = points[index+1:]
    elif index==numOfPoints-1:
        x = xCoordinates[:index]
        y = yCoordinates[:index]
        p = points[:index]
    else:
        x=xCoordinates[:index]+xCoordinates[index+1:]
        y=yCoordinates[:index]+yCoordinates[index+1:]
        p = points[:index]+points[index+1:]
    qx,qy = xCoordinates[index],yCoordinates[index]
    if qx in x:
        id = x.index(qx)
        ans.append(p[id])
    elif qy in y:
        id = y.index(qy)
        ans.append(p[id])
    else:
        ans.append(None)
print(ans)

