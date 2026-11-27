Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\images\seo-experts-hero.jpg"
$wpDestPath = "C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\images\seo-experts-hero.jpg"

$bmp = [System.Drawing.Bitmap]::FromFile($srcPath)
$newBmp = [System.Drawing.Bitmap]::new($bmp.Width, $bmp.Height)

$g = [System.Drawing.Graphics]::FromImage($newBmp)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality

# Brightness adjustment matrix: scale RGB by 1.18, preserve alpha
$cm = [System.Drawing.Imaging.ColorMatrix]::new(@(
    @(1.18, 0,    0,    0, 0),
    @(0,    1.18, 0,    0, 0),
    @(0,    0,    1.18, 0, 0),
    @(0,    0,    0,    1, 0),
    @(0.04, 0.04, 0.04, 0, 1)
))

$ia = [System.Drawing.Imaging.ImageAttributes]::new()
$ia.SetColorMatrix($cm, [System.Drawing.Imaging.ColorMatrixFlag]::Default, [System.Drawing.Imaging.ColorAdjustType]::Bitmap)

$rect = [System.Drawing.Rectangle]::new(0, 0, $bmp.Width, $bmp.Height)
$g.DrawImage($bmp, $rect, 0, 0, $bmp.Width, $bmp.Height, [System.Drawing.GraphicsUnit]::Pixel, $ia)

$g.Dispose()
$bmp.Dispose()
$ia.Dispose()

# Save with high quality JPEG
$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
$ep = [System.Drawing.Imaging.EncoderParameters]::new(1)
$ep.Param[0] = [System.Drawing.Imaging.EncoderParameter]::new([System.Drawing.Imaging.Encoder]::Quality, [long]95)

$tempPath = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\images\seo-experts-hero-bright.jpg"
$newBmp.Save($tempPath, $codec, $ep)
$newBmp.Dispose()

Copy-Item -Path $tempPath -Destination $srcPath -Force
Copy-Item -Path $tempPath -Destination $wpDestPath -Force
Remove-Item -Path $tempPath

Write-Host "Brightened hero image saved successfully to both static site and WP theme!"
