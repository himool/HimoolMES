from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from extensions.common.schema import *
from extensions.common.base import *
from extensions.permissions import *
from extensions.exceptions import *
from extensions.viewsets import *
from apps.system.serializers import *
from apps.system.permissions import *
from apps.system.filters import *
from apps.system.schemas import *
from apps.system.models import *


class PermissionGroupViewSet(ListViewSet):
    """权限组"""

    serializer_class = PermissionGroupSerializer
    permission_classes = [IsAuthenticated]
    ordering = ['id']
    prefetch_related_fields = ['permission_set']
    queryset = PermissionGroup.objects.all()


class RoleViewSet(ModelViewSet):
    """角色"""

    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsManagerPermission]
    search_fields = ['name', 'code', 'remark']
    ordering_fields = ['id', 'name', 'update_time', 'create_time']
    prefetch_related_fields = ['permission_set']
    queryset = Role.objects.all()

    @transaction.atomic
    def perform_update(self, serializer):
        role = serializer.save()

        # 同步用户权限
        user_set = role.user_set.prefetch_related('role_set', 'role_set__permission_set').all()
        for user in user_set:
            permissions = {permission.code for role in user.role_set.all()
                           for permission in role.permission_set.all()}
            user.permissions = list(permissions)
        User.objects.bulk_update(user_set, ['permissions'])

    @transaction.atomic
    def perform_destroy(self, instance):
        user_set = instance.user_set.all()
        super().perform_destroy(instance)

        # 同步用户权限
        for user in user_set.prefetch_related('role_set', 'role_set__permission_set').all():
            permissions = {permission.code for role in user.role_set.all()
                           for permission in role.permission_set.all()}
            user.permissions = list(permissions)

        User.objects.bulk_update(user_set, ['permissions'])


class UserViewSet(ModelViewSet):
    """用户"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsManagerPermission]
    filterset_class = UserFilter
    search_fields = ['username', 'name', 'code', 'phone', 'remark']
    ordering_fields = ['id', 'username', 'name', 'update_time', 'create_time']
    prefetch_related_fields = ['role_set']
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        if instance.is_manager:
            raise ValidationError('无法删除管理员账号')

        super().perform_destroy(instance)

    @extend_schema(request=None, responses={204: None})
    @action(detail=True, methods=['post'])
    def reset_password(self, request, *args, **kwargs):
        """重置密码"""

        instance = self.get_object()
        instance.password = make_password(self.user.username)
        instance.save(update_fields=['password'])

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserActionViewSet(FunctionViewSet):
    """用户操作"""

    @extend_schema(request=MakeTokenRequest, responses={200: MakeTokenResponse})
    @action(detail=False, methods=['post'])
    def make_token(self, request, *args, **kwargs):
        """生成令牌"""

        serializer = MakeTokenRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if not (user := User.objects.filter(team__number=validated_data['number'],
                                            username=validated_data['username']).first()):
            raise ValidationError('用户不存在')

        if not check_password(validated_data['password'], user.password):
            raise AuthenticationFailed('密码错误')

        token = RefreshToken()
        token['user_id'] = user.id

        data = {'access': str(token.access_token), 'refresh': str(token)}
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(request=RefreshTokenRequest, responses={200: RefreshTokenResponse})
    @action(detail=False, methods=['post'])
    def refresh_token(self, request, *args, **kwargs):
        """刷新令牌"""

        serializer = RefreshTokenRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        try:
            token = RefreshToken(validated_data['refresh'])
            token.blacklist()
            token.set_jti()
            token.set_exp()
            token.set_iat()
        except TokenError as e:
            raise ValidationError('令牌失效') from e

        data = {'access': str(token.access_token), 'refresh': str(token)}
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(request=LogoffTokenRequest, responses={204: None})
    @action(detail=False, methods=['post'])
    def logoff_token(self, request, *args, **kwargs):
        """注销令牌"""

        serializer = LogoffTokenRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        try:
            token = RefreshToken(validated_data['refresh'])
            token.blacklist()
        except TokenError as e:
            raise NotAuthenticated('令牌失效') from e

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses={200: UserInfoResponse})
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def info(self, request, *args, **kwargs):
        """用户信息"""

        serializer = UserInfoResponse(instance=self.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=SetPasswordRequest, responses={204: None})
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def set_password(self, request, *args, **kwargs):
        """设置密码"""

        serializer = SetPasswordRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if not check_password(validated_data['old_password'], self.user.password):
            raise AuthenticationFailed('密码错误')

        self.user.password = make_password(validated_data['new_password'])
        self.user.save(update_fields=['password'])

        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = [
    'PermissionGroupViewSet', 'RoleViewSet', 'UserViewSet', 'UserActionViewSet',
]
