import requests
from bs4 import BeautifulSoup


class Culture:
    def __init__(self):
        self.svcid
        self.minclassnm
        self.svcstatnm
        self.svcnm
        self.payatnm
        self.placenm
        self.usetgtinfo
        self.imgurl
        self.svcurl
        self.x
        self.y
        self.rcptbgndt
        self.rcptenddt
        self.areanm

class CulService:
    def __init__(self):
        base_url = 'http://openAPI.seoul.go.kr:8088/'
        api_key='4c4c556a567375693633667243655a'

    def getInfo(self):
        url=self.base_url+self.api_key+'/xml/ListPublicReservationCulture/1/200/'
        xml = requests.get(url).text
        root = BeautifulSoup(xml, 'lxml-xml').text
        rows = root.select('row')


