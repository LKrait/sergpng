# models.py
from django.db import models
from django.utils import timezone

class SiteVisit(models.Model):
    visit_count = models.PositiveIntegerField(default=0)  # Track the number of visits
    last_visit = models.DateTimeField(null=True, blank=True)  # Store the timestamp of the last visit

    def update_visit(self):
        """Update visit count and last visit time"""
        self.visit_count += 1
        self.last_visit = timezone.now()  # Set the current time as the last visit time
        self.save()

    def __str__(self):
        return f"Visit Count: {self.visit_count}, Last Visit: {self.last_visit}"

