from extensions.routers import *
from apps.production.views import *


router = BaseRouter()
router.register('process_routes', ProcessRouteViewSet, 'process_route')
urlpatterns = router.urls
