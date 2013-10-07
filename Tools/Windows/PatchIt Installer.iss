;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;    In this manner, therefore, pray:
;
;     Our Father in heaven,
;     Hallowed be Your name.
;     Your kingdom come.
;     Your will be done
;     On earth as it is in heaven.
;     Give us this day our daily bread.
;     And forgive us our debts,
;     As we forgive our debtors.
;     And do not lead us into temptation,
;     But deliver us from the evil one.
;     For Yours is the kingdom and the power and the glory forever. Amen.
;    - Matthew 6:9-13
;
;    This file is part of PatchIt!
;
;    PatchIt! - the standard and simple way to package and install mods
;    for LEGO® Racers
;
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

; If any version below the specified version is used for compiling, 
; this error will be shown.
#if VER < EncodeVer(5,5,2)
  #error You must use Inno Setup 5.5.2 or newer to compile this script
#endif

#ifdef UNICODE
  ; Do nothing, since Unicode is needed to compile
#else
  ; If non-Unicode (AKA ANSI) Inno Setup is used
  #error You must use Unicode Inno Setup to compile this script
#endif 

; Global variables
#define MyAppName "PatchIt!" 
#define MyAppVersion "1.1.2"
#define MyAppVerName "PatchIt! Version 1.1.2 Unstable"
#define MyInstallerName "PatchIt-112-Unstable"
#define MyAppPublisher "Triangle717"
#define MyAppPublisherURL "http://Triangle717.WordPress.com/"
#define MyAppURL "http://le717.github.io/PatchIt"
#define MyAppExeName "PatchIt.exe"
   

[Setup]
; Name, version, publisher, support info
AppId={#MyAppVerName}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
VersionInfoVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppPublisherURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion={#MyAppVersion}
VersionInfoProductTextVersion={#MyAppVerName}
; License
AppCopyright=Created 2013 {#MyAppPublisher}
LicenseFile=..\..\License\LICENSE.txt
; Start menu\screen and Desktop shortcuts
DefaultDirName={code:InstallPath}
DefaultGroupName={#MyAppName}
AllowNoIcons=True
; Installer Graphics
SetupIconFile=..\..\Icons\PiIcon.ico
WizardImageFile=..\..\Icons\PatchItSidebar.bmp
WizardSmallImageFile=..\..\Icons\PatchItLogo.bmp
; Location of the compiled Installer 
; Hint: The same folder as this script
OutputDir=.\
OutputBaseFilename={#MyInstallerName}
; Uninstallation stuff
Uninstallable=not PortableInstall
UninstallDisplayIcon={app}\Icons\PiIcon.ico
CreateUninstallRegKey=not PortableInstall
UninstallDisplayName={#MyAppName}
; Compression
Compression=lzma2/ultra64
SolidCompression=yes
InternalCompressLevel=ultra
LZMAUseSeparateProcess=yes
; From top to bottom: Allows installation to C:\ (and the like),
; Explicitly set Admin rights, no other languages, 
; do not restart upon finishing
AllowRootDirectory=yes
PrivilegesRequired=admin
RestartIfNeededByRun=no
; Required for creating Shell extension
ChangesAssociations=True

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: francais; MessagesFile: compiler:Languages\French.isl; LicenseFile: "..\..\License\gpl-3.0.fr.txt" 
Name: nederlands; MessagesFile: compiler:Languages\Dutch.isl; LicenseFile: "..\..\License\gpl-v3-nl-101.pdf"

[Messages]
BeveledLabel={#MyAppVerName}
english.ConfirmUninstall=Are you sure you want to completely remove {#MyAppVerName} and all of its components?
english.UninstalledAll={#MyAppVerName} was successfully removed from your computer.
francais.UninstalledAll={#MyAppVerName} a été correctement désinstallé de cet ordinateur.
francais.ConfirmUninstall=Voulez-vous vraiment désinstaller complètement {#MyAppVerName} ainsi que tous ses composants ?
nederlands.ConfirmUninstall=Weet u zeker dat u {#MyAppVerName} en alle bijbehorende componenten wilt verwijderen?
nederlands.UninstalledAll={#MyAppVerName} is met succes van deze computer verwijderd.

[CustomMessages]
english.Options=Insallation Options:
english.Settings_Reset=Reset {#MyAppName} Preferences
english.Admin=Run {#MyAppName} with Administrator Rights
english.Shell=Associate .PiP File with {#MyAppName}
francais.Options=Options insallation: 
francais.Settings_Reset=Réinitialiser {#MyAppName} préférences
francais.Admin=Exécuter {#MyAppName} avec des droits administrateur
francais.Shell=Associer fichier. PiP Avec {#MyAppName}
nederlands.Options=Installatie opties:
nederlands.Settings_Reset=Reset {#MyAppName} voorkeuren  
nederlands.Admin=Run {#MyAppName} met beheerdersrechten   
nederlands.Shell=Associëren .PiP File Met {#MyAppName}

[Tasks]
Name: Admin; Description: {cm:Admin}; GroupDescription: {cm:Options}; Check: not PortableInstall
Name: Settings_Reset; Description: {cm:Settings_Reset}; GroupDescription: {cm:Options}; Flags: unchecked

Name: Shell; Description: {cm:Shell}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked; Check: not PortableInstall
Name: desktopicon; Description: {cm:CreateDesktopIcon}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked; Check: not PortableInstall
   

[Registry]
; Registry strings are always hard-coded (!!NO ISPP!!) to ensure everything works correctly.
; Run as Admin for this user only
Root: "HKCU"; Subkey: "Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"; ValueType: string; ValueName: "{app}\PatchIt.exe"; ValueData: "RUNASADMIN"; Flags: uninsdeletevalue; Tasks: Admin

; Shell extension
Root: "HKCR"; Subkey: ".PiP"; ValueType: string; ValueData: "PatchIt! Patch"; Flags: uninsdeletekey; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\DefaultIcon"; ValueType: string; ValueData: "{app}\Icons\PiIcon.ico"; Flags: uninsdeletevalue; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell"; ValueType: string; ValueData: "open"; Flags: uninsdeletevalue; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell\open"; ValueType: none; Flags: uninsdeletekey; Tasks: Shell
Root: "HKCR"; Subkey: ".PiP\shell\open\command"; ValueType: string; ValueData: "{app}\PatchIt.exe --open ""%1"""; Flags: uninsdeletevalue; Tasks: Shell

[Files] 
; PatchIt! Uninstaller                                                                              
Source: ..\Uninstaller\bin\PiUninstaller.exe; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy
Source: ..\Uninstaller\bin\_bz2.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy
Source: ..\Uninstaller\bin\library.zip; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy
Source: ..\Uninstaller\bin\python33.dll; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy
Source: ..\Uninstaller\bin\select.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy
Source: ..\Uninstaller\bin\unicodedata.pyd; DestDir: {app}\Uninstaller; Flags: ignoreversion dontcopy

; Readme
Source: ..\..\Documentation\Readme\*; DestDir: {app}\Documentation; Flags: ignoreversion recursesubdirs createallsubdirs

; RunAsAdmin utility
Source: RunAsAdmin\RunAsAdmin.cfg; DestDir: {app}; Flags: ignoreversion
Source: RunAsAdmin\RunAsAdmin.exe; DestDir: {app}; Flags: ignoreversion  

; License files
Source:  ..\..\License\*; DestDir: {app}\License; Flags: ignoreversion

; Settings files
Source: ..\..\bin\Settings\Racers.cfg; DestDir: {app}\Settings; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall
Source: ..\..\bin\Settings\LOCO.cfg; DestDir: {app}\Settings; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall

; Settings files for Settings_Reset switch
Source: ..\..\bin\Settings\Racers.cfg; DestDir: {app}\Settings; Tasks: Settings_Reset; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall 
Source: ..\..\bin\Settings\LOCO.cfg; DestDir: {app}\Settings; Tasks: Settings_Reset; Permissions: users-modify; Flags: ignoreversion uninsneveruninstall 

; PatchIt! itself (a 32-bit Windows binary)
Source: ..\..\bin\Windows\*; Excludes: Logs; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Launch PatchIt!, view Readme, Uninstall
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\Icons\PiIcon.ico"; Comment: "Run {#MyAppVerName}"
Name: "{group}\{#MyAppName} - Experimental Mode"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\Icons\PiIcon.ico"; Parameters: "--test"; Comment: "Run {#MyAppVerName} - Experimental Mode"
; Name: "{group}\{#MyAppName} Updater"; Filename: "{app}\Documentation\index.html"; IconFilename: "{app}\Icons\PiIcon.ico"; Comment: "Run {#MyAppName} Updater"
Name: "{group}\{#MyAppName} Readme"; Filename: "{app}\Updater\PiUpdater.exe"; IconFilename: "{app}\Icons\PiIcon.ico"; Comment: "View {#MyAppName} Readme"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\Icons\PiIcon.ico"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\Icons\PiIcon.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\Documentation\index.html"; Flags: nowait postinstall skipifsilent shellexec; Description: "View Readme"
Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall runascurrentuser skipifsilent; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"

[UninstallDelete]
; Because for some reason, these are not getting deleted at uninstall
Type: filesandordirs; Name: {app}\tcl
Type: filesandordirs; Name: {app}\tk  

[InstallDelete]
; Remove V1.0.x settings file
; Not doing so breaks V1.1.x
Type: files; Name: {app}\settings

[Dirs]
; So the Settings are never uninstalled
Name: "{app}\Settings"; Flags: uninsneveruninstall

[Code]  
// Portable Switch taken from https://github.com/jrsoftware/issrc/blob/master/setup.iss
function PortableInstall: Boolean;
begin
  Result := ExpandConstant('{param:portable|0}') = '1';
end;

// Code based on Launchy Inno Setup installer
// https://sourceforge.net/p/launchy/code/671/tree/trunk/Launchy_QT/win/installer/SETUP.iss
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
