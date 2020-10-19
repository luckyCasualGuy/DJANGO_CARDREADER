from .util import Extractor
from cv2 import VideoCapture, imencode, imdecode, INTER_AREA, resize

from urllib.request import urlopen
from urllib.error import URLError
from numpy import array, uint8

class VideoCamera(object):
    extractor = Extractor()
    urlError = False

    def __init__(self):
        self.video = VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        self.extractor.setImage(image)
        ret, jpeg = imencode('.jpg', image)
        # self.extractor.setUrlError(False)
        return jpeg

    @staticmethod
    def gen(camera):
        while True:
            frame = camera.get_frame()
            frame = frame.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class MobileCamera():
    extractor = Extractor()
    url='http://192.168.0.101:8080/shot.jpg' #keeping this default for now
    urlError = False
    
    def get_frame(self):
        try:
            imgResp=urlopen(self.url)
            imgNp=array(bytearray(imgResp.read()),dtype=uint8)
            image=imdecode(imgNp,-1)
            image = resize(image, (640, 480), INTER_AREA)
            self.extractor.setImage(image)    
            ret, jpeg = imencode('.jpg', image)
            self.extractor.setUrlError(False)
            return jpeg
        except URLError:
            self.extractor.setUrlError(True)
            print("Error Received!")
            

    @staticmethod
    def gen(camera):
        while True:
            try:
                frame = camera.get_frame()
                frame = frame.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            except AttributeError:
                pass
            except TypeError:
                pass
                
    @classmethod
    def setUrl(cls, url):
        setThis = f"http://{url}/shot.jpg"
        if setThis != cls.url:
            cls.url = setThis
        return setThis