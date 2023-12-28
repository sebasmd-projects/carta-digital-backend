from apps.users.api.filters import UserModelFilter
from apps.users.api.serializers import (UserModelSerializer,
                                        UserModelSerializerGET,
                                        UserModelSerializerPOST_PUT_PATCH)
from apps.users.models import UserModel
from apps.utils.api import DefaultPaginationSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    permission_classes = [IsAdminUser]
    pagination_class = DefaultPaginationSerializer
    filterset_class = UserModelFilter

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserModelSerializerGET
        elif self.request.method in ['POST', 'PUT', 'PATCH']:
            return UserModelSerializerPOST_PUT_PATCH

class UserApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserModelSerializerGET(request.user)
        return Response(serializer.data)

class UserLogoutView(APIView):
    def post(self, request):
        request.session.flush()
        return Response({'message': 'Logged out successfully'})
