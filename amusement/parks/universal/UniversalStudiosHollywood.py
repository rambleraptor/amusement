from amusement.parks.universal.UniversalPark import UniversalPark

class UniversalStudiosHollywood(UniversalPark):
    def __init__(self):
        super(UniversalStudiosHollywood, self).__init__()

    def getId(self):
        return 13825

    def getName(self):
        return 'Universal Studios Hollywood'

    def getUrl(self):
        return 'https://services.universalorlando.com/api/pointsofinterest/rides?pageSize=all&city=hollywood'

