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
AppId={#MyAppVerName}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVerName}
AppPublisher={#MyAppPublisher}
AppCopyright=© 2013 {#MyAppPublisher}
LicenseFile=LICENSE.txt
; Start menu\screen and Desktop shortcuts
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Installer Graphics
SetupIconFile=PatchIt.ico
WizardImageFile=PatchIt Sidebar.bmp
WizardSmallImageFile=PatchIt Logo.bmp
; Location of the compiled Installer 
OutputDir=Here Lie the Installer
OutputBaseFilename={#MyAppVerName}
; Uninstallation stuff
UninstallDisplayIcon={#MyAppExeName}
CreateUninstallRegKey=yes
UninstallDisplayName={#MyAppName}
; Compression
Compression=lzma
SolidCompression=True
InternalCompressLevel=ultra
; From top to bottom: Allows installation to C:\ (and the like),
; Explicitly set Admin rights, no other languages, do not restart upon finishing.
AllowRootDirectory=yes
PrivilegesRequired=admin
ShowLanguageDialog=no
RestartIfNeededByRun=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Messages]
english.BeveledLabel={#MyAppVerName}

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "PatchIt.exe"; DestDir: "{app}"; Flags: ignoreversion;
Source: "_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion;
Source: "python33.dll"; DestDir: "{app}"; Flags: ignoreversion;
Source: "unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion;  

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Comment: "Run {#MyAppVerName}";
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
