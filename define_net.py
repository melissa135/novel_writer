 #import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self, words):
        super(Net, self).__init__()
        self.embedding_size = 256
        self.hidden_size = 256
        
        self.embedding = nn.Embedding(words, self.embedding_size)
        self.lstm = nn.LSTM(self.embedding_size, self.hidden_size)
        self.linear = nn.Linear(self.hidden_size, words)
        self.softmax = nn.LogSoftmax()

    def forward(self, input, hidden):
        length = input.size()[0]
        embed = self.embedding(input).view((length, 1, -1)) # the LSTM can olny accept input in mini-batch
        output, hidden = self.lstm(embed, hidden)
        output = F.relu(self.linear(output.view(length, -1)))
        output = self.softmax(output)
        return output, hidden

    def initHidden(self, length=1):
        return (Variable(torch.zeros(length, 1, self.hidden_size)),
                Variable(torch.zeros(length, 1, self.hidden_size)))
