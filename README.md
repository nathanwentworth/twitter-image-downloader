# twitter-image-downloader
simple python script using tweepy to download all images from a tweet (or list of tweets)

## requirements
[tweepy](https://docs.tweepy.org/en/stable/install.html)
which can be installed by running `pip install tweepy`

twitter v1.1 api key, which can be gotten from [twitter's developer portal](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api). duplicate the file `sample.env` and name it `.env`, inserting the required variables

## usage

in the folder:

`python3 main.py [url(s) of tweets to download]`

ie, `python3 main.py https://twitter.com/nathanwentworth/status/1486104957921202181 https://twitter.com/nathanwentworth/status/1485722732109123592` will download these two tweets, and all images within each one.

the downloaded file names are in the format of `username-tweetid-index`, ie `nathanwentworth-1486104957921202181-01.jpg`
