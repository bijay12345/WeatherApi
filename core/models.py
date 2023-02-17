from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# HERE I AM DEFINING A CUSTOM USER MODEL, THE MODEL INHERITS FROM THE BaseUserManager AND OVERRIDES SOME OF ITS METHODS.
class UserManager(BaseUserManager):
	def create_user(self,email,name,password=None,password2=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
				email=self.normalize_email(email),
				name=name,	
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,name,password=None):
		user=self.create_user(
				email,
				password=password,
				name=name,
			)
		user.is_admin=True  
		user.save(using=self._db)
		return user


# THIS IS THE ACTUAL USER MODEL THAT IS USED FOR THE LOGIN FUNCTIONALITY, IT INHERITS THE AbstractBaseUser.

class User(AbstractBaseUser):
	email=models.EmailField(verbose_name="Email Address",
		max_length=255,
		unique=True
		)
	name=models.CharField(max_length=100,unique=True)
	is_active=models.BooleanField(default=True)
	is_admin=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects=UserManager()

	USERNAME_FIELD="name"
	REQUIRED_FIELDS=['email']

	def __str__(self):
		return self.name

	def has_perm(self,perm,obj=None):
		"Does User has a specific permission"
		return self.is_admin

	def has_module_perms(self,app_label):
		"Does the user has the permission to view the app `app_label` ?"
		return True  

	@property
	def is_staff(self):
		"Is user a member of staff"
		return self.is_admin




# THIS IS THE WEATHER MODEL WHERE ALL THE DATA FROM THE 'openweathermap.org' GETS SAVED, I HAVE USED 4 FIELDS TO CAPTURE SOME BASIC INFORMATION ACCORDING TO THE CITY.

class Weather(models.Model):
    city = models.CharField(max_length=200, blank=True, null=True)
    weather_date = models.CharField(max_length=20)
    maximum_temperature = models.FloatField(blank=True, null=True)
    minimum_temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.city}"