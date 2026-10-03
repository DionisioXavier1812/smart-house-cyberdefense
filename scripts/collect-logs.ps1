Get-EventLog -LogName Security -Newest 200 | Export-Csv security_logs.csv
Get-Content "C:\iot\camera\auth.log" | Out-File camera_auth.log
Get-Content "C:\iot\smartlock\events.log" | Out-File smartlock_events.log
