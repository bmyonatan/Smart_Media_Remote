#Queries 
* **?P** - query main zone power state: PWR1=Off, PWR0=On
* **?ZEP** - query hdzone power state: ZEP1=Off, ZEP0=On
* **?V** - qury main zone volume level: VOL*** - {000:-∞, 001:-80dB, ..., 181:12dB
* **?HZV** - query hdzone volume level: XV*** - {00:-∞, 01:-80dB, ..., 81:0dB}
* **?M** - query Main Zone mute state - MUT1=NotMuted, MUT0=Muted
* **?HZM** - query HDZone mute state - ZHMUT1=NotMuted, HZMUT0=Muted
* <b>?RGB**</b> - query name of number of input. For Example: *?RGB25 - RGB251Hot*


#Commands
* **PO** - power on main zone
* **PF** - power off main zone
* **ZEO** - power on hdzone
* **ZEF** - power off hdzone
* **VD** - turn down main volume by 1 step.
* **VU** - turn up main volumn by 1 step.
* **HZD** - turn down hdzone volume by 1 step.
* **HZU** - turn up hdzone volume by 1 step.
* **HZMO** - Mute HDZone.
* **HZMF** - UnMute HDZone.
* **MO** - Mute Main zone.
* **MF** - UnMute Main zone. 
* **\*\*FN** - Set Main Input to **.
* **\*\*ZEA** set HDZone input to **.

    | ** | Input |
    |----|:-----------------:|
    | **02** | **Tuner** |
    | **04** | **Kodi** |
    | **05** | **TV** |
    | **06** | **PS4** |
    | **20** | **Nintendo Switch** |
    | **25** | **Hot** |
    | **33** | **Bluetooth Audio** |
    | **38** | **Internet Radio** |
    | **53** | **Spotify** |
