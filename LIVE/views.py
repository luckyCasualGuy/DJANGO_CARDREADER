from django.http.response import JsonResponse
from .util import Extractor
from django.shortcuts import render
from django.http import StreamingHttpResponse


from django.views.generic import View

from .camera import MobileCamera, VideoCamera 

class LiveFeed(View):
    def get(self, request):
        camera = VideoCamera()
        return StreamingHttpResponse(camera.gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')


class LiveDetect(View):
    def get(self, request):
        return render(request, 'livedetect.html')

    def post(self, request):
        extractor = Extractor()
        extractor.detect()
        print(extractor.extractedDict['text'])
        return JsonResponse(extractor.extractedDict, status=200)

class MobileLiveFeed(View):
    def get(self, request):
        camera = MobileCamera()
        return StreamingHttpResponse(camera.gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')

    def post(self, request):
        value = request.POST.get("urlValue")
        
        camera = MobileCamera()
        setUrl = camera.setUrl(value)

        return JsonResponse({
            "setUrl": setUrl
        }, status=200)
        