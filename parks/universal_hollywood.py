import requests
import datetime
import database
import dateutil
from bs4 import BeautifulSoup

def main():
    page = get_page() 

    document = database.Document('Universal Studios Hollywood')
    for table_row in page.find_all('tr'):
        if table_row.find_all('td', 'ride'):
            try:
                name = table_row.contents[1].contents[0].text
                time = table_row.contents[3].text
                build_attraction(name, time, document)
            except:
                pass

    document.submit()

def get_page():
    r = requests.get('http://m.universalstudioshollywood.com/waittimes')
    return BeautifulSoup(r.text)

def build_attraction(name, time, document):
    attraction = database.Attraction(name)

    if 'CLOSED' in time:
        attraction.setClosed()
    elif 'OPENS' in time or 'OPENING SOON' in time:
        attraction.setClosed()
    else:
        attraction.setOpen()

    if 'LAST SHOW' in time:
        attraction.setShow()
        attr_time = time.split()[-2:]
        attr_time = ''.join(attr_time)
        attr_time = datetime.date.today().strftime("%B %d, %Y") + ' ' + attr_time
        attr_time = dateutil.parser.parse(attr_time)
        attraction.setTime(attr_time)
    elif 'AM' in time or 'PM' in time:
        try:
            time2 = time[0:2]
            attraction.setShow()
            time_obj = dateutil.parser.parse(time2)
            attraction.setTime(time_obj)
        except:
            attraction.setShow()
            time_obj = dateutil.parser.parse(time)
            attraction.setTime(time_obj)
    else:
        attraction.setRide()

    if attraction.isRide() and attraction.isOpen():
        waittime = int(time.split()[0])
        attraction.setTime(waittime)

    if attraction.validate():
        document.append_attraction(attraction)    


if __name__ == '__main__':
    main()

