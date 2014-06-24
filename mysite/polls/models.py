
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Poll(models.Model):

	def __unicode__(self): 
		return self.question
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field= 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	question = models.CharField(max_length=200)
	pub_date =models.DateTimeField('date published')

	def test_was_published_recently_with_old_poll(self):

		old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_poll.was_published_recently(), False)

	def test_was_published_recently_with_recent_poll(self):

		recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1)
		self.assertEqual(recent_poll.was_published_recently(), True)

class Choice(models.Model):
	def __unicode__(self):
		return self.choice_text
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
