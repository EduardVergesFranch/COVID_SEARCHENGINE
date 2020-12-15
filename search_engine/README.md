# SEARCH ENGINE

In this folder, you will find the code to:
1. Create a corpus streaming tweets from Twitter API and later on enrich them with their interactions: `data_acquisiton/`
2. Indexing the corpus offline: `Indexing.ipynb`
3. Building a search engine that answers queries in real time using different techniques: `Search_Engine.ipynb`

---

### Search engine execution details

First of all, you will need to execute the code for corpus generation and indexing or download the prebuilt data from [this Google Drive Folder](https://drive.google.com/drive/u/1/folders/16I4_ZCre59ufD9lDZbFK9cn1mALRmPjB) and store it in `~/data`.

Now, we are ready to execute the `Search_Engine.ipynb` script.

The first cells load the required data and define the `TwitterSearch` class that will be later used as our search engine. Finally, the last two cells declare an instance of this class and use the `interface()` method that will create a user friendly search engine.

#### Interface

The search engine will ask the user three different sequential questions:  
1. **Number of results that should be retrieved**.  
*Possible values*: `integer value greater than 0`, otherwise this will be interpreted as a signal to stop the search engine.  
*Description*: indicates how many tweets do we want the search engine to display after querying.

2. **Relevance score to be used**.  
*Possible values*: `1` for TF_IDF and `2` for TF_IDF and authority.  
*Description*: Our search engine implements two different techniques to retrieve results. One of them is based only in TF-IDF cosine similarity between tweets and query. The second one, also incorporates authority (computed using retweets, favorites and followers) to the relevance score. This second approach increases the performance of the search engine.

3. **Query**  
*Possible values*: any string  
*Description*: now it is time to introduce the query to search within our corpus.

4. **Do you want to input another query?**  
*Possible values*: `y` for yes and `n` for no.  
*Description*: if we select `y` the interface will be reseted to input new queries, otherwise the search engine will stop.

#### Output
The output of our search engine will display the desired number of tweets using the following format
````
--> Position
Tweet full text...

User name  |  Posted at  |  Hashtags  | Favorites  | Retweets |  URL  | Followers
````

This is a sample output:

`````
--> 2
England witnessed its highest death rate in over a decade in the year to end October as a result of the Covid pandemic, according to data released by the Office for National Statistics. 

katniss  |  19-11-2020 at 15:54  |  No hashtags  | Favorites:  2  | Retweets:  0  |  No url  | Followers:  3950
`````
