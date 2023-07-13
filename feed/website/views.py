from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import FeedModelSerializer
from advertisement.models import AdvertisementsModel
from ..models import FeedModel
from userprofile.models import UserProfileModel


class FeedModelDisplayGenericAPIView(generics.GenericAPIView):
    queryset = FeedModel.objects.all()
    serializer_class = FeedModelSerializer

    def get(self, request):
        try:
            user_instance = UserProfileModel.objects.get(user=request.user)
            friends_list_curr_user = user_instance.friends
            for friend in friends_list_curr_user:
                friend_user_instance = UserProfileModel.objects.get(user=friend.target_user.email)
                friend_posts_list = friend_user_instance.posts
            advertisement_instance = AdvertisementsModel.objects.all()
            # chained_query = friend_posts_list, advertisement_instance
            serializer = self.serializer_class(data=friend_posts_list)
            return Response({"message": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_200_OK)
