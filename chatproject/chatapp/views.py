from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView as BaseGraphQLView

class GraphQLView(BaseGraphQLView):
    @classmethod
    def can_display_graphiql(cls, request, data):
        if not request.user or not request.user.is_superuser:
            return False
        return super().can_display_graphiql(request, data)



class PrivateGraphQLView(BaseGraphQLView):
    @classmethod
    def can_display_graphiql(cls, request, data):
        if not request.user or not request.user.is_staff:
            return False
        return super().can_display_graphiql(request, data)