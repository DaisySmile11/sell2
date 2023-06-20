# sell2 log detail
Command: oryx build /tmp/zipdeploy/extracted -o /home/site/wwwroot --platform python --platform-version 3.10 -p virtualenv_name=antenv --log-file /tmp/build-debug.log  -i /tmp/8db7099551fa473 --compress-destination-dir | tee /tmp/oryx-build.log
Operation performed by Microsoft Oryx, https://github.com/Microsoft/Oryx
You can report issues at https://github.com/Microsoft/Oryx/issues

Oryx Version: 0.2.20230508.1, Commit: 7fe2bf39b357dd68572b438a85ca50b5ecfb4592, ReleaseTagName: 20230508.1

Build Operation ID: c3adbf43f31a7099
Repository Commit : 253de835-23f2-430c-ab54-130d1caf3c2a
OS Type           : bullseye
Image Type        : githubactions

Detecting platforms...
Detected following platforms:
  python: 3.10.8
Version '3.10.8' of platform 'python' is not installed. Generating script to install it...

Using intermediate directory '/tmp/8db7099551fa473'.

Copying files to the intermediate directory...
Done in 0 sec(s).

Source directory     : /tmp/8db7099551fa473
Destination directory: /home/site/wwwroot


Downloading and extracting 'python' version '3.10.8' to '/tmp/oryx/platforms/python/3.10.8'...
Detected image debian flavor: bullseye.
Downloaded in 1 sec(s).
Verifying checksum...
Extracting contents...
performing sha512 checksum for: python...
Done in 7 sec(s).

image detector file exists, platform is python..
OS detector file exists, OS is bullseye..
Python Version: /tmp/oryx/platforms/python/3.10.8/bin/python3.10
Creating directory for command manifest file if it does not exist
Removing existing manifest file
Python Virtual Environment: antenv
Creating virtual environment...
Activating virtual environment...
Running pip install...
[07:47:00+0000] Collecting blinker==1.6.2
[07:47:00+0000]   Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
[07:47:00+0000] Collecting click==8.1.3
[07:47:00+0000]   Downloading click-8.1.3-py3-none-any.whl (96 kB)
[07:47:00+0000]      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 4.6 MB/s eta 0:00:00
[07:47:00+0000] Collecting colorama==0.4.6
[07:47:00+0000]   Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
[07:47:00+0000] Collecting Flask==2.3.2
[07:47:00+0000]   Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
[07:47:00+0000]      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 1.7 MB/s eta 0:00:00
[07:47:01+0000] Collecting itsdangerous==2.1.2
[07:47:01+0000]   Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
[07:47:01+0000] Collecting Jinja2==3.1.2
[07:47:01+0000]   Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
[07:47:01+0000]      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━��━━━━━━━━━ 133.1/133.1 kB 5.9 MB/s eta 0:00:00
[07:47:01+0000] Collecting MarkupSafe==2.1.3
[07:47:01+0000]   Downloading MarkupSafe-2.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
[07:47:01+0000] Collecting Werkzeug==2.3.6
[07:47:01+0000]   Downloading Werkzeug-2.3.6-py3-none-any.whl (242 kB)
[07:47:01+0000]      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 5.0 MB/s eta 0:00:00
[07:47:01+0000] Collecting gunicorn
[07:47:01+0000]   Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
[07:47:01+0000]      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 4.9 MB/s eta 0:00:00
[07:47:01+0000] Requirement already satisfied: setuptools>=3.0 in ./antenv/lib/python3.10/site-packages (from gunicorn->-r requirements.txt (line 9)) (63.2.0)
[07:47:01+0000] Installing collected packages: MarkupSafe, itsdangerous, gunicorn, colorama, click, blinker, Werkzeug, Jinja2, Flask
[07:47:02+0000] Successfully installed Flask-2.3.2 Jinja2-3.1.2 MarkupSafe-2.1.3 Werkzeug-2.3.6 blinker-1.6.2 click-8.1.3 colorama-0.4.6 gunicorn-20.1.0 itsdangerous-2.1.2

[notice] A new release of pip available: 22.2.2 -> 23.1.2
[notice] To update, run: pip install --upgrade pip
Not a vso image, so not writing build commands
Preparing output...

Copying files to destination directory '/tmp/_preCompressedDestinationDir'...
Done in 1 sec(s).
Compressing content of directory '/tmp/_preCompressedDestinationDir'...
Copied the compressed output to '/home/site/wwwroot'

Removing existing manifest file
Creating a manifest file...
Manifest file created.
Copying .ostype to manifest output directory.

Done in 17 sec(s).
