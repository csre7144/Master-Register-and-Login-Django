from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class  UserProfile(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']\
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["first_name"].widget.attrs.update({"class":"input100"})
            self.fields["last_name"].widget.attrs.update({"class":"input100"})
            self.fields["username"].widget.attrs.update({"class":"input100"})
            self.fields["email"].widget.attrs.update({"class":"input100", "placeholder":"Re-Password"})
            self.fields["password1"].widget.attrs.update({"class":"input100" , "placeholder":"Re-Password"})
            self.fields["password2"].widget.attrs.update({"class":"input100", "placeholder":"Re-Password"})