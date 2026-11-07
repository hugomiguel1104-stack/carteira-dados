@echo off
rem Cria (ou recria) a tarefa agendada do Windows "Carteira - fichas", de 15 em 15 minutos.
rem Corre o sync_fichas.py desta pasta com o pythonw (sem abrir janela).
set PASTA=%~dp0
for /f "delims=" %%P in ('where pythonw 2^>nul') do (set PYW=%%P& goto :tem)
echo Nao encontrei o pythonw no PATH. Instala o Python ou indica o caminho completo neste ficheiro.
exit /b 1
:tem
schtasks /create /f /tn "Carteira - fichas" /sc minute /mo 15 /tr "\"%PYW%\" \"%PASTA%sync_fichas.py\""
echo.
echo Tarefa criada. Para ver o que fez: abre %PASTA%sync_fichas.log
