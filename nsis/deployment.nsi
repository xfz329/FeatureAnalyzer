;NSIS Modern User Interface
;Header Bitmap Example Script
;Written by Joost Verburg
 
;--------------------------------
;Include Modern UI
 
  !include "MUI2.nsh"
 
;--------------------------------
;General
 
  ;Name and file
  Name "USBDisplay"                                                         ;---- 程序名
  OutFile "USBDisplaySetup.exe"                                             ;---- 生成的目标文件名
 
  ;Default installation folder
  InstallDir "$PROGRAMFILES\USBDisplayer" 
 ;---- 安装的目标文件夹名称，这里要将前缀改成$ProgramFiles，不然会装到其它路经，不用担心64bit平台上目标目录的问题
 ;---- $PROGRAMFILE是NSIS的环境变量，会自动映射到C:\Program Files或64平台的C:\Program Files (x86)目录下
  
  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin
 
;--------------------------------
;Interface Configuration
 
  !define MUI_HEADERIMAGE
  !define MUI_HEADERIMAGE_BITMAP "win.bmp" ; optional    ---- 这里就用到了图片文件，是在生成的Setup.exe文件里的图标
  !define MUI_ABORTWARNING
 
;--------------------------------
;Pages
 
  !insertmacro MUI_PAGE_LICENSE "License.txt"    ;---- 这里就用到了License文件，我试过不用，但好像不行
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
 
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
 
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "SimpChinese"    ;---- 语言版本，没太研究，好像是控制安装程序安装过程中的显示语言为中文
  
;--------------------------------
;Installer Sections
 
Section "Application and Help(required)" SecDummy    ;---- 安装的第一部分内容，用Section来划分，这里的内容是程序的内容
 
  SetOutPath "$INSTDIR"
 
  ;ADD YOUR OWN FILES HERE...
	File 	"D3Dcompiler_47.dll"
	File 	"libEGL.dll"
	File	"libgcc_s_dw2-1.dll"
	File	"libGLESV2.dll"
	File	"libstdc++-6.dll"			
	File	"libusb0.dll"				
	File	"libwinpthread-1.dll"
	File	"opengl32sw.dll"
	File	"Qt5Core.dll"
	File	"Qt5Gui.dll"
	File	"Qt5PrintSupport.dll"
	File	"Qt5Svg.dll"
	File	"Qt5Widgets.dll"
	File	"USBDisplayer.exe"	
	File 	"License.txt"
	File	"label.ico"
	SetOutPath	"$INSTDIR\iconengines"
	File	"iconengines\*.*"
	SetOutPath	"$INSTDIR\imageformats"
	File	"imageformats\*.*"
	SetOutPath	"$INSTDIR\platforms"
	File	"platforms\*.*"
	SetOutPath	"$INSTDIR\printsupport"
	File	"printsupport\*.*"
	SetOutPath	"$INSTDIR\translations"
	File	"translations\*.*"
 
	;Create uninstaller
	WriteUninstaller "$INSTDIR\Uninstall.exe"     ;---- 这里是生成卸载程序
 
SectionEnd
 
;--------------------------------
;Descriptions
 
  ;Language strings
  LangString DESC_SecDummy ${LANG_ENGLISH} "Application and Help(required)"    ;---- 这里是语言配置，没有太研究
 
  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDummy} $(DESC_SecDummy)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
;--------------------------------
; Optional section (can be disabled by the user)
Section "StartMenu ShortCuts"    ;---- 安装的第二部分，同样用Section来划分，这里的内容是添加“开始菜单”的菜单项
 
  CreateDirectory "$SMPROGRAMS\USBDisplayer"    ;---- 开始菜单中安装的目录
  CreateShortCut "$SMPROGRAMS\USBDisplayer\USBDisplayer.lnk" "$INSTDIR\USBDisplayer.exe" "" "$INSTDIR\label.ico"     ;---- 目录中的快捷选项
  CreateShortCut "$SMPROGRAMS\USBDisplayer\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
 
SectionEnd
 
;--------------------------------
; Optional section (can be disabled by the user)
Section "Desktop ShortCuts"    ;---- 安装的第三部分，同样用Section来划分，这里的内容是添加“桌面”的快捷方式
 
  CreateShortCut "$DESKTOP\USBDisplayer.lnk" "$INSTDIR\USBDisplayer.exe" "" "$INSTDIR\label.ico"
 ;---- DESKTOP为NSIS的环境变量，会映射到系统桌面
SectionEnd
 
;--------------------------------
;Uninstaller Section
Section "Uninstall" ;---- 这里是控制卸载程序工作的内容
 
 ;ADD YOUR OWN FILES HERE...
	Delete "$INSTDIR\*.*"
	Delete "$INSTDIR\iconengines\*.*"
	Delete "$INSTDIR\imageformats\*.*"
	Delete "$INSTDIR\platforms\*.*"
	Delete "$INSTDIR\printsupport\*.*"
	Delete "$INSTDIR\translations\*.*"
	
	Delete "$SMPROGRAMS\USBDisplayer\*.*"
	Delete "$DESKTOP\USBDisplayer.lnk"
  
	; Remove directories used
	RMDir "$INSTDIR\iconengines"
	RMDir "$INSTDIR\imageformats"
	RMDir "$INSTDIR\platforms"
	RMDir "$INSTDIR\printsupport"
	RMDir "$INSTDIR\translations"
	RMDir "$INSTDIR" 
 
SectionEnd
