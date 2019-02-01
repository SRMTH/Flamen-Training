

def get_angles(x,y):
    th1, th2 = 45, 45
    return th1, th2

def get_xy():
    return 0, 0

if __name__ == '__main__':
    file = "data.csv"
    fout = open(file, "w")
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