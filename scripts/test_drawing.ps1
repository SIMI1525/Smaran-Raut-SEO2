Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap 1200, 630
Write-Host "Bitmap created: $($bmp.Width) x $($bmp.Height)"
$bmp.Dispose()
