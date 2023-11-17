import logging

from rest_framework import views, status
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class TmpViewForTestingZoomDeauthorizationUrl(views.APIView):
    def post(self, request, *args, **kwargs):
        logger.info(f'The Zoom Deauthorization Url works well. The request from Zoom has been received: {request}')
        logger.info(f'The Zoom Deauthorization Url request.params: {request.query_params}')
        logger.info(f'The Zoom Deauthorization Url request.data: {request.data}')

        print(f'The Zoom Deauthorization Url works well. The request from Zoom has been received: {request}')
        print(f'The Zoom Deauthorization Url request.params: {request.query_params}')
        print(f'The Zoom Deauthorization Url request.data: {request.data}')
        return Response({'Success.'}, status=status.HTTP_200_OK)
