class Synonyms:

    def __init__(self):
        self.synonyms = []

    @staticmethod
    def load(f, ignoreCase):
        """ Factory for creating a synonym object.
            Load a file of synonyms for matching.
            f can be either a filename (string), a file handle, or
            a list of lists (eg: [['rock', 'stone', 'Boulder'], ['pebble', 'rubble']]).
            Set ignoreCase to control whether the loaded results are loaded
            and matched as lowercase.
            """
        if isinstance(f, basestring):
            # Load from a string
            syn = Synonyms()
            syn._load_str(f, ignoreCase)
            return syn
        elif hasattr(f, 'read'):
            # Load from a file pointer
            syn = Synonyms()
            s = f.read()
            syn._load_str(s, ignoreCase)
            return syn
        else:
            # Check if the variable is iterable
            try:
                for x in f:
                    break;
            except TypeError:
                raise AssertionError("type %s is not iterable" % type(item))
            syn = Synonyms()
            for l in f:
                syn._load_list(l, ignoreCase)
            return syn

    def _load_str(self, s, ignoreCase):
        s = s.split("\n")
        for line in s:
            # Skip comment lines
            if line.strip().startswith('#'):
                continue
            l = line.split(',')
            self._load_list(l, ignoreCase)

    def _load_list(self, l, ignoreCase):
        if ignoreCase:
            r = [word.lower().strip() for word in l]
        else:
            r = [word.strip() for word in l]
        self.synonyms.append(r)
        self.ignoreCase = ignoreCase

    def __str__(self):
        return str(self.synonyms)

    def __contains__(self, key):
        """ Check if a synonym is found in the loaded dictionary. """
        return self.match(key) != None

    def match(self, key, all=False, ignoreCase=None):
        """ Check if key has a synonym.
            By default, return the first word of the synonym list.
            Set all=True to get the list of synonyms.
            Note that this function returns the first match for the
            synonym.  If you define the synonym in multiple places,
            only the first match is returned.
            If ignoreCase is not specified, the case of the key being
            tested is the same as specified on load.
            """
        if ignoreCase == None:
            ignoreCase = self.ignoreCase
        if ignoreCase == True:
            key = key.lower()
        for l in self.synonyms:
            if key in l:
                if all == True:
                    return l
                else:
                    return l[0]
        return None
