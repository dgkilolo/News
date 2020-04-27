class News:
  '''
  News class to define News Source Objects.
  '''

  def __init__(self,id,name,description,category,url):
    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.url = url

class Articles:
  '''
  Articles class to define news article objects.
  '''

  def __init__ (self, author, title, description, url, publishedAt, content, urlToImage):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.publishedAt = publishedAt
    self.content = content
    self.urlToImage = urlToImage