import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
import re
import nltk
from hdfs import InsecureClient
from nltk.tokenize import word_tokenize

hdfs_url = "http://localhost:9870"
output_path = "/user/hadoop/output/BSBI/0-r-00000"

client = InsecureClient(hdfs_url, user="hadoop")

inverted_index = {}
with client.read(output_path, encoding='utf-8') as reader:
    for line in reader:
        line = line.split()
        inverted_index[line[0]] = line[1:]
    

print(list(inverted_index.items())[:10])