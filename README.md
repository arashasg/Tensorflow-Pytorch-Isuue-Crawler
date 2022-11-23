# Tensorflow-Pytorch-Isuue-Crawler

In this project, first, I crawled issues of TensorFlow and PyTorch frameworks for the last two years. Then we analyzed the data collected in a notebook.
### Data Crawling
We used the Scrapy library to crawl data. We could use selenium and Beautiful Soup for data crawling as well. Scrapy, however, allows you to send parallel requests making the data collection process significantly faster.
I implemented the crawler using Scrapy, but due to the GitHub API request limit, I could only send 5000 requests per hour, making the data crawling process time-consuming. The features crawled from these two repositories are as follows: the number of comments, assignees, reviewers, participants, issue status, and if the issue description contains code.
### Data Analysis
I investigated the correlation between features and the status of issues. Among the features mentioned, only the number of participants shows a clear positive effect on the bug-fixing process. The more participants in an issue, the more the issue is probable to be closed(more graphs available in the notebook for other features).

We first hypothesized that adding code to the description of bug issues may make the issue easier to understand for contributors. But, to our surprise, it is not the case. The issues containing code revealing the failure are less likely to become closed. We guess attaching the code to the issue may give the impression to the bug reporters that the code is self-expressive and they do not need to explain the issue in detail anymore.


