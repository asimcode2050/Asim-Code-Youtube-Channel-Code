Write-Host -ForegroundColor Yellow "[+] Internet connectivity Check"
$IntConnStatus = [bool] (Test-Connection www.google.com -Count 1 -ErrorAction SilentlyContinue)
if($IntConnStatus -eq $true){
    Write-Host "Connected to Internet"
}
else{
    Write-Host "Not connected to Internet"
}
