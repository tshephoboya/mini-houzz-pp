from professionalsapi.viewsets import ProfesionalViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('professional', ProfesionalViewset)