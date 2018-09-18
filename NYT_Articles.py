from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='7cdfc030f2dd409bbf29b35e219abe84')



head = newsapi.get_top_headlines(sources='the-new-york-times')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_parameter='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/sources
sources = newsapi.get_sources()

a= 0
for i in head:
  print i
  a += 1
  if a == 10:
    break