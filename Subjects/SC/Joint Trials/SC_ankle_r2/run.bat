@ECHO OFF
REM SET AppExePath="%ProgramFiles%\AnyBody Technology\AnyBody.6.0\AnyBodyCon.exe"
SET AppExePath="F:\Program Files\AnyBody Technology\AnyBody.6.0\AnyBodyCon.exe"
SET "logfilename=%~n0%_outputlog.txt"
SET "macrofile=%~n0%.anymcr"

::::::::::: AnyBody macro to run :::::::::::::::::::::
(
echo load "Kinematics.main.any"
echo operation Main.JntParameterOptModel.AnatomicalStickFigureValues.Load_AnatomicalParameters
echo run
echo operation Main.Run_Kinematic_Optimization  
echo run
echo exit                                                                           
) > %macrofile%
:::::::::::::::::::::


@ECHO ON
echo %date%, %time% > %logfilename%
%AppExePath% /m %macrofile% |"..\..\..\wtee.exe" -a  %logfilename%
@ECHO OFF

del %macrofile%


