from flask import *
import os
import torch
from fairseq.models.bart import BARTModel
import os
import time
import numpy as np
import sys
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "POST"):
        source = request.form["enthinput"]
        sents = source.split(".")
        source = sents[0] + " #" + sents[1]
        model = request.form["modelselector"]
        if (model == "BART"):
            datadir = "enthymemes-bart"
            cpdir = "BART/"
        elif (model == "BART + ParaCOMET1"):
            datadir = "enthymemes-paracomet1"
            cpdir = "PARACOMET1/"
        elif (model == "BART + ParaCOMET2"):
            datadir = "enthymemes-paracomet2"
            cpdir = "PARACOMET2/"
        os.system("echo '" + source + "' > ie.source")
        print(source)
        print(cpdir)
        bart = BARTModel.from_pretrained(cpdir,checkpoint_file='checkpoint_best.pt',data_name_or_path=datadir)

        bart.cuda()
        bart.eval()
        np.random.seed(4)
        torch.manual_seed(4)

        count = 1
        bsz = 1
        maxb = 200
        minb = 7

        t = 0.7
        elem = []
        for val in [5]:
            with open('ie.source') as source, open('web_output.hypo', 'w') as fout:
                sline = source.readline().strip()
                slines = [sline]
                for sline in source:
                    if count % bsz == 0:
                        with torch.no_grad():
                            # hypotheses_batch = bart.sample(slines, sampling=True, sampling_topk=val, temperature=t, lenpen=2.0, max_len_b=maxb, min_len=minb, no_repeat_ngram_size=3)
                            
                            # Below line of code for beam search
                            hypotheses_batch = bart.sample(slines, beams=5, lenpen=2.0, max_len_b=maxb, min_len_b=minb, no_repeat_ngram_size=3)
                        for hypothesis in hypotheses_batch:
                            fout.write(hypothesis.replace('\n','') + '\n')
                            fout.flush()
                        slines = []

                    slines.append(sline.strip())
                    count += 1
                if slines != []:
                    
                    # hypotheses_batch = bart.sample(slines, sampling=True, sampling_topk=val, temperature=t, lenpen=2.0, max_len_b=maxb, min_len=minb, no_repeat_ngram_size=3)
                    
                    # Below line of code for beam search
                    hypotheses_batch = bart.sample(slines, beams=5, lenpen=2.0, max_len_b=maxb, min_len_b=minb, no_repeat_ngram_size=3)
                    for hypothesis in hypotheses_batch:
                        fout.write(hypothesis.replace('\n','') + '\n')
                        fout.flush()
            # f = open("web_output.hypo", "r")
            # print(f.read())
            """
            with open('web_output.hypo', 'r') as readerr:
              line = readerr.readline()
              while line != '':
                  print(line, end='')
                  line = readerr.readline()
                  argument = argument + line
                  """
            with open('web_output.hypo', 'r') as file:
              argument = file.read().replace('\n', '')
            return render_template("index.html", argument=argument)
    return render_template("index.html",f="")
  
app.run()