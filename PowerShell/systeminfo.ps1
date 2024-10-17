$hostname = $env:COMPUTERNAME
$whoami = $env:USERNAME
$arch = (Get-WmiObject Win32_OperatingSystem).OSArchitecture
$os = (Get-WmiObject -Class Win32_OperatingSystem).Caption + " ($arch)"
$domain = (Get-WmiObject Win32_ComputerSystem).Domain
$IP = (Get-WmiObject -Query "Select IPAddress From Win32_NetworkAdapterConfiguration where IPEnabled = True").IPAddress[0]
$finaldata = "OS: $os ** IP : $IP ** ARCH: $arch ** HOSTNAME: $hostname ** Domain: $domain ** USERNAME: $whoami"
$finaldata
