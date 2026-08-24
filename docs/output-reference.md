# Output reference

The default Dataset contains one auditable row for each submitted value that can be written within the run spending limit.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `success` | Boolean | Yes | `true` when public profile metadata was returned. |
| `status` | String | Yes | Result classification. |
| `input` | String | Yes | Original submitted value. |
| `username` | String or null | Yes | Normalized username when available. |
| `profileUrl` | String or null | Yes | Canonical public profile URL when available. |
| `duplicateOf` | String or null | Yes | First equivalent input for duplicate rows. |
| `scrapedAt` | String | Yes | UTC timestamp for the observation. |
| `attempts` | Integer | Yes | Collection attempts used for the row. |
| `responseTimeMs` | Integer | Yes | End-to-end response time in milliseconds. |
| `httpRequests` | Integer | Yes | HTTP requests used for this input. |
| `responseBytes` | Integer | Yes | Response bytes processed for this input. |
| `backoffTimeMs` | Integer | Yes | Retry backoff time. |
| `throttleWaitTimeMs` | Integer | Yes | Adaptive throttle wait time. |
| `error` | Object or null | Yes | Stable error code and message when unsuccessful. |
| `profile` | Object or null | Yes | Public profile data when successful. |

## Status values

| Status | Meaning |
| --- | --- |
| `ok` | A public, non-private profile was returned. |
| `private` | Public metadata for a private account was returned. |
| `invalid_input` | The submitted value was not a supported profile identifier. |
| `duplicate` | An equivalent username already appeared in the same input. |
| `not_found` | No public profile was available for the normalized username. |
| `failed` | Collection did not succeed after the allowed attempts. |

## Profile object

A successful `profile` can include:

- `id`, `username`, `fullName` and `biography`;
- `followersCount`, `followsCount` and `postsCount`;
- `isVerified`, `isPrivate`, `isBusinessAccount` and `isProfessionalAccount`;
- `accountType`, `accountTypeName` and `category`;
- `externalUrl` and `bioLinks`;
- `profilePicUrl` and `profilePicUrlHD`;
- `pronouns`, `location` and `dataQuality`.

Optional fields vary by account and collection time. Missing data remains `null` or empty; the Actor does not infer it.

## Complete example

[`data/sample-output.json`](../data/sample-output.json) contains every customer-visible field and nested value from one real successful run. [`data/sample-output.csv`](../data/sample-output.csv) is a reproducible flattened view.

