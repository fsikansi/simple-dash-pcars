# simple-dash-pcars
A simple dash to show some info from Project Cars game in a LCD 2x16 using Raspberry Pi 2

##Project Status
For now the only thing that this project do is read the udp package sent by the game and store the information on memory, there is some issues with the string enconde but I will not look to this for know since this info will not be used on Raspberry Dashboard.

##Project Dependencies

* Python 3.5
Using it for Enum, maybe it will work in older versions if you install the package enum34 (not tested)
>pip install enum34

* pySerial
>pip install pyserial
