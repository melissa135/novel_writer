import os
import re
import cPickle
import torch.utils.data as data


def read_files(folder):
    
    content = []

    for root, _, fnames in os.walk(folder):
        for fname in fnames:
            
            path = os.path.join(root, fname)
            f = open(path, 'r')
            lines = f.readlines()
            f.close()
    
            pt = r'<p>.*</p>'
            
            for l in lines:
                s = re.match(pt,l)
                if not s is None :
                    c = s.group()
                    c = c.replace('<p>','')
                    c = c.replace('</p>','')
		    c = c.decode('utf8')
		    if len(c) >= 20:
                        content.append(c.decode('utf8'))

    return content

def word_to_index(content):
    
    word_index = {}

    for para in content:
        for word in para:
            if word not in word_index:
                word_index[word] = len(word_index)

    word_index['<END>'] = len(word_index)
    word_index['<START>'] = len(word_index)

    path_ = os.path.abspath('.')
    f = file(path_+'/word_index', 'w')
    cPickle.dump(word_index, f)

    return word_index

class Paragraph_set(data.Dataset):

    def __init__(self, root):

        paragraphs = read_files(root)
        word_index = word_to_index(paragraphs)

        from my_transform import transform_input,transform_target
        
        self.root = root
        self.paragraphs = paragraphs
        self.word_size = len(word_index)
        self.transform_input = transform_input
        self.transform_target = transform_target

    def get_paragraph_size(self):
        return len(self.paragraphs)

    def get_word_size(self):
        return self.word_size

    def __getitem__(self, index):
        para = self.paragraphs[index]
        in_put = self.transform_input(para)
        target = self.transform_target(para)
        return in_put, target

    def __len__(self):
        return len(self.paragraphs)
