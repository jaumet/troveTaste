__author__ = 'jaume@nualart.cat'
from django.db import models
import datetime

try:
    from django.utils.timezone import now as datetime_now
except ImportError:
    datetime_now = datetime.datetime.now

'''
id
query (str)
self.articles, self.article, self.newspaper, self.book, self.picture, self.music, self.people, self.collection, self.map, self.list, self.date
'''
class Queries(models.Model):
    query = models.TextField(max_length=2000)
    article = models.IntegerField(default=0)
    newspaper = models.IntegerField(default=0)
    book = models.IntegerField(default=0)
    picture = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    people = models.IntegerField(default=0)
    collection = models.IntegerField(default=0)
    map = models.IntegerField(default=0)
    list = models.IntegerField(default=0)
    test_date = models.DateField(default=datetime.date.today, null=True)
    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.query, self.article, self.newspaper, self.book, self.picture, self.music, self.people, self.collection, self.map, self.list, self.date)