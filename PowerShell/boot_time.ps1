Write-Host -ForegroundColor Yellow "[+] Getting the last boot up time"
$BootUpTime = Get-CimInstance -Class CIM_OperatingSystem | Select-Object LastBootUpTime
Write-Host $BootUpTime
