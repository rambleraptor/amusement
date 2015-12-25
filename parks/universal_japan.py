# encoding: utf-8
import requests
import datetime
import database
import os
import json
import dateutil
import sys
from bs4 import BeautifulSoup


def main():
    page = get_page() 
    names = load_names()

    document = database.Document('Universal Studios Japan')
    if 'list' not in page:
        print 'USJ - nothing appeared'
        build_empty(names, document)
        document.submit()
        sys.exit()

    for list_thing in page['list']:
        time = list_thing['wait']
        if u'分' in time:
            time = int(unicode(time).replace(u'分', ''))
        elif u'休止中' in time or u'本日終了' in time:
            time = 'CLOSED'

        for thing in list_thing['rows']:
            attr = build_attraction(thing, time, names)
            if attr.validate():
                document.append_attraction(attr)

    # Showtimes
    page = get_showpage()

    shows_so_far = []
    for list_thing in page['list']:
        for show in list_thing['rows']:
            if show['text'] not in shows_so_far:

                shows_so_far.append(show['text'])
                try:
                    show_doc = build_show(show, names)

                    if show_doc.validate():
                        document.append_attraction(show_doc)
                except:
                    pass

    document.submit()

def get_page():
    r = requests.get('http://ar02.biglobe.ne.jp/app/waittime/waittime.json')
    return r.json()

def get_showpage():
    r = requests.get('http://ar02.biglobe.ne.jp/app/waittime/schedule.json')
    return r.json()

def build_attraction(attr, time, names):
    try:
        name = names[attr['text']]
    except:
        print unicode(attr['text'])
        name = attr['text']
    attraction = database.Attraction(name)

    attraction.setRide()
    if time == 'CLOSED':
        attraction.setClosed()
    else:
        attraction.setOpen()
        attraction.setTime(time)
    
    return attraction

def build_show(show, names):
    try:
        name = names[show['text']]
    except:
        print unicode(show['text'])
        name = show['text']
    attraction = database.Attraction(name)

    attraction.setShow()
    showtimes = show['schedule'].replace('/', ' ').split()
    for show in showtimes:
        time_obj = dateutil.parser.parse(show)
        attraction.setTime(time_obj)

    return attraction

def load_names():
    filepath = os.path.dirname(os.path.realpath(__file__))
    jsonpath = os.path.join(filepath, 'config/usj_strings.json')
    f = open(jsonpath, 'r')
    return json.load(f)

def build_empty(names, document):
    for key in names:
        attr_name = names[key]
        if attr_name is not 'Closed':
            attraction = database.Attraction(attr_name)
            attraction.setClosed()
            attraction.setRide()
            document.append_attraction(attraction)


if __name__ == '__main__':
    main()

