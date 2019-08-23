# Trump-Tweeter-NLP-Campaign-Analysis
### Authored by: Trevor McElhaney  
![](https://pmcvariety.files.wordpress.com/2018/04/twitter-logo.jpg?w=1000&h=562&crop=1)
## Problem Statement 

With the upcoming 2020 presidential election and the ever-growing importance of social media to communicate campaign messages, the goal of this repository is to determine whether or not candidate tweets have predictive power on their campaign donations. Specifically, this project focuses on using Natural Language Processing and time-series analysis to evaluate Donald Trump's tweets and to find correlation to whether or not his campaign donations go up or down based upon them. The success of this project is based on whether or not any information on donations can be gained from the analysis. The predictive power of the models will be measured against the naive accuracy of 51.9%.  

## Data dicionary  
|Feature|Type|Dataset|Description|
|-------|----|-------|-----------|
|text|object|trump_tweets.csv|Text from the @therealdonaldtrump twitter account.|
|created_at|object|trump_tweets.csv|Date and time of tweet post.|
|favorite_count|integer|trump_tweets.csv|Number of times the tweet post has been marked as a user's favorite.|
|title_char_count|integer|reddit_clean_dataset|The number of characters in the title of a sub-reddit post.|
|selftext_char_count|integer|reddit_clean_dataset|The number of characters in the body of a sub-reddit post.|
|title_word_count|integer|reddit_clean_dataset|The number of words in the title of a sub-reddit post.|
|selftext_word_count|integer|reddit_clean_dataset|The number of words in the body of a sub-reddit post.|
|compound|float|sentiment_dataset|The compound sentiment score of a sub-reddits title|
|neg|float|sentiment_dataset|The negative sentiment score of a sub-reddits title|
|neu|float|sentiment_dataset|The neutral sentiment score of a sub-reddits title|
|pos|float|sentiment_dataset|The positive sentiment score of a sub-reddits title|  

## Repo Structure  
- code folder  
  - Cleaning Data- Contains the gathering, cleaning, and merging of the necessary datasets.
  - Tweet EDA- Contains the initial exploratory data analysis of Trump's tweets and donations.
  - Time Series Analysis- Contains the time series analysis of Trump's campaign donations to find any patterns.
  - Model Predictions-Contains multiple models using the findings of the Tweet EDA to predict whether or not Trump's tweets affect his donations. 
- datasets  
  - frequency_dataset.csv
  - full_dataset.csv
  - lsa_dataset.csv
  - schedule_a-2019-08-07T17_19_59.csv  
  - trump_tweets.csv
- images  
  - Saved images and figures from notebooks  
- presentation
  - A .pdf file for the presentation of findings
  
## Exectutive Summary 
