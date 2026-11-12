$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

$python = Join-Path $env:LOCALAPPDATA 'Python\bin\python.exe'
if (-not (Test-Path $python)) {
    throw "Python was not found at $python"
}

& $python -m pelican content --delete-output-directory --autoreload --listen
exit $LASTEXITCODE
