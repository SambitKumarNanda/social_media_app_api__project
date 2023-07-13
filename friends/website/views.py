from .serializer import FriendModelListSerializer
from ..models import FriendModel
from userprofile.models import UserProfileModel
from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializer import FriendModelAcceptSerializer


class FriendRequestModelSendRequestAPIView(views.APIView):
    def post(self, request, id):
        try:
            friend_instance = UserProfileModel.objects.get(id=id)
            userprofile_instance = UserProfileModel.objects.get(
                user=request.user)
            print(userprofile_instance.user.email)

            if friend_instance.friends.filter(id=userprofile_instance.id).exists():
                return Response({"message": "You are already friends"}, status=status.HTTP_200_OK)
            else:
                new_friend_instance = FriendModel.objects.create(
                    request_status="PENDING"
                )
                new_friend_instance.target_user.add(friend_instance.user)
                new_friend_instance.save()
                # data=userprofile_instance.friends.all()
                # data.append(new_friend_instance)
                userprofile_instance.friends.add(new_friend_instance)
                userprofile_instance.save()
                return Response({"message": "Friend request sent successfully"}, status=status.HTTP_200_OK)

        except UserProfileModel.DoesNotExist:
            return Response({"message": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class FriendRequestModelAcceptRequestGenericAPIView(views.APIView):
#     def post(self, request, id):
#         try:
#             current_user_userprofile_instance = UserProfileModel.objects.get(
#                 user=request.user)
#             friend_userprofile_instance = UserProfileModel.objects.get(id=id)
#             FriendModel.objects.get()

#         except Exception as e:
#             return Response({"message": e}, status=status.HTTP_200_OK)


# class FriendRequestModelRejectRequestAPIView(views.APIView):
#     def post(self, request, id):
#         return Response({"message": "Friend Request has been rejected"}, status=status.HTTP_200_OK)
