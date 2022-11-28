import graphene
from rest_framework import serializers
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserEditSerializer,GroupnameSerializer,GroupSerializer,GroupViewSerializer,MessageSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
from .types import UserType,GroupType,GroupNameType,MessageType
from .models import GroupDetails,GroupName,Message
from django_model_mutations import mutations
from django_graphene_permissions import permissions_checker
from django_graphene_permissions.permissions import IsAuthenticated
from graphql_jwt.decorators import login_required

"""
User CRUD
"""
# @login_required
# @permissions_checker([IsAuthenticated])

class UserMutation(mutations.CreateModelMutation):
    class Meta:
        serializer_class = UserEditSerializer




class UpdateUser(mutations.UpdateModelMutation):
    class Meta:
        serializer_class = UserEditSerializer


class DeleteUser(mutations.DeleteModelMutation):
    class Meta:
        model = User

"""
GroupName CRUD
"""

class CreateGroupName(mutations.CreateModelMutation):
    class Meta:
        serializer_class = GroupSerializer


class UpdateGroupName(mutations.UpdateModelMutation):
    class Meta:
        serializer_class = GroupSerializer

class DeleteGroupName(mutations.DeleteModelMutation):
    class Meta:
        model = GroupName


"""
GroupDetails CRUD
"""
class CreateGroupdetails(mutations.CreateModelMutation):
    class Meta:
        serializer_class = GroupViewSerializer

class UpdateGroupdetails(mutations.UpdateModelMutation):
    class Meta:
        serializer_class = GroupViewSerializer

class DeleteGroupdetails(mutations.DeleteModelMutation):
    class Meta:
        model = GroupDetails



"""
message CRUD
"""

class CreateMessage(mutations.CreateModelMutation):
    class Meta:
        serializer_class = MessageSerializer


class UpdateMessage(mutations.UpdateModelMutation):
    class Meta:
        serializer_class = MessageSerializer

class DeleteMessage(mutations.DeleteModelMutation):
    class Meta:
        model = Message







# class CreateGroupdetails(graphene.Mutation):
#     class Arguments:
#         # id=graphene.ID()
#         group_name_id=graphene.ID()
#         members_id=graphene.ID()
#     group=graphene.Field(GroupType)
#
#     def mutate(root,info,group_name_id,members_id):
#         group_name_id = GroupName.objects.get(id=group_name_id)
#         members_id = User.objects.get(id=members_id)
#         group = GroupDetails.objects.create(group_name_id=group_name_id,member_id=members_id)
#         return CreateGroupdetails(group)

#
# class GroupNameInput(graphene.InputObjectType):
#     name=graphene.String()
#
# class UserInput(graphene.InputObjectType):
#     username = graphene.String()
#
# class GroupDetailsInput(graphene.InputObjectType):
#     group_name = graphene.Field(GroupNameInput)
#     members = graphene.Field(UserInput)
#
#
# class CreateGroupdetails(graphene.Mutation):
#     group = graphene.Field(GroupType)
#     class Arguments:
#         groupdata = GroupDetailsInput(required=True)
#
#     @staticmethod
#     def mutate(root,info,groupdata):
#         group = GroupDetails.objects.create(**groupdata)
#         return CreateGroupdetails(group=group)

