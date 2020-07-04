import urllib.request


class ImageDownloader():

    def __init__(self, url_image, filename):
        self._url_image = url_image
        self._filename = filename
        self.successfull_download = False
        self._saveImage()

    def _saveImage(self):
        try:
            urllib.request.urlretrieve(self._url_image, self._filename)
            self.successfull_download = True
            print('Succesfull download: {}'.format(self.successfull_download))
        except Exception as e:
            self.successfull_download = False
            print('Error {}'.format(e))
