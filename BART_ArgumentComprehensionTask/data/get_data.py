# -*- coding: utf-8 -*-
"""enthymemes_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nSFAjiv-vsZbAcn304PSB_sE8Ge--gzL
"""

!pwd

# Commented out IPython magic to ensure Python compatibility.
# %cd fairseq/enthymemes/

"""# Preprocessing data from Argument Comprehension Task Dataset
https://github.com/UKPLab/argument-reasoning-comprehension-task/tree/master/mturk/annotation-task/data/final

Creating four files


* train.source
* train.target
* val.source
* val.target


"""

import csv

tsv_file = open("train.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")

reasons = []
claims = []
warrants = []

counter = -1

for row in read_tsv:
  counter += 1
  if (counter == 0):
    continue
  
  reasons.append(row[4])
  claims.append(row[5])

  correct_label = int(row[3])
  warrant0 = 1
  warrant1 = 2

  if (correct_label == 0):
    warrant_index = warrant0
  elif (correct_label == 1):
    warrant_index = warrant1

  warrants.append(row[warrant_index])

print(warrants)

print("Reasons: " + str(len(reasons)))
print("Claims: " + str(len(claims)))
print("Warrants: " + str(len(warrants)))

dataset_size = 1210
cwr_array = []
for i in range(dataset_size):
  claim = claims[i]
  warrant = warrants[i]
  reason = reasons[i]

  source = reason + " # " + claim
  target = warrant

  cwr_array.append([source, target])

len(cwr_array)
cwr_array[0]

train_source = open("train.source", "w")
train_target = open("train.target", "w")
for line in cwr_array:
  train_source.write(line[0])
  train_source.write("\n")
  train_target.write(line[1])
  train_target.write("\n")
train_source.close()
train_target.close()

test_tsv_file = open("test.tsv")
test_read_tsv = csv.reader(test_tsv_file, delimiter="\t")

test_reasons = []
test_claims = []
test_warrants = []

test_counter = -1

for row in test_read_tsv:
  test_counter += 1
  if (test_counter == 0):
    continue
  
  test_reasons.append(row[4])
  test_claims.append(row[5])

  test_correct_label = int(row[3])
  test_warrant0 = 1
  test_warrant1 = 2

  if (test_correct_label == 0):
    test_warrant_index = test_warrant0
  elif (correct_label == 1):
    test_warrant_index = test_warrant1

  test_warrants.append(row[test_warrant_index])
print(test_warrants)
print("Reasons: " + str(len(test_reasons)))
print("Claims: " + str(len(test_claims)))
print("Warrants: " + str(len(test_warrants)))

test_dataset_size = 444
test_cwr_array = []
for i in range(test_dataset_size):
  test_claim = test_claims[i]
  test_warrant = test_warrants[i]
  test_reason = test_reasons[i]

  test_source = test_reason + " # " + test_claim
  test_target = test_warrant

  test_cwr_array.append([test_source, test_target])


val_source = open("val.source", "w")
val_target = open("val.target", "w")
for line in test_cwr_array:
  val_source.write(line[0])
  val_source.write("\n")
  val_target.write(line[1])
  val_target.write("\n")
val_source.close()
val_target.close()