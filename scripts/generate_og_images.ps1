Add-Type -AssemblyName System.Drawing

$staticImgDir = "C:\Users\BN\.gemini\antigravity\scratch\smaran-raut-seo\images"
$wpImgDir = "C:\Users\BN\Local Sites\smaran-raut\app\public\wp-content\themes\smaran-seo\images"
$logoPath = Join-Path $staticImgDir "logo.png"

function Save-ImageBothDirs($bmp, $filename) {
    $staticOut = Join-Path $staticImgDir $filename
    $wpOut = Join-Path $wpImgDir $filename
    
    # Save with high quality JPEG encoder
    $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters 1
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality, [long]95)
    
    $bmp.Save($staticOut, $jpegCodec, $encoderParams)
    $bmp.Save($wpOut, $jpegCodec, $encoderParams)
    Write-Host "Generated: $filename ($($bmp.Width)x$($bmp.Height))"
}

# Helper to draw a styled social card
function Create-SocialCard($filename, $badgeText, $titleText, $subText, $domainText, $accentColorHex) {
    $bmp = [System.Drawing.Bitmap]::new(1200, 630)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

    # 1. Background Gradient: Deep dark navy (#0B111A to #162032)
    $cTop = [System.Drawing.ColorTranslator]::FromHtml("#0B111A")
    $cBottom = [System.Drawing.ColorTranslator]::FromHtml("#162032")
    $rect = [System.Drawing.Rectangle]::new(0, 0, 1200, 630)
    $bgBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new($rect, $cTop, $cBottom, [single]45.0)
    $g.FillRectangle($bgBrush, $rect)
    $bgBrush.Dispose()

    # 2. Outer Subtle Border
    $borderPen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#1E293B"), [single]2.0)
    $g.DrawRectangle($borderPen, 1, 1, 1198, 628)
    $borderPen.Dispose()

    # 3. Decorative subtle glow line at top (Accent color)
    $accentColor = [System.Drawing.ColorTranslator]::FromHtml($accentColorHex)
    $accentPen = [System.Drawing.Pen]::new($accentColor, [single]5.0)
    $g.DrawLine($accentPen, 0, 0, 1200, 0)
    $accentPen.Dispose()

    # 4. Draw Logo if available
    if (Test-Path $logoPath) {
        $logoBmp = [System.Drawing.Bitmap]::FromFile($logoPath)
        $g.DrawImage($logoBmp, 80, 70, 75, 75)
        $logoBmp.Dispose()
    }

    # 5. Badge Chip
    $fontBadge = [System.Drawing.Font]::new("Segoe UI", [single]13.0, [System.Drawing.FontStyle]::Bold)
    $badgeBrush = [System.Drawing.SolidBrush]::new($accentColor)
    $g.DrawString($badgeText.ToUpper(), $fontBadge, $badgeBrush, [single]175.0, [single]80.0)
    $badgeBrush.Dispose()
    $fontBadge.Dispose()

    # 6. Secondary Header Line
    $fontBrand = [System.Drawing.Font]::new("Segoe UI", [single]14.0, [System.Drawing.FontStyle]::Regular)
    $brandBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#94A3B8"))
    $g.DrawString("SMARAN RAUT · OFFICIAL WEBSITE", $fontBrand, $brandBrush, [single]175.0, [single]108.0)
    $brandBrush.Dispose()
    $fontBrand.Dispose()

    # 7. Big Main Title
    $fontTitle = [System.Drawing.Font]::new("Segoe UI", [single]38.0, [System.Drawing.FontStyle]::Bold)
    $titleBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#FFFFFF"))
    $titleRect = [System.Drawing.RectangleF]::new([single]80.0, [single]190.0, [single]1040.0, [single]170.0)
    $sf = [System.Drawing.StringFormat]::new()
    $sf.LineAlignment = [System.Drawing.StringAlignment]::Near
    $sf.Alignment = [System.Drawing.StringAlignment]::Near
    $g.DrawString($titleText, $fontTitle, $titleBrush, $titleRect, $sf)
    $titleBrush.Dispose()
    $fontTitle.Dispose()

    # 8. Subtitle / Key Features
    $fontSub = [System.Drawing.Font]::new("Segoe UI", [single]19.0, [System.Drawing.FontStyle]::Regular)
    $subBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#CBD5E1"))
    $subRect = [System.Drawing.RectangleF]::new([single]80.0, [single]385.0, [single]1040.0, [single]95.0)
    $g.DrawString($subText, $fontSub, $subBrush, $subRect, $sf)
    $subBrush.Dispose()
    $fontSub.Dispose()

    # 9. Bottom Horizontal Divider
    $divPen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#334155"), [single]1.0)
    $g.DrawLine($divPen, 80, 505, 1120, 505)
    $divPen.Dispose()

    # 10. Bottom Footer: Domain & Geographical Anchor
    $fontFooter = [System.Drawing.Font]::new("Segoe UI", [single]16.0, [System.Drawing.FontStyle]::Bold)
    $footerBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#38BDF8"))
    $g.DrawString($domainText, $fontFooter, $footerBrush, [single]80.0, [single]535.0)
    $footerBrush.Dispose()
    $fontFooter.Dispose()

    $fontLoc = [System.Drawing.Font]::new("Segoe UI", [single]15.0, [System.Drawing.FontStyle]::Regular)
    $locBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#94A3B8"))
    $sfRight = [System.Drawing.StringFormat]::new()
    $sfRight.Alignment = [System.Drawing.StringAlignment]::Far
    $g.DrawString("Itahari, Koshi Province, Nepal", $fontLoc, $locBrush, [single]1120.0, [single]537.0, $sfRight)
    $locBrush.Dispose()
    $fontLoc.Dispose()
    $sfRight.Dispose()
    $sf.Dispose()

    # Save
    Save-ImageBothDirs $bmp $filename
    $g.Dispose()
    $bmp.Dispose()
}

# 1. Homepage & General Branded Card
Create-SocialCard "og-smaran-raut.jpg" `
    "Web Developer & SEO Specialist" `
    "Web Developer & SEO Expert in Nepal" `
    "High-performance business website development, technical search optimization, and verified local ranking strategies." `
    "https://smaranraut.com.np/" `
    "#0D9488"

# 2. Services Hub & Service Pages Card
Create-SocialCard "og-services.jpg" `
    "Professional Digital Services" `
    "SEO & Website Development Services in Nepal" `
    "Technical SEO Audits, Custom Web Engineering, Local Search Optimization & WordPress SEO." `
    "https://smaranraut.com.np/services/" `
    "#38BDF8"

# 3. Geographical / Location Pages Card
Create-SocialCard "og-locations.jpg" `
    "Local Search & Web Development" `
    "SEO Specialist & Web Developer in Nepal" `
    "Dominating local Google Map Pack rankings and organic search in Itahari, Biratnagar, Dharan, and nationwide." `
    "https://smaranraut.com.np/" `
    "#10B981"

# 4. Knowledge Hub & General Blog Guides Card
Create-SocialCard "og-knowledge-hub.jpg" `
    "Knowledge Hub & Technical Guides" `
    "SEO & Web Development Insights for Nepal" `
    "Practical guides on technical audits, algorithmic search rankings, speed optimization, and internal linking." `
    "https://smaranraut.com.np/blog/" `
    "#F59E0B"

# 5. Top SEO Experts in Nepal Dedicated Card (Framed from brightened hero + branded overlay)
$heroSource = Join-Path $staticImgDir "seo-experts-hero.jpg"
if (Test-Path $heroSource) {
    $srcBmp = [System.Drawing.Bitmap]::FromFile($heroSource)
    $bmp5 = [System.Drawing.Bitmap]::new(1200, 630)
    $g5 = [System.Drawing.Graphics]::FromImage($bmp5)
    $g5.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g5.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g5.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    
    # Scale to cover 1200x630
    $scale = [Math]::Max(1200.0 / $srcBmp.Width, 630.0 / $srcBmp.Height)
    $drawW = [int]($srcBmp.Width * $scale)
    $drawH = [int]($srcBmp.Height * $scale)
    $drawX = [int]((1200 - $drawW) / 2)
    $drawY = [int]((630 - $drawH) / 2)
    
    $g5.DrawImage($srcBmp, $drawX, $drawY, $drawW, $drawH)
    $srcBmp.Dispose()
    
    # Apply elegant dark overlay gradient
    $c1 = [System.Drawing.Color]::FromArgb(190, 11, 17, 26)
    $c2 = [System.Drawing.Color]::FromArgb(235, 15, 23, 42)
    $rect5 = [System.Drawing.Rectangle]::new(0, 0, 1200, 630)
    $overlayBrush = [System.Drawing.Drawing2D.LinearGradientBrush]::new($rect5, $c1, $c2, [single]90.0)
    $g5.FillRectangle($overlayBrush, $rect5)
    $overlayBrush.Dispose()
    
    # Border
    $bPen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#1E293B"), [single]2.0)
    $g5.DrawRectangle($bPen, 1, 1, 1198, 628)
    $bPen.Dispose()
    
    # Top Accent line
    $aPen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#10B981"), [single]5.0)
    $g5.DrawLine($aPen, 0, 0, 1200, 0)
    $aPen.Dispose()
    
    # Badge
    $fontBadge5 = [System.Drawing.Font]::new("Segoe UI", [single]13.0, [System.Drawing.FontStyle]::Bold)
    $bBrush5 = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#6EE7B7"))
    $g5.DrawString("EDITORIAL DIRECTORY · 2026 EDITION", $fontBadge5, $bBrush5, [single]80.0, [single]95.0)
    $bBrush5.Dispose()
    $fontBadge5.Dispose()
    
    # Title
    $fontTitle5 = [System.Drawing.Font]::new("Segoe UI", [single]44.0, [System.Drawing.FontStyle]::Bold)
    $tBrush5 = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#FFFFFF"))
    $tRect5 = [System.Drawing.RectangleF]::new([single]80.0, [single]160.0, [single]1040.0, [single]160.0)
    $sf5 = [System.Drawing.StringFormat]::new()
    $g5.DrawString("Top SEO Experts in Nepal", $fontTitle5, $tBrush5, $tRect5, $sf5)
    $tBrush5.Dispose()
    $fontTitle5.Dispose()
    
    # Subtitle
    $fontSub5 = [System.Drawing.Font]::new("Segoe UI", [single]19.0, [System.Drawing.FontStyle]::Regular)
    $sBrush5 = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#E2E8F0"))
    $sRect5 = [System.Drawing.RectangleF]::new([single]80.0, [single]340.0, [single]1040.0, [single]90.0)
    $g5.DrawString("Verified Directory of SEO Specialists, Consultants & Organic Growth Practitioners", $fontSub5, $sBrush5, $sRect5, $sf5)
    $sBrush5.Dispose()
    $fontSub5.Dispose()
    
    # Bottom Divider
    $divPen5 = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml("#475569"), [single]1.0)
    $g5.DrawLine($divPen5, 80, 505, 1120, 505)
    $divPen5.Dispose()
    
    # URL and Author
    $fFont5 = [System.Drawing.Font]::new("Segoe UI", [single]16.0, [System.Drawing.FontStyle]::Bold)
    $fBrush5 = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#38BDF8"))
    $g5.DrawString("https://smaranraut.com.np/blog/top-seo-experts-in-nepal/", $fFont5, $fBrush5, [single]80.0, [single]535.0)
    $fBrush5.Dispose()
    $fFont5.Dispose()
    
    $locFont5 = [System.Drawing.Font]::new("Segoe UI", [single]15.0, [System.Drawing.FontStyle]::Regular)
    $locBrush5 = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml("#94A3B8"))
    $sfRight5 = [System.Drawing.StringFormat]::new()
    $sfRight5.Alignment = [System.Drawing.StringAlignment]::Far
    $g5.DrawString("Researched by Smaran Raut", $locFont5, $locBrush5, [single]1120.0, [single]537.0, $sfRight5)
    $locBrush5.Dispose()
    $locFont5.Dispose()
    $sfRight5.Dispose()
    $sf5.Dispose()
    
    Save-ImageBothDirs $bmp5 "og-seo-experts-nepal.jpg"
    $g5.Dispose()
    $bmp5.Dispose()
}

Write-Host "All 5 dedicated OG images generated successfully!"
