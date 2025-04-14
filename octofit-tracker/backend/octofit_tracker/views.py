# views.py
# Updated views to include the codespace URL for API responses

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Import models for the viewsets
from .models import User, Team, Activity, Leaderboard, Workout
# Import serializers for the viewsets
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://silver-fishstick-v6rq7vpw7v5j2j4x-8000.app.github.dev"
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
