#Queries 
* **?P** - query main zone power state: PWR1=Off, PWR0=On
* **?ZEP** - query hdzone power state: ZEP1=Off, ZEP0=On
* **?V** - qury main zone volume level: VOL??? - {000:-∞, 001:-80dB, ..., 181:12dB
* **?HZV** - query hdzone volume level: XV?? - {00:-∞, 01:-80dB, ..., 81:0dB}
* **?M** - query Mute state - MUT1=NotMuted, MUT0=Muted

#Commands
* **PO** - power on main zone
* **PF** - power off main zone
* **ZEO** - power on hdzone
* **ZEF** - power off hdzone
* **VD** - turn down main volume by 1 step. Output is {VD, FL004D2E564F4C20202D33342E356442, VOL???}
* **VU** - turn up main volumn by 1 step. Output is {VU FL004D2E564F4C20202D33342E356442, VOL???}
* **HZD** - turn down hdzone volume by 1 step. Output is {HZD, FL0048445A564F4C202D35352E306442, XV??}
* **HZU** - turn up hdzone volume by 1 step. Output is {HZU, FL0048445A564F4C202D35352E306442, XV??}
* **HZMO** - Mute HDZone. Output is {HZMO, FL0248445A204D555445204F4E202020, HZMUT0}
* **HZMF** - UnMute HDZone. Output is {HZMF, FL0248445A204D555445204F4E202020, HZMUT1}
* **MO** - Mute Main zone. Output is {MO, FL022020204D555445204F4E20202020, MUT0}
* **MF** - UnMute Main zone. Output is {MF, FL022020204D555445204F4646202020, MUT1}
* **??FN** - Set Main Input to ??. Output is {FL0220202020204B6F64692020202020}
| ?? 	| Input           	|
|----	|-----------------	|
| 02 	| Tuner           	|
| 04 	| Kodi            	|
| 05 	| TV              	|
| 06 	| PS4             	|
| 20 	| Nintendo Switch 	|
| 25 	| Hot             	|
| 38 	| Internet Radio  	|
| 53 	| Spotify         	|