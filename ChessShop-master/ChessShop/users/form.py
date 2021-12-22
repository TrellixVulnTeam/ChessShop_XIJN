from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['firstName','lastName','profilePicture','city','gender','experience']