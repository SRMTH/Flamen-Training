import dxl


def init():
    ports = dxl.get_available_ports()
    print ("Available ports:", ports)
    global arm
    arm = dxl.dxl(a[0], 1000000)
    motors = arm.scan(20)
    print (motors)
    if (len(motors)!=7)
        raise IOError("All motors not detected")

    print ("Connected to %s"%a[0])


def get_angles(x,y):
    th1, th2 = 45, 45
    return th1, th2

def get_xy():
    th1 = arm.read(3, "Present Position")
    th2 = arm.read(4, "Present Position")
    return th1, th2

if __name__ == '__main__':
    init()
    file = "data.csv"
    fout = open(file, "w")
    fout.write("x,y,th1,th2\n")
    
    print ("Important!!!! use ^C to exit else the data wont be saved\n")

    while True:
        try:
            x, y = get_xy()
            th1, th2 = get_angles(x, y)
            string = str(x)+","+str(y)+","+str(th1)+","+str(th2)+"\n"
            fout.write(string)
            input()
        except KeyboardInterrupt:
            break

    fout.close()