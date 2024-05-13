from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile


class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="test_user", email="test@example.com", password="test_password"
        )

    def test_create_profile(self):
        # Check if the profile already exists for the user
        existing_profile = Profile.objects.filter(user=self.user).first()
        if existing_profile:
            existing_profile.bio = "Updated bio"
            existing_profile.save()
        else:
            # Create a profile if it doesn't exist
            Profile.objects.create(
                user=self.user,
                bio="Test bio",
                profile_image="http://example.com/image.jpg",
                address="Test Address",
            )

        # Retrieve the profile
        profile = Profile.objects.get(user=self.user)

        # Ensure that the profile is associated with the correct user
        self.assertEqual(profile.user, self.user)

        # Check additional profile fields if needed
        self.assertEqual(profile.bio, "Updated bio")
        profile_str_rep = f"<Profile for {self.user.username}>"
        self.assertEqual(str(profile), profile_str_rep)
