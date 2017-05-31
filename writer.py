# coding:utf-8
import os
import torch
import cPickle
import random
import math
from define_net import Net
from torch.autograd import Variable
from my_transform import transform_sample

def prob_select(log_probs,regularity): # select a word according to the probability
    probs = []
    total = 0
    for i in range(0,len(log_probs)):
        # regular = 0, totally random; regular = 1, standard probability by LogSoftmax; regular > 1, prefer words with high probability
        prob = math.pow(10,log_probs[i]*regularity)
        probs.append(prob)
        total = total + prob
    r = random.uniform(0,total)
    i = 0
    summ = probs[i]
    while summ < r:
        i = i + 1
        summ = summ + probs[i]
    return i

def sample(start,regularity=1.0):

    start = start.decode('utf-8')
    print 'Start with: ',start, ' regularity=', regularity
    in_put = transform_sample(start)
    in_put = Variable(in_put)
    hidden = net.initHidden()
    output_string = ''

    output, hidden = net(in_put, hidden)
    
    for i in range(max_length):

        n = prob_select(output.data[-1],regularity)
        w = word_index[n]
        
        if w == "<END>":
            break
        else :
            output_string = output_string + w
            
        in_put = transform_sample(w)
        in_put = Variable(in_put)
        
        output, hidden = net(in_put, hidden)
        
    return start + output_string

if __name__ == '__main__':

    path_ = os.path.abspath('.')
    
    f = file(path_+'/word_index', 'r')
    word_index = cPickle.load(f)
    word_index = dict((v, k) for k, v in word_index.iteritems())

    net = Net(len(word_index)) 
    net.load_state_dict(torch.load(path_+'/net.pth'))

    max_length = 1000

    print sample('到了宁府',0.5)
    print sample('到了宁府',1.0)
    print sample('到了宁府',2.0)
    
    
    print sample('')
    print sample('探春笑道')
    print sample('来了一僧一道，且行且谈。')
