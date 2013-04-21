;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;    This file is part of PatchIt!
;
;    PatchIt! -  the standard yet simple way to package and install mods for LEGO Racers
;    Created 2013 Triangle717 <http://triangle717.wordpress.com>
;
;    PatchIt! is free software: you can redistribute it and/or modify
;    it under the terms of the GNU General Public License as published by
;    the Free Software Foundation, either version 3 of the License, or
;    (at your option) any later version.
;
;    PatchIt! is distributed in the hope that it will be useful,
;    but WITHOUT ANY WARRANTY; without even the implied warranty of
;    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;    GNU General Public License for more details.
;
;    You should have received a copy of the GNU General Public License
;    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; PatchIt! Windows Installer
; Created 2013 Triangle717
; http://Triangle717.WordPress.com
; Written with Inno Setup 5.5.2 Unicode

; If any version below the specified version is used for compiling, this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

[Define]
#define MyAppName "PatchIt!"
#define MyAppVersion "1.1.0"
#define MyAppVerName "PatchIt! Version 1.1.0 Unstable"
#define MyInstallerName "PatchIt-Version-1.1.0-Unstable"
#define MyAppPublisher "Triangle717"
#define MyAppURL "http://Triangle717.WordPress.com"
#define MyAppExeName "PatchIt.exe"

[Setup]
AppId={#MyAppVerName}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppCopyright=Created 2013 {#MyAppPublisher}
LicenseFile=..\License\LICENSE.txt
; Start menu\screen and Desktop shortcuts
DefaultDirName={code:InstallPath}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Installer Graphics
SetupIconFile=..\Icons\PatchItIcon.ico
WizardImageFile=..\Icons\PatchItSidebar.bmp
WizardSmallImageFile=..\Icons\PatchItLogo.bmp
; Location of the compiled Installer 
; Hint: The same folder as this script
OutputDir=.\
OutputBaseFilename={#MyInstallerName}
; Uninstallation stuff
Uninstallable=not PortableInstall
UninstallDisplayIcon={app}\PatchItIcon.ico
CreateUninstallRegKey=not PortableInstall
UninstallDisplayName={#MyAppName}
; This is required because Inno is having issues figuring out how large the files are. :|
; TODO: Check if this is fixed yet!
UninstallDisplaySize=16252928
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
; TODO: Check if this is fixed yet!
ExtraDiskSpaceRequired=16252928

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: francais; MessagesFile: compiler:Languages\French.isl; LicenseFile: "..\License\gpl-3.0.fr.txt"
Name: nederlands; MessagesFile: compiler:Languages\Dutch.isl; LicenseFile: "..\License\gpl-v3-nl-101.pdf"

[Messages]
english.BeveledLabel={#MyAppVerName}

[CustomMessages]
english.Settings_Reset=Reset {#MyAppName} Preferences
francais.Settings_Reset=Réinitialiser {#MyAppName} préférences
nederlands.Settings_Reset=Reset {#MyAppName} voorkeuren
english.Admin=Run {#MyAppName} with Administrator Rights
francais.Admin=Exécuter {#MyAppName} avec des droits administrateur
nederlands.Admin=Run {#MyAppName} met beheerdersrechten

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; Check: not PortableInstall
Name: "Settings_Reset"; Description: "{cm:Settings_Reset}"; Flags: unchecked
Name: "Admin"; Description: "{cm:Admin}"; Flags: unchecked; Check: not PortableInstall

[Registry]
; Registry strings are always hard-coded (!!NO ISPP!!) to ensure everything works correctly.
Root: "HKCU"; Subkey: "Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"; ValueType: string; ValueName: "{app}\PatchIt.exe"; ValueData: "RUNASADMIN"; Flags: uninsdeletevalue; Tasks: Admin

[Files]
; PatchIt! Icon
Source: "..\Icons\PatchItIcon.ico"; DestDir: "{app}"; Flags: ignoreversion
; HTML Readme
Source: "..\Documentation\Read Me First.html"; DestDir: "{app}"; Flags: ignoreversion
; PatchIt! LEGO Racers settings file
Source: "..\Compile\Settings\Racers.cfg"; DestDir: "{app}\Settings"; Flags: ignoreversion
; Again for Settings_Reset switch
Source: "..\Compile\Settings\Racers.cfg"; DestDir: "{app}\Settings"; Flags: ignoreversion; Tasks: Settings_Reset
; PatchIt! LEGO LOCO settings file
Source: "..\Compile\Settings\LOCO.cfg"; DestDir: "{app}\Settings"; Flags: ignoreversion
; Again for Settings_Reset switch
Source: "..\Compile\Settings\LOCO.cfg"; DestDir: "{app}\Settings"; Flags: ignoreversion; Tasks: Settings_Reset
; 64-bit Windows build                                                     
Source: "..\Compile\Windows64\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin64
; 32-bit Windows build
Source: "..\Compile\Windows32\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Check: IsWin32
; Move the PatchIt! 1.0.x Logs out of the way; The user may still want them
; TODO: Rename the folder, rather than just make a copy of it                                                  
Source: "{app}\Logs\*.*"; DestDir: "{app}\PatchIt10xLogs"; Flags: external skipifsourcedoesntexist uninsneveruninstall

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


[InstallDelete]
; Remove PatchIt V1.0.x settings file
Type: files; Name: "{app}\settings"

[Code]   
// Taken from CamStudio (http://camstudio.org) 2.6 r294 Inno Setup installer                                                                                         
function IsWin32: Boolean;
begin
 Result := not IsWin64;
end;

// Portable Switch taken from https://github.com/jrsoftware/issrc/blob/master/setup.iss
function PortableInstall: Boolean;
begin
  Result := ExpandConstant('{param:portable|0}') = '1';
end;

/// Code based on Launchy Inno Setup installer
// http://launchy.svn.sourceforge.net/viewvc/launchy/trunk/Launchy_QT/win/installer/SETUP.iss
function InstallPath(Param: String): String;
begin
  if PortableInstall then
    Result := ExpandConstant('{src}')
  else
    Result := ExpandConstant('{pf}');
  Result := Result + '\PatchIt';
end;