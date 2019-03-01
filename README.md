# Smart Remote Smart Home Project
smart remote that will manage multiple media devices ( TV, AV Reciever, Kodi, etc)
____
I have a lot of appliances that each have a separte physical remote/smartphone app. I wanted to make a single app/hub that will control everything, and be compatabile with google assistant.
My first objective was to control my A/V Reciever. The model that I have is a Pionerr vsx-1130k.
It has its own smartphone app that can control all of its features. The reciever also supports UPnP to control basic settings.
The features I wanted to include in my solution are:
* Powering on/off main and second zones.
* Controling input of main and second zones.
* Adjusting Volume in each zone.
* Streaming from spotify to each zone (Using google assistant)
* Controling the listening mode in the main zone (Auto Surround vs Stereo vs Extended Stereo)
* Controling Tuner Frequency/Preset to play in main zone.
At first, I tried controling the reciever with upnp. I researched about UPnP and SOAP, and realized that the amount of control I will have with going with UPnP will be very minimal.
I knew that there is some way of controling the reciever through my local network, because it does have an app that enables these features.
My first thougt was to try to reverse engineer the app, but because I never developed an app for android, the process quickly became very confusing.
Next, I thougt about sniffing traffic from my phone while using the app and reverse engineer the protocols used for controlling the reciever through the app.
Luckily, the data wasn't encrypted (honestly didn't expect it to be), and there were no difficult or complicated protocols involved. In the pcaps, I could clearly see packets sent from my phone with certain data as text, and recieving some output from the reciever as text.
Now all that was left was using the app for all the actions I would like to be able to perform, and figure out what command is being sent, and what is the format of the response.
I had a few problems while trying to accomplish this (Mainly in sniffing traffic from my phone). I found a way to capture traffic from my smartphone without root, but it required using an app that I would connect to as a VPN. That resulted in all the IP addresses in the pcap to be messed up, and a lot of dropped packets. I also tried using a virtual machine running android and using the app there, but the user experience was really buggy. I think my best and next option will be to use a raspberry pi as a wireless AP and sniff traffic off of it.
My findings of commands are documented in av_reciever/commands_documentation.txt
