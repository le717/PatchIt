; PatchIt! Windows Installer
; Copyright © 2013 Triangle717
; http://triangle717.wordpress.com
; Written with Inno Setup 5.5.2 Unicode

; If any version below the specified version is used for compiling, this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

[Define]
#define MyAppName "PatchIt!"
#define MyAppVersion "1.0.3.1"
#define MyAppVerName "PatchIt! Version 1.0.3.1 Stable"
#define MyInstallerName "PatchIt-Version-1.0.3.1-Stable"
#define MyAppPublisher "Triangle717"
#define MyAppURL "http://Triangle717.WordPress.com"
#define MyAppExeName "PatchIt.exe"

[Setup]
AppId={#MyAppVerName}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
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
OutputBaseFilename={#MyInstallerName}
; Uninstallation stuff
Uninstallable=not PortableCheck
UninstallDisplayIcon={app}\PatchItIcon.ico
CreateUninstallRegKey=not PortableCheck
UninstallDisplayName={#MyAppName}
; This is required because Inno is having issues figuring out how large the files are. :|
UninstallDisplaySize=16269312
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
; This is required because Inno is having issues figuring out how large the files are. :|
ExtraDiskSpaceRequired=16269312

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: francais; MessagesFile: compiler:Languages\French.isl; LicenseFile: "..\License\gpl-3.0.fr.txt"
Name: nederlands; MessagesFile: compiler:Languages\Dutch.isl; LicenseFile: "..\License\gpl-v3-nl-101.pdf"

[Messages]
BeveledLabel={#MyAppVerName}
english.ConfirmUninstall=Are you sure you want to completely remove {#MyAppVerName} and all of its components?
english.UninstalledAll={#MyAppVerName} was successfully removed from your computer.
francais.UninstalledAll={#MyAppVerName} a été correctement désinstallé de cet ordinateur.
francais.ConfirmUninstall=Voulez-vous vraiment désinstaller complètement {#MyAppVerName} ainsi que tous ses composants ?
nederlands.ConfirmUninstall=Weet u zeker dat u {#MyAppVerName} en alle bijbehorende componenten wilt verwijderen?
nederlands.UninstalledAll={#MyAppVerName} is met succes van deze computer verwijderd.

[CustomMessages]
english.Settings_Reset=Reset {#MyAppName} Preferences
francais.Settings_Reset=Réinitialiser {#MyAppName} préférences
nederlands.Settings_Reset=Reset {#MyAppName} voorkeuren

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "Settings_Reset"; Description: "{cm:Settings_Reset}"; Flags: unchecked

[Files]
; PatchIt! Icon
Source: "..\Icons\PatchItIcon.ico"; DestDir: "{app}"; Flags: ignoreversion
; HTML Readme
Source: "..\Documentation\Read Me First.html"; DestDir: "{app}"; Flags: ignoreversion  
; Favicon for HTML Readme
Source: "..\Icons\favicon.png"; DestDir: "{app}"; Flags: ignoreversion
; PatchIt! settings file (with first-run set to 0)
Source: "..\Compile\settings"; DestDir: "{app}"; Flags: ignoreversion onlyifdoesntexist
; Again for Settings_Reset switch
Source: "..\Compile\settings"; DestDir: "{app}"; Flags: ignoreversion; Tasks: Settings_Reset
; 64-bit Windows build
Source: "..\Compile\Windows64\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin64
; 32-bit Windows build
Source: "..\Compile\Windows32\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin32

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Comment: "Run {#MyAppVerName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\PatchItIcon.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\PatchItIcon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall runascurrentuser skipifsilent; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"
Filename: "{app}\Read Me First.html"; Flags: nowait postinstall shellexec skipifsilent; Description: "View Readme"

[UninstallDelete]
; Because for some reason, these are not getting deleted at uninstall
Type: filesandordirs; Name: "{app}\tcl"
Type: filesandordirs; Name: "{app}\tk"

[Code]                                                                                            
function IsWin32: Boolean;
begin
 Result := not IsWin64;
end;

// Portable Switch taken from https://github.com/jrsoftware/issrc/blob/master/setup.iss
function PortableCheck: Boolean;
begin
  Result := ExpandConstant('{param:portable|0}') = '1';
end;