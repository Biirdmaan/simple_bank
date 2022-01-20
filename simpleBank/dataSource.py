

class DataSource:
    data = {}

    # Max läste filhanteringen med denna funktionen.
    def _load(filename):
        return [v.strip() for v in open(filename).readlines()]

