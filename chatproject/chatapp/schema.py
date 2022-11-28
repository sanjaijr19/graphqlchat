import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.contrib.auth.models import User
from .models import GroupDetails,GroupName,Message
from .types import UserType,GroupType,GroupNameType,MessageType
from .mutation import UserMutation,UpdateUser,DeleteUser,CreateGroupName,UpdateGroupName,DeleteGroupName,CreateGroupdetails,UpdateGroupdetails,DeleteGroupdetails,CreateMessage,UpdateMessage,DeleteMessage
from graphql_auth import mutations
import graphql_jwt
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from django_graphene_permissions import permissions_checker
from django_graphene_permissions.permissions import IsAuthenticated
from graphene import relay

class AuthMutation(graphene.Mutation):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    verify_account = mutations.VerifyAccount.Field()



"""User query"""
class Query(graphene.ObjectType):

    # user = graphene.Field(UserType)
    all_user = graphene.List(UserType)

    def resolve_all_user(root, info):
        return User.objects.all()

    # def resolve_user(self, info):
    #     user = info.context.user
    #     if user.is_anonymous:
    #         raise Exception('Not logged in!')
    #
    #     return user



    """groupname query"""
    groupname = graphene.List(GroupNameType)

    def resolve_groupname(root, info):
        return GroupName.objects.all()

    """groupdetails query"""
    group = graphene.List(GroupType)

    def resolve_group(root, info):
        return GroupDetails.objects.all()
    """message query"""
    message = graphene.List(MessageType)
    def resolve_message(root,info):
        return Message.objects.all()

class Mutation(AuthMutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    update_user=UpdateUser.Field()
    create_user=UserMutation.Field()
    delete_user=DeleteUser.Field()
    update_group = UpdateGroupdetails.Field()
    create_group = CreateGroupdetails.Field()
    delete_group= DeleteGroupdetails.Field()
    update_groupname = UpdateGroupName.Field()
    create_groupname = CreateGroupName.Field()
    delete_groupname = DeleteGroupName.Field()
    update_message = UpdateMessage.Field()
    create_message = CreateMessage.Field()
    delete_message = DeleteMessage.Field()

class MessageMutation(AuthMutation,graphene.ObjectType):
    update_message = UpdateMessage.Field()
    create_message = CreateMessage.Field()
    delete_message = DeleteMessage.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)
schemas=graphene.Schema(query=Query,mutation=MessageMutation)