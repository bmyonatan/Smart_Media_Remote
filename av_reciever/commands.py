class _MainZoneQuery(object):
    def __init__(self):
        self.Power = '?P'
        self.Volume = '?V'
        self.Mute = '?M'

class _HdZoneQuery(object):
    def __init__(self):
        self.Power = '?ZEP'
        self.Volume = '?HZV'
        self.Mute = '?HZM'


class _Inputs(object):
    def __init__(self, zone):
        if zone == 'main':
            self.Tuner = '02FN'
            self.Kodi = '04FN'
            self.TV = '05FN'
            self.PS4 = '06FN'
            self.NintendoSwitch = '20FN'
            self.Hot = '25FN'
            self.Bluetooth = '33FN'
            self.NetRadio = '38FN'
            self.Spotify = '53FN'

        elif zone == 'hdzone':
            self.Tuner = '02ZEA'
            self.Kodi = '04ZEA'
            self.TV = '05ZEA'
            self.PS4 = '06ZEA'
            self.NintendoSwitch = '20ZEA'
            self.Hot = '25ZEA'
            self.Bluetooth = '33ZEA'
            self.NetRadio = '38ZEA'
            self.Spotify = '53ZEA'


class _MainZoneCommand(object):
    ChangeInput = _Inputs('main')

    def __init__(self):
        self.PowerOn = 'PO'
        self.PowerOff = 'PF'
        self.VolumeUp = 'VU'
        self.VolumeDown = 'VD'
        self.Mute = 'MO'
        self.Unmute = 'MF'


class _HdZoneCommand(object):
    ChangeInput = _Inputs('hdzone')

    def __init__(self):
        self.PowerOn = 'ZEO'
        self.PowerOff = 'ZEF'
        self.VolumeUp = 'HZU'
        self.VolumeDown = 'HZD'
        self.Mute = 'HZMO'
        self.Unmute = 'HZMF'


class _MainZone(object):
        Command = _MainZoneCommand()
        Query = _MainZoneQuery()
        PowerIsOn = 'PWR0'
        PowerIsOff = 'PWR1'


class _HdZone(object):
    Command = _HdZoneCommand()
    Query = _HdZoneQuery()
    PowerIsOn = 'ZEP0'
    PowerIsOff = 'ZEP1'


class AvReceiverCommands(object):
    MainZone = _MainZone()
    HDZone = _HdZone()

