from rest_framework import serializers
from .models import Profile
state_choices = (
    ("pradesh1", "Koshi Pradesh"),
    ("pradesh2", "Madhesh Pradesh"),
    ("pradesh3", "Bagmati Pradesh"),
    ("pradesh4", "Gandaki Pradesh"),
    ("pradesh5", "Lumbini Pradesh"),
    ("pradesh6", "Karnali Pradesh"),
    ("pradesh7", "Sudurpashchim Pradesh"),
)

class ProfileSerializers(serializers.Serializer):
    name = serializers.CharField(
        max_length = 100 ,
        allow_null=False,
        allow_blank=False,
        required=True,
        error_messages={
         'invalid': 'Not a valid string.',
        'blank': 'This field may not be blank.',
        'max_length': 'Ensure this field has no more than {max_length} characters.',
        'min_length': 'Ensure this field has at least {min_length} characters.',
        }        
                           )
    email = serializers.EmailField( required=True)
    dob = serializers.DateField( required=True)
    state = serializers.ChoiceField(choices=state_choices)
    gender = serializers.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        required=True
    )
    location = serializers.CharField(max_length=200, required=False)
    profile_image = serializers.ImageField(
        required=False,
        allow_null=True,
        error_messages = {
        'invalid_image': 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.'
        }
    )
    document = serializers.FileField(
        required=True,
        allow_null=True,
        error_messages = {
        'required': 'No file was submitted.',
        'invalid': 'The submitted data was not a file. Check the encoding type on the form.',
        'no_name': 'No filename could be determined.',
        'empty': 'The submitted file is empty.',
        }
    )
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)