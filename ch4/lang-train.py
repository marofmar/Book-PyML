from sklearn import svm, metrics 
import glob, os.path, re, json 
#import os 
#print(os.listdir())
# read text and check the frequency of Alphabet in each language
def check_freq(fname):
    name = os.path.basename(fname) 
    lang = re.match(r'^[a-z]{2,}', name).group() 
    with open(fname, 'r', encoding = 'utf-8') as f:
        text = f.read() 
    text = text.lower() 
    
    # initialize counter 
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a") # ord() returns an integer representing the Unicode character 
    code_z = ord("z") 

    # alphabet frequency 1-
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # if within the range a to z,
            cnt[n-code_a] += 1
        
    # normalize     
    total = sum(cnt)
    freq = list(map(lambda n: n/total, cnt)) 
    
    return (freq, lang) 

# process each file 
def load_files(path):
    freqs = [] 
    labels = [] 
    file_list = glob.glob(path) 
    for fname in file_list:
        r = check_freq(fname) 
        
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs": freqs, "labels": labels}

data = load_files("./Book-PyML/ch4/lang/train/*.txt")
test = load_files("./Book-PyML/ch4/lang/test/*.txt")

# save the result in json 
with open("./Book-PyML/ch4/lang/freq.json", "w", encoding = 'utf-8') as fp:
    json.dump([data, test], fp)

# train 
clf = svm.SVC(gamma = 'auto')
clf.fit(data['freqs'], data['labels'])

# predict 
predict = clf.predict(test['freqs']) 

# check performance 
ac_score = metrics.accuracy_score(test['labels'], predict) 
cl_report = metrics.classification_report(test['labels'], predict) 
print("Accuracy: ", ac_score) 
print("Classification report: ")
print(cl_report)
