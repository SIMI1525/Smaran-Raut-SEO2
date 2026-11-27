Add-Type -AssemblyName System.Drawing
$c = [System.Drawing.Color]::Red
$p = [System.Drawing.Pen]::new($c, [single]2.0)
$f = [System.Drawing.Font]::new("Segoe UI", [single]14.0, [System.Drawing.FontStyle]::Bold)
Write-Host "Success: Pen width=$($p.Width), Font size=$($f.Size)"
$p.Dispose()
$f.Dispose()
