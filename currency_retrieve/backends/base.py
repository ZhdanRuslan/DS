class BackendBase:
    alias = None # class attribute

    def extract(self, start_date, end_date, currencies=None):
        pass

    def transform(self):
        pass

    def load(self):
        pass

