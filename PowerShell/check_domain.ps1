Write-Host -ForegroundColor Red "[+] Checking if the computer is in domain or workgroup"
$DomainStatus = systeminfo | findstr /b "Domain"
if($domainStatus -match "WORKGROUP"){
    Write-Host "Domain: WORKGROUP"
}
else{
    Write-Host "Domain: Part of a domain"
}
