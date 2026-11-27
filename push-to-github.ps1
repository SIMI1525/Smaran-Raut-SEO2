# High-Performance GitHub Push Script using GitHub CLI API
param(
    [string]$Repo = "SIMI1525/Smaran-Raut-SEO2",
    [string]$Branch = "main",
    [string]$CommitMessage = "Optimize written content across homepage, geographical landing pages, and service hub"
)

$ErrorActionPreference = "Stop"
$gh = "C:\Program Files\GitHub CLI\gh.exe"
$localDir = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo"

Write-Host "Connecting to GitHub: $Repo ($Branch)..." -ForegroundColor Cyan

# 1. Get latest commit & base tree
$refJson = & $gh api "repos/$Repo/git/ref/heads/$Branch" | ConvertFrom-Json
$latestCommitSha = $refJson.object.sha
$commitJson = & $gh api "repos/$Repo/git/commits/$latestCommitSha" | ConvertFrom-Json
$baseTreeSha = $commitJson.tree.sha

Write-Host "Parent Commit SHA: $latestCommitSha"
Write-Host "Base Tree SHA:     $baseTreeSha"

# 2. Fetch remote tree
$remoteTreeJson = & $gh api --method GET "repos/$Repo/git/trees/$baseTreeSha" -f "recursive=1" | ConvertFrom-Json
$remoteBlobs = @{}
foreach ($item in $remoteTreeJson.tree) {
    if ($item.type -eq "blob") {
        $remoteBlobs[$item.path] = $item.sha
    }
}

# 3. Detect modified & new files
$sha1 = [System.Security.Cryptography.SHA1]::Create()
$files = Get-ChildItem -Path $localDir -Recurse -File | Where-Object {
    $_.FullName -notmatch '\\\.git' -and
    $_.FullName -notmatch '\\scripts' -and
    $_.Name -ne 'test.json' -and
    $_.Name -ne 'test.txt' -and
    $_.Extension -ne '.bak' -and
    $_.Name -ne 'push-to-github.ps1'
}

$changedFiles = @()
foreach ($file in $files) {
    $relPath = $file.FullName.Substring($localDir.Length + 1).Replace('\', '/')
    $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
    $header = [System.Text.Encoding]::ASCII.GetBytes("blob $($bytes.Length)`0")
    $full = New-Object byte[] ($header.Length + $bytes.Length)
    [System.Buffer]::BlockCopy($header, 0, $full, 0, $header.Length)
    [System.Buffer]::BlockCopy($bytes, 0, $full, $header.Length, $bytes.Length)
    $localSha = ($sha1.ComputeHash($full) | ForEach-Object { $_.ToString("x2") }) -join ""

    if (-not $remoteBlobs.ContainsKey($relPath) -or $remoteBlobs[$relPath] -ne $localSha) {
        $changedFiles += [PSCustomObject]@{
            Path = $relPath
            Bytes = $bytes
            LocalSha = $localSha
            RemoteSha = $remoteBlobs[$relPath]
        }
    }
}

Write-Host "Found $($changedFiles.Count) changed/new files to upload." -ForegroundColor Yellow

# 4. Upload blobs for changed files using stdin (avoids command-line length limit & BOM)
$treeItems = @()
$count = 0
foreach ($item in $changedFiles) {
    $count++
    $b64 = [Convert]::ToBase64String($item.Bytes)
    $blobPayload = @{
        content  = $b64
        encoding = "base64"
    } | ConvertTo-Json -Compress

    $blobRes = $blobPayload | & $gh api "repos/$Repo/git/blobs" --input - | ConvertFrom-Json
    $treeItems += @{
        path = $item.Path
        mode = "100644"
        type = "blob"
        sha  = $blobRes.sha
    }
    Write-Host "[$count/$($changedFiles.Count)] Uploaded blob for: $($item.Path)" -ForegroundColor DarkGray
}

# 5. Create new Git Tree with base_tree
Write-Host "Creating Git Tree on GitHub..." -ForegroundColor Cyan
$treePayload = @{
    base_tree = $baseTreeSha
    tree      = $treeItems
} | ConvertTo-Json -Depth 10

$newTreeRes = $treePayload | & $gh api "repos/$Repo/git/trees" --input - | ConvertFrom-Json
$newTreeSha = $newTreeRes.sha
Write-Host "New Tree SHA: $newTreeSha" -ForegroundColor Green

# 6. Create Commit
Write-Host "Creating Commit..." -ForegroundColor Cyan
$commitPayload = @{
    message = $CommitMessage
    tree    = $newTreeSha
    parents = @($latestCommitSha)
} | ConvertTo-Json -Depth 10

$newCommitRes = $commitPayload | & $gh api "repos/$Repo/git/commits" --input - | ConvertFrom-Json
$newCommitSha = $newCommitRes.sha
Write-Host "New Commit SHA: $newCommitSha" -ForegroundColor Green

# 7. Update branch reference
Write-Host "Updating branch reference $Branch..." -ForegroundColor Cyan
$patchPayload = @{
    sha   = $newCommitSha
    force = $false
} | ConvertTo-Json -Compress

$patchPayload | & $gh api -X PATCH "repos/$Repo/git/refs/heads/$Branch" --input - | Out-Null

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "SUCCESSFULLY PUSHED ALL CHANGES TO GITHUB!" -ForegroundColor Green
Write-Host "Commit: https://github.com/$Repo/commit/$newCommitSha" -ForegroundColor Green
Write-Host "Repo:   https://github.com/$Repo" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
