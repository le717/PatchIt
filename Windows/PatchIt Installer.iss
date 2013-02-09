; PatchIt! 1.0 Beta 3 Windows Installer
; Copyright © 2013 le717
; http://triangle717.wordpress.com
; Written with Inno Setup 5.5.2 Unicode

; If any version below the specified version is used for compiling, this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

[Define]
#define MyAppName "PatchIt!"
#define MyAppVersion "Version 1.0 Beta 3"
#define MyAppVerName "PatchIt! Version 1.0 Beta 3"
#define MyAppPublisher "le717"
#define MyAppURL "http://triangle717.wordpress.com"
#define MyAppExeName "PatchIt.exe"

[Setup]
;AppId=
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVerName}
AppPublisher={#MyAppPublisher}
AppCopyright=© 2013 {#MyAppPublisher}
LicenseFile=LICENSE.txt
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
SetupIconFile=PatchIt.ico
WizardImageFile=PatchIt Sidebar.bmp
WizardSmallImageFile=PatchIt Logo.bmp
AllowNoIcons=yes

OutputDir=Here Lie the Installer
OutputBaseFilename={#MyAppVerName}
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "PatchIt!"; DestDir: "{app}"; Flags: ignoreversion


[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
