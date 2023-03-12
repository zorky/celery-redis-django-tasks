# coding=utf-8
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.tasks import execute_long_task

class ExecuteTaskApi(APIView):
    permission_classes = [AllowAny]
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        execute_long_task.delay('Exécute ma longue tâche !', 5,
                                ['Vais attendre', 'le super pouvoir de Celery'])
        return Response({'data': 'je réponds immédiatement sans attendre la fin de la tâche !'})