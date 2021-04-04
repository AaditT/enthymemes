git clone https://github.com/pytorch/fairseq &&
cd fairseq &&
pip3 install --editable ./ &&
wget https://dl.fbaipublicfiles.com/fairseq/models/bart.large.tar.gz &&
tar -xzvf bart.large.tar.gz &&
mkdir enthymemes &&
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/encoder.json' &&
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/vocab.bpe' &&
wget -N 'https://dl.fbaipublicfiles.com/fairseq/gpt2_bpe/dict.txt'