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

Furthermore, if there are cloned git repos in e.g. your .vim/plugged that can cause error when you try to `git add .`. So you should clone them with git submodules.

# Installing st
Download St from https://st.suckless.org/ and extract it into $HOME/st. In the README it says how to install it. The installation requires Xlib header files, in Debian based distributions you need,

```
sudo apt-get install libxft-dev
```

If there is something else missing, you can potentially find that with, e.g.,

```
sudo apt-get install apt-file
sudo apt-file update
apt-file search X11/Xlib.h
sudo apt install libx11-dev
```

Now for the installation,

```
tar xf st-0.8.2.tar.gz
cd st-0.8.2
patch -Np1 -i ~/st/patches/st-alpha-0.8.2.diff
patch -Np1 -i ~/st/patches/st-clipboard-0.8.2.diff
patch -Np1 -i ~/st/patches/st-scrollback-0.8.2.diff
patch -Np1 -i ~/st/patches/st-solarized-both-20190128-3be4cf1.diff
sudo make clean install
st
```

For unicode characters in st you want to install a "powerline patched font", this is , e.g., necessary if you want your font to be compatilbe with Vim Airline which uses PowerlineSymbols unicode. [Nerds fonts](https://github.com/ryanoasis/nerd-fonts) have several alternatives for fonts. I use the font called [Hack](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/Hack), and it can be installed with,

```
sudo apt-get install fonts-hack-ttf
```

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

### Non-free Firmware
I have actually had Debian 10 crash a couple of times, with the error messages regarding the CPU. I do not know exactly what the error is, I have only heard that it has previously been problems with AMD Ryzen CPUs and some kernels. If this problem occurs, one idea is to install the non-free firmware including AMD proprietary CPU drivers. For more information see [this thread](https://community.amd.com/thread/225795).

```
sudo apt-get install firmware-linux-nonfree
```
### Update on AMD Ryzen crash
Installing drivers seems not to be enough. It seems to be a power bug, after I changed "PowerSupplyIdle" from Auto to Typical in my BIOS, I haven't had any more issues.

The reason why I did not have any problems on Ubuntu, I think, is beacuse I was running version 18, which ran a kernel where this bug wasn't present.

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
### Change /etc/sudoers
There are some programs that you perhaps want all users to be able to execute without sudo. I have changed my /etc/sudoers file so that I can run poweroff and reboot without sudo. Change the default editor in Debian to Vim (set to Nano by default) and then edit the /etc/sudoers file. The file must be edited with the 'visudo' command as root.

```
sudo update-alternatives --config editor
sudo which shutdown
sudo which poweroff
sudo which reboot
sudo visudo
```
Then add the following line to the file (with the correct paths),
```
magnus ALL=(ALL) NOPASSWD: /usr/sbin/shutdown, /usr/sbin/poweroff, /usr/sbin/reboot
```
Now you can, e.g., run "sudo shutdown" without the need to enter your password. Set an alias in your.bashrc file, e.g.,
```
alias shutdown=sudo shutdown now
alias reboot=sudo reboot
```

### Change login screen
In Debian based distribution to find which [display manager](https://wiki.debian.org/DisplayManager) you can look in /etc/X11/default-display-manager. It happens that I have [LightDM](https://wiki.debian.org/LightDM),
```
sudo which lightdm
/usr/sbin/lightdm
```
To change the background of the login screen you can change to an image file at /etc/lightdm/lightdm-gtk-greeter.conf. At the Debian wiki it says you can choose either .svg or .png, however .jpg works as well. Add the following to the conf,
```
[greeter]
background=/path/to/file.jpg
```


