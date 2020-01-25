import matplotlib.pyplot as plt 
import pandas as pd 
import json

with open("c:/Users/Mads/Documents/Book-PyML/ch4/lang/freq.json", "r", encoding = 'utf-8') as fp:
    freq = json.load(fp) 

# counts by language 
lang_dic = {} # {"freqs": freqs, "labels": labels}
for i, lbl in enumerate(freq[0]['labels']):
    fq = freq[0]['freqs'][i] 
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq 
        continue 
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v)/2 

# inset data into Pandas 
asclist = [[chr(n) for n in range( 97, 97+26)]]
df = pd.DataFrame(lang_dic, index = asclist)

# plot graphs 
plt.style.use('ggplot') 
#df.plot(kind = 'bar', subplots = True, ylim = (0,0.15)) 
#plt.savefig('lang-plot-histo.png')
df.plot(kind = 'line')
plt.savefig("lang-plot-line.png")
