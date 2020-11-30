import pandas as pd
import pickle
from search_engine.constants import *
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from utils import clean_text
nltk.download('stopwords')

class TwitterSearch:
    def __init__(self):
        self.data, self.tf_idf, self.vectorizer = self._load_information()

    def _load_information(self):
        # Load pretrained vectorizer
        vectorizer = pickle.load(open(INPUT_PATH + VECTORIZER, "rb"))

        # Load corpus
        df = pd.read_csv(INPUT_PATH + AUTHORITY_DATASET)
        corpus = df['clean_text']
        corpus = corpus.fillna('')
        tf_idf = vectorizer.transform(corpus)

        return df, tf_idf, vectorizer

    def _get_tweet_fields(self, df, i):
        """
        Returns the relevant fields for each tweet
        df: database with the tweets information
        i: id of the tweet we want to extract the information
        returns various fields needed for showing the result to the user
        """
        user_name = eval(df.iloc[i]['user'])['name']
        text = df.iloc[i]['full_text']
        entities = eval(df.iloc[i]['entities'])
        urls = entities['urls']
        if urls:
            url = urls[0]['url']
            text = text.replace(url, '')
        else:
            url = 'No url'

        hashtags = entities['hashtags']

        if not hashtags:
            hashtags = 'No hashtags'

        favorite_count = df.iloc[i]['favorite_count']
        retweet_count = df.iloc[i]['retweet_count']
        followers_count = df.iloc[i]['followers_count']

        return user_name, text, url, hashtags, favorite_count, retweet_count, followers_count

    def return_top_n_doc(self, query, n, show=True, authority=None):
        """
        df: Dataset containing our tweets
        query: Query that the user writes. It must be preprocessed
        tf_idf: dataframe containing tfidf weights for each word in each doc
        n: number of doc to return to the user
        show: if you want to visualize the results
        authority: optional list for each tweet authority

        returns a list with the most top n relevant tweets
        """
        query = clean_text(query)  # Clean the query as the original text
        query_vec = self.vectorizer.transform([query])  # calculate its tf-idf score
        results = cosine_similarity(self.tf_idf, query_vec) # Compute similarity between query and tweets
        results = results.flatten()

        documents_retrieved = []

        # Return the results
        rank = 0

        # Include authority if specified
        if authority is not None:
            results = 3 * results * 0.5 * authority

        for i in results.argsort()[-n:][::-1]:
            user_name, text, url, hashtags, favorites, retweets, followers = self._get_tweet_fields(self.data, i)
            if show == True:
                print("{} -- User: {} ({} followers) | RT: {} | FAV: {}".format(rank+1, user_name, followers, retweets, favorites))
                print("-------------------------")
                print("text")
                print("-------------------------")
                print("Additional information -- Hashtags: {} | URL: {}".format(", ".join(hashtags[:]), url))
                print()

            documents_retrieved.append(i)
            rank += 1

        return documents_retrieved

    def query(self, query, n=20, authority=None):
        self.return_top_n_doc(query, n, authority)

    def interface(self):
        while True:
            n = input("Enter the desired number of results: ")
            while True:
                mode = input("""Which mode would you like to use (insert number for the desired option)
                1: TF-IDF
                2: TF-IDF and authority""")

                if mode in MODES:
                    break
                else:
                    print("Please insert some of these options: {}".format(', '.join(MODES)))

            query = input("Enter your query: ")
            if mode == 1:
                self.query(query, n)
            elif mode == 2:
                self.query(query, n, authority=True)

if __name__ == "__main__":
    se = TwitterSearch()
    se.interface()











