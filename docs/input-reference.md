# Input reference

Instagram Profile Scraper accepts one required field.

| Field | Type | Required | Limits | Description |
| --- | --- | :---: | --- | --- |
| `profiles` | Array of strings | Yes | 1–10,000 items | Instagram usernames, @handles or complete public profile URLs. |

## Accepted forms

These values identify the same profile:

```text
nasa
@nasa
https://www.instagram.com/nasa/
```

Whitespace is removed and usernames are normalized. A valid Instagram profile URL must use an Instagram host and a profile path.

## Deduplication

Equivalent usernames are fetched once. The first input can return `ok` or `private`; later equivalents receive `status: "duplicate"` and `duplicateOf` points to the first submitted value. Duplicate rows are not charged.

## Invalid and unavailable inputs

Invalid values receive `status: "invalid_input"` without a network request. A username that does not expose a profile can receive `not_found`. Temporary collection failures receive `failed` and structured `error` information.

The Actor does not accept credentials, cookies, hashtags, post URLs or search queries.

