# cURL request

Set `APIFY_API_TOKEN` in your shell, then send the checked-in input to the synchronous Dataset endpoint.

```bash
curl --request POST "https://api.apify.com/v2/acts/datascraperes~instagram-profile-scraper-no-login/run-sync-get-dataset-items?token=$APIFY_API_TOKEN" --header "Content-Type: application/json" --data @data/sample-input.json
```

PowerShell:

```powershell
$headers = @{ Authorization = "Bearer $env:APIFY_API_TOKEN" }
Invoke-RestMethod `
  -Method Post `
  -Uri "https://api.apify.com/v2/acts/datascraperes~instagram-profile-scraper-no-login/run-sync-get-dataset-items" `
  -Headers $headers `
  -ContentType "application/json" `
  -Body (Get-Content .\data\sample-input.json -Raw)
```

The endpoint waits for the Actor to finish and returns default Dataset items. Keep the token in an environment variable and never commit it.

