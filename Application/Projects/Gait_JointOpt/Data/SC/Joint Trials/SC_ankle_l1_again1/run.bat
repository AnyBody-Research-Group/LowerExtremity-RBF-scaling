
SET AppExePath="%ProgramFiles(x86)%\AnyBody Technology\AnyBody.5.1\AnyBodyCon.exe"
IF NOT EXIST %AppExePath% SET AppExePath="%ProgramFiles%\AnyBody Technology\AnyBody.5.0\AnyBodyCon.exe"
%AppExePath% /m ConExe.anymcr
exit
