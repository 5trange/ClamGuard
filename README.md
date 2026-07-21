# ClamGuard

<!--toc:start-->
- [ClamGuard](#clamguard)
  - [Installation](#installation)
  - [Releases](#releases)
  - [Screenshot](#screenshot)
<!--toc:end-->

Free and open source antivirus software based on ClamAV.
Simple GUI with functionalities including different types of scans,
quarantine system, etc.

> A background process of ClamGuard watches the system
drive for any malicious code.  

## Installation

Clone the repository and install the project dependencies using [UV](https://docs.astral.sh/uv/):

```sh
git clone https://github.com/5trange/ClamGuard
cd ClamGuard
# sync the dependencies
uv sync
```

Run the application:

```sh
uv run python src/main.py
```

## Screenshot

![application Screenshot](
  https://user-images.githubusercontent.com/64513428/139042686-87e9d2fa-c747-4cd7-9f6a-b1395c1ef540.png
)

## Releases

[![Download ClamGuard](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/clamguard/files/latest/download)
