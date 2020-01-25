from sklearn import svm 
import joblib 
import json 

# read JSON 
with open("c:/Users/Mads/Documents/Book-PyML/ch4/lang/freq.json", "r", encoding = 'utf-8') as fp:
    d = json.load(fp) 
    data = d[0] # only loading traniing data


# train data
clf = svm.SVC(gamma = 'auto') 
clf.fit(data['freqs'], data['labels'])

# save the trained one
joblib.dump(clf, "c:/Users/Mads/Documents/Book-PyML/ch4/lang/freq.pkl")
print('Done! ')  