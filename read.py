import pandas as pd 
data = pd.read_csv("test.csv")
x_data = data["x"]
y_data = data["y"]
th1 = data["th1"]
th2 = data["th2"]
#print (len(x_data))
input_data = []
output_data = []
for i in range(len(x_data)):
    input_data.append([data.iloc[i]["x"],data.iloc[i]["y"]])
    output_data.append([[data.iloc[i]["th1"]],data.iloc[i]["th2"]])

print (input_data)
print (output_data)