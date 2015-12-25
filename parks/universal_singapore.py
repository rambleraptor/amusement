import database
import requests
import dateutil
from bs4 import BeautifulSoup

def main():
    url = 'http://cma.rwsentosa.com/Service.svc/GetUSSContent?languageID=1&filter=Show,Ride,MeetAndGreet,&Latitude=1.254251&Longitude=103.823797'
    page = get_page(url)
    document = database.Document('Universal Studios Singapore')

    zone_list = page.html.body.responseofuss.result.find_all('usszonelist')[0]
    for zone in zone_list.find_all('usszone'):
        for attraction in zone.content.find_all('usscontent'):
            attraction_doc = get_attraction(attraction)

            if attraction_doc.validate():
                document.append_attraction(attraction_doc)

    document.submit()
   
def get_attraction(attraction):
    document = database.Attraction(attraction.find('name').text)

    if attraction.availability.text == 'True':
        document.setOpen()
    else:
        document.setClosed()

    if attraction.contenttype.text == 'USSShow':
        document.setShow()
        if 'ashx' in attraction.showtime.text:
            return document

        showtimes = get_showtimes(attraction.showtime.text)
        for show in showtimes:
            try:
                time_obj = dateutil.parser.parse(show)
                document.setTime(time_obj)
            except:
                pass

    if attraction.contenttype.text == 'Ride':
        document.setRide()
        if 'Guests' in attraction.queuetime.text:
            document.setTime(0)
        else:
            document.setTime(attraction.queuetime.text)
        
    return document

def get_showtimes(showtimes):
    showtimes = showtimes.replace('and', '')
    showtimes = showtimes.replace(',', '')
    showtimes = showtimes.split(' ')
    array_times = []
    for x in showtimes:
        time_obj = None
        if x != '':
            if 'pm' in x:
                time_obj = ' pm'.join(x.split('pm'))
            if 'am' in x:
                time_obj = ' am'.join(x.split('am'))

        if time_obj:
            array_times.append(time_obj)
       
    return array_times

    

            

def get_page(url):
    r = requests.get(url)
    return BeautifulSoup(r.text)

if __name__ == "__main__":
    main()
