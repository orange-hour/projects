from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from django.http import HttpResponse
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics

# def index(request):
#     return HttpResponse("Hello, world!")

class RegisterView(CreateAPIView):
    """ 회원가입 뷰 - 사용자를 생성합니다. """

    serializer_class = RegisterSerializer

# Blog의 목록을 보여주기 + 새로운 객체 등록
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog detail 보기 + 객체 수정 + 객체 삭제
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer