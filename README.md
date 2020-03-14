# dotfiles

# Introduciton
After a fresh intall of Debian + Xfce, here are instructions of how to configure the system.

# Things that you may want to do
When installing Debian you can give your user sudo by not typing in a root password. However, if you typed in a root password you need to add your user to the sudo group.

## To take away the option screen on boot:

```
sudo vim /etc/default/grub
```

Set GRUB_TIMEOUT=0.

```
sudo update-grub
```

## Fan control with Nouveau drivers
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

## Proprietary Nvidia drivers
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

