from django import forms 
from .models import Tweet



class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['Post','Image']
        # exclude = ('slug',)
        widgets = {
            'Post': forms.Textarea(attrs={'class':'form-control textarea textarea-Post-main','style':'height: 108px','placeholder':"What's Happening ?"}),
            'Image': forms.ClearableFileInput(attrs={'class':'Post_Image_load r-xfsgu1 r-4qtqp9 r-yyyyoo r-1q142lx r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1srniue','style':''}),
            # 'Image': forms.Select(attrs={'class':'form-control','style':'border: 1px solid #e8e8e8;background: transparent;height: 45px;'}),       
        }