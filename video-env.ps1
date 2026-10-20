# Load with: . .\video-env.ps1
$videoTools = Join-Path $env:USERPROFILE '.codex-video-tools'
$videoMetadata = Get-Content -LiteralPath (Join-Path $videoTools 'installation.json') -Raw | ConvertFrom-Json
$videoOtherPaths = @($env:Path -split ';' | Where-Object { $_ -and $_ -notin $videoMetadata.paths })
$env:Path = (@($videoMetadata.paths) + $videoOtherPaths) -join ';'
$env:PYTHONUTF8 = '1'
$videoChrome = Join-Path $PSScriptRoot 'shotcraft-demo\node_modules\.remotion\chrome-headless-shell\win64\chrome-headless-shell-win64\chrome-headless-shell.exe'
if (Test-Path -LiteralPath $videoChrome) { $env:PUPPETEER_EXECUTABLE_PATH = $videoChrome }
Write-Output 'Ambiente de video ativo: node, npm, npx, ffmpeg, ffprobe, python e uv.'
