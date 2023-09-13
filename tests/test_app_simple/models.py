from django.db import models


class Note(models.Model):
    """
    Note couldn't be read by anyone but the author.
    """

    user_attribute = "author"

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)


class Post(models.Model):
    """
    Post could be read by anyone.
    """

    user_attribute = "author"

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
