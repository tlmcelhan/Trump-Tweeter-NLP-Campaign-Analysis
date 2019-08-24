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

What if istead of looking at the money raised as the sole means to advertise to get votes, we looked at the money raised as an indicator of how many votes you might already have? If candidates started looking at the problem from this perspective outlets like twitter become even more important. In order to evaluate this, I will be looking at Trump's Twitter feed along side his campaign donations to determine if what he tweets has any impact on how much he raises.  
  
In the year before the 2020 presidential election and with the importance of the outcome for many, candidates are looking for the edge. And as most would suspect the more a candidate spends on thier campaign, the more likely they are to win. "For House seats, more than 90 percent of candidates who spend the most win. From 2000 through 2016, there was only one election cycle where that wasn’t true: 2010."[[1]](https://fivethirtyeight.com/features/money-and-elections-a-complicated-love-story/) This doesn't tell the whole story though. Suprisingly, in "big" elections like presidential general elections the more a candidate spends on advertising actually has little affect on the outcome. [[1]](https://fivethirtyeight.com/features/money-and-elections-a-complicated-love-story/) This is where twitter and social media come into play... The whole point to spending large amounts of money on a campaign is to get the candidates message out. Typically, this takes a large amount of money, but social media has word of mouth free advertisement you can't buy.  

The assumption was made that picking a candidate that tweets the most would provide the largest most complete dataset available for NLP analysis. Thus, Trump was selected for this project. To determine the success of his tweeting in regards to his campaign, both the analysis and modeling will be used to determine whether or not his donations go up as a result of his words.  

In gathering the data for Trump's Twitter account @therealdonaldtrump, the Twitter API was very limited allowing non-paying users to pull only 200 tweets going back only 30 days. Because of this, an archived dataset was downloaded from the [Trump Twitter Archive](http://www.trumptwitterarchive.com/archive). This dataset included all non-retweeted posts from January 1, 2019 until June 30,2019. Please refer to the original dataset in this repository's datasets folder for complete dataset information. The twitter dataset was then joined with a dataset gathered from [FEC.gov](https://www.fec.gov/data/candidates/president/?election_year=2020&cycle=2020&election_full=true)(Federal Election Commitee).This dataset is a comprehensive set of all donations made to the Trump presidential campaign between Jan. 1, 2019 and June 30,2019. By law all candidates must post quarterly reports of all inidividual donations to their campaign. Thus as of the time of this project, this was he most up-to-date filing available. "The Federal Election Commission (FEC) is the independent regulatory agency charged with administering and enforcing the federal campaign finance law. The FEC has jurisdiction over the financing of campaigns for the U.S. House, Senate, Presidency and the Vice Presidency."[[2]](fec.gov/about/mission-and-history/)  



## Resources 
- [[1] How Money Affects Election, Maggie Koerth-Baker](https://fivethirtyeight.com/features/money-and-elections-a-complicated-love-story/)
- [[2] FEC.org](fec.gov/about/mission-and-history/)
