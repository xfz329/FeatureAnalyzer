;NSIS Modern User Interface
;Header Bitmap Example Script
;Written by Joost Verburg
 
;--------------------------------
;Include Modern UI
 
  !include "MUI2.nsh"
 
;--------------------------------
;General
 
  ;Name and file
  Name "USBDisplay"                                                         ;---- ������
  OutFile "USBDisplaySetup.exe"                                             ;---- ���ɵ�Ŀ���ļ���
 
  ;Default installation folder
  InstallDir "$PROGRAMFILES\USBDisplayer" 
 ;---- ��װ��Ŀ���ļ������ƣ�����Ҫ��ǰ׺�ĳ�$ProgramFiles����Ȼ��װ������·�������õ���64bitƽ̨��Ŀ��Ŀ¼������
 ;---- $PROGRAMFILE��NSIS�Ļ������������Զ�ӳ�䵽C:\Program Files��64ƽ̨��C:\Program Files (x86)Ŀ¼��
  
  ;Request application privileges for Windows Vista
  RequestExecutionLevel admin
 
;--------------------------------
;Interface Configuration
 
  !define MUI_HEADERIMAGE
  !define MUI_HEADERIMAGE_BITMAP "win.bmp" ; optional    ---- ������õ���ͼƬ�ļ����������ɵ�Setup.exe�ļ����ͼ��
  !define MUI_ABORTWARNING
 
;--------------------------------
;Pages
 
  !insertmacro MUI_PAGE_LICENSE "License.txt"    ;---- ������õ���License�ļ������Թ����ã���������
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
 
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
 
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "SimpChinese"    ;---- ���԰汾��û̫�о��������ǿ��ư�װ����װ�����е���ʾ����Ϊ����
  
;--------------------------------
;Installer Sections
 
Section "Application and Help(required)" SecDummy    ;---- ��װ�ĵ�һ�������ݣ���Section�����֣�����������ǳ��������
 
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
	WriteUninstaller "$INSTDIR\Uninstall.exe"     ;---- ����������ж�س���
 
SectionEnd
 
;--------------------------------
;Descriptions
 
  ;Language strings
  LangString DESC_SecDummy ${LANG_ENGLISH} "Application and Help(required)"    ;---- �������������ã�û��̫�о�
 
  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDummy} $(DESC_SecDummy)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
;--------------------------------
; Optional section (can be disabled by the user)
Section "StartMenu ShortCuts"    ;---- ��װ�ĵڶ����֣�ͬ����Section�����֣��������������ӡ���ʼ�˵����Ĳ˵���
 
  CreateDirectory "$SMPROGRAMS\USBDisplayer"    ;---- ��ʼ�˵��а�װ��Ŀ¼
  CreateShortCut "$SMPROGRAMS\USBDisplayer\USBDisplayer.lnk" "$INSTDIR\USBDisplayer.exe" "" "$INSTDIR\label.ico"     ;---- Ŀ¼�еĿ��ѡ��
  CreateShortCut "$SMPROGRAMS\USBDisplayer\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
 
SectionEnd
 
;--------------------------------
; Optional section (can be disabled by the user)
Section "Desktop ShortCuts"    ;---- ��װ�ĵ������֣�ͬ����Section�����֣��������������ӡ����桱�Ŀ�ݷ�ʽ
 
  CreateShortCut "$DESKTOP\USBDisplayer.lnk" "$INSTDIR\USBDisplayer.exe" "" "$INSTDIR\label.ico"
 ;---- DESKTOPΪNSIS�Ļ�����������ӳ�䵽ϵͳ����
SectionEnd
 
;--------------------------------
;Uninstaller Section
Section "Uninstall" ;---- �����ǿ���ж�س�����������
 
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
