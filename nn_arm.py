import torch
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[1.0],[2.0],[3.0]]))
y_data = Variable(torch.Tensor([[2.0],[4.0],[6.0]]))

class LinearRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LinearRegressionModel,self).__init__()
        self.linear = torch.nn.Linear(1,1)
    
    def forward(self,x):
        y_pred = self.linear(x)
        return y_pred

our_model = LinearRegressionModel()
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(our_model.parameters(), lr = 0.01)

for epoch in range(500):
    pred_y = our_model(x_data)
    loss = criterion(pred_y, y_data)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('epoch {}, loss {}'.format(epoch, loss.data[0]))

new_var = Variable(torch.Tensor([[4.0]]))
pred_y = our_model(new_var)
print("predict (after training)", 4, our_model(new_var).data[0][0]) 