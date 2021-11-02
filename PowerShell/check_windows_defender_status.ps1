Write-Host -ForegroundColor Yellow "[+] Checking Windows Defender Status"
$WindowsDStatus = Get-MpComputerStatus
$AVStatus = '{0}' -f $WindowsDStatus.AntivirusEnabled
Write-Host "Anti Virus Enabled:  $AVStatus"
$RealTimeProtection = '{0}' -f $WindowsDStatus.RealTimeProtectionEnabled

if($RealTimeProtection -eq $true){
    Write-Host "Real-Time Protection : Enabled"
}
else{
    Write-Host "Real-Time Protection: Disabled"
}
