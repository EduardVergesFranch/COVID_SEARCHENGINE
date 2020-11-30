import argparse
import pandas as pd
import os
import json
from utils import clean_text, personalized_tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def get_full_text(short_text, full_text):
  if str(full_text) != 'nan':
    return full_text['full_text']
  else:
    return short_text

def main(input_file, hydrate, output_path):

    print("Reading source file...\n")

    with open(input_file, "rb") as f:
        data = f.readlines()
        data = [json.loads(str_) for str_ in data]

    df_tweets = pd.DataFrame.from_records(data)

    print("Filtering out retweets to keep only original tweets... \n")
    df_tweets = df_tweets.loc[~df_tweets['full_text'].str.startswith("RT")]

    print("Your dataset has {} tweets".format(len(df_tweets)))

    print("Identifying full text... \n")
    df_tweets['full_text'] = df_tweets.apply(lambda x: get_full_text(x['text'], x['extended_tweet']), axis=1)

    print("Cleaning text...\n")
    df_tweets['clean_text'] = df_tweets['full_text'].apply(lambda x: clean_text(x))

    print("Exporting resulting dataframe as `df_tweets.csv...\n")
    df_tweets.to_csv(output_path + 'df_tweets.csv')

    print("Vectorizing information using TF-IDF...\n")
    corpus = df_tweets['clean_text']
    vectorizer = TfidfVectorizer(tokenizer=personalized_tokenizer, lowercase=False)
    tf_idf = vectorizer.fit_transform(corpus)

    print("Storing vectorizer as `vectorizer.pickle`")
    pickle.dump(vectorizer, open(output_path + "vectorizer.pickle", "wb"))

    if hydrate:
        print("Hydrating tweets...\n")
        hydrated_tweets = df_tweets
        #TODO: include code to hydrate

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Indexing tweets for search engine')
    parser.add_argument('-i', '--input_file',
                        help='Specify the json file to read tweets from',
                        required=True)
    parser.add_argument('-o', '--output_file',
                        help='Specify the output file. By default, current folder',
                        default='./')
    parser.add_argument('-h', '--hydrate',
                        help='Specify if you want to hydrate the tweets to include further information',
                        default=True)

    args = parser.parse_args()

    main(input_file=args.input_file, hydrate=args.hydrate, output_path=args.output_file)