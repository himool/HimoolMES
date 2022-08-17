from extensions.routers import *
from apps.material.views import *


router = BaseRouter()
router.register('material_categories', MaterialCategoryViewSet, 'material_category')
router.register('materials', MaterialViewSet, 'material')
router.register('material_bills', MaterialBillViewSet, 'material_bill')
urlpatterns = router.urls
