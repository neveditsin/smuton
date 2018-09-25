from rest_framework import views
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from core.serializers import RoundResults
from core.models import Responses
from core.utils.aggregator import Agg
from core.utils import csvutils


class RoundResultView(views.APIView):
    @api_view(['GET'])
    @renderer_classes((JSONRenderer,))
    def get(self):
        #csvutils.import_csv_simple(4, True)
        Agg.aggregate(Responses, 2, 1, 'sum')
        data= [{"team": "t1", "score": 11}, {"team": "t2", "score": 23}]
        
        results = RoundResults(data, many=True).data        
        return Response(results)