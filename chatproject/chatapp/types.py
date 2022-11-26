from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import GroupDetails,GroupName,Message
from graphene import relay
# from django_graphene_permissions import PermissionDjangoObjectType
# from django_graphene_permissions.permissions import IsAuthenticated
# from graphene_permissions.mixins import AuthNode,AuthFilter
# from graphene_permissions.permissions import AllowAuthenticated,AllowSuperuser


class UserType(DjangoObjectType):
    class Meta:
        model=User

        # exclude = ('Is_active',)
        fields = ("id", "username", "email", 'password')
        # interfaces = (relay.Node, )

    # @staticmethod
    # def permission_classes():
    #     return [IsAuthenticated]


class GroupType(DjangoObjectType):
    class Meta:
        model=GroupDetails
        fields=("id","group_name","members","date")



class GroupNameType(DjangoObjectType):

    class Meta:
        model=GroupName
        fields=("id","name")
        # interfaces = (relay.Node,)

# class AllowAuthenticatedFilter(AuthFilter):
#     permission_classes = (AllowAuthenticated,)
# class GnameQuery:
#     gname = relay.Node.Field(GroupNameType)
#     all_gname = AllowAuthenticatedFilter(GroupNameType)

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields= ('id','sender', 'group', 'message', 'timestamp')


