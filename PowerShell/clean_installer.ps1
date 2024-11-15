$installerPath = "C:\Windows\Installer"

if (-not (Test-Path -Path $installerPath)) {
    Write-Host "Installer directory not found."
    exit
}

$installerFiles = Get-ChildItem -Path $installerPath -Recurse -Include "*.msi", "*.msp" -ErrorAction SilentlyContinue

foreach ($file in $installerFiles) {
    $isFileInUse = Get-Process | Where-Object { $_.Path -eq $file.FullName }
            
    if ($isFileInUse) {
        Write-Host "File in use: $($file.FullName) - skipping."
    }
    else {
        Write-Host "Deleted: $($file.FullName)"
    }
}

Write-Host "Cleanup complete!"
