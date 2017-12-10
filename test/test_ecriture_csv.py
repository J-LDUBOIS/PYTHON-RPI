with open("C:/Users/Flo/PycharmProjects/raspy/raspy.csv") as f:     
    reader = csv.reader(f)     #for row in reader:     
    for i in range(2):         #print(file2.readline())         
    print (reader.next())
with open("C:/Users/Flo/PycharmProjects/raspy/raspy.csv") as f:
    reader = csv.reader(f)
    #for row in reader:
    for i in range(2):
        #print(file2.readline())
        print (reader.next())


csvfile = "C:/Users/Flo/PycharmProjects/raspy/classeur.csv"

row = ((list_test[1][0]),(list_test[3][0]))
with open('C:/Users\Flo/PycharmProjects/raspy/classeur.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow(row)