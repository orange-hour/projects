from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    """ 회원가입 뷰 - 사용자를 생성합니다. """

    serializer_class = RegisterSerializer


# def index(request):
#     return HttpResponse(HTMLtemplate())
    
# def create(request):
#     return HttpResponse('Create')

# def read(request, id): #바뀔 수 있는 값을 파라미터로 지정(id)
#     return HttpResponse('Read!'+id)

