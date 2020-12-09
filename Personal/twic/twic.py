import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
twic_site = "https://theweekinchess.com/twic"
webpage_response = requests.get(twic_site, headers = headers)

soup = BeautifulSoup(webpage_response.content, "html.parser")
href_tags = soup.find_all("a", href = True)

zip_tags = [tag for tag in href_tags if "PGN" in tag]

htmls = [re.findall('"([^"]*)"', str(html))[0] for html in zip_tags]
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

for url in htmls:
    with urlopen(url) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall()