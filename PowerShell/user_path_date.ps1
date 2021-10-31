$UserName = [System.Environment]::UserName
$CurrentPath = pwd | Select-Object | %{$_.ProviderPath}
$TheDate = Get-Date
Write-Host "User Name: " $UserName
Write-Host "Current Path: " $CurrentPath
Write-Host "Date : " $TheDate
