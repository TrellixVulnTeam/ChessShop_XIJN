from .models import UserAccount
from rest_framework import serializers,validators

class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = UserAccount
        fields =  fields = ('firstName','lastName','profilePicture','city','gender','experience')

        extra_kwargs = {
            "password":{"write_only":True},
            "validators":[
                validators.UniqueValidator(
                    UserAccount.objects.all(),"That user already has an account!"
                )
            ]
        }
    
    def create(self,validated_data):
        firstName = validated_data["firstName"]
        lastName = validated_data["lastName"]
        patronymic = validated_data["patronymic"]
        profilePicture = validated_data["profilePicture"]
        gender = validated_data["gender"]
        experience = validated_data["experience"]
        city = validated_data["city"]
        user = UserAccount.objects.create(  
            firstName = firstName
            lastName = lastName
            patronymic = patronymic
            profilePicture = profilePicture
            gender = gender
            experience = experience
            city = city)
          
        
        return user
