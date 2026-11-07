@echo off
setlocal
rem Duplo clique: copia o repositorio carteira-dados para C:\Users\<tu>\carteira-dados
rem e cria a tarefa do Windows "Carteira - fichas" (de 15 em 15 minutos).
rem Escreve o que fez em instalar_log.txt, na mesma pasta deste ficheiro.
set LOG=%~dp0instalar_log.txt
set DEST=%USERPROFILE%\carteira-dados
echo Inicio %date% %time% > "%LOG%"

where git >> "%LOG%" 2>&1
if errorlevel 1 goto semgit
where pythonw >> "%LOG%" 2>&1
if errorlevel 1 goto sempython

if exist "%DEST%\.git" goto atualizar
echo A copiar o repositorio para %DEST% ...
echo Se abrir uma janela do GitHub, entra com a tua conta.
git clone https://github.com/hugomiguel1104-stack/carteira-dados.git "%DEST%" >> "%LOG%" 2>&1
if errorlevel 1 goto erroclone
goto tarefa

:atualizar
echo Ja existe %DEST% - a atualizar...
git -C "%DEST%" pull >> "%LOG%" 2>&1

:tarefa
call "%DEST%\tools\instalar_sync.bat" >> "%LOG%" 2>&1
echo --- teste do sync --- >> "%LOG%"
python "%DEST%\tools\sync_fichas.py" --dry-run >> "%LOG%" 2>&1
echo OK >> "%LOG%"
echo.
echo Feito. A tarefa "Carteira - fichas" corre de 15 em 15 minutos.
echo O registo ficou em instalar_log.txt
goto fim

:semgit
echo ERRO: git nao encontrado >> "%LOG%"
echo Nao encontrei o Git. Instala o Git for Windows e volta a correr.
goto fim

:sempython
echo ERRO: pythonw nao encontrado >> "%LOG%"
echo Nao encontrei o Python. Instala o Python 3, com a opcao Add to PATH, e volta a correr.
goto fim

:erroclone
echo ERRO: o clone falhou >> "%LOG%"
echo O clone falhou. Ve o ficheiro instalar_log.txt.
goto fim

:fim
echo.
pause
