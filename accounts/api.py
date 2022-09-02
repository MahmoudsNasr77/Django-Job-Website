from .models import Profile
from rest_framework.decorators import api_view
from .serializers import profileSerializer
from rest_framework.response import Response
@api_view(['GET'])
def profile_list_api(reqeust):
    all_profile=Profile.objects.all()
    data=profileSerializer(all_profile,many=True).data
    return Response({'data':data})
    