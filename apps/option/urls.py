from extensions.routers import *
from apps.option.views import *


router = BaseRouter()

# System
router.register('roles/options', RoleOptionViewSet, 'role_option')
urlpatterns = router.urls
