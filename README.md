# RethinkingObjects
Code Examples From the Book "Rethinking Objects"

This repository uses the Pants build system, which runs under Linux. If you are
either running on MacOS or Linux, you're ready to use this repository if you
know how to use the Linux terminal on those systems (although you might still
need to install additional Python interpreters, described later in this README).

We are using Pants version 2 here; there are differences in the commands from Pants V1.

## Windows Setup

On Windows, Pants only runs under Windows Subsystem for Linux (WSL). (_They are working on supporting Windows directly)._ If you have not installed WSL on your
machine, the following instructions will guide you.

### Installing WSL on Windows 10 from the MS Store

- (Assuming there is no prior WSL on your system).
- Inside the MS Store, find Ubuntu 22.04.1 LTS, click the "get" button.
- Upon clicking the "Open" button after installing from the MS Store, you will
  see:
- `Error: 0x800701bc WSL 2 requires an update to its kernel component. For
  information please visit
  [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)`
- Follow the instructions at the link to install the update.
- Opening Ubuntu again produces a "virtual disk system limitation" error.
- To fix this, open the Windows File Explorer and navigate to:
- **`C:\Users\YOUR_USER\AppData\Local\Packages\CanonicalGroupLimited...`**
- Right click on "LocalState", then "Properties," then "Advanced."
- Ensure "Compress contents to save disk space" and "Encrypt contents to secure data" are both **de**selected.
- Click "OK," then "Apply," then "Apply changes to this folder only."
- Now when you start Ubuntu it should be successful, and will ask for a username and password.
- As per the suggestion, run **`wsl.exe --update`**
- Double check your OS version by running **`lsb_release -a`**
- Now try this [getting-started tutorial for
  Pants](https://semaphoreci.com/blog/building-python-projects-with-pants). This
  was written for Pants V1, so there are some commands in the tutorial that have
  small mistakes but Pants V2 will help you correct the issues).  You will run
  into the following problem:
- The default interpreter for Ubuntu 22.04.1 is Python 3.10.6, so trying to run
  Pants produces: \
`No valid Python interpreter found. For pants_version = "2.16.0.dev0", Pants requires Python 3.7, 3.8, or 3.9 to run. Please check that a valid interpreter is installed and on your $PATH.`
- We need to install a Python interpreter that Pants can work with.

## Installing Additional Python Interpreters

- See [here](https://hackersandslackers.com/multiple-python-versions-ubuntu-20-04/) for details.
- Ubuntu depends on its default Python installation so you can't remove or
  replace it.
- Note: If you have problems connecting to repos, make sure your VPN is turned
  off.
- The "deadsnakes" repository was the one used in all the posts I found.
- **`sudo add-apt-repository ppa:deadsnakes/ppa`**
- **`sudo apt update`**
- We'll look for Python 3.9:
- **`apt list | grep python3.9`**
- Install it:
- **`sudo apt install python3.9`**
- We only need to add it to `$PATH`. No need to use `update-alternatives`.
- If you run **`which python3.9`**, you should see `/usr/bin/python3.9`
- Add the path for python3.9 to the `$PATH` variable. Open the file with
  **`code ~/.bashrc`** and add this to the end:
- `export PATH="$PATH:/usr/bin/python3.9"`
- Either **`source ~/.bashrc`** or start a new bash shell.
- **`echo $PATH`** to verify it's at the end.
- Now when you run Pants you may get a new error: \
`ModuleNotFoundError: No module named 'distutils.util'`
- Fix with: **`sudo apt install python3.9-distutils`**

## Notes

- If you want to know more about Pants, their documentation is [here](https://www.pantsbuild.org/docs).

- There are [reasons to consider using WSL 1](https://learn.microsoft.com/en-us/windows/wsl/compare-versions#exceptions-for-using-wsl-1-rather-than-wsl-2) rather than WSL 2.

## Windows 11
(NOTE: Retest this process after removing WSL)
- After installing throught the Windows Store as above, when you click the "Open" button you may see:
```
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x8007019e
The Windows Subsystem for Linux optional component is not enabled. Please enable it and try again.
See https://aka.ms/wslinstall for details.
```
- Open a Powershell window in System Administrator mode. Run **`wsl --install`**
- It will perform a number of operations and then produce the message: `The requested operation is successful. Changes will not be effective until the system is rebooted.`
- Reboot the computer. Note that if you have Windows updates pending you might have to reboot more than once before WSL is enabled.
- Open an Ubuntu shell from the Windows terminal.
- At this writing, the default Python installed with Ubuntu 22.04.1 is version 3.10.6. To run Pants, you will need to [add Python 3.9](https://github.com/BruceEckel/RethinkingObjects#installing-additional-python-interpreters)
