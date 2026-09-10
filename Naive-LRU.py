class NaiveLRU:
    def __init__(self, cap):
        self.cap = cap
        self.entries = []   # list of (key, value); most-recent first

    def get(self, key):
        for i, (k, v) in enumerate(self.entries):
            if k == key:
                self.entries.pop(i)
                self.entries.insert(0, (k, v))
                return v
        return None

    def put(self, key, value):
        for i, (k, _) in enumerate(self.entries):
            if k == key:
                self.entries.pop(i); break
        self.entries.insert(0, (key, value))
        if len(self.entries) > self.cap:
            self.entries.pop()