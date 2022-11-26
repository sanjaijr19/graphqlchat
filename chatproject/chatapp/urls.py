from django.urls import path
from .views import GraphQLView
from chatapp.schema import schema,schemas
from .views import PrivateGraphQLView

urlpatterns = [
    path("",GraphQLView.as_view(graphiql=True,schema=schema)),
    path("user/",PrivateGraphQLView.as_view(graphiql=True,schema=schemas))
]