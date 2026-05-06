from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date=date(2024, 5, 1))
        Activity.objects.create(user=steve, type='swim', duration=45, date=date(2024, 5, 2))
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=date(2024, 5, 3))
        Activity.objects.create(user=clark, type='fly', duration=120, date=date(2024, 5, 4))

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='marvel')
        Workout.objects.create(name='Flight Training', description='Flight workout for heroes', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=110)
        Leaderboard.objects.create(user=clark, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
