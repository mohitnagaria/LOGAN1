from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=120)
	category = models.CharField(max_length=200, default='Enter trek type, e.g. Himalyan Trek, Western Ghats Trek etc')
	region = models.CharField(max_length=120, default='Let us know if you have been here..')
	
	Post_List_img = models.FileField(null=True, blank=True)
	Cover_Pic = models.FileField(null=True, blank=True)
	Content_Pic = models.FileField(null=True, blank=True)

	trail_highlights = models.TextField(default='Let us know if you have been here..')
	highest_altitude = models.CharField(max_length=120, default='Let us know if you have been here..')
	about_the_trek = models.TextField(default='Let us know if you have been here..')
	access_time = models.TextField(default='Let us know if you have been here..')
	best_time = models.TextField(default='Let us know if you have been here..')
	Exploration_Spots = models.TextField(default='Let us know if you have been here..')

	trek_duration = models.CharField(max_length=120, default='Let us know if you have been here..')
	trek_length = models.CharField(max_length=120, default='Let us know if you have been here..')
	endurance_level = models.CharField(max_length=120, default='Let us know if you have been here..')
	difficulty = models.CharField(max_length=120, default='Let us know if you have been here..')
	
	route_to_base_camp = models.CharField(max_length=120, default='Let us know if you have been here..')
	route_details = models.TextField(default='Let us know if you have been here..')
	trek_route = models.TextField(default='Let us know if you have been here..')
	wildlife_reserve = models.CharField(max_length=120, default='Let us know if you have been here..')
	food_availability = models.TextField(default='Let us know if you have been here..')
	water_availability = models.TextField(default='Let us know if you have been here..')
	shade_availability = models.TextField(default='Let us know if you have been here..')
	accomodation = models.TextField(default='Let us know if you have been here..')
	police_station = models.CharField(max_length=200, default='Let us know if you have been here..')
	bus_stand = models.CharField(max_length=200, default='Let us know if you have been here..')
	railway_station = models.CharField(max_length=200, default='Let us know if you have been here..')
	airport = models.CharField(max_length=200, default='Let us know if you have been here..')
	local_govt_authority = models.TextField(default='Let us know if you have been here..')
	Summit_Lat = models.DecimalField(max_digits=19, decimal_places=15, default='0.000')
	Summit_Lng = models.DecimalField(max_digits=19, decimal_places=15, default='0.000')
	base_village = models.CharField(max_length=120, default='Let us know if you have been here..')
	Base_Village_Lat = models.DecimalField(max_digits=19, decimal_places=15, default='0.000')
	Base_Village_Lng = models.DecimalField(max_digits=19, decimal_places=15, default='0.000')
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
