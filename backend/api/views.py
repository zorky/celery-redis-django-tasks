# coding=utf-8
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.tasks import send_mail_task

class SendMailApi(APIView):
    permission_classes = [AllowAny]
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        send_mail_task.delay('ne-pas-repondre@duval.dev',
                             'Un mail !',
                              ['olivier@ntld.dev'])
        return Response({'data': 'je réponds immédiatement sans attendre la fin de la tâche !'})