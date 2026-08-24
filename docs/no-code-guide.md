# Run Instagram Profile Scraper without code

Use Apify's web interface to scrape public Instagram profile metadata without Python, an Instagram login or cookies.

## Step by step

1. Open [Instagram Profile Scraper on Apify](https://apify.com/datascraperes/instagram-profile-scraper-no-login?fpr=edudata).
2. Select the **Input** tab.
3. Add a username, @handle or complete profile URL under **Instagram profiles**.
4. Click **Start**.
5. Open the **Dataset** tab after the run succeeds.
6. Check `success` and `status` before using `profile`.
7. Export JSON, CSV, Excel or JSONL.

## First test

Use a single known public account to keep the first run small:

```json
{
  "profiles": [
    "nasa"
  ]
}
```

The checked-in [sample input](../data/sample-input.json) uses this exact request.

## Interpret the result

- `ok` means public profile data was returned.
- `private` means the account is private but its public profile metadata was returned.
- `invalid_input` means the value was not a supported username, handle or profile URL.
- `duplicate` means an equivalent profile already appeared in the run.
- `not_found` means no public profile was available.
- `failed` identifies a temporary or exhausted collection failure.

Counts are snapshots. Profile image URLs can expire, and optional business fields may be absent.

## Cost control

The Actor charges $0.001 for each successfully delivered `profile-result`. Start with one profile, inspect the row, then increase the batch. Invalid, duplicate, nonexistent and failed inputs do not create the event.

Apify's Free plan currently includes $5 in monthly prepaid usage. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) for account-level terms.

