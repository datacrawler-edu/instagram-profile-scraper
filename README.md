# Instagram Profile Scraper

Use this **Instagram profile scraper** to collect structured public profile data from usernames, @handles or Instagram profile URLs. Run it without code in Apify, or integrate it with Python, JavaScript and cURL.

[Open Instagram Profile Scraper on Apify](https://apify.com/datascraperes/instagram-profile-scraper-no-login?fpr=edudata)

## What this repository helps you do

- Scrape public Instagram profile metadata without an Instagram login.
- Extract biographies, follower and following counts, post totals, verification, links, profile images and available account signals.
- Process one profile or batches of up to 10,000 inputs.
- Keep invalid, duplicate, unavailable and failed inputs visible for auditing.
- Export results as JSON, CSV, Excel or JSONL.

The repository contains working API examples, a no-code guide, a complete Dataset item from a real successful run and a reproducible CSV export.

## Example result

The complete verified item is available in [`data/sample-output.json`](data/sample-output.json). A shortened view is shown below:

```json
{
  "success": true,
  "status": "ok",
  "input": "nasa",
  "username": "nasa",
  "profileUrl": "https://www.instagram.com/nasa/",
  "duplicateOf": null,
  "profile": {
    "fullName": "NASA",
    "biography": "Making the seemingly impossible, possible. ✨",
    "followersCount": 104429166,
    "followsCount": 92,
    "postsCount": 4888,
    "isVerified": true,
    "isPrivate": false,
    "externalUrl": "https://www.nasa.gov"
  }
}
```

The values are point-in-time public observations. Counts and media URLs can change after collection.

## Run without code

1. Open [Instagram Profile Scraper on Apify](https://apify.com/datascraperes/instagram-profile-scraper-no-login?fpr=edudata).
2. Add usernames, @handles or complete public profile URLs in **Instagram profiles**.
3. Click **Start**.
4. Open the **Dataset** tab when the run succeeds.
5. Review `success`, `status`, `profile` and `error`.
6. Export the results in your preferred format.

See the [no-code guide](docs/no-code-guide.md) for a complete walkthrough.

## Try it with Apify's free plan

Apify's Free plan currently includes $5 in monthly prepaid usage and does not require a credit card to start. It can cover a small test while credit remains; it is not unlimited free usage. Unused credits expire at the end of the billing cycle.

Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) before running a large batch.

## Quick start for developers

### Python

Install the client:

```bash
pip install -r examples/python/requirements.txt
```

Set your Apify API token:

```bash
export APIFY_API_TOKEN="your-token"
```

On Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

Run the example:

```bash
python examples/python/instagram_profile_scraper.py
```

## Input example

```json
{
  "profiles": [
    "nasa"
  ]
}
```

`profiles` is required and accepts 1–10,000 strings. Supported forms include `nasa`, `@nasa` and `https://www.instagram.com/nasa/`. Inputs are normalized by username. Duplicates are reported but are not fetched or charged twice.

Read the [input reference](docs/input-reference.md) for validation details.

## Request examples

- [cURL and PowerShell](examples/curl-request.md)
- [Python minimal example](examples/python/instagram_profile_scraper.py)
- [Python batch example](examples/python/batch_instagram_profiles.py)
- [JavaScript example](examples/javascript/request.mjs)
- [Local JSON-to-CSV exporter](examples/python/export_instagram_profiles_csv.py)

All request examples call the hosted Actor. They do not require the private Actor source, Instagram cookies or Instagram credentials.

## Output fields

Every submitted value that can be written within the spending limit receives an auditable Dataset row.

| Field | Meaning |
| --- | --- |
| `success` | Whether public profile data was returned successfully. |
| `status` | `ok`, `private`, `invalid_input`, `duplicate`, `not_found` or `failed`. |
| `input` | Original submitted value. |
| `username` | Normalized Instagram username when available. |
| `profileUrl` | Normalized Instagram profile URL when available. |
| `duplicateOf` | First equivalent input when this row is a duplicate. |
| `profile` | Public profile fields for successful rows, otherwise `null`. |
| `error` | Structured error information for unsuccessful rows, otherwise `null`. |
| `scrapedAt` | UTC collection timestamp. |

The successful `profile` object can include identity, biography, counts, privacy and verification flags, account type, category, website, bio links, profile images, pronouns, location and data-quality information. See the [output reference](docs/output-reference.md).

## Common use cases

- Creator and influencer research.
- Brand and competitor monitoring.
- Public lead-list enrichment.
- Audience-size and verification analysis.
- Website and bio-link discovery.
- Periodic snapshots of public account metrics.

See [use cases](docs/use-cases.md) for practical input and interpretation guidance.

## Scrape Instagram profiles with Python

Use [`instagram_profile_scraper.py`](examples/python/instagram_profile_scraper.py) for the checked-in input or [`batch_instagram_profiles.py`](examples/python/batch_instagram_profiles.py) for repeated command-line profiles:

```bash
python examples/python/batch_instagram_profiles.py --profile nasa --profile natgeo
```

Each profile is processed independently. Inspect `status` instead of assuming that every input returned profile data.

## Export Instagram profile data to CSV

Apify can export the Dataset directly. For a saved JSON response, run:

```bash
python examples/python/export_instagram_profiles_csv.py data/sample-output.json data/exported-instagram-profiles.csv
```

The exporter flattens useful profile fields while serializing nested links, pronouns, location, quality and error values as JSON.

## Instagram profile data API example

Use the synchronous cURL example for a direct response, or the official Apify clients when you need run metadata, scheduling or Dataset pagination. The complete nested response remains in [`data/sample-output.json`](data/sample-output.json).

## FAQ

Read [`docs/faq.md`](docs/faq.md) for billing, private profiles, duplicate handling, missing business fields and expiring image URLs.

## Limits and pricing

The verified price is **$0.001 per successfully delivered `profile-result`**, equal to **$1 per 1,000 successful public profiles**. Invalid, duplicate, nonexistent or failed inputs do not create that event. A private account whose public profile metadata is returned successfully is delivered with `status: "private"` and is chargeable.

A run accepts up to 10,000 inputs. Instagram exposes different optional fields for different accounts, so missing values can be `null` or empty. Platform storage, transfer or other account-level usage costs may apply.

## Hosted version

The hosted Actor provides web execution, API calls, schedules, webhooks and managed Dataset storage:

[Open Instagram Profile Scraper on Apify](https://apify.com/datascraperes/instagram-profile-scraper-no-login?fpr=edudata)

## Responsible use

Collect only publicly accessible information for a lawful purpose. Respect Instagram's terms, privacy and data-protection laws, intellectual-property rights and applicable retention requirements. Do not use profile data for spam, harassment, discrimination or unlawful profiling.

Never commit API tokens, cookies, proxy URLs or credentials to this repository.

## Support

For documentation or example problems, [open a GitHub issue](https://github.com/datacrawler-edu/instagram-profile-scraper/issues). For Actor execution problems, include the Apify run ID and a small sanitized input, but never include a token or credential.

## License

Released under the MIT License.
