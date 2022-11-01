#%%
import torchvision
import torch
import torch.nn as nn
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
import os
from torch.utils.data import DataLoader, Dataset

path = r'I:\PythonProject\DataLog\TEOS'

dirs = os.listdir(path)

#%%
pres = []
max_size = (0, 0)
for i in dirs:
    if i[-4:] == 'prp]':
        arr = np.genfromtxt(os.path.join(path, i), skip_header=3)
        pres.append(arr[:, [3,4]].T)
        if max_size[1] <= pres[-1].shape[1]:
            print(arr.shape[1], pres[-1].shape[1])
            max_size = pres[-1].shape

#%%
for i in range(len(pres)):
    tmp = np.zeros(max_size)
    tmp[:,:pres[i].shape[1]] = pres[i]
    pres[i] = tmp

pres = np.array(pres)
# %%

er = np.genfromtxt(os.path.join(path, 'ER.csv'))
er = np.reshape(er, [-1, 1])
#%%
batch_size = 4

class MyModel(nn.Module):
	def __init__(self, embedding_length, hidden_size):
		super(MyModel, self).__init__()
		self.hidden_size = hidden_size
		self.lstm = nn.LSTM(embedding_length, hidden_size)
		self.label = nn.Linear(hidden_size, 1)


	def forward(self, input, batch_size):


		h_0 = Variable(torch.zeros(1, batch_size, self.hidden_size))
		c_0 = Variable(torch.zeros(1, batch_size, self.hidden_size))

		output, (final_hidden_state, final_cell_state) = self.lstm(input, (h_0, c_0))

		return self.label(final_hidden_state[-1]) 



class CustomImageDataset(Dataset):
    def __init__(self, data,label, transform=None, target_transform=None):
        arr = np.array(data)
        self.data = np.array(data, dtype=np.float32)
        self.dat_labels = np.array(label, dtype=np.float32)
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.dat_labels)

    def __getitem__(self, idx):
        data = torch.from_numpy(self.data[idx])
        label = torch.from_numpy(self.dat_labels[idx])
        # if self.transform:
        #     data = self.transform(data)
        # if self.target_transform:
        #     label = self.target_transform(label)
        return data, label


dataset = CustomImageDataset(pres, er, torchvision.transforms.ToTensor(), torchvision.transforms.ToTensor())
train_dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

#%%
learningRate = 0.01
model = MyModel(2, 8)
wd = 5e-1

criterion = torch.nn.MSELoss() 
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate, weight_decay=wd)

losses = []
epochs =   100
for epoch in range(epochs):
    # Converting inputs and labels to Variable
    for batch in train_dataloader:
        inputs, labels = batch
    # Clear gradient buffers because we don't want any gradient from previous epoch to carry forward, dont want to cummulate gradients
        optimizer.zero_grad()

        # get output from the model, given the inputs
        outputs = model(inputs, batch_size)

        # get loss for the predicted output
        loss = criterion(outputs, labels)
        # print(loss)
        # get gradients w.r.t to parameters
        loss.backward()

        # update parameters
        optimizer.step()

        # print('epoch {}, loss {}'.format(epoch, loss.item()))
        loss_val = loss.item()
        losses.append(loss_val)

# %%
