# 一条命令推送（Windows PowerShell）
# 用法：
#   powershell -ExecutionPolicy Bypass -File scripts\push.ps1 -User yourname
#   powershell -ExecutionPolicy Bypass -File scripts\push.ps1 -User yourname -Repo rfid-nfc-toolkit -Message "feat: initial release"

param(
    [Parameter(Mandatory = $true)][string]$User,
    [string]$Repo = "rfid-nfc-toolkit",
    [string]$Message = "feat: initial release of rfid-nfc-toolkit",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "[1/5] 替换占位用户名 ..." -ForegroundColor Cyan
Get-ChildItem -Recurse -File -Include *.md,*.toml,*.yml,*.json,*.py |
    ForEach-Object {
        $c = Get-Content $_.FullName -Raw
        if ($c -match 'WilliamChen55') {
            ($c -replace 'WilliamChen55', $User) | Set-Content $_.FullName -NoNewline
        }
    }

Write-Host "[2/5] 初始化仓库 ..." -ForegroundColor Cyan
if (-not (Test-Path ".git")) {
    git init -b $Branch | Out-Null
}

Write-Host "[3/5] 提交 ..." -ForegroundColor Cyan
git add -A
git commit -m $Message

Write-Host "[4/5] 设置远程 ..." -ForegroundColor Cyan
$url = "https://github.com/$User/$Repo.git"
$existing = git remote 2>$null
if ($existing -contains "origin") { git remote remove origin }
git remote add origin $url

Write-Host "[5/5] 推送 ..." -ForegroundColor Cyan
git push -u origin $Branch

Write-Host ""
Write-Host "完成：$url" -ForegroundColor Green
Write-Host "接下来去网页端补：Description、Topics、Pages(/docs)、v0.1.0 Release、Pin。" -ForegroundColor Yellow
