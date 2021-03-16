# BART Zero Shot Mask Generation

* Data from aNLG Data in `val.source`
* Used [BART](https://github.com/pytorch/fairseq/tree/master/examples/bart) Zero Shot to fill masks

```
bart = torch.hub.load('pytorch/fairseq', 'bart.large')
bart.eval()
bart.fill_mask(['The cat <mask> on the <mask>.'], topk=3, beam=10)
```
* Results in `enthymeme.hypo`