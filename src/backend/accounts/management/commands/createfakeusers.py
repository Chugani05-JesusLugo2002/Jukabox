from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from users.models import Profile

class Command(BaseCommand):
    help = 'Sign up profiles with given usernames.'

    def add_arguments(self, parser):
        parser.add_argument('usernames', nargs='+', help='List of usernames to create profiles for')
        
    def handle(self, *args, **kwargs):
        usernames = kwargs['usernames']
        for username in usernames:
            email = f"{username}@example.com"
            try:
                user = User.objects.create_user(username=username, email=email, password='1234')
                profile = Profile.objects.create(user=user) 
                self.stdout.write(self.style.SUCCESS(f'Successfully created profile for {username} with id {profile.id}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating profile for {username}: {e}'))