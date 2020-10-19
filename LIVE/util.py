from keras.models import load_model

from cv2 import COLOR_BGR2GRAY, cvtColor, resize, INTER_CUBIC

from numpy import expand_dims

from PIL.Image import fromarray

from numpy import ndarray

from pytesseract import image_to_string, pytesseract
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class Detector():
    valid = 0.5
    counter = 0
    sendValidAfter = 5 #number of frames

    def __init__(self, model='LIVE\Model\classifier2.h5'):
        self.model = load_model(model)
        
    def makePredictions(self, image):
        gray = cvtColor(image, COLOR_BGR2GRAY)
        value = self.model.predict(expand_dims(expand_dims(gray, 2),0))
        return value

    def makeValidPredictions(self, image):
        value = self.makePredictions(image)
        # print(value)
        if value > self.valid: self.counter += 1
        else: self.resetCounter()

        if self.counter == self.sendValidAfter: return (True, value)
        return (False, value)

    def resetCounter(self):
        self.counter = 0

class Extractor():
    extractedDict = {
        "text": 'NOTHING EXTRACTED !!',
        "Value": '0'
    }
    image = None
    detector = Detector()
    urlError = False

    @classmethod
    def extractText(cls, image):
        cam_pic_size = (1280, 720)
        frame = resize(image, dsize=cam_pic_size, interpolation=INTER_CUBIC)
        text = image_to_string(fromarray(frame))
        cls.extractedDict["text"] = text

    @classmethod
    def detect(cls):
        if type(cls.image) == ndarray:
            valid, value = cls.detector.makeValidPredictions(cls.image)
            cls.extractedDict["Value"] = str(value[0][0])
            # print(valid)
            if valid:
                cls.extractText(cls.image)

    @classmethod
    def setImage(cls, image):
        cls.image = image

    @classmethod
    def setUrlError(cls, value):
        cls.extractedDict["urlError"] = value