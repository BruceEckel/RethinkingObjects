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

* (Not starting with wsl command-line commands)
* Inside the MS Store, find Ubuntu 22.04.1 LTS, click the “get” button
* Upon clicking the “Open” button after installing from the MS Store, you will
  see:
* <code>Error: 0x800701bc WSL 2 requires an update to its kernel component. For
  information please visit
  [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)</code>
* Follow the instructions at the link to install the update.
* Opening Ubuntu again produces a “virtual disk system limitation” error.
* To fix this, open the Windows File Explorer and navigate to:
* <strong><code>C:\Users\YOUR_USER\AppData\Local\Packages\CanonicalGroupLimited...</code></strong>
* Right click on “LocalState”, then “Properties,” then “Advanced.”
* Ensure “Compress contents to save disk space” and “Encrypt contents to secure data” are both <strong>de</strong>selected.
* Click “OK,” then “Apply,” then “Apply changes to this folder only.”
* Now when you start Ubuntu it should be successful, and will ask for a username and password.
* As per the suggestion, run <strong><code>wsl.exe --update</code></strong>
* Double check your OS version by running <strong><code>lsb_release -a</code></strong>
* Now try this [getting-started tutorial for Pants](https://semaphoreci.com/blog/building-python-projects-with-pants). (Note that there are some commands in the tutorial that have small mistakes but Pants will help you correct the issues).  You will run into the following problem:
* The default interpreter for Ubuntu 22.04.1 is Python 3.10.6, so trying to run Pants produces: \
<code>No valid Python interpreter found. For `pants_version = "2.16.0.dev0"`, Pants requires Python 3.7, 3.8, or 3.9 to run. Please check that a valid interpreter is installed and on your $PATH.</code>
* We need to install a Python interpreter that Pants can work with.

## Installing Additional Python Interpreters on Linux

* See [here](https://hackersandslackers.com/multiple-python-versions-ubuntu-20-04/) for details.
* Ubuntu depends on its default Python installation so you can’t remove or replace it.
* Note: If you have problems connecting to repos, make sure your VPN is turned off
* The “deadsnakes” repository was the one used in all the posts I found.
* <strong><code>sudo add-apt-repository ppa:deadsnakes/ppa</code></strong>
* <strong><code>sudo apt update</code></strong>
* We’ll look for Python 3.9:
* <strong><code>apt list | grep python3.9</code></strong>
* Install it:
* <strong><code>sudo apt install python3.9</code></strong>
* Let’s try just adding it to <code>$PATH</code> without messing with <code>update-alternatives</code>
* If you run <strong><code>which python3.9</code></strong>, you should see <code>/usr/bin/python3.9</code>
* Edit it into the $PATH: <strong><code>code ~/.bashrc </code></strong>and add this at the end of the file:
* <strong><code>export PATH="$PATH/usr/bin/python3.9"</code></strong>
* Either <strong><code>source ~/.bashrc</code></strong> or start a new bash shell
* <strong><code>echo $PATH</code></strong> to verify it’s at the end.
* Now when you run Pants you may get a new error: \
<code>ModuleNotFoundError: No module named 'distutils.util'</code>
* Fix with: <strong><code>sudo apt install python3.9-distutils</code></strong>

## Notes

* If you want to know more about Pants, their documentation is [here](https://www.pantsbuild.org/first_tutorial.html.)

* There are [reasons to consider using WSL 1](https://learn.microsoft.com/en-us/windows/wsl/compare-versions#exceptions-for-using-wsl-1-rather-than-wsl-2) rather than WSL 2.
