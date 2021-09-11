import urllib.request
from src.Detection import PersonnelDetection
class DownloadImage:

    def __init__(self, imageUrl):
        self.imageUrl = imageUrl

    def download(self):
        urllib.request.urlretrieve(self.imageUrl, "image.jpg")