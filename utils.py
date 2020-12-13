import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
import re
from sklearn.manifold import TSNE
import scipy.cluster.hierarchy as sch
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import pandas as pd


def clean_text(input_text: str,
               STOPWORDS=stopwords.words('english')):
    """
    Given an input sentence, it returns a processed string after applying:
    - Lowercasing
    - Multiple spaces removal
    - Removing mention to users (@XXXX)
    - Removing punctuation and other undesired symbols (# will be kept since they are essential to understand tweets)
    - Stop-words removal
    - Stemming (Using Porter Stemmer) - HASHTAGS will not be stemmed
    """

    stemmer = PorterStemmer()

    # remove "RT" string indicating a retweet
    output = input_text.replace("RT", "")

    # remove URLs
    output = re.sub(r'https?:\/\/.*[\r\n]*', '', output, flags=re.MULTILINE)

    # remove mentions and users in the string
    output = re.sub(r"\@[\w]+", "", output)

    # Removing multiple spaces
    output = re.sub(r'\s+', ' ', output)

    # lowering text
    output = output.lower()

    # removing all the punctuations
    output = re.sub("[^A-Za-z0-9\s#]+", "", output).strip()

    # remove stopwords
    tokens = [word for word in output.split() if word not in STOPWORDS]

    # remove double hashtags
    tokens = [re.sub("[#]+", "#", token) for token in tokens]

    # Stemming. Avoid stemming hashtags
    output = " ".join([stemmer.stem(token) if not token.startswith('#') else token for token in tokens])

    # remove single letters (meaning errors while writing)
    output = re.sub(r'\s[A-Z,a-z]\s', '', output)

    return output

def get_tweet_fields(df_tweets,i):
    """
        df_tweets: database with the tweets information
        i: id of the tweet we want to extract the information
        returns various fields needed for showing the result to the user
    """
    user_name = eval(df_tweets.iloc[i]['user'])['name']
    text = df_tweets.iloc[i]['full_text']
    entities = eval(df_tweets.iloc[i]['entities'])
    urls = entities['urls']
    if urls:
        url = urls[0]['url']
        text = text.replace(url,'')
    else:
        url = None
    hashtags = entities['hashtags']
    if not hashtags:
        hashtags.append('No hashtags')

    favorite_count = df_tweets.iloc[i]['favorite_count']
    retweet_count =  df_tweets.iloc[i]['retweet_count']

    return user_name, text, url, hashtags, favorite_count, retweet_count


def run_TSNE(X,df_tweets = None,labels = None, doc = False,name = 'default.png'):
    """
    X: matrix containing the embeddings
    model: word2vec trained model (Gensim library)
    df_tweets: Only needed if we are printing doc. Database with tweets information 
    labels: text we want that the scatters have
    doc: If true we will be printing doc embeddings. If False, printing word embeddings


    Return: X_tsne matrix containing 2D representation of the embeddings.
    """
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)

    x  = X_tsne[:, 0]
    y = X_tsne[:, 1]

    if doc:
        labels = [df_tweets.iloc[n]['id_str'] for n in range(0,len(x))]
    if labels:
        fig, ax = plt.subplots(figsize=(15,15))
        plt.scatter(x, y)
        #for i, txt in enumerate(labels):
            #ax.annotate(txt, (x[i], y[i]))
        #plt.savefig(results_path + name)
        plt.show()
    return X_tsne

def print_cluster(embeddings,labels,cluster_labels,print_cluster = None):
    """
        embeddings:document embedding representation
        labels: cluster labels
        cluster: cluster
        print_cluster: bool, True for print, False for not print
    """
    x = []
    y = []
    labels_p = []
    clusters_p = []
    if print_cluster != None:
        indices_to_print = [i for i in np.where(cluster_labels == 0)[0]]
        for i in indices_to_print:
            x.append(embeddings[i,0])
            y.append(embeddings[i,1])
            clusters_p.append(cluster_labels[i]) 
            labels_p.append(labels[i]) 
    else:
        x = embeddings[:,0]
        y = embeddings[:,1]
        labels_p = labels
        clusters_p = cluster_labels

    fig, ax = plt.subplots(figsize=(15,15))
    plt.scatter(x,y,c=clusters_p)
    #for i, txt in enumerate(labels_p):
    #ax.annotate(txt, (x[i], y[i]))
    plt.show()

def get_tokens(text):
    # Get the tokens
    if isinstance(text, nltk.Text):
        tokens = text.tokens
    else:
        tokens = text.split(" ")
        
    return tokens

def remove_stopwords(text, language):
    # Import stopwords
    from nltk.corpus import stopwords
    
    # Get stop words for the given language
    stopwords_list = stopwords.words(language)
    
    # Get the tokens
    tokens = get_tokens(text)
        
    # TODO: Remove the words from the text (tip: check the nltk.Text object and stopwords in NLTK)
    cleaned_text = [w for w in tokens if not w in stopwords_list]
    
    # Return cleaned text
    if isinstance(text, nltk.Text):
        output = nltk.Text(cleaned_text)
    else:
        output = " ".join(cleaned_text)
    
    return output

def stem_text(text,language):
    # TODO: Create the stemmer (tip: see the class nltk.stem)
    stemmer = nltk.stem.PorterStemmer()
    
    # Get the tokens
    tokens = get_tokens(text)
    
    # TODO: Stem each token in text object
    stemmas = [stemmer.stem(t) for t in tokens]
    
    # Return stemmed text
    if isinstance(text, nltk.Text):
        output = nltk.Text(stemmas)
    else:
        output = " ".join(stemmas)
    
    return output

def standardize_text(text,language):
    # Remove the stop words
    standardized_text = remove_stopwords(text, language)
    
    # Stem the text
    standardized_text = stem_text(standardized_text, language)
    
    # Return
    return standardized_text


def personalized_tokenizer(text):
    return text.split()