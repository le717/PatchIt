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
#define MyAppVersion "Version 1.1 Stable"
#define MyAppVerName "PatchIt! Version 1.1 Stable"
#define MyAppPublisher "Triangle717"
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
RestartIfNeededByRun=no
ArchitecturesInstallIn64BitMode=x64 ia64
ArchitecturesAllowed=x86 x64 ia64

[Languages]
; TODO: Add more languages
Name: english; MessagesFile: compiler:Default.isl
Name: francais; MessagesFile: compiler:Languages\French.isl; LicenseFile: "..\License\gpl-3.0.fr.txt"
Name: nederlands; MessagesFile: compiler:Languages\Dutch.isl; LicenseFile: "..\License\gpl-v3-nl-101.pdf"

[Messages]
english.BeveledLabel={#MyAppVerName}

[CustomMessages]
english.Settings_Reset=Reset {#MyAppName} Preferences
francais.Settings_Reset=RÃ©intialiser les paramÃ¨tres {#MyAppName}
nederlands.Settings_Reset=Reset {#MyAppName} voorkeuren

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "Settings_Reset"; Description: "{cm:Settings_Reset}"; Flags: unchecked

[Files]
; 64-bit Windows build
Source: "..\Compile\Windows x64\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin64
; 32-bit Windows build
Source: "..\Compile\Windows x86\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin32
Source: "..\Compile\settings"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Tasks: Settings_Reset
Source: "..\Icons\PatchItIcon.ico"; DestDir: "{app}"; Flags: createallsubdirs recursesubdirs
Source: "..\Documentation\Read Me First.html"; DestDir: "{app}"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Comment: "Run {#MyAppVerName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\PatchItIcon.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall runascurrentuser skipifsilent; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"
Filename: "{app}\Read Me First.html"; Flags: nowait postinstall shellexec skipifsilent; Description: "View Readme"

[Code]                                                                                            
function IsWin32: Boolean;
begin
 Result := not IsWin64;
end;