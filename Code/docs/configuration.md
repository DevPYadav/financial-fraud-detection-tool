# Configuration

How the PoC is configured in each environment, and how secrets are kept out of the repository.

## Environments

| Environment | Where it runs | Where settings come from |
| --- | --- | --- |
| `local` | A developer's machine | `Code/.env` (copied from `Code/config/example.env`) and the shell environment |
| `test` | `uv run pytest`, locally or in CI | Nothing is required. Tests set what they need and use fakes for AWS and the network |
| `aws` | TEKMentors' AWS account | Non-secret settings come from environment variables on the running service. Secrets come from AWS Secrets Manager |

The `FFD_ENV` setting says which environment is running.

## Settings

Every setting is an environment variable. "Needed in" lists the environments where the app stops if the setting is missing. Secrets are marked **secret**.

| Name | Purpose | Example value | Needed in |
| --- | --- | --- | --- |
| `FFD_ENV` | Which environment is running: `local`, `test` or `aws` | `local` | local, aws |
| `LOG_LEVEL` | Logging level | `INFO` | optional (default `INFO`) |
| `DATABASE_URL` | PostgreSQL (with pgvector) connection string. **secret** because it includes the password | `postgresql+psycopg://ffd:change-me@localhost:5432/ffd` | local, aws |
| `AWS_REGION` | AWS region for S3, Textract and Bedrock | `ap-south-1` | local, aws |
| `AWS_PROFILE` | Named AWS CLI profile for local access to AWS. Not used in AWS, where the service role is used | `ffd-dev` | optional (local only) |
| `S3_BUCKET` | Bucket for permitted PoC artifacts (#20) | `ffd-poc-artifacts-example` | local, aws |
| `S3_TEXTRACT_PREFIX` | Key prefix for temporary PDF copies sent to Textract. These are deleted after processing | `textract-input/` | local, aws |
| `TEXTRACT_FEATURES` | Textract analysis features, comma-separated | `TABLES,FORMS` | local, aws |
| `BEDROCK_MODEL_ID` | Bedrock text model used for approved AI tasks (#60) | `example.text-model-id` | local, aws |
| `BEDROCK_EMBEDDING_MODEL_ID` | Bedrock embedding model for pgvector search | `example.embedding-model-id` | local, aws |
| `NSE_BASE_URL` | Base URL for NSE public filings | `https://www.nseindia.com` | local, aws |
| `BSE_BASE_URL` | Base URL for BSE public filings | `https://www.bseindia.com` | local, aws |
| `NEWS_SOURCES_FILE` | Path to the approved news publication list (#9) | `config/news-sources.yaml` | local, aws |
| `HTTP_USER_AGENT` | User-Agent sent to public sources so the client can be identified | `ffd-poc/0.1 (contact@example.com)` | local, aws |
| `HTTP_REQUEST_DELAY_SECONDS` | Minimum delay between requests to the same site | `2` | optional (default `2`) |
| `APP_USERNAME` | Username for the shared PoC login (#58) | `analyst` | local, aws |
| `APP_PASSWORD_HASH` | Hash of the shared PoC password (#58). Never store the plain password. **secret** | `replace-with-password-hash` | local, aws |

Tasks that add a setting must add it to this table and to `Code/config/example.env` in the same change.

## Secrets

- **Local:** secrets come from environment variables, normally loaded from `Code/.env`. That file is git-ignored and must never be committed. AWS credentials come from the AWS CLI (`aws configure` or `aws sso login`) through `AWS_PROFILE`, never from `.env`.
- **AWS:** secrets are stored in AWS Secrets Manager and passed to the service at start-up. AWS access uses the service's IAM role, so no access keys are configured.
- **Tests:** no secrets and no AWS access. Tests use fake clients and local or in-memory data (see `testing-guidelines.md`).
- No real credential, password, password hash or access key may appear in any tracked file, including examples and docs. Example values are placeholders.

## Local setup

```sh
cp config/example.env .env
```

Then edit `Code/.env` and replace the placeholders with your local values. Check that git ignores it: `git status` must not list `.env`.

## Missing or invalid settings

When a setting that the current environment needs is missing or empty, the app stops at start-up with a message naming the setting, for example:

```
Missing required setting: DATABASE_URL
```

It does not start with a default for a required setting or skip the feature silently. Optional settings use the default shown in the table.

Code that loads configuration is written by the tasks that need it. Those tasks must follow this behaviour.
