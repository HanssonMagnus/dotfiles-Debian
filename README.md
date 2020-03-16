# dotfiles-Debian
This is a repository for dotfiles and settings I use in Debian. The configuration should work with other Debian based distros.

A visual of my current setup with i3, Compton, and i3blocks:
![Fig 1](/debian_blue_1.png)
![Fig 2](/debian_blue_2.png)
![Fig 3](/Config_2020-03-15_23-03-46.png)

# Introduciton
After a fresh intall of Debian + Xfce, here are instructions of how to configure the system. Note that apt installs dependencies by default, so e.g., `sudo apt-get install i3` installs dependencies and dmenu etc.

# Install Debian
Either you can install [the regular](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/) (free software) version of Debian or you can install the [non free version](https://cdimage.debian.org/images/unofficial/non-free/images-including-firmware/). This depends on your hardware and requirements. I usually go with the free version and then add specific non free packages if I need to. Download the iso and burn it to an usb,

```
sudo umount /dev/sdX
sudo dd if=/path/to/debian.iso of=/dev/sdX bs=4M && sync
```
(Note that you should locate e.g. sdb and not sdb1.)

# Run script
* Clone the repositor to ~/Git/github or your dir of choice
* cd into directory
* chmod +x install
* run script ./install

# Dotfiles and git
Sometimes dotfiles and dotdirectories are owned by root and ownership needs to be changed with `sudo chown -R magnus:magnus .` in order for git to be able to add, commit, and push. Likewise premissions might need to be changed with `sudo chmod -R 756 .`, and groups with `sudo chgrp -R group .`.

Furthermore, if there are cloned git repos in e.g. your .vim/plugged that can cause error when you try to `git add .`.

# Configuring music players

### Configure input and output devices
Check what output devices you have,
```
pacmd list-sinks
```
Set the default output sink,
```
pacmd set-default-sink "SINKNAME"
```
Check what input devices you have,
```
pact1 list | grep alsa_input
```
Set the default input device,
```
pacmd set-default-source "DEVICE NAME"
```

### Configure Mpd and Ncmpcpp
From my experience Mpd is by default running a global session and hence the config file in /etc/mpd.conf will be used and not one in your home directory. You could most certainly change this, or write a script that kills the session and opens a one pointing at the config file in the home directory. This is what I used before,
```
sudo service mpd stop
mpd /home/magnus/.config/mpd/mpd.conf
```
However, recently I've just started to modify the /etc/mpd.conf file.

### Non-daemon CLI music players
If you think it's overkill to run a daemon for music (mpd), you can instead run a CLI music player. Some examples are CMus (a good option), Moc, and mp3blaster.

# You may want to do after installing Debian
When installing Debian you can give your user sudo by not typing in a root password. However, if you typed in a root password you need to add your user to the sudo group.

### Take away the option screen on boot:

```
sudo vim /etc/default/grub
```

Set GRUB_TIMEOUT=0.

```
sudo update-grub
```

### Fan control with Nouveau drivers
When running the [Nouveau](https://wiki.archlinux.org/index.php/Nouveau) free graphics drivers, the fans are spinning loudly at all temperatures. To change this,

```
sudo find /sys -name pwm1_enable
```

yielding e.g.,

```
/sys/devices/platform/eeepc-wmi/hwmon/hwmon2/pwm1_enable
/sys/devices/pci0000:00/0000:00:03.1/0000:09:00.0/hwmon/hwmon0/pwm1_enable
```

Now you can change pwm1_enable to 0 (off), 1 (manual), or 2 (auto).

### Proprietary Nvidia drivers
It might be necessary to use the proprietary drivers for optimal performance, see [Debian wiki](https://wiki.debian.org/NvidiaGraphicsDrivers). This will also solve the loud fan problem.
Identify your card with,

```
lspci -nn | egrep -i "3d|display|vga"
```

Add non-free repositories,

```
sudo vim /etc/apt/sources.list
```

and add "contrib non-free" to all lines. Run,

```
sudo apt-get update
sudo apt-get install nvidia-detect
nvidia-detect
sudo apt-get install nvidia-driver
sudo poweroff
```

### Mouse sensitivity in Debian
Xset doesn't natively work to set mouse sensitivity, xinput is what have to be used (which is not installed by default in Debian 10). To list your devices, list properties for device 2, and change them to half the speed for device "Primax Kensington Eagle Trackball",
```
xinput list
xinput -list-props 2
xinput -set-prop "Primax Kensington Eagle Trackball" "Coordinate Transformation Matrix" 0.5 0 0 0 0.5 0 0 0 1
```
Note that these changed reset at reboot, thus they should be added to either an Xsession config or executed at startup with e.g. i3 config.

### Copying and pasting
There are different mechanisms for copying and pasting in the X window system. There is the "primary selection" and then there's several key bindings (e.g. ctrl+c/v) that programs use. E.g. urxvt uses primary selection with copy at "ctrl+insert" and paste at "shift+insert". This means that if you copy something from e.g. Firefox with "ctrl+c" you cannot directly paste it in urxvt.

One way to join the primary selection and the clipboard is to use a program such as [Autocutsel](http://www.nongnu.org/autocutsel/), and at startup run,
```
autocutsel -s PRIMARY -fork
```
