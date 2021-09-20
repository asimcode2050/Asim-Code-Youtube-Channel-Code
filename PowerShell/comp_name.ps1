Write-Host -ForegroundColor Green "[+] Collecting Computer Name"
if(Test-Path -Path HKLM:"\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName"){
    $Computer_Name = Get-ItemPropertyValue HKLM:"\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" -Name "ComputerName"
    Write-Host $Computer_Name
}
else{
    Write-Host -ForegroundColor Red "[-] Could not find the Computer Name"
}
