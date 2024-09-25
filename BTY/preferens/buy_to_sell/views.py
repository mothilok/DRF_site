from django.shortcuts import render
from .models import Poster
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Serializer_post

class home(APIView):
    def get(self, request):
        model_data_set = Poster.objects.all()
        serializer = Serializer_post(model_data_set, many=True)
        return Response(serializer.data)

class post(APIView):
    def get(self, request, post_id):
        model_data_set = Poster.objects.get(pk=post_id)
        serializer = Serializer_post(model_data_set)
        return Response(serializer.data)


class create_poster(APIView):
    def post(self, request):
        pass









# def create_poster(request):
#     request_post = request.POST
#     if request.method == "POST":
#         create_poster = Poster()
#         create_poster.title = request_post['create_title']
#         create_poster.description = request_post['create_description']
#         create_poster.price = request_post['create_price']
#         create_poster.image = request.FILES['create_image']
#         create_poster.phone_number = request_post['create_number']
#         create_poster.miniature = request.FILES['create_image']
#         create_poster.save()
#     return render(request, 'buy_to_sell/create_poster.html')
