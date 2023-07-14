from ..models import FriendModel, FriendRequestModel, FriendRequestSentModel
from userprofile.models import UserProfileModel
from rest_framework import generics, status, views
from rest_framework.response import Response 
from django.core.exceptions import ObjectDoesNotExist

class FriendRequestModelSendRequestAPIView(views.APIView):
    def post(self, request, id):
        try:
            current_userprofile_instance = UserProfileModel.objects.get(user=request.user)
            friend_userprofile_instance = UserProfileModel.objects.get(id=id)
            print(current_userprofile_instance)
            print(friend_userprofile_instance)
            print(type(current_userprofile_instance.friends))
            if UserProfileModel.objects.filter(friends=current_userprofile_instance.user).exists():
                return Response({"message":"You are already a friend of this user"}, status=status.HTTP_200_OK)
            elif UserProfileModel.objects.filter(friend_reqests_sent=friend_userprofile_instance.user).exists():
                return Response({"message": "You have already sent a friend request to this userprofile"}, status=status.HTTP_200_OK)
            elif UserProfileModel.objects.filter(friend_reqests_recieved=current_userprofile_instance.user).exists():
                return Response({"message": "You have got a friend request from this userprofile"}, status=status.HTTP_200_OK)
            else:
                user_friend_sent_request_instance = current_userprofile_instance.friend_reqests_sent
                friend_req_obj = FriendRequestSentModel.objects.create(
                    sent_to=friend_userprofile_instance.user
                )
                
                user_friend_sent_request_instance.add(friend_req_obj)                                                                                                   
                current_userprofile_instance.save()

                friend_req_sent_obj = FriendRequestModel.objects.create(
                    requested_user = current_userprofile_instance.user
                )
                friend_userprofile_instance.friend_reqests_recieved.add(friend_req_sent_obj)
                friend_userprofile_instance.save()
                return Response({"message": "You have successfully sent a friend request"}, status=status.HTTP_200_OK)
                

        except UserProfileModel.DoesNotExist:
            return Response({"message": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class FriendRequestModelAcceptAPIView(views.APIView):
    
    def post(self, request, id):
        try:
            current_user_profile_instance = UserProfileModel.objects.get(user=request.user)
            friend_instance = UserProfileModel.objects.get(id=id)

            if current_user_profile_instance.friend_reqests_recieved.filter(requested_user=friend_instance.user).exists():
                friend_model_current_user = FriendModel.objects.create(
                    friends = friend_instance.user,
                    request_status = "ACCEPTED"
                )
                current_user_profile_instance.friends.add(friend_model_current_user)
                current_user_profile_instance.save()
                friend_model_for_friend = FriendModel.objects.create(
                    friends = current_user_profile_instance.user,
                    request_status = "ACCEPTED"
                )
                friend_instance.friends.add(friend_model_for_friend)
                friend_instance.save()
                current_user_profile_instance.friend_reqests_recieved.filter(requested_user=friend_instance.user).delete()
                current_user_profile_instance.save()
                friend_instance.friend_reqests_sent.filter(sent_to=current_user_profile_instance.user).delete()
                friend_instance.save()
                return Response({"message": "Friend request accepted"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Sorry! the requested user is not your request list"})

        except ObjectDoesNotExist as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# class FriendRequestModelRejectAPIView(views.APIView):
    
#     def post(self, request, id):
#         try:
            
#         except Exception as e:
#             return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)