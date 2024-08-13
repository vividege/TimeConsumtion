import os.path
from urllib.request import Request, urlopen


class ProductService:

    def download_img(self, url: str):
        site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(site_url) as web_file:
            img_data = web_file.read()

        if not img_data:
            raise Exception('Error: cannot load the image from {0}'.format(url))

        file_name = os.path.basename(url)
        with open(file_name, 'wb') as file:
            file.write(img_data)

        return "Download image successfully, {0}".format(file_name)
