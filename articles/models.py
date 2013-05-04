from django.db import models
from django.core.validators import MaxLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=200)
    article_text = models.TextField(validators=[MaxLengthValidator(3000)])
    date_change = models.DateTimeField('date last changes')

    def __unicode__(self):
        if len(self.title)<50:
            return self.title
        else:
            return self.title[:46]+' ...'

    def preview(self):
        if len(self.article_text)<200:
            return self.article_text
        else:
            return self.article_text[:196]+' ...'

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment_text = models.TextField(validators=[MaxLengthValidator(1000)])
    date_pub = models.DateTimeField('date published', auto_now=True)

    def __unicode__(self):
        if len(self.comment_text)<50:
            return self.comment_text
        else:
            return self.comment_text[:45]+' ...'
    
