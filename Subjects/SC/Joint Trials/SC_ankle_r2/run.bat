
SET AppExePath="%ProgramFiles(x86)%\AnyBody Technology\AnyBody.5.3\AnyBodyCon.exe"
IF NOT EXIST %AppExePath% SET AppExePath="%ProgramFiles%\AnyBody Technology\AnyBody.5.3\AnyBodyCon.exe"
echo %date%, %time% > outputlog.txt
%AppExePath% /m ConExe.anymcr |"..\..\..\wtee.exe" -a outputlog.txt
exit
