import os
import torch
import cPickle
import torchvision.transforms as transforms

class str_to_list(object):
    def __call__(self,string):
        lst = [ '<START>' ]
        for s in string:
            lst.append(s)
        lst.append('<END>')
        return lst

class list_to_input(object):
    def __call__(self,lst):
        in_put = []
        for i in range(0, len(lst)-1):
            w = lst[i]
            in_put.append(index_to_tensor(w))
        return torch.cat(in_put)

class list_to_target(object):
    def __call__(self,lst):
        target = []
        for i in range(1, len(lst)):
            w = lst[i]
            target.append(index_to_tensor(w))
        return torch.cat(target)


class str_to_sample(object):
    def __call__(self,string):
	if string == '':
            lst = [ '<START>' ]
	else :
	    lst = []

        for s in string:
            lst.append(s)

        in_put = []
        for i in range(0, len(lst)):
            w = lst[i]
            in_put.append(index_to_tensor(w))
        return torch.cat(in_put)

def index_to_tensor(w):
    tensor = torch.LongTensor([word_index[w]])
    return tensor

path_ = os.path.abspath('.')            
f = file(path_+'/word_index', 'r')
word_index = cPickle.load(f)

transform_input = transforms.Compose([str_to_list(),
                                      list_to_input()])
transform_target = transforms.Compose([str_to_list(),
                                       list_to_target()])

transform_sample = transforms.Compose([str_to_sample()])
