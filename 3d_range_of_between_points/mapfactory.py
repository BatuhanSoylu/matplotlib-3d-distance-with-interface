def dataEdit(data):
    x=[]
    y=[]
    z=[]
    for i in data:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x,y,z
'''    
    a = [0, 0, 0, 0, 30, 30]
    b = [0, 0, 30, 30, 30, 30]
    c = [0, 40, 40, 0, 0, 40]
    device = [10, 10, 0]'''

def threeD(a,b,c,device):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    lines = []
    for i in range(len(a)):
        line = []
        x = [a[i], device[0]]
        y = [b[i], device[1]]
        z = [c[i], device[2]]
        line.append(x)
        line.append(y)
        line.append(z)
        lines.append(line)
    print(lines)
    print(len(lines))
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    ax.scatter(a, b, c, color="b", s=150)
    # ax.plot(a,b,c, color="red")
    ax.scatter(device[0], device[1], device[2], color="r", s=150)
    # ax.plot(lines[0],color="g")
    for i in lines:
        ax.plot(i[0], i[1], i[2])

    ax.text(0, 0, 20, "Batuhan SOYLU", color="red")

    # ax.plot(p,device,color="black")
    # plt.plot(x,y,z,color="green")
    plt.show()
    return lines

def dim(beacons_to_device):
    import math
    import numpy
    totalllist=[]
    for i in beacons_to_device:
        xylist=[]
        for j in i:
            a=j[0]-j[1]
            b=pow(a,2)
            xylist.append(b)
        totalllist.append(xylist)
    distances=[]
    for i in totalllist:
        a=i[0]+i[1]
        b=a+i[2]
        c=math.sqrt(b)
        distances.append(c)
    array=numpy.array(distances)
    minimum_distance_index=array.argmin()
    print("index of min distance",minimum_distance_index)
    print("distance of min distance(meters):",distances[minimum_distance_index])
    print("points of minimum distance have two point(device2beacon):",beacons_to_device[minimum_distance_index])
    return minimum_distance_index,distances[minimum_distance_index],beacons_to_device[minimum_distance_index]
def set_beacondb(point):
    import sqlite3
    point_x = point[0]
    point_y = point[1]
    point_z = point[2]

    data = sqlite3.connect("../mapdata.db")
    cursor = data.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS coordinatesbeacon(x INTEGER,y INTEGER,z INTEGER)")
    cursor.execute("INSERT INTO coordinatesbeacon(x,y,z) VALUES(?,?,?)",(point_x, point_y, point_z))
    data.commit()

def set_devicebd(point):
    import sqlite3
    point_x = point[0]
    point_y = point[1]
    point_z = point[2]  

    data = sqlite3.connect("../mapdata.db")
    cursor = data.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS coordinatesdevice(x INTEGER,y INTEGER,z INTEGER)")
    cursor.execute("INSERT INTO coordinatesdevice(x,y,z) VALUES(?,?,?)", (point_x, point_y, point_z))
    data.commit()

def get_db():
    import sqlite3
    data = sqlite3.connect("../mapdata.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM coordinatesbeacon")
    da=cursor.fetchall()
    daa=[]
    for i in da:
        l=list(i)
        daa.append(l)
    return daa
def getdbdevice():
    import sqlite3
    data = sqlite3.connect("../mapdata.db")
    cursor = data.cursor()
    cursor.execute("SELECT * FROM coordinatesdevice")
    da=cursor.fetchall()
    for i in da:
        j=list(i)
    return j

def deletedb():
    import sqlite3
    import sqlite3
    data = sqlite3.connect("../mapdata.db")
    cursor = data.cursor()
    cursor.execute("DELETE FROM coordinatesdevice")
    cursor.execute("DELETE FROM coordinatesbeacon")
    data.commit()




a = [0, 0, 0, 0, 30, 30,30,30]
b = [0, 0, 30, 30, 30, 30,0,0]
c = [0, 40, 40, 0, 0, 40,0,40]
device = [10, 10, 0]
device2=[20,20,40]
def threeF(a,b,c,device,device2):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    lines = []
    for i in range(len(a)):
        line = []
        x = [a[i], device[0]]
        y = [b[i], device[1]]
        z = [c[i], device[2]]
        line.append(x)
        line.append(y)
        line.append(z)
        lines.append(line)
    lines2 = []
    for i in range(len(a)):
        line2 = []
        x = [a[i], device2[0]]
        y = [b[i], device2[1]]
        z = [c[i], device2[2]]
        line2.append(x)
        line2.append(y)
        line2.append(z)
        lines2.append(line2)
    print(lines2)
    print(len(lines2))
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")
    ax.scatter(a, b, c, color="b", s=150)
    # ax.plot(a,b,c, color="red")
    ax.scatter(device[0], device[1], device[2], color="r", s=150)
    ax.scatter(device2[0], device2[1], device2[2], color="green", s=150)
    # ax.plot(lines[0],color="g")
    for i in lines:
        ax.plot(i[0], i[1], i[2])
    for i in lines2:
        ax.plot(i[0], i[1], i[2])
    ax.text(0, 0, 20, "Batuhan SOYLU", color="red")

    # ax.plot(p,device,color="black")
    # plt.plot(x,y,z,color="green")
    plt.show()
    return lines,lines2
#threeF(a,b,c,device,device2)