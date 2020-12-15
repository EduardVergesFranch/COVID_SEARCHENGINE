# COVID SEARCH ENGINE
#### Repository for IRWA final project, UPF 2020/2021
#### Javier Rando - Marc Teixidor - Eduard Vergés

This repository contains the code for:
* Streaming tweets related with COVID using Twitter API and hydrate later with interactions: `search_engine/data_acquisition/`
* Indexing this information to build a search engine: `search_engine/Indexing.ipynb`
* A search engine interface to query the content: `search_engine/Search_Engine.ipynb`
* 3 research questions that assess our search engine: output analysis, output diversification and link analysis: `notebook/`
* Useful data for the search engine such as pretrained vectorizer and models: `data/`

----

### Important note
In order to fully execute the code, it is required to download all files contained in [this Google Drive folder](https://drive.google.com/drive/u/1/folders/16I4_ZCre59ufD9lDZbFK9cn1mALRmPjB) and store them in the `data/` folder.

These files contain the corpus for our search engine and several intermediate steps that will avoid executing the full code to test a specific component.

----

### Execution pipeline
