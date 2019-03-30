from av_reciever.commands import AvReceiverCommands
from av_reciever.send_avr_command import send_to_avr
from kodi.actions import KodiActions

def play_tv_show_in_living_room(tvshow):
    main_zone_power = send_to_avr(AvReceiverCommands.MainZone.Query.Power).strip()

    if main_zone_power == AvReceiverCommands.MainZone.PowerIsOff:
        send_to_avr(AvReceiverCommands.MainZone.Command.PowerOn)

    send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Kodi)

    kodi_remote = KodiActions('living room')
    kodi_remote.play_latest_episode_of_show(tvshow)