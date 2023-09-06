[Setup]
AppName=ClamGuard Security
AppVersion=0.7.7
AppCopyright=Copyright � 2021, The ClamGuard Developers
AppId={{1A402BF3-535F-412A-87A2-BE331147C413}
LicenseFile=E:\Binary\dist\LICENSE
DefaultDirName={commonpf}\ClamGuard
MinVersion=0,6.2
Compression=lzma2/ultra
InternalCompressLevel=ultra
VersionInfoVersion=0.7.7
VersionInfoCompany=The ClamGuard Developers
VersionInfoDescription=Free and opensource antivirus based on ClamAV
VersionInfoCopyright=Copyright � 2021, The ClamGuard Developers
VersionInfoProductName=ClamGuard Security
VersionInfoProductVersion=0.7.7
UninstallDisplayName=ClamGuard Security
UninstallDisplaySize=1
AppPublisher=The ClamGuard Developers
AppPublisherURL=https://github.com/5trange
AppSupportURL=https://github.com/5trange/ClamGuard
AppUpdatesURL=https://github.com/5trange/ClamGuard
DefaultGroupName=ClamGuard Security
DisableWelcomePage=False
ArchitecturesInstallIn64BitMode=x64
OutputBaseFilename=ClamGuard_Setup

[Files]
Source: "..\..\..\Binary\dist\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\_win32sysloader.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\clamd.conf"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\clamd.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\clamdscan.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\ClamGuard.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\ClamGuard.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\clamscan.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\clamsubmit.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\concrt140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\freshclam.conf"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\freshclam.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\json-c.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libbz2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libclamav.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libclammspack.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libclamunrar.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libclamunrar_iface.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libcrypto-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libcrypto-1_1-x64.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libcurl.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libffi-7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libfreshclam.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libssh2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libssl-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libssl-1_1-x64.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\libxml2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\MSVCP140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\MSVCP140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\msvcp140_2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\nghttp2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\opengl32sw.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pcre2-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pdcurses.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pthreadvc2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pyside6.abi3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\pywintypes39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Core.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Gui.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Network.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6OpenGL.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Qml.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6QmlModels.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Quick.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Svg.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6VirtualKeyboard.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\Qt6Widgets.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\shiboken6.abi3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\VCRUNTIME140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\win32api.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\win32event.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\clamguard.ico"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\clamguard.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\GitHub.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\gpl.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\home.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\info.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\pixelmoon.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\search.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\update.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\voyager.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\img\warning.png"; DestDir: "{app}\img"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\qt.conf"; DestDir: "{app}\PySide6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\QtCore.pyd"; DestDir: "{app}\PySide6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\QtGui.pyd"; DestDir: "{app}\PySide6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\QtNetwork.pyd"; DestDir: "{app}\PySide6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\QtWidgets.pyd"; DestDir: "{app}\PySide6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\iconengines\qsvgicon.dll"; DestDir: "{app}\PySide6\plugins\iconengines"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qgif.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qicns.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qico.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qjpeg.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qsvg.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qtga.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qtiff.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qwbmp.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\imageformats\qwebp.dll"; DestDir: "{app}\PySide6\plugins\imageformats"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\platforminputcontexts\qtvirtualkeyboardplugin.dll"; DestDir: "{app}\PySide6\plugins\platforminputcontexts"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\platforms\qminimal.dll"; DestDir: "{app}\PySide6\plugins\platforms"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\platforms\qoffscreen.dll"; DestDir: "{app}\PySide6\plugins\platforms"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\platforms\qwindows.dll"; DestDir: "{app}\PySide6\plugins\platforms"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\plugins\styles\qwindowsvistastyle.dll"; DestDir: "{app}\PySide6\plugins\styles"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_ar.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_bg.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_ca.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_cs.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_da.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_de.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_en.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_es.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_fa.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_fi.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_fr.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_gd.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_he.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_hr.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_hu.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_it.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_ja.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_ko.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_lv.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_nl.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_nn.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_pl.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_pt_BR.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_ru.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_sk.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_tr.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_uk.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_zh_CN.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\PySide6\translations\qtbase_zh_TW.qm"; DestDir: "{app}\PySide6\translations"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\shiboken6\Shiboken.pyd"; DestDir: "{app}\shiboken6"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\fonts\Ubuntu-B.ttf"; DestDir: "{fonts}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\fonts\Ubuntu-M.ttf"; DestDir: "{fonts}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\fonts\UbuntuMono-R.ttf"; DestDir: "{fonts}"; Flags: ignoreversion
Source: "..\..\..\Binary\dist\programdata\db\bytecode.cvd"; DestDir: "{commonappdata}\ClamGuard\db\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\programdata\db\daily.cld"; DestDir: "{commonappdata}\ClamGuard\db\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\programdata\db\freshclam.dat"; DestDir: "{commonappdata}\ClamGuard\db\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\programdata\db\main.cld"; DestDir: "{commonappdata}\ClamGuard\db\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\programdata\logs\clamguard_clamd.log"; DestDir: "{commonappdata}\ClamGuard\logs\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\programdata\logs\clamguard_fresh.log"; DestDir: "{commonappdata}\ClamGuard\logs\"; Flags: ignoreversion; Permissions: everyone-full
Source: "..\..\..\Binary\dist\install_config.exe"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{commonappdata}\ClamGuard\quarantine"; Permissions: everyone-full

[Icons]
Name: "{commondesktop}\ClamGuard Security"; Filename: "{app}\ClamGuard.exe"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0
Name: "{group}\ClamGuard Security"; Filename: "{app}\ClamGuard.exe"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0
Name: "{group}\Uninstall ClamGuard"; Filename: "{uninstallexe}"; WorkingDir: "{app}"; IconFilename: "{app}\ClamGuard.exe"; IconIndex: 0

[Run]
Filename: "{app}\install_config.exe"; WorkingDir: "{app}"; Flags: waituntilterminated; Description: "Configures ClamGuard installation."; StatusMsg: "Configuring ClamGuard..."
