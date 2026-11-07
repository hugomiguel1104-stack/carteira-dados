@echo off
rem Duplo clique: copia o repositorio carteira-dados para C:\Users\<tu>\carteira-dados
rem e cria a tarefa do Windows "Carteira - fichas" (de 15 em 15 minutos).
rem Pode ser corrido outra vez sem estragar nada.
chcp 65001 >nul
set DEST=%USERPROFILE%\carteira-dados
where git >nul 2>nul || (echo Nao encontrei o Git. Instala o "Git for Windows" e volta a correr. & pause & exit /b 1)
where pythonw >nul 2>nul || (echo Nao encontrei o Python. Instala o Python 3 (marca "Add to PATH") e volta a correr. & pause & exit /b 1)
if exist "%DEST%\.git" (
  echo Ja existe %DEST% - a atualizar...
  git -C "%DEST%" pull -q
) else (
  echo A copiar o repositorio para %DEST% ...
  echo Se abrir uma janela do GitHub, entra com a tua conta.
  git clone https://github.com/hugomiguel1104-stack/carteira-dados.git "%DEST%" || (echo O clone falhou. & pause & exit /b 1)
)
call "%DEST%\tools\instalar_sync.bat"
echo.
echo A fazer um teste (so mostra o que copiaria, sem enviar nada):
python "%DEST%\tools\sync_fichas.py" --dry-run
echo.
echo Feito. A tarefa "Carteira - fichas" corre de 15 em 15 minutos.
pause
