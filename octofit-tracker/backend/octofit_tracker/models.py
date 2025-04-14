# models.py
# Define models for users, teams, activity, leaderboard, and workouts collections.

from bson import ObjectId
from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=255)
    members = models.JSONField(default=list)  # Store user IDs as a list of strings
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.user.email}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    id = models.ObjectIdField(primary_key=True, default=ObjectId)

    def __str__(self):
        return f"{self.user.email} - {self.score}"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
