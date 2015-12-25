from attraction import Attraction
class Show(Attraction):
    
    _added_keys = ['showtimes']

    def __init__(self):
        self._addKeys(self._added_keys)
        super(Show, self).__init__()

    def addTime(self, time):
        if self['showtimes'] is None:
            self['showtimes'] = [time]

        else:
            self['showtimes'].append(time)

    def getTimes(self):
        return self['showtimes']
