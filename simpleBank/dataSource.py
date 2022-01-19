

class DataSource:
    data = {}

    def _load(filename):
        return [v.strip() for v in open(filename).readlines()]

