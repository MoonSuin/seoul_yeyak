import requests
from bs4 import BeautifulSoup


class Culture:
    def __init__(self,minClassNm=None,svcStateNm=None,svcNm=None,payAtNm=None,placeNm=None,useTgtInfo=None,imgUrl=None, svcUrl=None, x=None, y=None):
        #self.svcid
        self.minClassNm = minClassNm
        self.svcStateNm = svcStateNm
        self.svcNm = svcNm
        self.payAtNm = payAtNm
        self.placeNm = placeNm
        self.useTgtInfo = useTgtInfo
        self.imgUrl = imgUrl
        self.svcUrl = svcUrl
        self.x = x
        self.y = y
        '''
        self.rcptbgndt
        self.rcptenddt
        self.areanm'''

class CulService:
    def __init__(self):
        self.base_url = 'http://openAPI.seoul.go.kr:8088/'
        self.api_key = 'api_key입력'

    def getList(self):
        url = self.base_url+self.api_key+'/xml/ListPublicReservationCulture/1/231/'
        xml = requests.get(url).text
        root = BeautifulSoup(xml, 'lxml-xml')
        code = root.find('CODE').text
        culList=[]
        if code == 'INFO-000':
            rows = root.select('row')
            for r in rows:
                minClassNm = r.find('MINCLASSNM').text
                svcStateNm = r.find('SVCSTATNM').text
                svcNm = r.find('SVCNM').text

                svcNm = svcNm.replace('&#39;', '')
                svcNm = svcNm.replace('&quot;', '')
                svcNm = svcNm.replace('&uarr;', '')
                svcNm = svcNm.replace('&lt;', '')
                svcNm = svcNm.replace('&gt;', '')
                svcNm = svcNm.replace('& amp;', '')

                payAtNm = r.find('PAYATNM').text
                placeNm = r.find('PLACENM').text
                useTgtInfo = r.find('USETGTINFO').text
                imgUrl = r.find('IMGURL').text
                svcUrl = r.find('SVCURL').text
                x = r.find('X').text
                y = r.find('Y').text
                culList.append(Culture(minClassNm=minClassNm, svcStateNm=svcStateNm, svcNm=svcNm, payAtNm=payAtNm,
                                           placeNm=placeNm, useTgtInfo=useTgtInfo, imgUrl=imgUrl, svcUrl=svcUrl, x=x, y=y))
            return culList

        else:
            print(root.find('RESULT').text)

    def getFree(self):
        culList = self.getList()
        freeList = []
        for c in culList:
            if c.payAtNm == '무료':
                freeList.append(c)
        return freeList

    def getOngoing(self):
        culList = self.getList()
        ongoingList = []
        for c in culList:
            if c.svcStateNm == '접수중':
                ongoingList.append(c)
        return ongoingList

    def getByKeyword(self, culList, keyword):
        result = []
        if keyword == None:
            return culList
        else:
            for c in culList:
                if keyword in c.svcNm:
                    result.append(c)
            return result

    def getByCondition(self, condition, keyword):
        if condition == 'free':
            culList = self.getFree()
            result = self.getByKeyword(culList, keyword)
        elif condition == 'ongoing':
            culList = self.getOngoing()
            result = self.getByKeyword(culList, keyword)
        else:
            culList = self.getList()
            result = self.getByKeyword(culList, keyword)
        return result





