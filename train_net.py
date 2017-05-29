import os
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
import torch
import torchvision
from define_net import Net
from torch.autograd import Variable
from paragraph_set import Paragraph_set
from dataloader_modified import DataLoader


if __name__ == '__main__':
	
    path_ = os.path.abspath('.')

    trainset = Paragraph_set(path_+'/hongloumeng/')
    print trainset.get_paragraph_size()
    print trainset.get_word_size()
    
    trainloader = DataLoader(trainset,batch_size=8,shuffle=True,num_workers=2)

    net = Net(trainset.get_word_size())
    print net

    criterion = nn.NLLLoss()

    optimizer = optim.RMSprop(net.parameters(), lr=0.01, weight_decay=0.0001)

    for epoch in range(2): #

        running_loss = 0.0
        for i,batch in enumerate(trainloader,0):

	    loss = 0
	    optimizer.zero_grad()

	    for data in batch:
                inputs,targets = data
                inputs,targets = Variable(inputs),Variable(targets)
                hidden = net.initHidden()
                outputs,hidden = net(inputs,hidden)   
                loss = loss + criterion(outputs,targets)

            loss.backward()
            optimizer.step()

            running_loss += loss.data[0]
            if i%10 == 9: # step is 10 and batch_size is 8
                print('[%d, %4d] loss: %.3f' % (epoch+1,i+1,running_loss/80))
                running_loss = 0.0

    print('Finished Training')
    torch.save(net.state_dict(),path_+'/net.pth')
