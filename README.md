# COVID SEARCH ENGINE
#### Repository for IRWA final project, UPF 2020/2021
#### Javier Rando - Marc Teixidor - Eduard Vergés

This repository contains the code to implement a Search Engine for Tweets related with COVID-19. It is divided in 5 different sections:
* Streaming tweets related with COVID using Twitter API and hydrate later with interactions: `search_engine/data_acquisition/`
* Indexing this information to build a search engine: `search_engine/Indexing.ipynb`
* A search engine interface to query the content: `search_engine/Search_Engine.ipynb`
* 3 research questions that assess our search engine: output analysis, output diversification and link analysis: `notebook/`
* Useful data for the search engine such as pretrained vectorizer and models: `data/`

All code has been documented and details will be found to ensure reproducibility of the experimental setup.

----

### Important note
In order to fully execute the code, it is required to download all files contained in [this Google Drive folder](https://drive.google.com/drive/u/1/folders/16I4_ZCre59ufD9lDZbFK9cn1mALRmPjB) and store them in the `data/` folder.

These files contain the corpus for our search engine and several intermediate steps that will avoid executing the full code to test a specific component.

----

### Execution pipeline
To simulate the whole experimental process, you will need to follow these steps. If you just want to execute partial code, see [Partial executions](#Partial executions)
1. Stream around 100.000 tweets related to COVID-19 using [`search_engine/data_acquisition/Crawler.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/search_engine/data_acquisition/Crawler.ipynb)
2. Hydrate these tweets after several days to include information about their interactions with [`search_engine/data_acquisition/Hydrate_Tweets.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/search_engine/data_acquisition/Hydrate_Tweets.ipynb)
3. Now, we have our corpus ready to build a search engine. The first step will be indexing the information. For this, use [`search_engine/Indexing.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/search_engine/Indexing.ipynb)
4. The previous script will store all the components that will be required by our final search engine that can be declared and executed through [`search_engine/Search_Engine.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/search_engine/Search_Engine.ipynb). More information about the funcionalities will be found in the search engine README file.

After these four steps we will have a working search engine for COVID-19 related tweets. Afterwards, we can execute the code for 3 different research questions:

1. **Output analysis**. We study the output of our search engine and how the data can be clustered according to their embeddings. The code is found under [`notebook/RQ1_OutputAnalysis.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/notebook/RQ1_OutputAnalysis.ipynb)
2. **Output diversification**. We implement a fairness technique to ensure a fair representation of all semantic clusters within the first results in the ranking. Code is found in [`notebook/RQ2_OutputDiversification.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/notebook/RQ2_OutputDiversification.ipynb)
3. **Link analysis**. We generate a retweets graph for our dataset and implement different techniques to perform recommendations to users and evaluate their accuracy. We use this script [`notebook/RQ3_LinkAnalysis.ipynb`](https://github.com/EduardVergesFranch/COVID_SEARCHENGINE/blob/main/notebook/RQ3_LinkAnalysis.ipynb)

----

### Partial executions
In the previously mentioned [Google Drive Folder](https://drive.google.com/drive/u/1/folders/16I4_ZCre59ufD9lDZbFK9cn1mALRmPjB), we have prepared all intermediate outputs to ease execution of independent parts of the pipeline. At the beggining of each notebook file, you will find the loading cells or further details about which sections can be skipped because output is already prepared.
