$installPath = Read-Host "Enter full installation path (e.g. C:\BurpSuite)"

if (!(Test-Path -Path $installPath)) {
    New-Item -ItemType Directory -Path $installPath -Force | Out-Null
    Write-Host "Created directory: $installPath"
} else {
    Write-Host "Directory already exists."
}

$burpUrl = "https://portswigger.net/burp/releases/download?product=pro&type=Jar"
$javaUrl = "https://download.oracle.com/java/21/archive/jdk-21_windows-x64_bin.exe"
$loaderUrl = "https://github.com/xiv3r/Burpsuite-Professional/raw/refs/heads/main/loader.jar"

$burpJar = Join-Path $installPath "burpsuite_pro.jar"
$javaInstaller = Join-Path $installPath "jdk-21_windows-x64_bin.exe"
$loaderJar = Join-Path $installPath "loader.jar"

Write-Host "Downloading Burp Suite..."
Invoke-WebRequest -Uri $burpUrl -OutFile $burpJar

Write-Host "Downloading Java JDK 21..."
Invoke-WebRequest -Uri $javaUrl -OutFile $javaInstaller

Write-Host "Downloading loader.jar..."
Invoke-WebRequest -Uri $loaderUrl -OutFile $loaderJar

Write-Host "Installing Java..."
Start-Process -FilePath $javaInstaller -ArgumentList "/s" -Wait

Write-Host "Installation completed successfully!"
Write-Host "Files located in: $installPath"