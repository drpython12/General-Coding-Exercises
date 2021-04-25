def vectorize(tokens):
    ''' This function takes list of words in a sentence as input 
    and returns a vector of size of filtered_vocab. It puts 0 if the 
    word is not present in tokens and count of token if present. '''
    vector=[]
    for w in filtered_vocab:
        vector.append(tokens.count(w))
    return vector
def unique(sequence):
    ''' This functions returns a list in which the order remains 
    same and no item repeats. Using the set() function does not 
    preserve the original ordering, so I didnt use that instead. '''
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

# Example list of stopwords
stopwords=["to","is","a"]

# List of special characters
special_char=[",",":"," ",";",".","?"]

# Write the sentences in the corpus, in this case, just two 
sentence1 = "Welcome to Great Learning , Now start learning"
sentence2 = "Learning is a good practice"

# Convert them to lower case
sentence1 = sentence1.lower()
sentence2 = sentence2.lower()
# Split the sentences into tokens
tokens1 = sentence1.split()
tokens2 = sentence2.split()
print(tokens1)
print(tokens2)

# Create a vocabulary list
vocab = unique(tokens1+tokens2)
print(vocab)

# Filter the vocabulary list
filtered_vocab = []
for w in vocab: 
    if w not in stopwords and w not in special_char: 
        filtered_vocab.append(w)
print(filtered_vocab)

# Convert sentences into vectors
vector1=vectorize(tokens1)
print(vector1)
vector2=vectorize(tokens2)
print(vector2)

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
sentence_1="This is a good job.I will not miss it for anything"
sentence_2="This is not good at all"
 
 
 
CountVec = CountVectorizer(ngram_range=(1,1), # to use bigrams ngram_range=(2,2)
                           stop_words='english')
#transform
Count_data = CountVec.fit_transform([sentence_1,sentence_2])
 
#create dataframe
cv_dataframe=pd.DataFrame(Count_data.toarray(),columns=CountVec.get_feature_names())
print(cv_dataframe)

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
sentence_1="This is a good job.I will not miss it for anything"
sentence_2="This is not good at all"
 
# Without smooth IDF
print("Without Smoothing:")

# Define tf-idf
tf_idf_vec = TfidfVectorizer(use_idf=True, 
                        smooth_idf=False,  
                        ngram_range=(1,1),stop_words='english') # to use only  bigrams ngram_range=(2,2)

# Transform
tf_idf_data = tf_idf_vec.fit_transform([sentence_1,sentence_2])

# Create dataframe
tf_idf_dataframe = pd.DataFrame(tf_idf_data.toarray(),columns=tf_idf_vec.get_feature_names())
print(tf_idf_dataframe)
print("\n")
 
# With smoothing
tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,  
                        smooth_idf=True,  
                        ngram_range=(1,1),stop_words='english')
 
 
tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform([sentence_1,sentence_2])
 
print("With Smoothing:")
tf_idf_dataframe_smooth = pd.DataFrame(tf_idf_data_smooth.toarray(),columns=tf_idf_vec_smooth.get_feature_names())
print(tf_idf_dataframe_smooth)