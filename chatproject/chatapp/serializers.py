from rest_framework import serializers,validators
from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User



class GroupnameSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.ListField(write_only=True)
    group_name = serializers.CharField(required=False)

    class Meta:
        model = GroupDetails
        fields = ['id','group_name','members','date']

    def create(self, validated_data):
        # print(validated_data["group_name"])
        # print(validated_data["members"])
        group_name,created = GroupName.objects.get_or_create(name=validated_data["group_name"])

        for user in validated_data["members"]:
            user = User.objects.get(id=user)
            #print(user.id)
            if user:
                GroupDetails.objects.create(group_name=group_name,members=user)
                print(group_name.id)
            else:
                raise serializers.ValidationError("user does not exist")

            return validated_data


# class UserMessageSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=20)
#     class Meta:
#         model = User
#         fields = ['username']
#
#
# class GroupMessageSerializer(serializers.ModelSerializer):
#     group_name=serializers.SlugRelatedField(many=False, slug_field="name", queryset=GroupName.objects.all())
#
#     class Meta:
#         model = GroupDetails
#         # fields = ['group_name']
#         exclude = ('members',)


# Message Serializer
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field="username", queryset=User.objects.all())
    # group = serializers.SlugRelatedField(many=False, slug_field="name", queryset=GroupName.objects.all())
    # sender = serializers.ListField(child=serializers.CharField())
    sender = serializers.IntegerField()
    group= serializers.ListField(child=serializers.IntegerField())
    message= serializers.CharField()

    # sender = UserMessageSerializer()
    # print(sender)
    # group = GroupMessageSerializer()
    # print(group)
    # message = serializers.CharField()
    #
    # group = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['id','sender', 'group', 'message', 'timestamp']

    # def create(self, validated_data):
    #     return Message.objects.create(**validated_data)

    def create(self, validated_data):
        # print(validated_data["group"])
        # print(validated_data["sender"])
        # print(validated_data["message"])
        sender=User.objects.get(id=(validated_data["sender"]))
        for grp in validated_data["group"]:
            group= GroupDetails.objects.get(group_name_id=grp)
            message= Message.objects.create(message=validated_data["message"])
            msg = Message.objects.create(sender=sender,group=group,message=message)
            return msg
class MessageEditSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only=True)
    group = serializers.CharField(read_only=True)
    class Meta:
        model = Message
        fields = ['id','sender', 'group', 'message', 'timestamp']
    def create(self, validated_data):
        return Message.objects.create(**validated_data)


class GroupViewSerializer(serializers.ModelSerializer):
    group_name = serializers.SlugRelatedField(many=False,slug_field="name",queryset=GroupName.objects.all())
    members = serializers.SlugRelatedField(many=False,slug_field="username",queryset=User.objects.all())
    class Meta:
        model = GroupDetails
        fields = ['id', 'group_name', 'members', 'date']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # groupname = GroupmemberSerializer(many=True,read_only=True)
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = GroupName
        fields = ['id', 'name',]

    def validate(self, attrs):
        if GroupName.objects.filter(name=attrs['name']).exists():
            raise serializers.ValidationError("group already exists")
        return super().validate(attrs)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="CreateUser")
    members = GroupnameSerializer(many=True,read_only=True)
    password = serializers.CharField(write_only=True)
    sender = MessageEditSerializer(many=True,read_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password','members','sender']
    def create(self, validated_data):
        return User.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)




from graphql_jwt.decorators import superuser_required

class UserEditSerializer(serializers.ModelSerializer):

    is_staff=serializers.BooleanField(default=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", 'password','is_staff')


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                            validated_data['password'])
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance



    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)




