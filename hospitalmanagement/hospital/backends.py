from django.contrib.auth.backends import ModelBackend

from .models import User

 

class EmailOTPBackend(ModelBackend):

    def authenticate(self, request, email=None, otp=None, **kwargs):

       

        try:

            user = User.objects.get(email=email)

            if user.otp == otp:

                user.otp = None

                user.is_email_verified = True

                user.save()

                return user

        except User.DoesNotExist:

            return None