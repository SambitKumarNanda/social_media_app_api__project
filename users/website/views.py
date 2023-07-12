from .serializers import WebsiteRegisterSerializer, WebsiteVerifyUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, status, views
from rest_framework.response import Response
from ..utils import generate_otp
from django.core.exceptions import ObjectDoesNotExist
from ..models import OTPModel
from rest_framework_simplejwt.tokens import RefreshToken


class WebsiteCreateOTPView(views.APIView):
    
    def post(self, request):
        new_otp = generate_otp()
        if not (get_user_model().objects.get(email=request.data['email'])):
            return Response({f"Create a new account using this otp {new_otp}"}, status=status.HTTP_200_OK)
        if OTPModel.objects.filter(email=request.data['email']).exists():
            prev_otp = OTPModel.objects.get(
                email=request.data['email'])
            prev_otp.is_active = False
            prev_otp.save()
            OTPModel.objects.create(
                email=request.data['email'],
                code=new_otp,
            )
        else:
            new_otp = generate_otp()
            print(new_otp)
            OTPModel.objects.create(
                email=request.data['email'],
                code=new_otp,
            )
        return Response({"message": f"Your new otp is {new_otp}"}, status=status.HTTP_200_OK)


class WebsiteVerifyUserLogin(generics.GenericAPIView):
    queryset = OTPModel.objects.all()
    serializer_class = WebsiteVerifyUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        user_instance = get_user_model().objects.get(email=request.data['email'])
        refresh = RefreshToken.for_user(user_instance)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Logging in successful',
                             'refresh-token': f"{str(refresh)}",
                             'access-token': f"str(refresh.access_token)"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":f"Something is wrong {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class WebsiteRegisterGenericAPIView(generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = WebsiteRegisterSerializer
    
    def put(self, request):
        serializer = self.serializer_class(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)