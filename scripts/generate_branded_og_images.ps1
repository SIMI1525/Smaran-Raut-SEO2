Add-Type -AssemblyName System.Drawing

$staticImgDir = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\images"
$wpImgDir = "C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\images"
$artifactDir = "C:\Users\BN\.gemini\antigravity\brain\549e7608-99e6-4503-8a3a-8488d44e74e0"

$logoPath = Join-Path $staticImgDir "logo.png"
$heroPath = Join-Path $staticImgDir "hero-smaran-seo.jpg"
$dirHeroPath = Join-Path $staticImgDir "seo-experts-hero.jpg"

function Save-ImageAllDirs($bmp, $filename) {
    $staticOut = Join-Path $staticImgDir $filename
    $wpOut = Join-Path $wpImgDir $filename
    $artOut = Join-Path $artifactDir $filename
    
    $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters 1
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality, [long]95)
    
    $bmp.Save($staticOut, $jpegCodec, $encoderParams)
    $bmp.Save($wpOut, $jpegCodec, $encoderParams)
    $bmp.Save($artOut, $jpegCodec, $encoderParams)
    Write-Host "Generated: $filename ($($bmp.Width)x$($bmp.Height))"
}

# Helper to create authentic brand card with seamless photo blending and exact brand colors
function Create-BrandedCard($filename, $bgPhotoPath, $badgeText, $titleText, $subText, $domainText, $rightNote) {
    $bmp = [System.Drawing.Bitmap]::new(1200, 630)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

    # 1. Base dark forest tone (#101A14)
    $cBase = [System.Drawing.ColorTranslator]::FromHtml("#101A14")
    $g.Clear($cBase)

    # 2. Draw authentic background photo covering the right half / canvas
    if (Test-Path $bgPhotoPath) {
        $photoBmp = [System.Drawing.Bitmap]::FromFile($bgPhotoPath)
        $scale = [Math]::Max(850.0 / $photoBmp.Width, 630.0 / $photoBmp.Height)
        $pW = [int]($photoBmp.Width * $scale)
        $pH = [int]($photoBmp.Height * $scale)
        $pX = [int](1200 - $pW)
        $pY = [int]((630 - $pH) / 2)
        $g.DrawImage($photoBmp, $pX, $pY, $pW, $pH)
        $photoBmp.Dispose()
    }

    # 3. Apply ONE single seamless horizontal gradient overlay across entire 1200 width!
    # Left (x=0): #0D1611 at 98% opacity
    # Right (x=1200): Primary Color #245037 at 48% opacity
    $cLeft = [System.Drawing.Color]::FromArgb(250, 13, 22, 17)
    $cRight = [System.Drawing.Color]::FromArgb(125, 36, 80, 55) # Primary #245037
    
    $fullRect = [System.Drawing.Rectangle]::new(0, 0, 1200, 630)
    $fullBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new($fullRect, $cLeft, $cRight, [single]0.0)
    $g.FillRectangle($fullBrush, $fullRect)
    $fullBrush.Dispose()

    # 4. Top Accent Line: Dual brand gradient (#245037 to #8F6B38)
    $primaryColor = [System.Drawing.ColorTranslator]::FromHtml("#245037")
    $secondaryColor = [System.Drawing.ColorTranslator]::FromHtml("#8F6B38")
    
    $topLineRect = [System.Drawing.Rectangle]::new(0, 0, 1200, 5)
    $topLineBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new($topLineRect, $primaryColor, $secondaryColor, [single]0.0)
    $topLinePen = [System.Drawing.Pen]::new($topLineBrush, [single]5.0)
    $g.DrawLine($topLinePen, 0, 0, 1200, 0)
    $topLinePen.Dispose()
    $topLineBrush.Dispose()

    # 5. Subtle outer border in warm secondary gold #8F6B38 (translucent)
    $borderPen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(80, 143, 107, 56), [single]2.0)
    $g.DrawRectangle($borderPen, 1, 1, 1198, 628)
    $borderPen.Dispose()

    # 6. Logo at top-left
    if (Test-Path $logoPath) {
        $logoBmp = [System.Drawing.Bitmap]::FromFile($logoPath)
        $g.DrawImage($logoBmp, 75, 60, 80, 80)
        $logoBmp.Dispose()
    }

    # 7. Badge Chip in Primary Color #245037 with Secondary #8F6B38 Gold Border
    $fontBadge = [System.Drawing.Font]::new("Segoe UI", [single]11.0, [System.Drawing.FontStyle]::Bold)
    $badgeTextSize = $g.MeasureString($badgeText.ToUpper(), $fontBadge)
    $badgeW = [int]($badgeTextSize.Width + 28)
    $badgeH = 32
    $badgeRect = [System.Drawing.Rectangle]::new(175, 68, $badgeW, $badgeH)
    
    $badgeBgBrush = [System.Drawing.SolidBrush]::new($primaryColor) # Primary #245037
    $g.FillRectangle($badgeBgBrush, $badgeRect)
    $badgeBgBrush.Dispose()

    $badgeBorderPen = [System.Drawing.Pen]::new($secondaryColor, [single]1.5) # Secondary #8F6B38
    $g.DrawRectangle($badgeBorderPen, $badgeRect)
    $badgeBorderPen.Dispose()

    $badgeTextBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#FAF8F5"))
    $g.DrawString($badgeText.ToUpper(), $fontBadge, $badgeTextBrush, [single]189.0, [single]75.0)
    $badgeTextBrush.Dispose()
    $fontBadge.Dispose()

    # Brand Title: SMARAN RAUT · SEO & WEB DEVELOPMENT
    $fontBrand = [System.Drawing.Font]::new("Segoe UI", [single]12.5, [System.Drawing.FontStyle]::Bold)
    $brandBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#DFB87E")) # Gold
    $g.DrawString("SMARAN RAUT · SEO & WEB DEVELOPMENT", $fontBrand, $brandBrush, [single]175.0, [single]110.0)
    $brandBrush.Dispose()
    $fontBrand.Dispose()

    # 8. Main Heading in warm crisp white (#FAF8F5)
    $fontTitle = [System.Drawing.Font]::new("Segoe UI", [single]40.0, [System.Drawing.FontStyle]::Bold)
    $titleBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#FAF8F5"))
    $titleRect = [System.Drawing.RectangleF]::new([single]75.0, [single]180.0, [single]880.0, [single]175.0)
    $sf = [System.Drawing.StringFormat]::new()
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Near
    $sf.Alignment = [System.Drawing.StringAlignment]::Near
    $g.DrawString($titleText, $fontTitle, $titleBrush, $titleRect, $sf)
    $titleBrush.Dispose()
    $fontTitle.Dispose()

    # 9. Subtitle in soft mint slate (#CBD5CB)
    $fontSub = [System.Drawing.Font]::new("Segoe UI", [single]18.0, [System.Drawing.FontStyle]::Regular)
    $subBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#CBD5CB"))
    $subRect = [System.Drawing.RectangleF]::new([single]75.0, [single]380.0, [single]860.0, [single]95.0)
    $g.DrawString($subText, $fontSub, $subBrush, $subRect, $sf)
    $subBrush.Dispose()
    $fontSub.Dispose()

    # 10. Horizontal divider in subtle secondary gold (#8F6B38)
    $divPen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(90, 143, 107, 56), [single]1.0)
    $g.DrawLine($divPen, 75, 505, 1125, 505)
    $divPen.Dispose()

    # 11. Footer: Domain (Gold highlight #8F6B38) & Location
    $fontFooter = [System.Drawing.Font]::new("Segoe UI", [single]16.0, [System.Drawing.FontStyle]::Bold)
    $footerBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#DFB87E")) # Gold
    $g.DrawString($domainText, $fontFooter, $footerBrush, [single]75.0, [single]535.0)
    $footerBrush.Dispose()
    $fontFooter.Dispose()

    $fontLoc = [System.Drawing.Font]::new("Segoe UI", [single]15.0, [System.Drawing.FontStyle]::Regular)
    $locBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#9FB2A2"))
    $sfRight = [System.Drawing.StringFormat]::new()
    $sfRight.Alignment = [System.Drawing.StringAlignment]::Far
    $g.DrawString($rightNote, $fontLoc, $locBrush, [single]1125.0, [single]537.0, $sfRight)
    $locBrush.Dispose()
    $fontLoc.Dispose()
    $sfRight.Dispose()
    $sf.Dispose()

    Save-ImageAllDirs $bmp $filename
    $g.Dispose()
    $bmp.Dispose()
}

# 1. Homepage & General Brand Card (Uses real hero-smaran-seo.jpg with brand colors #245037 & #8F6B38)
Create-BrandedCard "og-smaran-raut.jpg" `
    $heroPath `
    "Web Developer & SEO Specialist" `
    "Web Developer & SEO Expert in Nepal" `
    "High-performance website development, technical search engine optimization, and verified local ranking strategies." `
    "https://smaranraut.com.np/" `
    "Itahari, Koshi Province, Nepal"

# 2. Services Card (Uses real hero texture with brand colors #245037 & #8F6B38)
Create-BrandedCard "og-services.jpg" `
    $heroPath `
    "Professional Digital Services" `
    "SEO & Website Development Services in Nepal" `
    "Technical SEO Audits, Custom Website Development, Local Search Optimization & WordPress Architecture." `
    "https://smaranraut.com.np/services/" `
    "Itahari · Biratnagar · Nationwide"

# 3. Locations Card (Uses real hero texture with brand colors #245037 & #8F6B38)
Create-BrandedCard "og-locations.jpg" `
    $heroPath `
    "Local Search & Map Pack Rankings" `
    "SEO Specialist & Web Developer in Nepal" `
    "Dominating local Google Map Pack rankings and organic search in Itahari, Biratnagar, Dharan, and across Nepal." `
    "https://smaranraut.com.np/" `
    "Eastern Nepal & Nationwide"

# 4. Knowledge Hub Card (Uses analytics desk monitor from seo-experts-hero.jpg with brand colors #245037 & #8F6B38)
Create-BrandedCard "og-knowledge-hub.jpg" `
    $dirHeroPath `
    "Knowledge Hub & Industry Guides" `
    "SEO & Web Development Insights for Nepal" `
    "Practical guides on technical audits, Google ranking factors, page speed optimization, and search architecture." `
    "https://smaranraut.com.np/blog/" `
    "Researched by Smaran Raut"

# 5. Top SEO Experts in Nepal Dedicated Card (Uses real seo-experts-hero.jpg with brand colors #245037 & #8F6B38)
Create-BrandedCard "og-seo-experts-nepal.jpg" `
    $dirHeroPath `
    "Editorial Industry Directory · 2026" `
    "Top SEO Experts in Nepal" `
    "A verified directory and comparative analysis of search engine optimization practitioners, consultants, and specialists." `
    "https://smaranraut.com.np/blog/top-seo-experts-in-nepal/" `
    "Researched by Smaran Raut"

Write-Host "All 5 authentic brand OG images successfully regenerated with #245037 and #8F6B38!"
