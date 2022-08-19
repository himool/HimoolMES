from extensions.routers import *
from apps.option.views import *


router = BaseRouter()

# System
router.register('roles/options', RoleOptionViewSet, 'role_option')
router.register('material_categories/options', MaterialCategoryOptionViewSet, 'material_category_option')
router.register('materials/options', MaterialOptionViewSet, 'material_option')

urlpatterns = router.urls
