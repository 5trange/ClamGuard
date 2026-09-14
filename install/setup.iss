[Setup]
AppName=ClamGuard Security
AppVersion=1.3.1
AppCopyright=Copyright © 2026, ClamGuard
AppId={{1A402BF3-535F-412A-87A2-BE331147C413}
LicenseFile=..\LICENSE
DefaultDirName={commonpf}\ClamGuard
MinVersion=0,6.2
Compression=lzma2/ultra
InternalCompressLevel=ultra
VersionInfoVersion=1.3.0
VersionInfoCompany=The ClamGuard Developers
VersionInfoDescription=Free and opensource antivirus based on ClamAV
VersionInfoCopyright=Copyright © 2026, The ClamGuard Developers
VersionInfoProductName=ClamGuard Security
VersionInfoProductVersion=1.3.0
UninstallDisplayName=ClamGuard Security
UninstallDisplaySize=1
AppPublisher=The ClamGuard Developers
AppPublisherURL=https://github.com/5trange
AppSupportURL=https://github.com/5trange/ClamGuard
AppUpdatesURL=https://github.com/5trange/ClamGuard
DefaultGroupName=ClamGuard Security
DisableWelcomePage=False
ArchitecturesInstallIn64BitMode=x64
OutputDir=dist
OutputBaseFilename=ClamGuard-Setup

[Files]
Source: "..\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{commonappdata}\ClamGuard\db"; Permissions: everyone-full
Name: "{commonappdata}\ClamGuard\logs"; Permissions: everyone-full
Name: "{commonappdata}\ClamGuard\quarantine"; Permissions: everyone-full

[Icons]
Name: "{commondesktop}\ClamGuard Security"; Filename: "{app}\ClamGuard.exe"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0
Name: "{group}\ClamGuard Security"; Filename: "{app}\ClamGuard.exe"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0
Name: "{group}\Uninstall ClamGuard"; Filename: "{uninstallexe}"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0
