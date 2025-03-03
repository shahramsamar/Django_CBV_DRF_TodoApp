from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models.users import User
from accounts.models.profiles import Profile
from blog.models import Post



class Command(BaseCommand):
    help= 'inserting dummy data'

    def __init__(self, *args, **kwargs):
        super(Command,self).__init__(*args, **kwargs)
        self.fake = Faker()


    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),
                                        password="Test@#123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.file_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()

        for _ in range(6):
            Post.objects.create(
            user = user,
            title = self.fake.text(max_nb_chars=10),
            content = self.fake.paragraph(nb_sentences=3),
            status = True
            )
        print(f'created {_} post successfully')

        # print(user)
        # print(profile)
        # return super().handle(*args, **options)