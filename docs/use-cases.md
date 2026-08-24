# Use cases

Instagram Profile Scraper is designed for workflows that begin with known public Instagram usernames or profile URLs.

## Creator research

Collect biography, follower counts, post totals, verification, category and public links for a reviewed list of creators.

```json
{
  "profiles": [
    "nasa",
    "natgeo"
  ]
}
```

Use `scrapedAt` because counts are point-in-time observations.

## Brand and competitor monitoring

Save periodic snapshots of `followersCount`, `followsCount` and `postsCount`. Compare only equivalent collection periods and retain the original status so unavailable accounts are not treated as zero.

## Public lead enrichment

Use `biography`, `category`, `externalUrl` and `bioLinks` when those fields are publicly exposed. Retain only data needed for a documented purpose and do not use the results for unsolicited bulk messaging.

## Link discovery

Read `externalUrl` and the structured `bioLinks` array. A missing link means Instagram did not expose one at collection time; it should not be inferred from another source.

## Auditable batches

Every row preserves `input`, normalized `username`, `status`, `duplicateOf`, `error` and `scrapedAt`. Retry `failed` rows later while leaving invalid, duplicate and not-found inputs visible in the audit trail.

