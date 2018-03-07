# novel_writer
Using LSTM to writer novel-like text (HongLouMeng here) in Pytorch.    
Online writer: http://www.predictor.xin/writer/

## Requirements
* Pytorch

## Usage
0. Prepare your novel text (Optional, we have `/hongloumeng` already).
1. Train LSTM using `train_net.py`. The trained LSTM will be saved as a disk file `net.pth`, the mapping dict will be saved as `word_index`.
2. Run `writer.py` to writer a paragraph starting with the given words (you can modify them in source code). The parameter `regularity` decides the output is diversity but more mistakes (when `regularity` < 1, if `regularity` = 0, totally random) or more correct & likely but boring (when `regularity` > 1). When `regularity` = 1, it takes standard probability from LogSoftmax.

## Examples
```
Start with:  到了宁府  regularity= 0.5
到了宁府来了。大家罄了一回，邢夫人又说：“你们殓使老爷，说的是谁的二爷跟前说了病结了，过来挑飞子的。”贾母道：“谁敢告诉他呢，别人周些，倘或好的花儿好，别的婶娘好。”凤姐儿道：“我们都在家里了，莫不怎么，只管作什么着。我因拿我这个给他作什么？”凤姐儿把手拍手笑道：“我也找不上去了！”又指“柱”

Start with:  到了宁府  regularity= 1.0
到了宁府中，他们也不敢造次。今见他进来，说道：“我也不能够了。”说着，便又悄悄的说：“这话告诉了你，你们自己也不能够了。”凤姐儿道：“你们别人说话，我也不用说了。”贾琏道：“我的人也不知道。如今老爷说，叫我们请安，叫我请老爷给二奶奶们请安，请老爷回去。”凤姐儿道：“我也不过是个主意。”贾母听了，便说：“我们这里有什么事？”凤姐笑道：“你们为什么不好，我们家里也是这样说，也不用说话了。”贾琏道：“我的也是个好的，我的人都不敢说我的，就在这里呢。”贾蓉道：“我也不能够了。”凤姐儿道：“我也不好，我和你们说话。”贾琏笑道：“我的奶奶也是个聪明人，不过是我们家里的。”凤姐儿道：“我也不好。”贾政道：“这不是我的。”贾琏道：“我们家里不进去的，我也要问你。”凤姐儿笑道：“我也不用说了。”说着，便回身回道：“你们那里去，我也要你们家里去。”凤姐儿听了，忙问：“我的奶奶在那里呢？”凤姐道：“我也不好了。”凤姐儿道：“我也太太疼他的，不知怎么说话。”王夫人道：“你们去罢，我们要去。”说着，便起身走了。

Start with:  到了宁府  regularity= 2.0
到了宁府中，只见一个老婆子走来，说：“你们这么说，你们都不去，我也不好了。”贾母道：“我也不能够了。”贾琏道：“你们这么说，你们这么着呢。”

Start with:    regularity= 1.0
却说贾妃看毕，喜之不尽，说：“老爷请坐，我们再作一点儿。”贾政道：“正是呢，只是我们家里的人，你们都在这里，不用说话，只管叫他去罢。”凤姐道：“你瞧瞧这个，我也没有见你的。”贾琏道：“你们这个不是？”贾琏道：“你们都在这里呢，我也不能够了。”说着，便回身去了。

Start with:  探春笑道  regularity= 1.0
探春笑道：“你们别人说，我就回去了。”黛玉道：“我也要瞧瞧，我们家里的人，不过是个女孩儿，我便不好，他就是了。”宝玉道：“你们都是我的，我也知道了。”


Start with:  来了一僧一道，且行且谈。  regularity= 1.0
来了一僧一道，且行且谈。这里凤姐儿说：“我们这里有个好歹，且别人家不管他，只管他们两个人，说他们好。”凤姐儿道：“我也是个好的，不过是我的，我也不用说了。”宝玉道：“你们都没有了。”宝钗听了，说：“我也不用说了，你们也不能够了。”贾母听了，便说：“你也是个好的，只管叫他们去。”凤姐笑道：“你们都不大理我，我就不理我，我也不用说了。”
```

## Tips
* If training LSTM with your own text, you may need to modify `paragraph_set.py` to adapt the different format.
