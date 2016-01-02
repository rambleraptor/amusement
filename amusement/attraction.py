class Attraction(dict):

    _keys = ['name']

    def __init__(self):
        super(Attraction, self).__init__()
        for key in self._keys:
            self[key] = None

    def __setitem__(self, key, value):
        if key not in self._keys:
            raise Exception("'" + key + "'" + " is not a valid key")
        dict.__setitem__(self, key, value)

    def _addKeys(self, array):
        for key in array:
            self._keys.append(key)
            self[key] = None

    def attributes(self):
        return self._keys

    def setName(self, name):
        self['name'] = name

    def getName(self):
        return self['name']
