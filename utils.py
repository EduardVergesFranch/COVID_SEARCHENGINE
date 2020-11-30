import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords

def personalized_tokenizer(text):
    return text.split()

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