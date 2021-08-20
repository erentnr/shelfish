from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.

class Book(models.Model):

    BOOK_STATUS = (
        (-1, 'Not Available'),
        (0, 'Draft'),
        (1, 'Available'),
    )

    title = models.CharField(max_length=70)
    isbn = models.CharField(max_length=13, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    listing_date = models.DateTimeField('date listed', default=timezone.now)
    description = models.TextField(max_length=1000, blank=True)
    number_of_pages = models.IntegerField(default=0)
    author = models.CharField(max_length=70, blank=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='book_owner')
    status = models.IntegerField(choices=BOOK_STATUS, default=1)


    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Proposal(models.Model):

    PROPOSAL_STATUS = (
        (-1, 'Rejected'),
        (0, 'Waiting'),
        (1, 'Accepted'),
    )

    requested_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requested_book')
    proposed_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='proposed_book')
    proposal_date = models.DateTimeField('date published', default=timezone.now)
    status = models.IntegerField(choices=PROPOSAL_STATUS, default=0)

    def __str__(self):
        proposal_name = '{req.title} - {pro.title}'.format(req=self.requested_book, pro=self.proposed_book)
        return proposal_name
