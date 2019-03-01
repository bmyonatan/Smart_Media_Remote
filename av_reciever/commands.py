class _MainZoneQuery(object):
    def __init__(self):
        self.Power = '?P'
        self.Volume = '?V'


class _HdZoneQuery(object):
    def __init__(self):
        self.Power = '?ZEP'
        self.Volume = '?HZV'


class _MainZoneCommand(object):
    def __init__(self):
        self.PowerOn = 'PO'
        self.PowerOff = 'PF'


class _HdZoneCommand(object):
    def __init__(self):
        self.PowerOn = 'ZEO'
        self.PowerOff = 'ZEF'


class _MainZone(object):
        Command = _MainZoneCommand()
        Query = _MainZoneQuery()


class _HdZone(object):
    Command = _HdZoneCommand()
    Query = _HdZoneQuery()


class AvReceiverCommands(object):
    MainZone = _MainZone()
    HdZone = _HdZone()

