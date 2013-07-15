;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;    This file is part of PatchIt!
;
;    PatchIt! -  the standard and simple way to package and install mods for LEGO Racers
;    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>
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
; Written with Inno Setup 5.5.2 Unicode

; If any version below the specified version is used for compiling, this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

#ifdef UNICODE
  ; Do nothing, since Unicode is needed to compile
#else
  ; If non-Unicode (AKA ANSI) Inno Setup is used
  #error You must use Unicode Inno Setup to compile this script
#endif 
       
#define MyAppName "PatchIt!"
#define MyAppVersion "1.1.1"
#define MyAppVerName "PatchIt! Version 1.1.1 Stable"
#define MyInstallerName "PatchIt-111-Stable"
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
AllowNoIcons=True
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
UninstallDisplayIcon={app}\Icons\PatchItIcon.ico
CreateUninstallRegKey=not PortableInstall
UninstallDisplayName={#MyAppName}
; This is required so Inno can correctly report the installation size.
UninstallDisplaySize=31457280
; Compression
Compression=lzma2/ultra64
SolidCompression=True
InternalCompressLevel=ultra
LZMAUseSeparateProcess=yes
; From top to bottom: Allows installation to C:\ (and the like),
; Explicitly set Admin rights, no other languages, do not restart upon finishing.
AllowRootDirectory=yes
PrivilegesRequired=admin
RestartIfNeededByRun=no
; This is required so Inno can correctly report the installation size.
ExtraDiskSpaceRequired=31457280
; Required for creating Shell extension
ChangesAssociations=True

[Languages]
Name: english; MessagesFile: compiler:Default.isl
;Name: francais; MessagesFile: compiler:Languages\French.isl; LicenseFile: "..\License\gpl-v3-fr.txt"
Name: nederlands; MessagesFile: compiler:Languages\Dutch.isl; LicenseFile: "..\License\gpl-v3-nl-101.pdf"

[Messages]
BeveledLabel={#MyAppVerName}
english.ConfirmUninstall=Are you sure you want to completely remove {#MyAppVerName} and all of its components?
english.UninstalledAll={#MyAppVerName} was successfully removed from your computer.
; francais.UninstalledAll={#MyAppVerName} a été correctement désinstallé de cet ordinateur.
; francais.ConfirmUninstall=Voulez-vous vraiment désinstaller complètement {#MyAppVerName} ainsi que tous ses composants ?
nederlands.ConfirmUninstall=Weet u zeker dat u {#MyAppVerName} en alle bijbehorende componenten wilt verwijderen?
nederlands.UninstalledAll={#MyAppVerName} is met succes van deze computer verwijderd.

[CustomMessages]
english.Settings_Reset=Reset {#MyAppName} Preferences
english.Admin=Run {#MyAppName} with Administrator Rights
english.Shell=Associate .PiP File with {#MyAppName}
; francais.Settings_Reset=Réinitialiser {#MyAppName} préférences
; francais.Admin=Exécuter {#MyAppName} avec des droits administrateur
; francais.Shell=Associer fichier. PiP Avec {#MyAppName}
nederlands.Settings_Reset=Reset {#MyAppName} voorkeuren  
nederlands.Admin=Run {#MyAppName} met beheerdersrechten   
nederlands.Shell=Associëren .PiP File Met {#MyAppName}

[Tasks]
Name: desktopicon; Description: {cm:CreateDesktopIcon}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked; Check: not PortableInstall
Name: Shell; Description: {cm:Shell}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked; Check: not PortableInstall

Name: Admin; Description: {cm:Admin}; Check: not PortableInstall
Name: Settings_Reset; Description: {cm:Settings_Reset}; Flags: unchecked     

[Registry]
; Registry strings are always hard-coded (!!NO ISPP!!) to ensure everything works correctly.
; Run as Admin for this user only
Root: "HKCU"; Subkey: "Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"; ValueType: string; ValueName: "{app}\PatchIt.exe"; ValueData: "RUNASADMIN"; Flags: uninsdeletevalue; Tasks: Admin

; Shell extension
Root: "HKCR"; Subkey: ".PiP"; ValueType: string; ValueData: "PatchIt! Patch"; Flags: uninsdeletekey; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\DefaultIcon"; ValueType: string; ValueData: "{app}\Icons\PatchItIcon.ico"; Flags: uninsdeletevalue; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell"; ValueType: string; ValueData: "open"; Flags: uninsdeletevalue; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell\open"; ValueType: none; Flags: uninsdeletekey; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell\open\command"; ValueType: string; ValueData: "{app}\PatchIt.exe ""%1"""; Flags: uninsdeletevalue; Tasks: Shell

[Files]
; PatchIt! Uninstaller
Source: Uninstaller\PiUninstaller.exe; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall
Source: Uninstaller\_bz2.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall
Source: Uninstaller\library.zip; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall
Source: Uninstaller\python33.dll; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall
Source: Uninstaller\select.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall
Source: Uninstaller\unicodedata.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion uninsneveruninstall

; Readme and Icon
Source: ..\Icons\PatchItIcon.ico; DestDir: {app}\Icons; Flags: ignoreversion
Source: ..\Icons\PiTk.gif; DestDir: {app}\Icons; Flags: ignoreversion
Source: ..\Icons\cghbnjcGJfnvzhdgbvgnjvnxbv12n1231gsxvbhxnb.jpg; DestDir: {app}\Icons; Flags: ignoreversion
Source: ..\Documentation\Readme\index.html; DestDir: {app}\Documentation; Flags: ignoreversion isreadme
Source: ..\Documentation\Readme\*; Excludes: index.html; DestDir: {app}\Documentation; Flags: ignoreversion recursesubdirs createallsubdirs

; Settings files
; Source: ..\Compile\Settings\Racers.cfg; DestDir: {app}\Settings; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall
; Source: ..\Compile\Settings\LOCO.cfg; DestDir: {app}\Settings; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall

; Settings files for Settings_Reset switch
; Source: ..\Compile\Settings\Racers.cfg; DestDir: {app}\Settings; Tasks: Settings_Reset; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall 
; Source: ..\Compile\Settings\LOCO.cfg; DestDir: {app}\Settings; Tasks: Settings_Reset; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall 

; PatchIt! itself (a 32-bit Windows binary)
Source: ..\Compile\Windows\*; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: {group}\{#MyAppName}; Filename: {app}\{#MyAppExeName}; IconFilename: {app}\Icons\PatchItIcon.ico; Comment: Run {#MyAppVerName}
Name: {group}\{cm:UninstallProgram,{#MyAppName}}; Filename: {uninstallexe}; IconFilename: {app}\Icons\PatchItIcon.ico
Name: {commondesktop}\{#MyAppName}; Filename: {app}\{#MyAppExeName}; IconFilename: {app}\Icons\PatchItIcon.ico; Tasks: desktopicon

[Run]
Filename: {app}\{#MyAppExeName}; Flags: nowait postinstall runascurrentuser skipifsilent; Description: {cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}

[UninstallDelete]
; Because for some reason, these are not getting deleted at uninstall
Type: filesandordirs; Name: {app}\tcl
Type: filesandordirs; Name: {app}\tk  

[InstallDelete]
; Remove V1.0.x settings file
; Not doing so breaks V1.1.x
Type: files; Name: {app}\settings

[Dirs]
; So the Settings do not ever get uninstalled
Name: "{app}\Settings"; Flags: uninsneveruninstall

[Code]   

// Portable Switch taken from https://github.com/jrsoftware/issrc/blob/master/setup.iss
function PortableInstall: Boolean;
begin
  Result := ExpandConstant('{param:portable|0}') = '1';
end;

// Code based on Launchy Inno Setup installer
// http://launchy.svn.sourceforge.net/viewvc/launchy/trunk/Launchy_QT/win/installer/SETUP.iss
function InstallPath(Param: String): String;
begin
  if PortableInstall then
    Result := ExpandConstant('{src}\PatchIt Portable')
  else
    Result := ExpandConstant('{pf}\PatchIt');
end;

// Uninstalls previous versions of PatchIt! before instaling the current one
// Code based on examples in Inno Setup help file and scripts on the Internet
function PrepareToInstall(var NeedsRestart: Boolean): String;
var
  ResultCode: Integer;
begin
  ExtractTemporaryFile('PiUninstaller.exe');
  ExtractTemporaryFile('python33.dll');
  ExtractTemporaryFile('library.zip');
  ExtractTemporaryFile('_bz2.pyd');
  ExtractTemporaryFile('select.pyd');
  ExtractTemporaryFile('unicodedata.pyd');
  if Exec(ExpandConstant('{tmp}\PiUninstaller.exe'), ExpandConstant('"{app}"'), '', SW_SHOWNORMAL, ewWaitUntilTerminated, ResultCode) then
  end;