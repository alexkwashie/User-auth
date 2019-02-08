from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #this  is soley for database purposes
from django import forms

#creat function to remove suplus words from webpage
class editProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email',)



#Use Widgets on django doc to add styling to the from
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label= "Enter Email",widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label= "Enter First Name",max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label= "Enter Last Name",max_length =100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].label= 'Username'
        self.fields['username'].help_text='<span><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].label= 'Password'
        self.fields['password1'].help_text=' '

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].label= 'Confirm Password'
        self.fields['password2'].help_text=' '