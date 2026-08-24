# FAQ

## Can I use the Instagram profile scraper without code?

Yes. Open [Instagram Profile Scraper on Apify](https://apify.com/datascraperes/instagram-profile-scraper-no-login?fpr=edudata), add profiles, click **Start** and inspect the Dataset. Follow the [no-code guide](no-code-guide.md).

## Do I need an Instagram login or cookies?

No. The Actor works with publicly exposed profile data and does not ask for Instagram credentials or cookies.

## What input formats are supported?

Use usernames such as `nasa`, handles such as `@nasa` or complete URLs such as `https://www.instagram.com/nasa/`. The required `profiles` array accepts up to 10,000 values.

## Are duplicate profiles charged twice?

No. Equivalent usernames are fetched once. Later equivalents receive `status: "duplicate"` and do not create a `profile-result` charge.

## Are private profiles supported?

The Actor can return the public metadata Instagram exposes for a private account. Such a successful item has `status: "private"`; it does not access private posts or bypass privacy controls.

## Why is a business field missing?

Instagram did not expose that optional value for the account at collection time. Optional fields can be `null` or empty and are not guessed.

## How much does it cost?

The verified price is $0.001 per successfully delivered profile, or $1 per 1,000 successful profiles. Invalid, duplicate, nonexistent and failed inputs are not charged.

## Can I export the results to CSV?

Yes. Export the Dataset from Apify or run [`export_instagram_profiles_csv.py`](../examples/python/export_instagram_profiles_csv.py) against saved JSON output.

## Why did a profile image URL stop working?

Instagram-hosted profile image URLs can expire. Download permitted images promptly if your lawful workflow requires durable storage.

