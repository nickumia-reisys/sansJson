
import json
import logging

log = logging.getLogger(__name__)

NONHOMOGENOUS_ORDER = [type(None), bool, int, float, str, list, object]


class Sorter:

    def __init__(self):
        self.data = None

    def sortable(self, sans):
        if isinstance(sans, dict):
            self.data = sans
            return True
        if isinstance(sans, str):
            try:
                self.data = json.loads(sans)
                return True
            except json.decoder.JSONDecodeError:
                log.error(
                    'Input is str, but could not be parsed into JSON dict.')
                return False
        if isinstance(sans, list):
            self.data = sans
            return True
        return False


def nonhomogenous(sans):
    try:
        return sorted(sans)
    except TypeError:
        parts = {}
        for s in sans:
            t = type(s)
            if t in parts:
                parts[t].append(s)
            else:
                parts[t] = [s]

        final = []
        for t in NONHOMOGENOUS_ORDER:
            print(t)
            if t in parts.keys():
                if isinstance(None, t):
                    final += parts[t]
                else:
                    final += sorted(parts[t])

        return final
