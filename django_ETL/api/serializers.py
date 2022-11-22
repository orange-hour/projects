from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#import 모듈 추가
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class RegisterSerializer(serializers.Serializer):
    """ 회원가입 시리얼라이저 """

    username = serializers.CharField(write_only=True, max_length=159)
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    password_check = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    name = serializers.CharField(write_only=True, max_length=10)
    email = serializers.EmailField(write_only=True)
    gender = serializers.ChoiceField(write_only=True, choices=User.GENDER_CHOICES, required=False,
                                     allow_null=True)
    age = serializers.IntegerField(write_only=True, min_value=1, required=False, allow_null=True)
    phone = serializers.CharField(write_only=True, required=False, allow_null=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        """
        회원가입 데이터를 검증합니다.
        1. 아이디 중복 체크
        2. 비밀번호
        """

        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError({'username', '이미 존재하는 아이디입니다.'})
        if attrs['password'] != attrs['password_check']:
            raise ValidationError({'password', '비밀번호와 비밀번호 확인이 일치하지 않습니다.'})
        return attrs

    def create(self, validated_data):
        """ validated_data를 받아 유저를 생성한 후 토큰을 반환합니다. """

        # 유저 생성
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            name=validated_data['name'],
            email=validated_data['email'],
        )

        # 추가 정보 저장
        user.gender = validated_data.get('gender', None)
        user.age = validated_data.get('age', None)
        user.phone = validated_data.get('phone', None)
        user.save()