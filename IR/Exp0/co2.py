import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
import re
import nltk
from hdfs import InsecureClient
from nltk.tokenize import word_tokenize

hdfs_url = "http://localhost:9870"
output_path = "/user/hadoop/output/part-00000"

client = InsecureClient(hdfs_url, user="hadoop")

with client.read(output_path, encoding='utf-8') as reader:
    output_text = reader.read().split()

# with open('file.txt', 'r', encoding='utf-8') as file:
#     output_text = file.read().split()

n = len(output_text)

word_freq_dict = {}

for i in range(0, n, 2):
    word = output_text[i].lower()
    word = re.sub(r'[",.()\[\]-]', '', word)
    if word and len(word) > 20:
        continue
    
    # if word in word_freq_dict:
    #     word_freq_dict[word] += 1
    # else:
    #     word_freq_dict[word] = 1
    if word not in word_freq_dict:
        word_freq_dict[word] = int(output_text[i + 1])
    else:
        word_freq_dict[word] += int(output_text[i+1])
        

soretd_words = dict(sorted(word_freq_dict.items(), key=lambda item:item[1], reverse=True))
df = pd.DataFrame(list(soretd_words.items()), columns=['Word', 'Frequency'])
df.insert(loc=2, column='Rank', value=range(1, len(word_freq_dict.items()) + 1))

def show_hist():
    df.plot(kind='scatter', x='Rank', y='Frequency', legend=False)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Power Law')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



log_df = df.copy()
log_df['Frequency'] = np.log(df['Frequency'].values)
log_df['Rank'] = np.log(df['Rank'].values)

A = log_df['Rank'].values
A = np.stack((A, np.ones(len(A))))
b = log_df['Frequency'].values
A = A.T
[m, c] = np.linalg.inv(A.T @ A) @ A.T @ b
x = np.linspace(0, A[-1][0], 1000)
y = m * x + c

log_df.plot(kind='scatter', x='Rank', y='Frequency', legend=False)
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency)')
plt.title('Validation of Zipf\'s Law')
plt.xticks(rotation=45)
plt.tight_layout()
plt.plot(x, y, color='red')
plt.show()


# print(len(word_freq_dict.items()))
# absent_words = 0
# for word in m:
    # if word not in word_freq_dict:
        # absent_words += 1
# 
# print(absent_words)