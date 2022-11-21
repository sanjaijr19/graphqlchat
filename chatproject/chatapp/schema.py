import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import GroupDetails,GroupName

class UserType(DjangoObjectType):
    class Meta:
        model=User
        fields=("id","username","email",'password')



class CreateUser(graphene.Mutation):
    class Arguments:
        # id=graphene.ID()
        username=graphene.String(required=True)
        email=graphene.String(required=True)
        password=graphene.String(required=True)
    user=graphene.Field(UserType)

    @classmethod
    def mutate(cls,root,info,username,email,password):
        user=User(username=username,email=email)
        user.username=username
        user.email=email
        user.password=password
        user.save()
        return CreateUser(user=user)
# class Mutation(graphene.ObjectType):
#     create_user=CreateUser.Field()
#
class UpdateUser(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        username=graphene.String(required=True)
        email=graphene.String(required=True)
        password=graphene.String()
    user=graphene.Field(UserType)

    @classmethod
    def mutate(cls,root,info,id,username,email,password):
        user=User.objects.get(id=id)
        # user=User(username=username,email=email)
        user.username=username
        user.email=email
        user.password=password
        user.save()
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
        username=graphene.String()
        email=graphene.String()
        password=graphene.String()
    user=graphene.Field(UserType)

    @classmethod
    def mutate(cls,root,info,id,username,email,password):
        user=User.objects.get(id=id)
        # user=User(username=username,email=email)
        user.username=username
        user.email=email
        user.password=password
        user.delete()
        return DeleteUser(user=user)


class GroupNameType(DjangoObjectType):
    class Meta:
        model=GroupName
        fields=("id","name")

class CreateGroupName(graphene.Mutation):
    class Arguments:
        # id=graphene.ID()
        name=graphene.String(required=True)
    group=graphene.Field(GroupNameType)

    @classmethod
    def mutate(cls,root,info,name):
        group=GroupName(name=name)
        group.name=name
        group.save()
        return CreateGroupdetails(group=group)

class UpdateGroupName(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name=graphene.String(required=True)
    group=graphene.Field(GroupNameType)

    @classmethod
    def mutate(cls,root,info,id,name):
        group=GroupName.objects.get(id=id)
        # user=User(username=username,email=email)
        group.name=name
        group.save()
        return UpdateGroupName(group=group)

class DeleteGroupName(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
        name=graphene.String()
    group=graphene.Field(GroupNameType)

    @classmethod
    def mutate(cls,root,info,id,name):
        group=GroupName.objects.get(id=id)
        # user=User(username=username,email=email)
        group.name=name
        group.delete()
        return DeleteGroupName(group=group)


class GroupType(DjangoObjectType):
    class Meta:
        model=GroupDetails
        fields=("id","group_name","members","date")


class CreateGroupdetails(graphene.Mutation):
    class Arguments:
        # id=graphene.ID()
        group_name=graphene.String(required=True)
        members=graphene.String(required=True)
    group=graphene.Field(GroupType)

    @classmethod
    def mutate(cls,root,info,group_name,members):
        group=GroupDetails(group_name=group_name,members=members)
        group.group_name=group_name
        group.members=members
        group.save()
        return CreateGroupdetails(group=group)

class UpdateGroupdetails(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        group_name=graphene.String(required=True)
        members=graphene.String(required=True)
    group=graphene.Field(GroupType)

    @classmethod
    def mutate(cls,root,info,id,group_name,members):
        group=User.objects.get(id=id)
        # user=User(username=username,email=email)
        group.group_name=group_name
        group.members=members
        group.save()
        return UpdateGroupdetails(group=group)

class DeleteGroupdetails(graphene.Mutation):
    class Arguments:
        id=graphene.ID(required=True)
        group_name=graphene.String()
        members=graphene.String()
    group=graphene.Field(GroupType)

    @classmethod
    def mutate(cls,root,info,id,group_name,members):
        group=GroupDetails.objects.get(id=id)
        # user=User(username=username,email=email)
        group.group_name=group_name
        group.members=members
        group.delete()
        return DeleteGroupdetails(group=group)



class Query(graphene.ObjectType):
    all_user = graphene.List(UserType)

    def resolve_all_user(root, info):
        return User.objects.all()


    groupname = graphene.List(GroupNameType)

    def resolve_groupname(root, info):
        return GroupName.objects.all()


    group = graphene.List(GroupType)

    def resolve_group(root, info):
        return GroupDetails.objects.all()


class Mutation(graphene.ObjectType):
    update_user=UpdateUser.Field()
    create_user=CreateUser.Field()
    delete_user=DeleteUser.Field()
    update_group = UpdateGroupdetails.Field()
    create_group = CreateGroupdetails.Field()
    delete_group= DeleteGroupdetails.Field()
    update_groupname = UpdateGroupName.Field()
    create_groupname = CreateGroupName.Field()
    delete_groupname = DeleteGroupName.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)