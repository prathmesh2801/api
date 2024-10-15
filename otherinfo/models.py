from django.db import models

class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class SixPhoto(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    pic1 = models.ImageField(upload_to='pic1/', null=True, blank=True)
    pic2 = models.ImageField(upload_to='pic2/', null=True, blank=True)
    pic3 = models.ImageField(upload_to='pic3/', null=True, blank=True)
    pic4 = models.ImageField(upload_to='pic4/', null=True, blank=True)
    pic5 = models.ImageField(upload_to='pic5/', null=True, blank=True)
    pic6 = models.ImageField(upload_to='pic6/', null=True, blank=True)

class IdProof(models.Model):
    id_proof = models.ImageField(upload_to='id_proofs/', null=True, blank=True)
    passport_size_photo = models.ImageField(upload_to='passport_photos/', null=True, blank=True)

class DocumentAddress(models.Model):
    address_id = models.CharField(max_length=200)
    certificates = models.FileField(upload_to='certificates/', null=True, blank=True)

class CompatibilityMatch(models.Model):
    how_often_do_you_go_out = models.CharField(max_length=255)
    how_would_you_describe_your_clothes = models.CharField(max_length=255)
    how_do_you_spend_your_free_time = models.CharField(max_length=255)
    how_many_times_do_you_visit_salon_or_beauty_parlour = models.IntegerField()
    how_many_times_do_you_go_out_drinking_or_in_a_pub = models.IntegerField()
    what_would_you_choose_for_a_romantic_date_with_your_partner = models.CharField(max_length=255)
    which_social_platform_do_you_use_most = models.CharField(max_length=255)
    do_you_like_shopping = models.BooleanField(default=False)
    preferences_while_traveling = models.CharField(max_length=255)
    which_personality_are_you = models.CharField(max_length=255)

class ReviewSection(models.Model):
    user_profile = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.FloatField()
    descriptions = models.TextField()
    profile_image = models.ImageField(upload_to='review_images/', null=True, blank=True)

class HabitsDetails(models.Model):
    smoking = models.CharField(max_length=50, choices=[('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')])
    drinking = models.CharField(max_length=50, choices=[('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')])
    food_preference = models.CharField(max_length=50, choices=[('Veg', 'Vegetarian'), ('Non_Veg', 'Non-Vegetarian'), ('Egg', 'Eggetarian')])
    sleep_habits = models.CharField(max_length=100)
    exercise_habits = models.CharField(max_length=100)
    other_habits = models.TextField(blank=True, null=True)

class HobbiesDetails(models.Model):
    hobbies = models.TextField(blank=True, null=True)

class HoroscopeDetails(models.Model):
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    zodiac_sign = models.CharField(max_length=50)
    horoscope_summary = models.TextField(blank=True, null=True)

class ProfileCompletes(models.Model):
    profile_photo_uploaded = models.BooleanField(default=False)
    basic_details_completed = models.BooleanField(default=False)
    education_details_completed = models.BooleanField(default=False)
    horoscope_details_completed = models.BooleanField(default=False)
    family_details_completed = models.BooleanField(default=False)
    partner_preference_details_completed = models.BooleanField(default=False)
    habits_details_completed = models.BooleanField(default=False)
    hobbies_details_completed = models.BooleanField(default=False)
    interest_details_completed = models.BooleanField(default=False)

    def calculate_completion_percentage(self):
        completion_percentage = 0
        total_fields = 9

        if self.profile_photo_uploaded:
            completion_percentage += 1
        if self.basic_details_completed:
            completion_percentage += 1
        if self.education_details_completed:
            completion_percentage += 1
        if self.horoscope_details_completed:
            completion_percentage += 1
        if self.family_details_completed:
            completion_percentage += 1
        if self.partner_preference_details_completed:
            completion_percentage += 1
        if self.habits_details_completed:
            completion_percentage += 1
        if self.hobbies_details_completed:
            completion_percentage += 1
        if self.interest_details_completed:
            completion_percentage += 1

        return (completion_percentage / total_fields) * 100
