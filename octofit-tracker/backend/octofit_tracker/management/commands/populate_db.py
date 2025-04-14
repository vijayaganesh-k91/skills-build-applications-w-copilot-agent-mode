from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta
import os

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        print('DJANGO_SETTINGS_MODULE:', os.environ.get('DJANGO_SETTINGS_MODULE'))
        print('DATABASES configuration:', settings.DATABASES)
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], int(settings.DATABASES['default']['PORT']))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod'),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek'),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool'),
            User(id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride'),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(id=ObjectId(), name='Blue Team', members=[str(users[0].id), str(users[1].id)]),
            Team(id=ObjectId(), name='Gold Team', members=[str(users[2].id), str(users[3].id), str(users[4].id)]),
        ]
        Team.objects.bulk_create(teams)

        # Convert timedelta to total seconds for the duration field
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Cycling', duration=int(timedelta(hours=1).total_seconds())),
            Activity(id=ObjectId(), user=users[1], type='Crossfit', duration=int(timedelta(hours=2).total_seconds())),
            Activity(id=ObjectId(), user=users[2], type='Running', duration=int(timedelta(hours=1, minutes=30).total_seconds())),
            Activity(id=ObjectId(), user=users[3], type='Strength', duration=int(timedelta(minutes=30).total_seconds())),
            Activity(id=ObjectId(), user=users[4], type='Swimming', duration=int(timedelta(hours=1, minutes=15).total_seconds())),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), user=users[0], score=100),
            Leaderboard(id=ObjectId(), user=users[1], score=90),
            Leaderboard(id=ObjectId(), user=users[2], score=95),
            Leaderboard(id=ObjectId(), user=users[3], score=85),
            Leaderboard(id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
