# Railway-ready Telegram worker

This package is configured to run `1.py` as a long-running Railway worker.

## 1. Upload the files to GitHub

Upload the **contents** of this folder to the root of your repository (not the ZIP file itself). The root should contain:

- `1.py`
- `requirements.txt`
- `Procfile`
- `railway.json`
- `.env.example`
- `.gitignore`
- `README_RAILWAY.md`

Commit the files to the branch you want Railway to deploy (normally `main`).

## 2. Configure Railway

1. Open Railway and select the service.
2. Under **Settings → Source Repo**, confirm the correct repository and branch are selected.
3. Under **Variables**, add the required variables below.
4. Deploy the service. The start command is `python -u 1.py` (also configured in `Procfile` and `railway.json`).
5. Open **Deployments → View Logs** to confirm startup.

### Required variables

- `BOT_TOKEN`: a **new** Telegram bot token from `@BotFather`.
- `CHAT_ID`: the Telegram user, group, or channel ID that should receive alerts. Make sure the bot is allowed to send messages there.

The code no longer includes a fallback token or chat ID. If either variable is missing, it exits with a clear error instead of silently using stale credentials.

### Recommended initial settings

Add these as Railway Variables to start with lower resource usage:

- `SCAN_WORKERS=10`
- `MONITOR_INTERVAL_SECONDS=60`
- `MAX_MONITOR_INTERVAL_SECONDS=180`
- `TELEGRAM_RETRIES=4`
- `WARMUP_ENABLED=1`
- `FLIPKART_ENABLED=1`
- `MAX_ALERT_PRICE=0`

Only add optional integrations if you use them: `KEEPA_API_KEY`, `REDIS_URL`, `DISCORD_WEBHOOK_URL`, `NTFY_TOPIC`, `ALERT_CHANNEL_ID`, `PREMIUM_CHAT_ID`, and `RESIDENTIAL_PROXY_URL`.

## 3. If Railway says “Could not load branches”

That is a GitHub/Railway authorization or branch lookup issue, not a Python code error. Try:

1. In GitHub, confirm the target branch exists and that the files are committed to it.
2. In Railway, open **Project → service → Settings → Source Repo**.
3. Re-authorize/reconnect the GitHub account or GitHub App and grant it access to this private repository.
4. Return to Railway, refresh the service settings, and select the correct branch.
5. If it still fails, disconnect and reconnect the repository from Railway, then retry deployment.

Do not make the repository public just to solve this. Keep it private and grant Railway access.

## 4. Secrets and persistent data

- The token previously embedded in the original source should be considered exposed. Revoke it with `@BotFather` and create a new one before deploying.
- Never commit `.env`, real tokens, cookies, or session files.
- SQLite databases and generated status/log files are stored beside the script. Railway's container filesystem may be ephemeral; attach a Railway Volume and configure storage if you need data to survive redeploys.
- Optional voice conversion may require the `ffmpeg` system package. The main worker may still run without that optional feature.

## 5. Validation

The source is syntax-checked during package preparation. A real deployment and Telegram connection cannot be verified until this package is deployed in your Railway account and valid environment variables are supplied.
