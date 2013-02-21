; PatchIt! V1.0 Stable Windows Installer
; Copyright © 2013 le717
; http://triangle717.wordpress.com
; Written with Inno Setup 5.5.2 Unicode

; If any version below the specified version is used for compiling, this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

[Define]
#define MyAppName "PatchIt!"
#define MyAppVersion "Version 1.0 Stable"
#define MyAppVerName "PatchIt! Version 1.0 Stable"
#define MyAppPublisher "le717"
#define MyAppURL "http://triangle717.wordpress.com"
#define MyAppExeName "PatchIt.exe"

[Setup]
AppId={#MyAppVerName}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppCopyright=© 2013 {#MyAppPublisher}
LicenseFile=..\License\LICENSE.txt
; Start menu\screen and Desktop shortcuts
DefaultDirName={pf}\PatchIt
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Installer Graphics
SetupIconFile=..\Icons\PatchItIcon.ico
WizardImageFile=..\Icons\PatchItSidebar.bmp
WizardSmallImageFile=..\Icons\PatchItLogo.bmp
; Location of the compiled Installer 
OutputDir=Here Lie the Installer
OutputBaseFilename={#MyAppVerName}
; Uninstallation stuff
UninstallDisplayIcon={#MyAppExeName}
CreateUninstallRegKey=yes
UninstallDisplayName={#MyAppName}
; Compression
Compression=lzma/ultra
SolidCompression=True
InternalCompressLevel=ultra
; From top to bottom: Allows installation to C:\ (and the like),
; Explicitly set Admin rights, no other languages, do not restart upon finishing.
AllowRootDirectory=yes
PrivilegesRequired=admin
ShowLanguageDialog=no
RestartIfNeededByRun=no
ArchitecturesInstallIn64BitMode=x64 ia64
ArchitecturesAllowed=x86 x64 ia64

[Languages]
; TODO: Add more languages
Name: "english"; MessagesFile: "compiler:Default.isl"

[Messages]
english.BeveledLabel={#MyAppVerName}

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\Compile\PatchIt64.exe"; DestDir: "{app}"; DestName: "PatchIt.exe"; Flags: ignoreversion; Check: IsWin64
Source: "..\Compile\PatchIt32.exe"; DestDir: "{app}"; DestName: "PatchIt.exe"; Flags: ignoreversion; Check: IsWin32
Source: "..\Compile\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\python33.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\tcl85.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\tk85.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\Compile\tcl\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\Compile\tk\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\Icons\PatchItIcon.ico"; DestDir: "{app}"; Flags: createallsubdirs recursesubdirs
Source: "Read Me First.html"; DestDir: "{app}"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Comment: "Run {#MyAppVerName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\PatchItIcon.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall runascurrentuser skipifsilent; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"
Filename: "{app}\Read Me First.html"; Flags: nowait postinstall skipifsilent shellexec unchecked; Description: "View Readme"

[Code]                                                                                            
function IsWin32: Boolean;
begin
 Result := not IsWin64;
end;