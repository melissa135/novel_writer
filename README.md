# novel_writer
Train LSTM to writer novel (HongLouMeng here) in Pytorch.

## Requirements
* Pytorch

## Usage
0. Prepare your novel text (Optional, we have `/hongloumeng` already).
1. Run `train_net.py` to train the LSTM. After training the LSTM will be saved as a disk file `net.pth`. The dict mapping word to index will also be saved in `word_index`.
2. Run `writer.py` to writer a paragraph starting with the given words (you can modify them in source code). The parameter `regularity` decide the output is diversity but more mistakes (when `regularity` < 1) or more correct & likely but boring (when `regularity` > 1). When `regularity` = 0, it is totally random; when `regularity` = 1, it takes standard probability from LogSoftmax.

## Examples

## Tips
* You can also prepare your own novel text to train the LSTM, but you may need to modify `paragraph_set.py` to adapt the different format.
