from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an email adress")
		if not username:
			raise ValueError("Users must have uername")

		user = self.model(
				email=self.normalize_email(email),
				username=username,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user 

	def create_superuser(self, email, username, password):
		user = self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,

			)
		user.is_admin = True
		user.is_staff = True 
		user.is_superuser = True 
		user.save(using=self._db)

		return user 

#extends the AbstractBaseUser for an easier implementaion
class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	#sets the login parameter to the user's email
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email + ", " + self.username 

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True 

class Grade(models.Model):
	
	student = models.ForeignKey(Account, on_delete=models.CASCADE)
	letter_grade = models.CharField(max_length=1, default="N")
	subject = models.CharField(max_length=50, default="null")
	percent = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)

	def __str__(self):
		return self.student.username + ": " + self.letter_grade + " in " + self.subject
	
class Subject(models.Model):
	name = models.CharField(max_length=10, default="NA")

	def __str__(self):
		return self.name
	
class Weights(models.Model):
	weight = models.IntegerField(default=0)
	crit = models.CharField(default="N", max_length=100)

	def __str__(self):
		return self.weight
	
class LetterGrades(models.Model):
	letter = models.CharField(max_length=1, default="N")

	def __str__(self):
		return self.letter