import sys

class StartingZone(object):
    """description of class"""

    def __init__(self, zone_type):
        self.zone_type = zone_type
        self.description = str(zone_type)

    def print_details(self):
        print(self.description)
        sys.stdout.flush()