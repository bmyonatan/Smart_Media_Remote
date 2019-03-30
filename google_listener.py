from flask import Flask, request
from av_reciever.commands import AvReceiverCommands
from av_reciever.send_avr_command import send_to_avr
from actions_wrapper import play_tv_show_in_living_room

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    data = request.json
    print data
    return 'Choose Option'

@app.route('/input',methods=['POST', 'GET'])
def change_input():
    data = request.json
    zone = data['zone'].lower()
    input = data['input'].lower()
    if zone == 'main':
        power = send_to_avr(AvReceiverCommands.MainZone.Query.Power).strip()
        if power == AvReceiverCommands.MainZone.PowerIsOff:
            send_to_avr(AvReceiverCommands.MainZone.Command.PowerOn)

        if input == 'hot':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Hot)
        elif input == 'kodi':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Kodi)
        elif input == 'tuner':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Tuner)
        elif input == 'tv':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.TV)
        elif input == 'ps4':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.PS4)
        elif input == 'nintendo':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.NintendoSwitch)
        elif input == 'bluetooth':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Bluetooth)
        elif input == 'internet radio' or input == 'net radio':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.NetRadio)
        elif input == 'spotify':
            send_to_avr(AvReceiverCommands.MainZone.Command.ChangeInput.Spotify)

    elif zone == 'hdzone':
        power = send_to_avr(AvReceiverCommands.HDZone.Query.Power).strip()
        if power == AvReceiverCommands.HDZone.PowerIsOff:
            send_to_avr(AvReceiverCommands.HDZone.Command.PowerOn)

        if input == 'hot':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.Hot)
        elif input == 'kodi':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.Kodi)
        elif input == 'tuner':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.Tuner)
        elif input == 'tv':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.TV)
        elif input == 'ps4':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.PS4)
        elif input == 'nintendo':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.NintendoSwitch)
        elif input == 'bluetooth':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.Bluetooth)
        elif input == 'internet radio' or input == 'net radio':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.NetRadio)
        elif input == 'spotify':
            send_to_avr(AvReceiverCommands.HDZone.Command.ChangeInput.Spotify)

    return 'Changing TV State'

@app.route('/play_show',methods=['POST', 'GET'])
def play_show():
    data = request.json
    tvshow = data['show_name']
    play_tv_show_in_living_room(tvshow)
    return "Playing {} on Kodi".format(tvshow)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)