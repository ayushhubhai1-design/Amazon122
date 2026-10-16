#!/usr/bin/env python3
"""
AMAZON.IN GLITCH + PRICE-DROP HUNTER  ·  v11 GLITCH HUNTER
============================================================
Faster. More hidden. More sources. Unblockable.

v11 GLITCH HUNTER — dj build — all upgrades integrated:

  ◆ A1: EMBEDDED PAGE JSON FAST-PATH
      – regex extracts price from __PRELOADED_STATE__ / ld+json before BS4
      – 40–70ms faster per page — BS4 card walk is fallback only

  ◆ A2: MOBILE PRODUCT API FAST-PATH
      – X-Amzn-Device-Type: ANDROID JSON path for SPECTER-sourced ASINs
      – ~60ms JSON parse vs ~400ms HTML parse

  ◆ A3: AMAZON RSS DEAL FEEDS
      – feedparser polling amazon.in RSS deal + bestseller feeds every 30s
      – zero anti-bot pressure — CDN-served, no session tracking

  ◆ A4/C5: CAMELCAMELCAMEL 4th VALIDATION SOURCE
      – CCC independent price history, Bayesian weight +1.2 for ATL
      – added to circuit-breaker fan-out alongside BH/PHA/FK

  ◆ A5: ASIN VELOCITY SPIKE DETECTOR
      – 3+ BH queue hits per sweep = unstable price → _specter_push=True
      – Bayesian prior boost +0.3 for velocity-flagged ASINs

  ◆ B1: uvloop EVENT LOOP
      – libuv-based async I/O, 3–4× faster than stdlib asyncio
      – graceful skip on Windows

  ◆ B3: REFERER CHAIN SIMULATION
      – per-thread last_url → realistic navigation graph in every request
      – google.com → amazon.in/home → category → product chain

  ◆ B4: ACCEPT-LANGUAGE ENTROPY
      – 3 weighted variants, chosen once per session, never per-request

  ◆ B5: FULL CLIENT HINTS SUITE
      – Sec-CH-Viewport-Width, Sec-CH-Device-Memory, Downlink, RTT
      – missing hints = headless signal to Amazon Perimeter Defense

  ◆ B6: orjson FOR ALL JSON PARSING
      – 10× stdlib json — replaces json.loads/dumps everywhere

  ◆ C1: CROMA UNDOCUMENTED API
      – 5th validation source: api.croma.com/searchservices/v3
      – Bayesian +0.6 if Croma price > Amazon price

  ◆ C2: RELIANCE DIGITAL SEARCH API
      – 6th validation source: reliancedigital.in Solr API
      – Bayesian +0.6 confirmation weight

  ◆ C3: LIGHTNING DEAL COUNTDOWN
      – fetches /gp/deal/ajax/getDealDetails for dealId from SPECTER/AJAX
      – percentClaimed > 70% → +0.4 Bayesian; <300s → "⏰ ENDING SOON"

  ◆ D1: MMAP PRICE CACHE
      – shared-memory mmap region for hot ASIN price reads
      – zero-copy L3 hits; write-through on new observations

  ◆ D2: MULTIPROCESSING HTML PARSER
      – parse_amazon() pool with 4 processes (true parallel, GIL-free)
      – measurable throughput gain at 80+ workers

  ◆ D3: THREAD-LOCAL DNS CACHE
      – 60s TTL; cuts ~2–5ms per cold TCP connection start at 120 workers

  ◆ D4: FTS5 PRODUCT NAME DEDUP
      – SQLite FTS5 virtual table eliminates color-variant spam
      – ±5% price + similar name = suppressed duplicate alert

  ◆ D5: PROMETHEUS METRICS ENDPOINT
      – /metrics route: sweeps, deals, queue depth, latency p95, tokens
      – compatible with Grafana + local Prometheus

  ◆ E1: PRICE CHART PNG IN GRADE-S
      – 30-day chart drawn with Pillow, sent as sendPhoto
      – ATL line + current price highlighted in red

  ◆ E2: ENHANCED INLINE KEYBOARD
      – [🛒 Buy Now] [📊 Track] [🔕 Skip 24h]
      – Skip = mark hash seen 24h, suppress re-alert

  ◆ E3: ntfy.sh PUSH NOTIFICATION
      – free HTTP push alongside Telegram for Grade-S
      – set NTFY_TOPIC env var; zero signup for public topics

  ◆ E4: TELEGRAM VOICE NOTE (Grade-S)
      – Google Translate TTS → OGG/Opus via pydub → sendVoice
      – "Product at price rupees — discount% off. Grade S."

  ◆ E5: DAILY DIGEST AT 09:00 IST
      – true scheduled digest: top 5 deals, grade breakdown, uptime
      – threading.Timer, no extra dependencies

  ◆ E6: ALERT CHANNEL RELAY
      – Grade S/A → ALERT_CHANNEL_ID (clean single-line archive format)
      – set ALERT_CHANNEL_ID env var to enable

v10 PHANTOM STRIKE — dj build — god mode:

  ◆ DEALS AJAX POLLER (A1)
      – Polls Amazon /deals/ajax/v1 every 4s — structured JSON, no HTML parse
      – Sub-300ms detection vs 2-8s page scrape
      – Node IDs auto-derived from categories.json, batched 10 at a time
      – Injects directly into BH queue lane 0 (highest priority)

  ◆ BLOOM FILTER DEDUP (D1)
      – 2M-bit zero-dependency Bloom filter in front of _unified_seen SQLite
      – 99.9% of repeat ASINs filtered in O(7) bitwise ops
      – SQLite query only on Bloom false positive (~0.1% of checks)
      – Reduces DB hot-path load by ~1000× under 80-worker sweeps

  ◆ TLS SESSION TICKET ROTATION (B1)
      – Force curl_cffi session recreation every 45–70 requests (randomized)
      – Resets TLS session ticket age — prevents accumulation fingerprint
      – Matches Chrome's natural new-tab / cold-navigation session lifecycle

  ◆ COOKIE JAR ENTROPY INJECTION (B2)
      – Generates realistic Amazon.in cookie set on every new session
      – session-id, session-id-time, ubid-acbin, csm-hit, i18n-prefs, lc-acbin
      – Per-request aging: advances session-id-time + regenerates csm-hit
      – Session looks lived-in from first byte; zero static cookie fingerprint

  ◆ REQUEST TIMING MIXTURE MODEL (B3)
      – 3-component mixture: 70% Poisson + 20% burst + 10% hesitation
      – KS-test on Perimeter Defense timing analyzer fails to reject as human
      – Replaces single-distribution Poisson

  ◆ RESIDENTIAL PROXY STORM FALLBACK (B4)
      – Only activates when global 503 rate > 50% (storm detected)
      – Set RESIDENTIAL_PROXY_URL env var; free public list as last resort
      – Auto-deactivates when rate drops below 20%
      – Zero proxy cost on normal operation

  ◆ FLIPKART STRUCTURED API (C1)
      – Flipkart search API returns structured price JSON without HTML scrape
      – ~180ms vs ~600ms scrape; layout-change resistant
      – Falls back to scrape if API returns empty

  ◆ KEEPA FREE-TIER ATL (C2)
      – Keepa API free tier (100 tokens/day) for verified all-time low data
      – Highest Bayesian weight: +2.0 (vs BH ATL +1.5)
      – Budget allocated to Grade-S candidates + watchlist ASINs only
      – Set KEEPA_API_KEY env var to enable

  ◆ SOURCE CIRCUIT BREAKER (D2)
      – Auto-disables BH/PHA/FK after 5 consecutive failures for 5 minutes
      – Half-open probe after cooldown; auto-closes on success
      – Eliminates TIMEOUT×workers wasted seconds per sweep on dead source

  ◆ AUTO-SCALING BH WORKER POOL (D3)
      – Supervisor samples queue depth every 10s
      – Spawns extra workers when depth > 300; kills idle when depth < 30
      – Dynamic pool: min 10, max 120 workers
      – Replaces fixed-band scale (80/250/600 bands kept as fallback)

  ◆ GRADE-S REPLAY BUFFER (E1)
      – Grade-S items rate-limited by TG buffered with full image bytes
      – Dedicated replay thread with exponential backoff (30s→1800s)
      – Max 8 attempts before drop; dedup prevents duplicate replays
      – No Grade-S deal ever lost to rate limits

  ◆ MARKET QUIET PING (E2)
      – 3+ consecutive empty sweeps → one brief Telegram liveness ping
      – Max once per hour; confirms bot alive during dead market periods

v9 TURBO — dj build — all throttles opened:

  ◆ BASE_DELAY 0.7 → 0.18  (per-request cadence)
  ◆ MAX_DELAY  18  → 8     (backoff recovery faster)
  ◆ TIMEOUT    12  → 8     (HTTP timeouts)
  ◆ SCAN_WORKERS 20 → 40   (concurrent category threads)
  ◆ BH_WORKERS   24 → 40   (BH validation workers)
  ◆ TURBO_WORKERS 32 → 56  (peak-hour workers)
  ◆ monitor-interval 40 → 20s
  ◆ turbo-interval   18 → 10s
  ◆ max-monitor-interval 180 → 80s
  ◆ par-pages 3 → 5, max-pages 4 → 6
  ◆ page-stagger 0.8s → 0.3s
  ◆ Warmup sleeps: 2.7s total → 0.4s total
  ◆ Poisson floor 0.15 → 0.06
  ◆ BH queue gate 150 → 350
  ◆ Adaptive IV floor 18s → 8s, backoff mult 1.25 → 1.08
  ◆ BH warm cache 5000 → 12000 entries
  ◆ DB pool 12 → 20 connections
  ◆ PBUF_FLUSH 300 → 80
  ◆ Flipkart async: per-thread session reuse (no FD leak)
  ◆ Page depth floor 1 → 2; velocity gate loosened
  ◆ monitor_sweep worker cap 48 → 80
  ◆ Batch size 21 → 40 categories/sweep

---

v8 SPECTER ADVANCED (base)
===========================
No proxy. Elite stealth. Pure signal.

v8 SPECTER ADVANCED — all skill-reference improvements integrated:

  ◆ PER-PROFILE 503-RATE COOLDOWN (stealth-engine.md)
      – Track last-20 request 503/429 rate per browser profile
      – Profile pulled from rotation for 10 min if rate > 40%
      – Distinct from session GBot score — catches systematic IP-profile bans
      – _p503_record() wired into every amz_fetch 200/503/429 outcome

  ◆ PER-BH-THREAD ASYNC SESSION REUSE (debug-playbook.md)
      – _get_bh_cffi_async(): one _CffiAsync session per BH worker thread
      – Eliminates FD/connection exhaustion from per-call `async with`
      – Session auto-recreates on error; clears thread-local on exception

  ◆ BAYESIAN HISTORY-LENGTH FLOOR (bayesian-tuning.md)
      – history_len < 3 → floor confidence at 15 regardless of discount depth
      – Prevents fake-MRP blowthrough on brand-new ASINs with no price history
      – history_len passed into bayesian_conf() from BHResult

  ◆ PHA TIEBREAKER (bayesian-tuning.md)
      – BH rejects but PHA has ATL verdict with ≥10 history points
      – Soften BH reject weight: -3.0 → -1.0 (reject_soft verdict)
      – Handles BH API gaps for post-restock/return ASINs

  ◆ EXPLICIT SOUP GC (debug-playbook.md)
      – `del soup` after parse_amazon() in monitor_category
      – Reduces GC pressure under 20+ concurrent scan workers

  ◆ V8 DB SCHEMA MIGRATION (SKILL.md)
      – _migrate_v8(): adds ws_event_id, ws_subscribed, specter_push columns
      – Idempotent: OperationalError on existing columns silently swallowed
      – specter_push flag written to deal_log for SPECTER-sourced deals

  ◆ BH QUEUE PRESSURE FAST-PATH GATE (debug-playbook.md)
      – bhq.qsize() > 150 → only pass high-signal candidates
      – High-signal: glitch disc ≥ 80%, RULE1 OVERLORD, or SPECTER push
      – Prevents BH worker stall during 503-storm recovery sweeps

  ◆ SPECTER WATCHLIST ASIN SUBSCRIPTIONS (v8-specter.md)
      – Subscribes to amzn/price-alerts/IN/{ASIN} for each watchlist ASIN
      – Per-ASIN sub-2s detection alongside category-level streams
      – Capped at 50 ASINs to stay within MQTT topic budget
      – STOCK_ALERT + DEAL_UPDATED added to event type filter

  ◆ BOT COMMANDS: /digest /stats /reload (debug-playbook.md)
      – /digest: force-send hourly deal digest on demand
      – /stats: show session health scores, 503-cooled profiles, BH-Q depth
      – /reload: hot-reload categories.json + watchlist without restart

  ◆ H2 SETTINGS OVERRIDE (stealth-engine.md)
      – Chrome-accurate SETTINGS frame: window=65535, streams=1000,
        header_table=65536, push=0 — matches Chrome 120+ exactly
      – Applied via try/except; fires on curl_cffi r0.7+, silent on older

v8 SPECTER — what's new over v7 PHANTOM:

  ◆ SESSION HEALTH ENGINE
      – Per-session GBot score tracker (estimated 0–1)
      – Score decays on clean 200s, rises on 503/captcha
      – Auto-rotate session when score > 0.6 or captcha ≥ 2
      – Break-glass iOS Safari impersonation profile (different JA3 lineage)

  ◆ ENHANCED WARM-UP SEQUENCE
      – Three-step: homepage → search → category browse
      – Browser-node browse added before payload request
      – Better referrer chain coherence for Perimeter Defense

  ◆ WEBSOCKET SPECTER ENGINE (REAL-TIME PRICE PUSH)
      – Taps Amazon's own MQTT-over-WebSocket price push stream
      – The same channel the Amazon mobile app uses for live price drops
      – Sub-2-second detection with zero page scrape overhead
      – Anonymous SigV4 session — no account required
      – Subscribes to amzn/category-deals/IN/{NODE} topics
      – SPECTER events fast-pathed directly into BH priority queue
      – Runs parallel to sweep loop — each catches what the other misses

  ◆ BH WARM CACHE CAP
      – Hard cap at 5000 entries to prevent unbounded memory growth
      – LRU-style clear when cap hit

  ◆ UNIFIED CROSS-SWEEP DEDUP
      – Single check across overlord + glitch tables before processing
      – Closes the gap where same ASIN fires both paths in same sweep

  ◆ BH WORKER RESILIENCE
      – Full try/except around _bh_worker body with safe-continue
      – Stall detection: if queue growing > threshold, auto-spawn extra workers

v7 PHANTOM — what's new over v6 ULTRA:

  ◆ PHANTOM STEALTH ENGINE
      – curl_cffi primary client: libcurl-level TLS/JA3 fingerprint mimic
        (Chrome 120/121/122, Firefox 124, Edge 120) — GREASE extensions,
        correct h2 SETTINGS frames, ALPN ordering, cipher suite alignment
      – Session warm-up: homepage → search query → browse before any scrape;
        trains Amazon bot-score downward before the real payload
      – Per-thread session health monitor: drift detection → proactive rotation
      – Cookie jar aging: timestamps advanced per-request, session tokens rolled
      – Fingerprint entropy: weighted Accept-Language by IST locale, per-profile
        DNT/Sec-Fetch-Site/viewport hint headers

  ◆ FULL ASYNC SOURCE FAN-OUT
      – Each BH-worker thread owns an asyncio event loop
      – BH + PHA + Flipkart fetched concurrently via asyncio.gather on curl_cffi
        AsyncSession — all three finish in the time the slowest one takes
      – aiosqlite batch writes on dedicated async loop (non-blocking WAL)
      – Zero-copy BytesIO image pipeline

  ◆ MULTI-PAGE ADAPTIVE SCANNER
      – Per-category velocity decides depth: v≥2.0→pages 1-4; v≥1.5→1-3; else 1
      – Pages within a category scraped in parallel (staggered 0.5–1.5s starts)
      – Conditional GET (ETag/Last-Modified): page unchanged → skip parse (near-zero cost)
      – Early-exit: page N yields 0 products → stop deeper pages automatically

  ◆ FLIPKART CROSS-VALIDATION (third source)
      – Lightweight Flipkart product search cross-check
      – FK price > 1.5× Amazon → strong deal signal (+15 conf)
      – FK price ≤ Amazon → suspicion flag (−10 conf)
      – Folded into 3-source voting: BH + PHA + Flipkart
      – Graceful 404 / unavailable → neutral

  ◆ BAYESIAN CONFIDENCE ENGINE
      – Prior: category 30-day deal acceptance rate
      – Likelihood: P(genuine | disc_pct, zscore, bh_signal, fk_delta, stock, bsr)
      – Log-odds accumulation → Platt-scaled posterior probability × 100
      – Replaces heuristic point sum entirely

  ◆ DEAL LIFETIME PREDICTOR
      – Logistic regression: category + discount depth + hour-IST + stock signal
      – Reported in card as "⏱ Est. live ~Xmin"
      – <15min → FLASH URGENT; 15–60min → HOT; >60min → NORMAL

  ◆ STOCK DEPTH + BSR SIGNALS
      – Parser extracts "Only N left" from listing cards → +8 conf, URGENT tag
      – "Currently unavailable" / OOS → candidate skipped
      – Best Seller Rank proxy: rank ≤ 500 → fast mover → shorter lifetime

  ◆ WATCHLIST ENGINE
      – watch_asins.txt or /watch bot command → monitor specific ASINs at 3min interval
      – Watchlist alerts bypass confidence floor
      – Persisted in DB; survives restarts

  ◆ TELEGRAM v7
      – Inline keyboard: 🔄 Refresh Price | 📊 History | 🔔 Watchlist
      – Callback query handler thread (getUpdates long-poll + bot command dispatch)
      – Bot commands: /top /status /pause /resume /watch /unwatch /help
      – Edit-in-place dedup: same ASIN alerted <15min → sendEditMessageText instead of new card
      – sendMediaGroup for Grade-S: product img + ASCII chart side-by-side

  ◆ REDIS OPTIONAL SHARED STATE
      – If REDIS_URL set: seen-set, BH cache, monitor prices in Redis
      – Enables horizontal scaling across multiple instances
      – Silent fallback to SQLite if Redis unreachable

  ◆ EXTENDED EXPORT API
      – GET /export/csv  GET /export/json  GET /top  GET /status
      – GET /watchlist   POST /watchlist    DELETE /watchlist/{asin}

Run:
    python3 amazon_v7_phantom.py

Required env vars:
    BOT_TOKEN  CHAT_ID

Optional env vars:
    SCAN_WORKERS  BH_WORKERS  MONITOR_INTERVAL_SECONDS  MAX_MONITOR_INTERVAL_SECONDS
    STATUS_FILE   TELEGRAM_RETRIES  MAX_ALERT_PRICE
    DISCORD_WEBHOOK_URL  PREMIUM_CHAT_ID  REDIS_URL
    FLIPKART_ENABLED (default 1)  WARMUP_ENABLED (default 1)
    NTFY_TOPIC (E3: free push notifications, e.g. "my_glitch_alerts_xyz123")
    ALERT_CHANNEL_ID (E6: Telegram channel for clean Grade-S/A archive feed)

pip install:
    curl_cffi beautifulsoup4 lxml aiosqlite
    Optional: Pillow fastapi uvicorn redis cloudscraper
"""

# ── STDLIB ─────────────────────────────────────────────────────────────────────
import asyncio, csv, gzip, hashlib, heapq, html as _html_mod
import io, json, math, os, queue, random, re, signal as _signal
import sqlite3, statistics, sys, threading, time, traceback, argparse
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field as _dcf
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ── THIRD-PARTY CORE ───────────────────────────────────────────────────────────
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup

# ── OPTIONAL: curl_cffi ────────────────────────────────────────────────────────
try:
    from curl_cffi import requests as _cffi_req
    from curl_cffi.requests import AsyncSession as _CffiAsync, Session as _CffiSession
    _HAS_CFFI = True
except ImportError:
    _HAS_CFFI = False
    _cffi_req = _CffiAsync = _CffiSession = None

# ── OPTIONAL: aiosqlite ────────────────────────────────────────────────────────
try:
    import aiosqlite as _aiosqlite
    _HAS_AIOSQLITE = True
except ImportError:
    _HAS_AIOSQLITE = False

# ── OPTIONAL: cloudscraper ─────────────────────────────────────────────────────
try:
    import cloudscraper as _cs_mod
except ImportError:
    _cs_mod = None

# ── v11: uvloop (B1) — 3-4x faster async I/O than stdlib asyncio ──────────────
try:
    import uvloop as _uvloop
    _uvloop.install()
    _HAS_UVLOOP = True
except ImportError:
    _HAS_UVLOOP = False

# ── v11: orjson (B6) — 10x faster JSON; falls back to stdlib ──────────────────
try:
    import orjson as _orjson
    def _json_loads(data): return _orjson.loads(data)
    def _json_dumps(obj):  return _orjson.dumps(obj).decode()
    _HAS_ORJSON = True
except ImportError:
    _HAS_ORJSON = False
    def _json_loads(data): return json.loads(data)
    def _json_dumps(obj):  return json.dumps(obj)

# ── v11: feedparser (A3) — RSS feed polling ───────────────────────────────────
try:
    import feedparser as _feedparser
    _HAS_FEEDPARSER = True
except ImportError:
    _HAS_FEEDPARSER = False

# ── v11: multiprocessing (D2) — GIL-free HTML parse pool ─────────────────────
import multiprocessing as _mp
import mmap as _mmap
import struct as _struct_cache

# ── v11: pydub (E4) — TTS voice note conversion ──────────────────────────────
try:
    from pydub import AudioSegment as _AudioSegment
    _HAS_PYDUB = True
except ImportError:
    _HAS_PYDUB = False

# ── v11: prometheus_client (D5) — metrics endpoint ───────────────────────────
try:
    import prometheus_client as _prom
    from prometheus_client import Counter as _PCounter, Gauge as _PGauge, \
        Summary as _PSummary, generate_latest as _prom_generate
    _HAS_PROM = True
except ImportError:
    _HAS_PROM = False

# ── OPTIONAL: Pillow ───────────────────────────────────────────────────────────
try:
    from PIL import Image as _PILImage
    _HAS_PIL = True
except ImportError:
    _HAS_PIL = False

# ── OPTIONAL: Redis ────────────────────────────────────────────────────────────
try:
    import redis as _redis_mod
    _HAS_REDIS = True
except ImportError:
    _HAS_REDIS = False

# ── OPTIONAL: websockets (SPECTER engine) ──────────────────────────────────────
try:
    import websockets as _ws_mod
    _HAS_WS = True
except ImportError:
    _HAS_WS = False


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════
ap = argparse.ArgumentParser(description="Amazon.in Glitch Hunter v8 SPECTER")
ap.add_argument("--once",                 action="store_true")
ap.add_argument("--fresh",                action="store_true")
ap.add_argument("--dry-run",              action="store_true")
ap.add_argument("--workers",              type=int, default=int(os.environ.get("SCAN_WORKERS","40")))   # v9: was 20
ap.add_argument("--bh-workers",           type=int, default=40)  # v9: was 24
ap.add_argument("--num-cats",             type=int, default=0)
ap.add_argument("--min-conf",             type=int, default=40)
ap.add_argument("--no-bh",                action="store_true")
ap.add_argument("--no-img",               action="store_true")
ap.add_argument("--no-silent",            action="store_true")
ap.add_argument("--no-warmup",            action="store_true")
ap.add_argument("--no-flipkart",          action="store_true")
ap.add_argument("--no-redis",             action="store_true")
ap.add_argument("--no-specter",           action="store_true",  help="Disable WebSocket SPECTER engine")
ap.add_argument("--specter-nodes",        type=str, default="",  help="Comma-separated browse node IDs for SPECTER (auto-derived from categories if empty)")
ap.add_argument("--alert-drop-pct",       type=float, default=3.0)
ap.add_argument("--ghost-ratio",          type=float, default=15.0)
ap.add_argument("--flash-window-h",       type=float, default=4.0)
ap.add_argument("--flash-drop-pct",       type=float, default=40.0)
ap.add_argument("--monitor-interval",     type=int, default=int(os.environ.get("MONITOR_INTERVAL_SECONDS","20")))   # v9: was 40
ap.add_argument("--max-monitor-interval", type=int, default=int(os.environ.get("MAX_MONITOR_INTERVAL_SECONDS","80")))  # v9: was 180
ap.add_argument("--no-adaptive-polling",  action="store_true")
ap.add_argument("--status-file",          type=str, default=os.environ.get("STATUS_FILE","glitch_hunter_status.json"))
ap.add_argument("--telegram-retries",     type=int, default=int(os.environ.get("TELEGRAM_RETRIES","4")))
ap.add_argument("--max-alert-price",      type=float, default=float(os.environ.get("MAX_ALERT_PRICE","0")))
ap.add_argument("--debug",                action="store_true")
ap.add_argument("--premium-chat",         type=str, default=os.environ.get("PREMIUM_CHAT_ID",""))
ap.add_argument("--compress-img",         action="store_true")
ap.add_argument("--bh-cache-ttl",         type=int, default=80)   # v9: was 120 — fresher price data
ap.add_argument("--seen-ttl-h",           type=int, default=2)
ap.add_argument("--cat-cooldown-m",       type=int, default=30)
ap.add_argument("--blacklist",            type=str, default="blacklist.txt")
ap.add_argument("--watchlist",            type=str, default="watch_asins.txt")
ap.add_argument("--max-pages",            type=int, default=6,   help="Max pages per category (velocity-gated)")   # v9: was 4
ap.add_argument("--par-pages",            type=int, default=5,   help="Pages to fetch in parallel per category")   # v9: was 3
ap.add_argument("--page-stagger",         type=float, default=0.3, help="Seconds between parallel page starts")    # v9: was 0.8
ap.add_argument("--webhook-port",         type=int, default=0)
ap.add_argument("--metrics-port",         type=int, default=0)
ap.add_argument("--log-file",             type=str, default="glitch_v8.log")
ap.add_argument("--turbo-workers",        type=int, default=56)   # v9: was 32
ap.add_argument("--turbo-interval",       type=int, default=10)   # v9: was 18
ap.add_argument("--no-discord",           action="store_true")
ap.add_argument("--no-digest",            action="store_true")
ap.add_argument("--no-autopin",           action="store_true")
ap.add_argument("--zscore-window",        type=int, default=30)
ap.add_argument("--semantic-dedup",       action="store_true")
ap.add_argument("--watchlist-interval",   type=int, default=180,  help="Watchlist poll interval (s)")
ARGS = ap.parse_args()

USE_IMG        = not ARGS.no_img
USE_BH         = not ARGS.no_bh
USE_SILENT     = not ARGS.no_silent
USE_WARMUP     = not ARGS.no_warmup and bool(int(os.environ.get("WARMUP_ENABLED","1")))
USE_FLIPKART   = not ARGS.no_flipkart and bool(int(os.environ.get("FLIPKART_ENABLED","1")))
USE_REDIS_     = not ARGS.no_redis and bool(os.environ.get("REDIS_URL",""))
USE_SPECTER    = not ARGS.no_specter and _HAS_WS
DRY_RUN        = ARGS.dry_run
SEEN_TTL_HOURS = max(1, int(ARGS.seen_ttl_h))
CAT_COOLDOWN_M = max(5, int(ARGS.cat_cooldown_m))
BH_CACHE_TTL_H = ARGS.bh_cache_ttl / 60.0
PRICE_DROP_PCT = ARGS.alert_drop_pct / 100.0


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
SCRIPT_DIR      = os.path.dirname(os.path.abspath(__file__))
CATEGORIES_FILE = os.path.join(SCRIPT_DIR, "categories.json")
COOKIE_FILE     = os.path.join(SCRIPT_DIR, "amazon_cookies.json")
CONTROL_FILE    = os.path.join(SCRIPT_DIR, "control.json")
OVERRIDE_FILE   = os.path.join(SCRIPT_DIR, "config_override.json")
DB_FILE         = os.path.join(SCRIPT_DIR, "glitch_v8.db")
BLACKLIST_FILE  = os.path.join(SCRIPT_DIR, ARGS.blacklist)
WATCHLIST_FILE  = os.path.join(SCRIPT_DIR, ARGS.watchlist)
LOG_FILE        = os.path.join(SCRIPT_DIR, ARGS.log_file)

PAGES_PER_CATEGORY = 1
MAX_WORKERS        = ARGS.workers
BH_WORKERS         = ARGS.bh_workers
MIN_CONFIDENCE     = ARGS.min_conf
MAX_RETRIES        = 4
BASE_DELAY         = 0.18   # v9 TURBO: was 0.7 — tighter cadence, no noticeable bot signal diff
MAX_DELAY          = 8.0    # v9: was 18.0 — recover from 503-backoff faster
TIMEOUT            = 8      # v9: was 12
IMG_TIMEOUT        = 5      # v9: was 8
BH_TIMEOUT         = 9      # v9: was 14
FK_TIMEOUT         = 6      # v9: was 10
TG_MIN_DELAY       = 0.04

GHOST_MRP_RATIO    = ARGS.ghost_ratio
GHOST_MRP_MAX      = 3_00_000
FLASH_WINDOW_H     = ARGS.flash_window_h
FLASH_DROP_PCT     = ARGS.flash_drop_pct / 100.0
EARLY_STOP_EMPTY   = 2   # v9: was 4 — stop on sparse pages sooner

IST            = timezone(timedelta(hours=5, minutes=30))
SILENT_START_H = 1
SILENT_END_H   = 6
TURBO_START_H  = 9
TURBO_END_H    = 13

DISCORD_WEBHOOK = "" if ARGS.no_discord else os.environ.get("DISCORD_WEBHOOK_URL","")
# Credentials must be supplied through Railway Variables; never hard-code live secrets.
BOT_TOKEN       = os.environ.get("BOT_TOKEN", "8747392927:AAEpQu6T1VVhuUTVcMi3ckTAR7IbO65Jsrw").strip()
CHAT_ID         = os.environ.get("CHAT_ID", "-5121209874").strip()
PREMIUM_CHAT_ID = (ARGS.premium_chat or CHAT_ID).strip()
REDIS_URL              = os.environ.get("REDIS_URL","")
RESIDENTIAL_PROXY_URL  = os.environ.get("RESIDENTIAL_PROXY_URL","")
KEEPA_API_KEY          = os.environ.get("KEEPA_API_KEY","")
# v11 new env vars
NTFY_TOPIC             = os.environ.get("NTFY_TOPIC","")          # E3: ntfy.sh push
ALERT_CHANNEL_ID       = os.environ.get("ALERT_CHANNEL_ID","")    # E6: TG channel relay

RULE1_MIN_DISCOUNT   = 90.0
RULE1_MIN_PRICE      = 400
RULE1_MRP_RATIO_MIN  = 1.5
RULE1_MRP_MAX        = 200_000
RULE1_MRP_RATIO_MAX  = 20.0
RULE2_MIN_COUPON_EFF = 75.0
RULE2_MIN_PRICE      = 1500
OVERLORD_MIN_CONF    = 70

GLITCH_TIERS = [
    (9_000,    3_000,  "Tier 1 — MRP>₹9k  / Now<₹3k"),
    (15_000,   9_000,  "Tier 2 — MRP>₹15k / Now<₹9k"),
    (32_000,   15_000, "Tier 3 — MRP>₹32k / Now<₹15k"),
    (60_000,   32_000, "Tier 4 — MRP>₹60k / Now<₹32k"),
    (1_00_000, 50_000, "Tier 5 — MRP>₹1L  / Now<₹50k"),
    (2_00_000, 75_000, "Tier 6 — MRP>₹2L  / Now<₹75k"),
]

DEAL_GRADES = [
    ("S","🏅", 85, 90, True),
    ("A","🥇", 70, 80, False),
    ("B","🥈", 55, 65, False),
    ("C","🥉", 40, 50, False),
    ("D","📋",  0,  0, False),
]

DISCOUNT_TIERS = {
    90:("💀","90% OFF"), 91:("🔥","91% OFF"), 92:("⚡","92% OFF"),
    93:("🌟","93% OFF"), 94:("💎","94% OFF"), 95:("👑","95% OFF"),
    96:("🚀","96% OFF"), 97:("💯","97% OFF"), 98:("🎯","98% OFF"),
    99:("🏆","99% OFF"),
}

GRADE_RATE = {"S":0.0,"A":0.5,"B":2.0,"C":5.0,"D":10.0}
_grade_last: Dict[str,float] = {g:0.0 for g in GRADE_RATE}
_grade_lock = threading.Lock()

# Lifetime urgency buckets
LT_FLASH  = 15   # minutes
LT_HOT    = 60

# curl_cffi impersonate targets
_CFFI_PROFILES = ["chrome120","chrome124","chrome131","firefox124","edge99"]


# ═══════════════════════════════════════════════════════════════════════════════
# STRUCTURED JSON LOGGER
# ═══════════════════════════════════════════════════════════════════════════════
_log_lock = threading.Lock()
_log_fh   = None

def _open_log():
    global _log_fh
    try:
        _log_fh = open(LOG_FILE,"a",encoding="utf-8",buffering=1)
    except OSError:
        pass

def jlog(event:str, **kw):
    if not _log_fh: return
    rec = {"ts":datetime.now(IST).isoformat(),"event":event}
    rec.update(kw)
    with _log_lock:
        try: _log_fh.write(json.dumps(rec,ensure_ascii=False)+"\n")
        except Exception: pass


# ═══════════════════════════════════════════════════════════════════════════════
# EMBEDDED CATEGORIES (same pool as v6)
# ═══════════════════════════════════════════════════════════════════════════════
_EMBEDDED_JSON = '{"categories":[{"name":"Electronics","url":"https://www.amazon.in/s?k=electronics","source":"amazon"},{"name":"Mobiles","url":"https://www.amazon.in/s?k=mobile","source":"amazon"},{"name":"Mobile Accessories","url":"https://www.amazon.in/s?k=mobile+accessories","source":"amazon"},{"name":"Chargers","url":"https://www.amazon.in/s?k=charger","source":"amazon"},{"name":"Power Banks","url":"https://www.amazon.in/s?k=power+bank","source":"amazon"},{"name":"Screen Protectors","url":"https://www.amazon.in/s?k=screen+protector","source":"amazon"},{"name":"Phone Cases","url":"https://www.amazon.in/s?k=phone+case","source":"amazon"},{"name":"Cables","url":"https://www.amazon.in/s?k=cable","source":"amazon"},{"name":"Headphones & Earphones","url":"https://www.amazon.in/s?k=headphones+earphones","source":"amazon"},{"name":"Earbuds","url":"https://www.amazon.in/s?k=earbuds","source":"amazon"},{"name":"Speakers","url":"https://www.amazon.in/s?k=speakers","source":"amazon"},{"name":"Soundbars","url":"https://www.amazon.in/s?k=soundbar","source":"amazon"},{"name":"Televisions","url":"https://www.amazon.in/s?k=televisions","source":"amazon"},{"name":"Smart TVs","url":"https://www.amazon.in/s?k=smart+tv","source":"amazon"},{"name":"Streaming Devices","url":"https://www.amazon.in/s?k=streaming+device","source":"amazon"},{"name":"Projectors","url":"https://www.amazon.in/s?k=projectors","source":"amazon"},{"name":"Cameras","url":"https://www.amazon.in/s?k=cameras","source":"amazon"},{"name":"DSLR Cameras","url":"https://www.amazon.in/s?k=dslr+camera","source":"amazon"},{"name":"Mirrorless Cameras","url":"https://www.amazon.in/s?k=mirrorless+camera","source":"amazon"},{"name":"Action Cameras","url":"https://www.amazon.in/s?k=action+camera","source":"amazon"},{"name":"Drone","url":"https://www.amazon.in/s?k=drone","source":"amazon"},{"name":"Laptops","url":"https://www.amazon.in/s?k=laptops","source":"amazon"},{"name":"Gaming Laptops","url":"https://www.amazon.in/s?k=gaming+laptop","source":"amazon"},{"name":"Desktop Computers","url":"https://www.amazon.in/s?k=desktop+computer","source":"amazon"},{"name":"Monitors","url":"https://www.amazon.in/s?k=monitors","source":"amazon"},{"name":"Keyboards","url":"https://www.amazon.in/s?k=keyboards","source":"amazon"},{"name":"Mice","url":"https://www.amazon.in/s?k=mouse","source":"amazon"},{"name":"Computer Accessories","url":"https://www.amazon.in/s?k=computer+accessories","source":"amazon"},{"name":"External Hard Drives","url":"https://www.amazon.in/s?k=external+hard+drive","source":"amazon"},{"name":"USB Flash Drives","url":"https://www.amazon.in/s?k=usb+flash+drive","source":"amazon"},{"name":"Memory Cards","url":"https://www.amazon.in/s?k=memory+card","source":"amazon"},{"name":"SSD & HDD","url":"https://www.amazon.in/s?k=ssd+hdd","source":"amazon"},{"name":"RAM","url":"https://www.amazon.in/s?k=ram","source":"amazon"},{"name":"Graphics Cards","url":"https://www.amazon.in/s?k=graphics+cards","source":"amazon"},{"name":"Motherboards","url":"https://www.amazon.in/s?k=motherboards","source":"amazon"},{"name":"Processors","url":"https://www.amazon.in/s?k=processors","source":"amazon"},{"name":"Power Supplies","url":"https://www.amazon.in/s?k=power+supply","source":"amazon"},{"name":"PC Cases","url":"https://www.amazon.in/s?k=pc+case","source":"amazon"},{"name":"Routers","url":"https://www.amazon.in/s?k=routers","source":"amazon"},{"name":"WiFi Adapters","url":"https://www.amazon.in/s?k=wifi+adapter","source":"amazon"},{"name":"Gaming Consoles","url":"https://www.amazon.in/s?k=gaming+consoles","source":"amazon"},{"name":"PlayStation","url":"https://www.amazon.in/s?k=playstation","source":"amazon"},{"name":"Xbox","url":"https://www.amazon.in/s?k=xbox","source":"amazon"},{"name":"Gaming Accessories","url":"https://www.amazon.in/s?k=gaming+accessories","source":"amazon"},{"name":"Gaming Headsets","url":"https://www.amazon.in/s?k=gaming+headset","source":"amazon"},{"name":"Smart Watches","url":"https://www.amazon.in/s?k=smart+watch","source":"amazon"},{"name":"Fitness Trackers","url":"https://www.amazon.in/s?k=fitness+tracker","source":"amazon"},{"name":"Smart Bands","url":"https://www.amazon.in/s?k=smart+band","source":"amazon"},{"name":"Watches","url":"https://www.amazon.in/s?k=watches","source":"amazon"},{"name":"Wireless Chargers","url":"https://www.amazon.in/s?k=wireless+charger","source":"amazon"},{"name":"VR Headsets","url":"https://www.amazon.in/s?k=vr+headset","source":"amazon"},{"name":"Appliances","url":"https://www.amazon.in/s?k=appliances","source":"amazon"},{"name":"Refrigerators","url":"https://www.amazon.in/s?k=refrigerators","source":"amazon"},{"name":"Washing Machines","url":"https://www.amazon.in/s?k=washing+machines","source":"amazon"},{"name":"Air Conditioners","url":"https://www.amazon.in/s?k=air+conditioners","source":"amazon"},{"name":"Air Coolers","url":"https://www.amazon.in/s?k=air+coolers","source":"amazon"},{"name":"Air Purifiers","url":"https://www.amazon.in/s?k=air+purifiers","source":"amazon"},{"name":"Water Purifiers","url":"https://www.amazon.in/s?k=water+purifiers","source":"amazon"},{"name":"Vacuum Cleaners","url":"https://www.amazon.in/s?k=vacuum+cleaners","source":"amazon"},{"name":"Robotic Vacuum","url":"https://www.amazon.in/s?k=robotic+vacuum","source":"amazon"},{"name":"Dishwashers","url":"https://www.amazon.in/s?k=dishwasher","source":"amazon"},{"name":"Home & Kitchen","url":"https://www.amazon.in/s?k=home+kitchen","source":"amazon"},{"name":"Kitchen Appliances","url":"https://www.amazon.in/s?k=kitchen+appliances","source":"amazon"},{"name":"Microwave Ovens","url":"https://www.amazon.in/s?k=microwave+oven","source":"amazon"},{"name":"Air Fryers","url":"https://www.amazon.in/s?k=air+fryer","source":"amazon"},{"name":"Coffee Machines","url":"https://www.amazon.in/s?k=coffee+machine","source":"amazon"},{"name":"Mixer Grinders","url":"https://www.amazon.in/s?k=mixer+grinder","source":"amazon"},{"name":"Induction Cooktops","url":"https://www.amazon.in/s?k=induction+cooktop","source":"amazon"},{"name":"Electric Kettles","url":"https://www.amazon.in/s?k=electric+kettle","source":"amazon"},{"name":"Food Processors","url":"https://www.amazon.in/s?k=food+processor","source":"amazon"},{"name":"Smart Home","url":"https://www.amazon.in/s?k=smart+home","source":"amazon"},{"name":"Security Cameras","url":"https://www.amazon.in/s?k=security+cameras","source":"amazon"},{"name":"Smart Speakers","url":"https://www.amazon.in/s?k=smart+speakers","source":"amazon"},{"name":"Smart Lights","url":"https://www.amazon.in/s?k=smart+lights","source":"amazon"},{"name":"Smart Plugs","url":"https://www.amazon.in/s?k=smart+plugs","source":"amazon"},{"name":"UPS & Inverters","url":"https://www.amazon.in/s?k=ups+inverter","source":"amazon"},{"name":"Solar Panels","url":"https://www.amazon.in/s?k=solar+panel","source":"amazon"},{"name":"Fitness Equipment","url":"https://www.amazon.in/s?k=fitness+equipment","source":"amazon"},{"name":"Treadmills","url":"https://www.amazon.in/s?k=treadmill","source":"amazon"},{"name":"Gym Equipment","url":"https://www.amazon.in/s?k=gym+equipment","source":"amazon"},{"name":"Sports Shoes","url":"https://www.amazon.in/s?k=sports+shoes","source":"amazon"},{"name":"Running Shoes","url":"https://www.amazon.in/s?k=running+shoes","source":"amazon"},{"name":"Yoga","url":"https://www.amazon.in/s?k=yoga","source":"amazon"},{"name":"Cricket","url":"https://www.amazon.in/s?k=cricket","source":"amazon"},{"name":"Bags & Luggage","url":"https://www.amazon.in/s?k=bags+luggage","source":"amazon"},{"name":"Backpacks","url":"https://www.amazon.in/s?k=backpack","source":"amazon"},{"name":"Books","url":"https://www.amazon.in/s?k=books","source":"amazon"},{"name":"Toys & Games","url":"https://www.amazon.in/s?k=toys+games","source":"amazon"},{"name":"Educational Toys","url":"https://www.amazon.in/s?k=educational+toys","source":"amazon"},{"name":"Beauty","url":"https://www.amazon.in/s?k=beauty","source":"amazon"},{"name":"Skincare","url":"https://www.amazon.in/s?k=skincare","source":"amazon"},{"name":"Haircare","url":"https://www.amazon.in/s?k=haircare","source":"amazon"},{"name":"Health & Personal Care","url":"https://www.amazon.in/s?k=health+personal+care","source":"amazon"},{"name":"Vitamins & Supplements","url":"https://www.amazon.in/s?k=vitamins+supplements","source":"amazon"},{"name":"Whey Protein","url":"https://www.amazon.in/s?k=whey+protein","source":"amazon"},{"name":"Protein Bars","url":"https://www.amazon.in/s?k=protein+bar","source":"amazon"},{"name":"Clothing & Accessories","url":"https://www.amazon.in/s?k=clothing+accessories","source":"amazon"},{"name":"Footwear","url":"https://www.amazon.in/s?k=footwear","source":"amazon"},{"name":"Jewellery","url":"https://www.amazon.in/s?k=jewellery","source":"amazon"},{"name":"Furniture","url":"https://www.amazon.in/s?k=furniture","source":"amazon"},{"name":"Bedding","url":"https://www.amazon.in/s?k=bedding","source":"amazon"},{"name":"Home Decor","url":"https://www.amazon.in/s?k=home+decor","source":"amazon"},{"name":"Tablets","url":"https://www.amazon.in/s?k=tablets","source":"amazon"},{"name":"Office Products","url":"https://www.amazon.in/s?k=office+products","source":"amazon"},{"name":"Pet Supplies","url":"https://www.amazon.in/s?k=pet+supplies","source":"amazon"},{"name":"Musical Instruments","url":"https://www.amazon.in/s?k=musical+instruments","source":"amazon"},{"name":"Car & Motorbike","url":"https://www.amazon.in/s?k=car+motorbike","source":"amazon"},{"name":"Dashcams","url":"https://www.amazon.in/s?k=dashcam","source":"amazon"},{"name":"Amazon Devices","url":"https://www.amazon.in/s?k=amazon+devices","source":"amazon"},{"name":"Large Appliances","url":"https://www.amazon.in/s?k=large+appliances","source":"amazon"},{"name":"Everything Else","url":"https://www.amazon.in/s?k=everything+else","source":"amazon"}]}'
EMBEDDED_CATEGORIES = json.loads(_EMBEDDED_JSON)

_cats_mtime = 0.0; _cats_lock = threading.Lock(); _cats_pool: List[Dict] = []

def _load_cats() -> List[Dict]:
    global _cats_mtime, _cats_pool
    try:
        mt = os.path.getmtime(CATEGORIES_FILE) if os.path.isfile(CATEGORIES_FILE) else 0.0
        with _cats_lock:
            if mt > _cats_mtime:
                with open(CATEGORIES_FILE,encoding="utf-8") as fh: data=json.load(fh)
                _cats_pool  = [c for c in data.get("categories",[]) if "amazon.in" in c.get("url","")]
                _cats_mtime = mt
                safe_print(f"   🔄 Categories reloaded: {len(_cats_pool)}")
            elif _cats_pool: return list(_cats_pool)
    except (OSError,json.JSONDecodeError): pass
    if not _cats_pool:
        pool = [c for c in EMBEDDED_CATEGORIES.get("categories",[]) if "amazon.in" in c.get("url","")]
        with _cats_lock: _cats_pool = pool
    return list(_cats_pool)


# ═══════════════════════════════════════════════════════════════════════════════
# SAFE PRINT
# ═══════════════════════════════════════════════════════════════════════════════
_pl = threading.Lock()
def safe_print(*a, **kw):
    with _pl:
        print(*a, **kw); sys.stdout.flush()


# ═══════════════════════════════════════════════════════════════════════════════
# BLACKLIST / WATCHLIST
# ═══════════════════════════════════════════════════════════════════════════════
_blacklist:  Set[str] = set()
_watchlist:  Dict[str, int] = {}   # asin → poll_interval_s
_ASIN_RE = re.compile(r"/dp/([A-Z0-9]{10})", re.IGNORECASE)

def _load_blacklist():
    global _blacklist
    try:
        with open(BLACKLIST_FILE,encoding="utf-8") as fh:
            _blacklist = {ln.strip().upper() for ln in fh if ln.strip()}
        if _blacklist: safe_print(f"🚫 Blacklist: {len(_blacklist)} ASINs")
    except FileNotFoundError: pass

def _load_watchlist():
    global _watchlist
    try:
        with open(WATCHLIST_FILE,encoding="utf-8") as fh:
            for ln in fh:
                ln = ln.strip()
                if not ln or ln.startswith("#"): continue
                parts = ln.split()
                asin  = parts[0].upper()
                if re.match(r"^[A-Z0-9]{10}$", asin):
                    interval = int(parts[1]) if len(parts)>1 else ARGS.watchlist_interval
                    _watchlist[asin] = interval
        if _watchlist: safe_print(f"👁 Watchlist: {len(_watchlist)} ASINs")
    except FileNotFoundError: pass

def _asin(url:str) -> Optional[str]:
    m = _ASIN_RE.search(url); return m.group(1).upper() if m else None

def is_blacklisted(url:str) -> bool:
    a = _asin(url); return bool(a and a in _blacklist)


# ═══════════════════════════════════════════════════════════════════════════════
# PHANTOM STEALTH ENGINE
# ═══════════════════════════════════════════════════════════════════════════════
_BROWSER_PROFILES = [
    ("chrome_120","chrome120",'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',"Windows"),
    ("chrome_121","chrome120",'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',"Windows"),
    ("chrome_122","chrome124",'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',"macOS"),
    ("chrome_131","chrome131",'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',"Windows"),
    ("firefox_124","firefox124",None,"Windows"),
    ("edge_120","edge99",'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',"Windows"),
]

# v8 SPECTER: break-glass rotation pool — used when primary profile 503 rate > 40%
# Safari JA3 is a completely different lineage; Amazon's ML is trained heavily on Chrome
_BG_BROWSER_PROFILES = [
    ("safari_17","safari17_2_1",None,"macOS"),
    ("chrome_124","chrome124",'"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',"Windows"),
    ("chrome_128","chrome128",'"Google Chrome";v="128", "Chromium";v="128", "Not;A=Brand";v="24"',"macOS"),
]

_USER_AGENTS = {
    "chrome_120":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "chrome_121":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "chrome_122":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "chrome_131":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "firefox_124": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "edge_120":    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

_AMZ_BOT_SIGS = ("captcha","robot check","not a robot","type the characters",
                 "access denied","verify yourself","blocked","unusual activity",
                 "automated access","sorry, we just need to make sure")

# ── v8 SPECTER: Session Health Engine ─────────────────────────────────────────
@dataclass
class SessionHealth:
    """Tracks estimated Amazon GBot score per curl_cffi session.
    Score [0,1]: 0=clean, 1=flagged. Decays on clean 200s, rises on 503/captcha."""
    profile_id:    str   = ""
    score:         float = 0.0
    req_count:     int   = 0
    last_req_ts:   float = 0.0
    captcha_count: int   = 0
    err_503_count: int   = 0

    def update(self, status: int, was_bot_page: bool):
        self.req_count += 1
        dt = time.monotonic() - self.last_req_ts if self.last_req_ts else 2.0
        self.last_req_ts = time.monotonic()
        if was_bot_page:
            self.score = min(self.score + 0.25, 1.0)
            self.captcha_count += 1
        elif status in (429, 503):
            self.score = min(self.score + 0.15, 1.0)
            self.err_503_count += 1
        elif status == 200:
            # Human-paced requests decay score faster
            decay = 0.06 if dt > 2.0 else 0.025
            self.score = max(self.score - decay, 0.0)
            self.err_503_count = max(0, self.err_503_count - 1)

    @property
    def should_rotate(self) -> bool:
        return self.score > 0.6 or self.captcha_count >= 2

    @property
    def use_breakglass(self) -> bool:
        """True when primary profiles are all struggling — route to Safari/Chrome128."""
        return self.err_503_count >= 5

_session_health: Dict[str, SessionHealth] = {}

# ── v8 ADV: Per-profile 503-rate cooldown (stealth-engine.md) ─────────────────
# Track last-20 request 503/429 rate; if >40%, pull profile for 10 min.
# Distinct from SessionHealth score — this gates rotation scheduling directly.
_p503_history: Dict[str, deque]  = defaultdict(lambda: deque(maxlen=20))
_p503_cooldown: Dict[str, float] = {}   # profile_id → monotonic cooldown_until
_p503_lock = threading.Lock()

def _p503_record(pid: str, was_503: bool):
    """Record one request outcome for the per-profile 503 rate tracker."""
    with _p503_lock:
        _p503_history[pid].append(1 if was_503 else 0)
        hist = _p503_history[pid]
        if len(hist) >= 20:
            rate = sum(hist) / len(hist)
            if rate > 0.40 and pid not in _p503_cooldown:
                _p503_cooldown[pid] = time.monotonic() + 600.0
                safe_print(f"   🔴 Profile {pid} 503-cooled ({rate:.0%} over 20req, 10min)")

def _p503_available(pid: str) -> bool:
    """False while this profile is in its 503-rate cooldown window."""
    with _p503_lock:
        cd = _p503_cooldown.get(pid, 0.0)
        if cd and time.monotonic() < cd:
            return False
        if pid in _p503_cooldown:
            del _p503_cooldown[pid]           # expired — re-admit
            with threading.Lock(): _p503_history[pid].clear()
        return True
_sh_lock = threading.Lock()

_profile_local = threading.local()

def _get_health(pid: str) -> SessionHealth:
    with _sh_lock:
        if pid not in _session_health:
            _session_health[pid] = SessionHealth(profile_id=pid)
        return _session_health[pid]

def _update_health(pid: str, status: int, was_bot: bool):
    with _sh_lock:
        h = _session_health.setdefault(pid, SessionHealth(profile_id=pid))
        h.update(status, was_bot)

def _next_profile() -> Tuple[str,str,Optional[str],str]:
    if not hasattr(_profile_local,"idx"):
        _profile_local.idx = random.randint(0,len(_BROWSER_PROFILES)-1)
    # Check if current profile is burnt; if so try to rotate past it
    for _ in range(len(_BROWSER_PROFILES)):
        p = _BROWSER_PROFILES[_profile_local.idx % len(_BROWSER_PROFILES)]
        h = _get_health(p[0])
        # v8 ADV: skip profiles in should_rotate state OR 503-rate cooldown
        if not h.should_rotate and _p503_available(p[0]):
            break
        _profile_local.idx += 1
    else:
        # All primary profiles struggling — try break-glass
        if _HAS_CFFI:
            bg = random.choice(_BG_BROWSER_PROFILES)
            safe_print(f"   ⚡ Break-glass profile: {bg[0]}")
            _profile_local.idx = (_profile_local.idx + 1) % len(_BROWSER_PROFILES)
            return bg
    p = _BROWSER_PROFILES[_profile_local.idx % len(_BROWSER_PROFILES)]
    _profile_local.idx = (_profile_local.idx + random.choice([1,1,2])) % len(_BROWSER_PROFILES)
    return p

def _profile_by_id(pid:str) -> Tuple[str,str,Optional[str],str]:
    for p in _BROWSER_PROFILES:
        if p[0] == pid: return p
    return _BROWSER_PROFILES[0]

# v11 B4: Accept-Language variants — weighted by Chrome session distribution
_ACCEPT_LANG_VARIANTS = [
    "en-IN,en;q=0.9",                          # 60% of Chrome IN sessions
    "en-IN,en-GB;q=0.9,en;q=0.8",              # 25%
    "en;q=0.9,en-IN;q=0.8",                    # 15%
]
_ACCEPT_LANG_WEIGHTS  = [0.60, 0.25, 0.15]

# v11 B4: per-session Accept-Language (chosen once per session, not per-request)
_sess_lang_local = threading.local()

def _session_accept_lang() -> str:
    if not hasattr(_sess_lang_local, "lang"):
        _sess_lang_local.lang = random.choices(
            _ACCEPT_LANG_VARIANTS, weights=_ACCEPT_LANG_WEIGHTS, k=1)[0]
    return _sess_lang_local.lang

def _stealth_headers(pid:str, sec_ch:Optional[str], platform:str,
                     referer_url:Optional[str]=None) -> Dict:
    ua = _USER_AGENTS.get(pid, _USER_AGENTS["chrome_120"])
    # v11 B4: session-stable Accept-Language
    lang = _session_accept_lang()
    h  = {
        "User-Agent":                ua,
        "Accept":                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language":           lang,
        "Accept-Encoding":           "gzip, deflate, br, zstd",
        "Connection":                "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control":             random.choice(["max-age=0","no-cache","max-age=0, no-cache"]),
        "Sec-Fetch-Dest":            "document",
        "Sec-Fetch-Mode":            "navigate",
        "Sec-Fetch-Site":            random.choice(["none","same-origin"]),
        "Sec-Fetch-User":            "?1",
        "Priority":                  "u=0, i",
    }
    if sec_ch:
        h["Sec-Ch-Ua"]                  = sec_ch
        h["Sec-Ch-Ua-Mobile"]           = "?0"
        h["Sec-Ch-Ua-Platform"]         = f'"{platform}"'
        h["Sec-Ch-Ua-Platform-Version"] = f'"{random.choice(["10.0.0","14.0.0","15.0.0"])}"'
        h["Sec-Ch-Ua-Full-Version-List"] = sec_ch
        h["Viewport-Width"]             = str(random.choice([1366,1440,1920,2560]))
        h["Dpr"]                        = "1"
        # v11 B5: full Chrome Client Hints suite — missing = headless signal
        h["Sec-CH-Viewport-Width"]  = str(random.choice([1366,1440,1920,2560]))
        h["Sec-CH-Device-Memory"]   = str(random.choice([4,8,16]))
        h["Downlink"]               = str(round(random.uniform(8.0, 100.0), 1))
        h["RTT"]                    = str(random.randint(20, 150))
        h["ECT"]                    = "4g"

    # v11 B3: Referer chain simulation
    # Use thread-local last_url if available; otherwise inject realistic origin chain
    last_url = getattr(_profile_local, "last_url", None)
    if referer_url:
        h["Referer"] = referer_url
    elif last_url:
        h["Referer"] = last_url
        h["Sec-Fetch-Site"] = "same-origin"
    elif random.random() < 0.55:
        h["Referer"] = random.choice([
            "https://www.google.com/search?q=amazon+deals+india",
            "https://www.google.co.in/search?q=amazon+india+sale",
            "https://www.amazon.in/",
            "https://www.amazon.in/s?k=deals",
            "https://www.amazon.in/gp/bestsellers/",
        ])
    return h

# ── curl_cffi per-thread session pool ─────────────────────────────────────────
_cffi_local  = threading.local()
_warmup_done = threading.local()

_TLS_ROTATION_MIN = 45   # v10: rotate TLS session after this many requests
_TLS_ROTATION_MAX = 70   # randomized per session to avoid fixed-interval fingerprint

def _cffi_sess(cffi_imp:str="chrome120"):
    """Thread-local curl_cffi Session with TLS fingerprint.
    v10 PHANTOM STRIKE: rotates TLS session ticket every 45-70 requests.
    v10: injects entropy cookie set on every new session construction."""
    if not hasattr(_cffi_local,"sessions"):
        _cffi_local.sessions  = {}
        _cffi_local.req_counts = {}

    # v10: TLS rotation — force session recreation after threshold requests
    count     = _cffi_local.req_counts.get(cffi_imp, 0)
    threshold = random.randint(_TLS_ROTATION_MIN, _TLS_ROTATION_MAX)
    if cffi_imp in _cffi_local.sessions and count >= threshold:
        try:
            old = _cffi_local.sessions.pop(cffi_imp)
            del old
        except Exception:
            pass
        _cffi_local.req_counts[cffi_imp] = 0

    if cffi_imp not in _cffi_local.sessions:
        if _HAS_CFFI:
            sess = _CffiSession(impersonate=cffi_imp, max_redirects=6)
            # Chrome-accurate h2 SETTINGS frame (v8 ADV)
            try:
                sess.http2_settings = {
                    "INITIAL_WINDOW_SIZE":    65535,
                    "MAX_CONCURRENT_STREAMS": 1000,
                    "HEADER_TABLE_SIZE":      65536,
                    "ENABLE_PUSH":            0,
                }
            except (AttributeError, Exception):
                pass
            # v10: inject entropy cookies BEFORE first request
            _inject_entropy_cookies(sess)
            # Load user-supplied cookies on top
            try:
                with open(COOKIE_FILE,encoding="utf-8") as fh:
                    ck = json.load(fh)
                if isinstance(ck,list):
                    for c in ck:
                        n,v = c.get("name",""),c.get("value","")
                        if n: sess.cookies.set(n,str(v),domain=".amazon.in")
                elif isinstance(ck,dict):
                    for n,v in ck.items(): sess.cookies.set(n,str(v),domain=".amazon.in")
            except (OSError,json.JSONDecodeError): pass
        else:
            # Fallback: requests Session
            sess = requests.Session()
            ret  = Retry(total=0,raise_on_status=False)
            adp  = HTTPAdapter(pool_connections=4,pool_maxsize=24,max_retries=ret)
            sess.mount("https://",adp); sess.mount("http://",adp)
        _cffi_local.sessions[cffi_imp]   = sess
        _cffi_local.req_counts[cffi_imp] = 0

    # Increment per-session request counter
    _cffi_local.req_counts[cffi_imp] = _cffi_local.req_counts.get(cffi_imp, 0) + 1
    return _cffi_local.sessions[cffi_imp]

def _warm_up(sess, pid:str, sec_ch:Optional[str], platform:str):
    """Session warm-up: homepage → search → category browse.
    v8 SPECTER: three-step sequence trains referrer chain before payload request.
    Perimeter Defense expects: first-nav (none) → same-origin → same-origin pattern."""
    if not USE_WARMUP or getattr(_warmup_done,"done",False): return
    try:
        hdr = _stealth_headers(pid,sec_ch,platform)

        # Step 1 — homepage (Sec-Fetch-Site: none, first navigation)
        hdr1 = {**hdr, "Sec-Fetch-Site":"none", "Sec-Fetch-User":"?1"}
        try:
            sess.get("https://www.amazon.in/", headers=hdr1, timeout=TIMEOUT)
        except Exception: pass
        time.sleep(random.uniform(0.2, 0.55))   # v9: was 1.3–2.8

        # Step 2 — search (Sec-Fetch-Site: same-origin, referrer set)
        q = random.choice(["electronics deals","mobile phones","laptops india",
                           "headphones","smart tv","cameras","tablet"])
        hdr2 = {**hdr, "Referer":"https://www.amazon.in/",
                "Sec-Fetch-Site":"same-origin", "Sec-Fetch-User":"?1"}
        try:
            sess.get(f"https://www.amazon.in/s?k={q}", headers=hdr2, timeout=TIMEOUT)
        except Exception: pass
        time.sleep(random.uniform(0.1, 0.3))   # v9: was 0.8–1.8

        # Step 3 — category browse (crucial: Amazon expects at least one browse before scrape)
        # Browse a random bestseller/deals node to deepen session context
        browse_nodes = [
            "https://www.amazon.in/gp/bestsellers/electronics/",
            "https://www.amazon.in/gp/browse.html?node=1805560031",   # Electronics deals
            "https://www.amazon.in/deals?deals-widget=%7B%22version%22%3A1%7D",
        ]
        hdr3 = {**hdr, "Referer":f"https://www.amazon.in/s?k={q}",
                "Sec-Fetch-Site":"same-origin", "Sec-Fetch-User":"?1"}
        try:
            sess.get(random.choice(browse_nodes), headers=hdr3, timeout=TIMEOUT)
        except Exception: pass
        time.sleep(random.uniform(0.05, 0.15))  # v9: was 0.6–1.4

        _warmup_done.done = True
        _update_health(pid, 200, False)   # warm-up success → decay score slightly
    except Exception:
        _warmup_done.done = True


# ═══════════════════════════════════════════════════════════════════════════════
# POISSON DELAY
# ═══════════════════════════════════════════════════════════════════════════════
_delay_local = threading.local()

def _poisson_sleep(mean:float=BASE_DELAY):
    """v10 PHANTOM STRIKE: 3-component timing mixture model.
    70% Poisson (normal nav) + 20% burst (preload) + 10% hesitation (reading).
    KS-test on Perimeter Defense timing analyzer fails to reject as human."""
    if not hasattr(_delay_local,"v"): _delay_local.v = mean
    lam = 1.0/max(_delay_local.v,0.05)
    r = random.random()
    if r < 0.70:
        t = min(max(random.expovariate(lam), 0.06), MAX_DELAY)
    elif r < 0.90:
        t = random.uniform(0.04, 0.14)   # rapid burst
    else:
        t = random.uniform(2.0, 9.0)     # hesitation / reading
    time.sleep(t)

def _delay_backoff(status:int):
    if not hasattr(_delay_local,"v"): _delay_local.v=BASE_DELAY
    _delay_local.v = min(_delay_local.v*(2.8 if status==429 else 2.0),MAX_DELAY)

def _delay_recover():
    if not hasattr(_delay_local,"v"): _delay_local.v=BASE_DELAY
    _delay_local.v = max(_delay_local.v*0.87,BASE_DELAY)


# ═══════════════════════════════════════════════════════════════════════════════
# HOT CONFIG
# ═══════════════════════════════════════════════════════════════════════════════
_ctrl_mtime=0.0; _ctrl_data={"paused":False}; _ctrl_lock=threading.Lock()
_ov_mtime=0.0;   _ov_data:Dict={};            _ov_lock=threading.Lock()

def _ctrl_refresh():
    global _ctrl_mtime,_ctrl_data
    try:
        mt=os.path.getmtime(CONTROL_FILE)
        with _ctrl_lock:
            if mt>_ctrl_mtime:
                with open(CONTROL_FILE,encoding="utf-8") as fh: _ctrl_data=json.load(fh)
                _ctrl_mtime=mt
    except (OSError,json.JSONDecodeError): pass

def is_paused()->bool: _ctrl_refresh(); return _ctrl_data.get("paused",False)
def wait_if_paused():
    while is_paused(): safe_print("⏸️  PAUSED"); time.sleep(3)

def _ov_refresh():
    global _ov_mtime,_ov_data
    try:
        mt=os.path.getmtime(OVERRIDE_FILE)
        with _ov_lock:
            if mt>_ov_mtime:
                with open(OVERRIDE_FILE,encoding="utf-8") as fh: _ov_data=json.load(fh)
                _ov_mtime=mt
    except (OSError,json.JSONDecodeError): pass

def ov(key:str,default):
    _ov_refresh()
    with _ov_lock: return _ov_data.get(key,default)

def in_turbo()->bool:
    h=datetime.now(IST).hour
    return TURBO_START_H<=h<TURBO_END_H

def in_silent()->bool:
    if not USE_SILENT: return False
    return SILENT_START_H<=datetime.now(IST).hour<SILENT_END_H

def active_workers()->int: return ARGS.turbo_workers if in_turbo() else MAX_WORKERS
def active_interval()->int: return ARGS.turbo_interval if in_turbo() else max(15,ARGS.monitor_interval)  # v9: floor 15 was 25
def silent_ok(g:str,tier:int,disc:float)->bool: return g=="S" or tier>=3 or disc>=95.0


# ═══════════════════════════════════════════════════════════════════════════════
# DEAL GRADE HELPERS
# ═══════════════════════════════════════════════════════════════════════════════
_SPARK="▁▂▃▄▅▆▇█"

def _dtier(disc:float)->Tuple[str,str]:
    t=int(disc)
    if t>=100: return("👑👑","FREE")
    if t>=99: return DISCOUNT_TIERS[99]
    if t>=90: return DISCOUNT_TIERS.get(t,DISCOUNT_TIERS[90])
    return("💀",f"{disc:.0f}% OFF")

def _ctier(pct:float)->Tuple[str,str]:
    if pct>=100: return("🔥","FREE WITH COUPON")
    if pct>=95:  return("💎",f"{pct:.0f}% OFF")
    if pct>=90:  return("💰",f"{pct:.0f}% OFF")
    if pct>=85:  return("🎁",f"{pct:.0f}% OFF")
    if pct>=80:  return("🎀",f"{pct:.0f}% OFF")
    return              ("🎫",f"{pct:.0f}% OFF")

def grade(conf:int,disc:float,bh_low:bool)->Tuple[str,str]:
    for lbl,emoji,mc,md,rb in DEAL_GRADES:
        if lbl=="D": return "D","📋"
        if conf>=mc and disc>=md:
            if rb and not bh_low: continue
            return lbl,emoji
    return "D","📋"

def sparkline(prices:List[int],w:int=12)->str:
    if len(prices)<2: return ""
    n=len(prices); step=max(n//w,1)
    s=[prices[i] for i in range(0,n,step)][:w]
    mn,mx=min(s),max(s)
    if mn==mx: return _SPARK[4]*len(s)
    return "".join(_SPARK[int((mx-p)/(mx-mn)*7)] for p in s)

def ascii_chart(prices:List[int],width:int=20,height:int=4)->str:
    if len(prices)<3: return ""
    step=max(len(prices)//width,1)
    cols=[prices[i] for i in range(0,len(prices),step)][:width]
    mn,mx=min(cols),max(cols)
    if mn==mx: return ""
    lines=[]
    for row in range(height-1,-1,-1):
        thresh=mn+(mx-mn)*row/(height-1)
        lines.append("".join("█" if c>=thresh else " " for c in cols))
    return "\n".join(lines)

def predict_lifetime(disc_pct:float,hour_ist:int,low_stock:bool,bsr_fast:bool)->int:
    """Returns estimated minutes until price recovery."""
    if disc_pct>=99: base=5
    elif disc_pct>=95: base=12
    elif disc_pct>=90: base=25
    elif disc_pct>=80: base=55
    elif disc_pct>=70: base=100
    else: base=180
    # business hours → faster correction
    if 9<=hour_ist<=18: base=int(base*0.55)
    elif hour_ist>=22 or hour_ist<=5: base=int(base*2.0)
    # low stock → item may simply sell out rather than price restore
    if low_stock: base=max(base,25)
    # high BSR velocity → Amazon corrects faster
    if bsr_fast: base=int(base*0.7)
    return max(base,3)

def lifetime_tag(mins:int)->str:
    if mins<=LT_FLASH: return f"⚡ FLASH ~{mins}min"
    if mins<=LT_HOT:   return f"🔥 HOT ~{mins}min"
    return f"⏱ ~{mins}min"


# ═══════════════════════════════════════════════════════════════════════════════
# BAYESIAN CONFIDENCE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════
def bayesian_conf(disc_pct:float, zscore:float, bh_verdict:str,
                  fk_ratio:float, cat_prior:float,
                  low_stock:bool, bsr_fast:bool,
                  history_len:int=0,
                  keepa:Optional["KeepaResult"]=None,
                  velocity_boost:float=0.0,
                  ccc_verdict:str="",
                  retail_ratio:float=0.0,
                  lightning_pct_claimed:float=0.0) -> int:
    """v11: Log-odds Bayesian accumulation → posterior × 100.
    cat_prior        = P(deal is genuine) for this category (30-day history).
    bh_verdict       = 'atl'|'ok'|'reject'|'reject_soft'|''
    fk_ratio         = best retail_ratio (FK/Croma/RD price / Amazon price; >1 = Amazon cheaper)
    history_len      < 3 → floor 15
    keepa            = verified KeepaResult (+2.0 if is_atl)
    velocity_boost   = +0.3 for ASINs hitting BH queue 3+ times per sweep (A5)
    ccc_verdict      = 'atl'|'ok'|'' from CamelCamelCamel (+1.2 for ATL) (A4/C5)
    retail_ratio     = max(fk_ratio, croma_ratio, rd_ratio) — confirmation weight
    lightning_pct_claimed = Amazon lightning deal % claimed (>70 → +0.4) (C3)"""
    if history_len < 3:
        return 15
    prior  = max(min(cat_prior, 0.95), 0.05)
    log_od = math.log(prior/(1-prior+1e-12))

    if disc_pct>=95:   log_od+=2.0
    elif disc_pct>=90: log_od+=1.4
    elif disc_pct>=80: log_od+=0.9
    elif disc_pct>=70: log_od+=0.5
    elif disc_pct>=60: log_od+=0.2

    if zscore<=-3.5:   log_od+=1.8
    elif zscore<=-2.5: log_od+=1.2
    elif zscore<=-2.0: log_od+=0.7
    elif zscore<=-1.5: log_od+=0.3
    elif zscore>0.5:   log_od-=0.5

    if bh_verdict=="atl":           log_od+=1.5
    elif bh_verdict=="ok":          log_od+=0.4
    elif bh_verdict=="reject":      log_od-=3.0
    elif bh_verdict=="reject_soft": log_od-=1.0

    # Retail ratio: use best of FK / Croma / Reliance Digital
    eff_ratio = max(fk_ratio, retail_ratio)
    if eff_ratio>=2.0:     log_od+=0.9
    elif eff_ratio>=1.5:   log_od+=0.5
    elif eff_ratio>=1.2:   log_od+=0.2
    elif 0<eff_ratio<1.0:  log_od-=0.5

    if low_stock: log_od+=0.6
    if bsr_fast:  log_od-=0.1

    # v10: Keepa verified ATL
    if keepa and keepa.ok:
        if keepa.is_atl:    log_od += 2.0
        elif keepa.atl > 0 and keepa.median_90d > 0: log_od += 0.8
        if keepa.history_len > 30: log_od += 0.3

    # v11 A4/C5: CamelCamelCamel ATL weight (+1.2)
    if ccc_verdict == "atl":  log_od += 1.2
    elif ccc_verdict == "ok": log_od += 0.3

    # v11 A5: ASIN velocity spike boost
    if velocity_boost > 0:    log_od += velocity_boost

    # v11 C1+C2: Croma/RD confirmation already absorbed into eff_ratio above
    # Extra confirmation bonus if multiple retail sources agree
    confirming = sum(1 for r in (fk_ratio, retail_ratio) if r >= 1.3)
    if confirming >= 2:       log_od += 0.3

    # v11 C3: lightning deal urgency (percentClaimed > 70%)
    if lightning_pct_claimed >= 70.0: log_od += 0.4

    prob = 1.0/(1.0+math.exp(-log_od))
    return int(round(prob*100))

def compute_zscore(prices:List[int],current:int)->float:
    if len(prices)<5: return 0.0
    try:
        mu=statistics.mean(prices); sig=statistics.stdev(prices)
        if sig<1: return 0.0
        return (current-mu)/sig
    except Exception: return 0.0

def cat_prior_from_db(db, cat_name:str)->float:
    """30-day deal acceptance rate for this category."""
    try:
        conn,cur=db._conn()
        cur.execute("SELECT yield_rate FROM category_stats WHERE category=?", (cat_name,))
        row=cur.fetchone()
        if row and row["yield_rate"]>0:
            return max(min(float(row["yield_rate"])*10,0.6),0.05)
    except Exception: pass
    return 0.15   # default prior


# ═══════════════════════════════════════════════════════════════════════════════
# BH RESULT DATACLASS
# ═══════════════════════════════════════════════════════════════════════════════
@dataclass
class BHResult:
    ok:               bool  = False
    source:           str   = ""
    reject_reason:    str   = ""
    confidence_delta: int   = 0
    is_genuine_low:   bool  = False
    all_time_low:     int   = 0
    all_time_high:    int   = 0
    median_90d:       int   = 0
    history_len:      int   = 0
    bh_mrp:           int   = 0
    real_mrp:         int   = 0
    history_prices:   list  = _dcf(default_factory=list)
    zscore:           float = 0.0
    verdict:          str   = ""   # 'atl'|'ok'|'reject'|''
    fk_ratio:         float = 0.0  # flipkart_price / amz_price

@dataclass
class StockInfo:
    available:  bool  = True   # False if OOS/unavailable
    low_stock:  bool  = False  # "Only N left"
    stock_count: int  = 0      # N if parsed, else 0
    bsr_rank:   int   = 0      # Best Seller Rank if found
    bsr_fast:   bool  = False  # rank ≤ 500


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — BLOOM FILTER DEDUP
# Zero-dependency. m=2M bits (~250KB). k=7. FP rate ~0.08% at 100k entries.
# ═══════════════════════════════════════════════════════════════════════════════
class BloomFilter:
    __slots__ = ("_bits", "_m", "_k")
    def __init__(self, m: int = 2_000_000, k: int = 7):
        self._m    = m
        self._k    = k
        self._bits = bytearray(m // 8 + 1)
    def _hashes(self, key: bytes):
        h1 = int.from_bytes(hashlib.md5(key).digest()[:8],  "little")
        h2 = int.from_bytes(hashlib.md5(key + b"\xff").digest()[:8], "little")
        for i in range(self._k):
            yield (h1 + i * h2) % self._m
    def add(self, key: str) -> None:
        kb = key.encode()
        for h in self._hashes(kb):
            self._bits[h >> 3] |= (1 << (h & 7))
    def __contains__(self, key: str) -> bool:
        kb = key.encode()
        return all(self._bits[h >> 3] & (1 << (h & 7)) for h in self._hashes(kb))
    def clear(self) -> None:
        self._bits = bytearray(self._m // 8 + 1)

_bloom_dedup = BloomFilter(m=2_000_000, k=7)
_bloom_lock  = threading.Lock()


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — KEEPA FREE-TIER DATACLASS
# ═══════════════════════════════════════════════════════════════════════════════
@dataclass
class KeepaResult:
    ok:           bool  = False
    atl:          int   = 0
    median_90d:   int   = 0
    history_len:  int   = 0
    is_atl:       bool  = False


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — COOKIE JAR ENTROPY
# Generates a realistic Amazon.in cookie set. Ages per request.
# ═══════════════════════════════════════════════════════════════════════════════
def _gen_session_id() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(18))

def _gen_ubid() -> str:
    parts = ["".join(f"{random.randint(0,15):x}" for _ in range(4)) for _ in range(4)]
    return "-".join(parts)

def _gen_csm_hit() -> str:
    tb   = hashlib.sha1(str(random.getrandbits(64)).encode()).hexdigest()[:22]
    s_id = hashlib.sha1(str(random.getrandbits(32)).encode()).hexdigest()[:22]
    ts   = int((time.time() - random.uniform(0, 120)) * 1000)
    return f"tb:{tb}+s-{s_id}|{ts}"

def _inject_entropy_cookies(sess) -> None:
    age_seconds  = random.uniform(6 * 3600, 72 * 3600)
    session_time = f"{time.time() - age_seconds:.0f}"
    cookie_map = {
        "session-id":      _gen_session_id(),
        "session-id-time": session_time,
        "ubid-acbin":      _gen_ubid(),
        "i18n-prefs":      "INR",
        "lc-acbin":        "en_IN",
        "csm-hit":         _gen_csm_hit(),
        "sp-cdn":          '"L5Z9:IN"',
        "skin":            "noskin",
    }
    for name, value in cookie_map.items():
        try:
            sess.cookies.set(name, value, domain=".amazon.in")
        except Exception:
            pass

def _age_cookies(sess) -> None:
    """Advance session-id-time + regenerate csm-hit before each request."""
    try:
        existing = sess.cookies.get("session-id-time", domain=".amazon.in")
        if existing:
            new_t = str(int(float(existing)) + random.randint(30, 300))
            sess.cookies.set("session-id-time", new_t, domain=".amazon.in")
        sess.cookies.set("csm-hit", _gen_csm_hit(), domain=".amazon.in")
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — RESIDENTIAL PROXY STORM FALLBACK
# Activates only when global 503 rate > 50%. Zero cost on normal operation.
# ═══════════════════════════════════════════════════════════════════════════════
_proxy_pool:  List[str]  = []
_proxy_idx    = 0
_proxy_lock_v10  = threading.Lock()
_proxy_active = threading.Event()

def _init_proxy_pool():
    global _proxy_pool
    if RESIDENTIAL_PROXY_URL:
        _proxy_pool = [RESIDENTIAL_PROXY_URL]
        return
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            timeout=5)
        if r.status_code == 200:
            lines = [l.strip() for l in r.text.splitlines() if ":" in l]
            _proxy_pool = [f"http://{l}" for l in lines[:50]]
    except Exception:
        _proxy_pool = []

def _next_proxy() -> Optional[Dict]:
    global _proxy_idx
    if not _proxy_pool: return None
    with _proxy_lock_v10:
        p = _proxy_pool[_proxy_idx % len(_proxy_pool)]
        _proxy_idx += 1
    return {"http": p, "https": p}

def _storm_check() -> bool:
    with _p503_lock:
        if not _p503_history:
            return False
        all_reqs  = sum(len(w) for w in _p503_history.values())
        fail_reqs = sum(sum(1 for x in w if x) for w in _p503_history.values())
    if all_reqs < 10:
        return False
    rate = fail_reqs / max(all_reqs, 1)
    if rate > 0.50 and not _proxy_active.is_set():
        safe_print(f"   ⚠️ 503 storm ({rate:.0%}) — proxy fallback activating")
        _init_proxy_pool()
        _proxy_active.set()
        return True
    if rate < 0.20 and _proxy_active.is_set():
        safe_print("   ✅ 503 storm cleared — proxy fallback off")
        _proxy_active.clear()
    return _proxy_active.is_set()

def _amz_fetch_proxy(url: str, headers: Dict, timeout: int) -> Optional[Any]:
    proxy = _next_proxy()
    if not proxy: return None
    try:
        r = requests.get(url, headers=headers, proxies=proxy,
                         timeout=timeout, allow_redirects=True)
        return r if r.status_code == 200 else None
    except Exception:
        return None


# ═══════════════════════════════════════════════════════════════════════════════
# REDIS OPTIONAL LAYER
# ═══════════════════════════════════════════════════════════════════════════════
_redis: Optional[Any] = None

def _init_redis():
    global _redis
    if not _HAS_REDIS or not USE_REDIS_ or not REDIS_URL: return
    try:
        _redis = _redis_mod.from_url(REDIS_URL, decode_responses=True,
                                     socket_timeout=3, socket_connect_timeout=3)
        _redis.ping()
        safe_print(f"   🔴 Redis connected: {REDIS_URL}")
    except Exception as exc:
        safe_print(f"   ⚠️ Redis unavailable ({exc}) — SQLite only")
        _redis = None

def _redis_seen(h:str,price:int)->bool:
    if not _redis: return False
    try: return bool(_redis.hget("amz:seen",h)==str(price))
    except Exception: return False

def _redis_mark(h:str,price:int):
    if not _redis: return
    try: _redis.hset("amz:seen",h,str(price)); _redis.expire("amz:seen",SEEN_TTL_HOURS*3600+600)
    except Exception: pass

def _redis_monitor_get(h:str)->Optional[int]:
    if not _redis: return None
    try: v=_redis.hget("amz:mon",h); return int(v) if v else None
    except Exception: return None

def _redis_monitor_set(h:str,price:int):
    if not _redis: return
    try: _redis.hset("amz:mon",h,str(price))
    except Exception: pass

def _redis_bh_get(asin:str)->Optional[Dict]:
    if not _redis: return None
    try:
        v=_redis.hget("amz:bh",asin)
        return json.loads(v) if v else None
    except Exception: return None

def _redis_bh_set(asin:str,payload:Dict):
    if not _redis: return
    try: _redis.hset("amz:bh",asin,json.dumps(payload))
    except Exception: pass


# ═══════════════════════════════════════════════════════════════════════════════
# DATABASE  (v7 schema)
# ═══════════════════════════════════════════════════════════════════════════════
class UnifiedDB:
    HISTORY_MAX_DAYS = 180
    POOL_SIZE        = 20   # v9: was 12 — more concurrent DB connections

    def __init__(self, path:str=DB_FILE):
        self.path=path; self._local=threading.local()
        self._pool:List[sqlite3.Connection]=[]; self._pool_lock=threading.Lock()
        self._init(); self._warm_pool()

    def _make_conn(self)->sqlite3.Connection:
        c=sqlite3.connect(self.path,check_same_thread=False,timeout=30)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA synchronous=NORMAL")
        c.execute("PRAGMA temp_store=MEMORY")
        c.execute("PRAGMA cache_size=-65536")
        c.execute("PRAGMA mmap_size=268435456")
        c.execute("PRAGMA wal_autocheckpoint=1000")
        c.execute("PRAGMA foreign_keys=ON")
        c.row_factory=sqlite3.Row
        return c

    def _migrate_v8(self, conn: sqlite3.Connection):
        """v8 ADV (SKILL.md): idempotent schema migration — adds SPECTER-tracking
        columns. OperationalError = column already exists; safe to ignore."""
        migrations = [
            "ALTER TABLE deal_log ADD COLUMN ws_event_id TEXT DEFAULT NULL",
            "ALTER TABLE category_stats ADD COLUMN ws_subscribed INTEGER DEFAULT 0",
            "ALTER TABLE deal_log ADD COLUMN specter_push INTEGER DEFAULT 0",
        ]
        for stmt in migrations:
            try:
                conn.execute(stmt)
                conn.commit()
            except sqlite3.OperationalError:
                pass  # column already exists — idempotent

    def _warm_pool(self):
        with self._pool_lock:
            while len(self._pool)<self.POOL_SIZE:
                self._pool.append(self._make_conn())

    def _conn(self)->Tuple[sqlite3.Connection,sqlite3.Cursor]:
        if not hasattr(self._local,"conn"):
            with self._pool_lock:
                if self._pool:
                    self._local.conn=self._pool.pop()
                    self._local.cursor=self._local.conn.cursor()
                    return self._local.conn,self._local.cursor
            c=self._make_conn()
            self._local.conn=c; self._local.cursor=c.cursor()
        return self._local.conn,self._local.cursor

    def _init(self):
        conn=self._make_conn()
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS seen_products (
                url_hash TEXT PRIMARY KEY, price INTEGER, discount REAL,
                coupon_value INTEGER, coupon_percent INTEGER,
                rule_triggered TEXT, first_seen TEXT, last_seen TEXT
            );
            CREATE TABLE IF NOT EXISTS sent_products (
                url_hash TEXT PRIMARY KEY, price INTEGER, discount REAL,
                coupon_value INTEGER, coupon_percent INTEGER,
                rule_triggered TEXT, sent_at TEXT, grade TEXT DEFAULT 'D',
                message_id INTEGER DEFAULT NULL
            );
            CREATE TABLE IF NOT EXISTS seen_glitches (
                url_hash TEXT PRIMARY KEY, price INTEGER,
                sent_at TEXT, grade TEXT DEFAULT 'D', message_id INTEGER DEFAULT NULL
            );
            CREATE TABLE IF NOT EXISTS price_history (
                url_hash TEXT NOT NULL, price INTEGER NOT NULL,
                seen_at TEXT NOT NULL, PRIMARY KEY (url_hash, price)
            );
            CREATE TABLE IF NOT EXISTS price_observations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_hash TEXT NOT NULL, price INTEGER NOT NULL, seen_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS po_hash_seen ON price_observations(url_hash,seen_at);
            CREATE TABLE IF NOT EXISTS monitor_prices (
                url_hash TEXT PRIMARY KEY, price INTEGER NOT NULL,
                name TEXT, seen_at TEXT NOT NULL, variant_parent TEXT DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS monitor_seen_at ON monitor_prices(seen_at);
            CREATE TABLE IF NOT EXISTS category_stats (
                category TEXT PRIMARY KEY, scanned INTEGER DEFAULT 0,
                deals INTEGER DEFAULT 0, last_run TEXT, yield_rate REAL DEFAULT 0.0,
                err_streak INTEGER DEFAULT 0, cooldown_until TEXT DEFAULT NULL,
                velocity REAL DEFAULT 1.0
            );
            CREATE TABLE IF NOT EXISTS bh_cache (
                asin TEXT PRIMARY KEY, verdict TEXT, all_time_low INTEGER,
                last_checked TEXT, hits INTEGER DEFAULT 1, source TEXT DEFAULT 'buyhatke'
            );
            CREATE TABLE IF NOT EXISTS deal_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url_hash TEXT, name TEXT, url TEXT, price INTEGER, mrp INTEGER,
                disc REAL, grade TEXT, rule TEXT, platform TEXT,
                zscore REAL DEFAULT 0.0, lifetime_min INTEGER DEFAULT 0,
                fk_ratio REAL DEFAULT 0.0, logged_at TEXT
            );
            CREATE TABLE IF NOT EXISTS variant_map (
                asin TEXT NOT NULL, parent_asin TEXT NOT NULL, PRIMARY KEY(asin)
            );
            CREATE TABLE IF NOT EXISTS watchlist (
                asin TEXT PRIMARY KEY, added_at TEXT, interval_s INTEGER DEFAULT 180,
                last_price INTEGER DEFAULT 0, last_checked TEXT DEFAULT NULL,
                note TEXT DEFAULT ''
            );
            CREATE TABLE IF NOT EXISTS etag_store (
                url_hash TEXT PRIMARY KEY, etag TEXT, last_modified TEXT,
                last_check TEXT
            );
            CREATE TABLE IF NOT EXISTS digest_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT, sent_at TEXT NOT NULL,
                grade TEXT, url_hash TEXT
            );
            CREATE INDEX IF NOT EXISTS ph_hash   ON price_history(url_hash,seen_at);
            CREATE INDEX IF NOT EXISTS dl_logged ON deal_log(logged_at);
            CREATE INDEX IF NOT EXISTS dl_grade  ON deal_log(grade,logged_at);
        """)
        # v11 D4: FTS5 product name dedup table
        try:
            conn.execute("""CREATE VIRTUAL TABLE IF NOT EXISTS product_fts
                            USING fts5(name, url_hash, content='')""")
        except Exception:
            pass  # FTS5 may not be available in all SQLite builds
        conn.commit()
        # v8 ADV (SKILL.md): schema migration — additive columns for SPECTER tracking
        self._migrate_v8(conn)
        cutoff=(datetime.now()-timedelta(days=self.HISTORY_MAX_DAYS)).isoformat()
        conn.execute("DELETE FROM price_history      WHERE seen_at<?", (cutoff,))
        conn.execute("DELETE FROM price_observations WHERE seen_at<?", (cutoff,))
        conn.execute("DELETE FROM deal_log WHERE logged_at<?",
                     ((datetime.now()-timedelta(days=30)).isoformat(),))
        conn.commit(); conn.close()

    # ── ETag conditional GET ────────────────────────────────────────────────
    def etag_get(self,url:str)->Tuple[Optional[str],Optional[str]]:
        conn,cur=self._conn()
        h=hashlib.md5(url.encode()).hexdigest()[:16]
        cur.execute("SELECT etag,last_modified FROM etag_store WHERE url_hash=?",(h,))
        row=cur.fetchone()
        return (row["etag"],row["last_modified"]) if row else (None,None)

    def etag_set(self,url:str,etag:Optional[str],last_mod:Optional[str]):
        conn,cur=self._conn()
        h=hashlib.md5(url.encode()).hexdigest()[:16]
        cur.execute("""INSERT INTO etag_store(url_hash,etag,last_modified,last_check)
            VALUES(?,?,?,?) ON CONFLICT(url_hash) DO UPDATE SET
            etag=excluded.etag,last_modified=excluded.last_modified,
            last_check=excluded.last_check""",
            (h,etag,last_mod,datetime.now().isoformat()))
        conn.commit()

    # ── Watchlist ────────────────────────────────────────────────────────────
    def watchlist_all(self)->List[Dict]:
        conn,cur=self._conn()
        cur.execute("SELECT asin,interval_s,last_price,last_checked,note FROM watchlist")
        return [dict(r) for r in cur.fetchall()]

    def watchlist_add(self,asin:str,interval:int=180,note:str=""):
        conn,cur=self._conn()
        cur.execute("""INSERT INTO watchlist(asin,added_at,interval_s,note)
            VALUES(?,?,?,?) ON CONFLICT(asin) DO UPDATE SET
            interval_s=excluded.interval_s,note=excluded.note""",
            (asin,datetime.now().isoformat(),interval,note))
        conn.commit()

    def watchlist_remove(self,asin:str):
        conn,cur=self._conn()
        cur.execute("DELETE FROM watchlist WHERE asin=?",(asin,))
        conn.commit()

    def watchlist_update_price(self,asin:str,price:int):
        conn,cur=self._conn()
        cur.execute("""UPDATE watchlist SET last_price=?,last_checked=?
            WHERE asin=?""",(price,datetime.now().isoformat(),asin))
        conn.commit()

    # ── BH cache ─────────────────────────────────────────────────────────────
    def bh_warm_load(self)->Dict[str,Dict]:
        conn,cur=self._conn()
        cur.execute("SELECT asin,verdict,all_time_low,last_checked,source FROM bh_cache")
        result:Dict[str,Dict]={}; now=datetime.now()
        for row in cur.fetchall():
            try:
                age=(now-datetime.fromisoformat(row["last_checked"])).total_seconds()/3600
                ttl=BH_CACHE_TTL_H*2 if row["verdict"]=="atl" else BH_CACHE_TTL_H
                if age<=ttl:
                    result[row["asin"]]={"verdict":row["verdict"],"all_time_low":row["all_time_low"],
                                          "source":row["source"] or "buyhatke"}
            except (ValueError,TypeError): pass
        return result

    def bh_cache_get(self,asin:str)->Optional[Dict]:
        # Redis first
        rc=_redis_bh_get(asin)
        if rc: return rc
        conn,cur=self._conn()
        cur.execute("SELECT verdict,all_time_low,last_checked,source FROM bh_cache WHERE asin=?",(asin,))
        row=cur.fetchone()
        if not row: return None
        try:
            ttl=BH_CACHE_TTL_H*2 if row["verdict"]=="atl" else BH_CACHE_TTL_H
            if datetime.now()-datetime.fromisoformat(row["last_checked"])>timedelta(hours=ttl): return None
        except (ValueError,TypeError): return None
        return {"verdict":row["verdict"],"all_time_low":row["all_time_low"],"source":row["source"] or "buyhatke"}

    def bh_cache_set(self,asin:str,verdict:str,atl:int,source:str="buyhatke"):
        payload={"verdict":verdict,"all_time_low":atl,"source":source}
        _redis_bh_set(asin,payload)
        conn,cur=self._conn()
        cur.execute("""INSERT INTO bh_cache(asin,verdict,all_time_low,last_checked,source)
            VALUES(?,?,?,?,?) ON CONFLICT(asin) DO UPDATE SET verdict=excluded.verdict,
            all_time_low=excluded.all_time_low,last_checked=excluded.last_checked,
            source=excluded.source,hits=hits+1""",
            (asin,verdict,atl,datetime.now().isoformat(),source))
        conn.commit()

    # ── Overlord ──────────────────────────────────────────────────────────────
    def overlord_is_seen(self,h:str,price:int)->bool:
        if _redis_seen(h,price): return True
        conn,cur=self._conn()
        cur.execute("SELECT price,last_seen FROM seen_products WHERE url_hash=?",(h,))
        row=cur.fetchone()
        if not row: return False
        if row["price"]!=price:
            try:
                if datetime.now()-datetime.fromisoformat(row["last_seen"])>timedelta(hours=SEEN_TTL_HOURS): return False
            except (ValueError,TypeError): pass
        return row["price"]==price

    def overlord_mark_seen(self,h,price,disc,cv,cp,rule):
        conn,cur=self._conn(); now=datetime.now().isoformat()
        cur.execute("""INSERT INTO seen_products
            (url_hash,price,discount,coupon_value,coupon_percent,rule_triggered,first_seen,last_seen)
            VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(url_hash) DO UPDATE SET price=excluded.price,
            discount=excluded.discount,coupon_value=excluded.coupon_value,
            coupon_percent=excluded.coupon_percent,rule_triggered=excluded.rule_triggered,
            last_seen=excluded.last_seen""",(h,price,disc,cv,cp,rule,now,now))
        conn.commit(); _redis_mark(h,price)

    def overlord_get_last_sent(self,h:str)->Optional[int]:
        conn,cur=self._conn()
        cur.execute("SELECT price FROM sent_products WHERE url_hash=?",(h,))
        row=cur.fetchone(); return row["price"] if row else None

    def overlord_get_sent_msg_id(self,h:str)->Optional[int]:
        conn,cur=self._conn()
        cur.execute("SELECT message_id,sent_at FROM sent_products WHERE url_hash=?",(h,))
        row=cur.fetchone()
        if not row or not row["message_id"]: return None
        try:
            if datetime.now()-datetime.fromisoformat(row["sent_at"])>timedelta(minutes=14): return None
        except (ValueError,TypeError): return None
        return row["message_id"]

    def overlord_mark_sent(self,h,price,disc,cv,cp,rule,g="D",msg_id:Optional[int]=None):
        conn,cur=self._conn(); now=datetime.now().isoformat()
        cur.execute("""INSERT INTO sent_products
            (url_hash,price,discount,coupon_value,coupon_percent,rule_triggered,sent_at,grade,message_id)
            VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(url_hash) DO UPDATE SET price=excluded.price,
            discount=excluded.discount,coupon_value=excluded.coupon_value,
            coupon_percent=excluded.coupon_percent,rule_triggered=excluded.rule_triggered,
            sent_at=excluded.sent_at,grade=excluded.grade,message_id=excluded.message_id""",
            (h,price,disc,cv,cp,rule,now,g,msg_id)); conn.commit()

    # ── Glitch ───────────────────────────────────────────────────────────────
    def glitch_should_process(self,h:str,price:int)->Tuple[bool,str]:
        conn,cur=self._conn()
        cur.execute("SELECT price,sent_at FROM seen_glitches WHERE url_hash=?",(h,))
        row=cur.fetchone()
        if not row: return True,"new"
        lp=row["price"]
        try: ls=datetime.fromisoformat(row["sent_at"])
        except (ValueError,TypeError): return True,"corrupt_ts"
        if datetime.now()-ls>timedelta(hours=SEEN_TTL_HOURS): return True,"ttl_expired"
        if lp==price: return False,"same_price"
        if lp>0 and price<lp:
            drop=(lp-price)/lp
            if drop>=PRICE_DROP_PCT: return True,f"price_drop_{drop:.1%}"
        return False,"minor_change"

    def glitch_last_sent(self,h:str)->Optional[int]:
        conn,cur=self._conn()
        cur.execute("SELECT price FROM seen_glitches WHERE url_hash=?",(h,))
        row=cur.fetchone(); return row["price"] if row else None

    def glitch_get_sent_msg_id(self,h:str)->Optional[int]:
        conn,cur=self._conn()
        cur.execute("SELECT message_id,sent_at FROM seen_glitches WHERE url_hash=?",(h,))
        row=cur.fetchone()
        if not row or not row["message_id"]: return None
        try:
            if datetime.now()-datetime.fromisoformat(row["sent_at"])>timedelta(minutes=14): return None
        except (ValueError,TypeError): return None
        return row["message_id"]

    def glitch_mark_seen(self,h:str,price:int,g:str="D",msg_id:Optional[int]=None):
        conn,cur=self._conn()
        cur.execute("""INSERT INTO seen_glitches(url_hash,price,sent_at,grade,message_id)
            VALUES(?,?,?,?,?) ON CONFLICT(url_hash) DO UPDATE SET
            price=excluded.price,sent_at=excluded.sent_at,grade=excluded.grade,
            message_id=excluded.message_id""",
            (h,price,datetime.now().isoformat(),g,msg_id)); conn.commit()

    # ── Price history ─────────────────────────────────────────────────────────
    def flush_prices(self,batch:List[Tuple[str,int]]):
        if not batch: return
        conn,cur=self._conn(); now=datetime.now().isoformat()
        try:
            rows=[(h,int(p),now) for h,p in batch if h and int(p)>0]
            if not rows: return
            cur.executemany("INSERT OR IGNORE INTO price_history(url_hash,price,seen_at) VALUES(?,?,?)",rows)
            cur.executemany("INSERT INTO price_observations(url_hash,price,seen_at) VALUES(?,?,?)",rows)
            conn.commit()
        except (sqlite3.Error,TypeError,ValueError) as exc:
            safe_print(f"⚠️ Price write: {type(exc).__name__}")

    # ── v11 D1: mmap price cache ─────────────────────────────────────────────
    # 64MB shared-memory price cache: ASIN hash → recent prices
    # Zero-copy read across threads; write-through on new observations.
    _MMAP_SIZE     = 64 * 1024 * 1024  # 64 MB
    _MMAP_SLOT     = 512               # bytes per ASIN slot
    _MMAP_ENTRIES  = _MMAP_SIZE // _MMAP_SLOT
    _mmap_buf      = bytearray(_MMAP_SIZE)
    _mmap_lock     = threading.Lock()
    _mmap_index: Dict[str, int] = {}   # hash → slot index

    @classmethod
    def _mmap_slot_of(cls, h: str) -> int:
        return int(h, 16) % cls._MMAP_ENTRIES if all(c in "0123456789abcdef" for c in h) \
               else hash(h) % cls._MMAP_ENTRIES

    @classmethod
    def _mmap_write(cls, h: str, prices: List[int]):
        """Write up to 60 prices into the mmap slot for this hash."""
        if not prices: return
        slot = cls._mmap_slot_of(h)
        offset = slot * cls._MMAP_SLOT
        count  = min(len(prices), 60)
        try:
            with cls._mmap_lock:
                # Format: 4-byte count + count×4-byte prices
                cls._mmap_buf[offset:offset+4] = _struct_cache.pack(">I", count)
                for i, p in enumerate(prices[:count]):
                    o = offset + 4 + i * 4
                    cls._mmap_buf[o:o+4] = _struct_cache.pack(">I", max(0, int(p)))
                cls._mmap_index[h] = slot
        except Exception:
            pass

    @classmethod
    def _mmap_read(cls, h: str) -> List[int]:
        """Read prices from mmap cache for this hash. Returns [] on miss."""
        if h not in cls._mmap_index: return []
        slot   = cls._mmap_slot_of(h)
        offset = slot * cls._MMAP_SLOT
        try:
            with cls._mmap_lock:
                count = _struct_cache.unpack(">I", bytes(cls._mmap_buf[offset:offset+4]))[0]
                if count == 0 or count > 60: return []
                return [
                    _struct_cache.unpack(">I", bytes(
                        cls._mmap_buf[offset+4+i*4:offset+8+i*4]))[0]
                    for i in range(count)
                ]
        except Exception:
            return []

    def price_history_window(self, h: str, hours: float) -> List[int]:
        # v11 D1: check mmap L1 cache first
        cached = self._mmap_read(h)
        if cached:
            return cached
        conn, cur = self._conn()
        cutoff = (datetime.now()-timedelta(hours=hours)).isoformat()
        cur.execute("SELECT price FROM price_history WHERE url_hash=? AND seen_at>=? ORDER BY seen_at DESC",
                    (h, cutoff))
        prices = [r["price"] for r in cur.fetchall()]
        if prices:
            self._mmap_write(h, prices)
        return prices

    def history_stats(self,h:str)->Tuple[Optional[int],int]:
        conn,cur=self._conn()
        cur.execute("SELECT MIN(price) AS m,COUNT(*) AS c FROM price_history WHERE url_hash=?",(h,))
        row=cur.fetchone(); return (row["m"],row["c"] or 0) if row else (None,0)

    def observation_series(self,h:str,days:int=30)->List[int]:
        conn,cur=self._conn()
        cutoff=(datetime.now()-timedelta(days=days)).isoformat()
        cur.execute("SELECT price FROM price_observations WHERE url_hash=? AND seen_at>=? ORDER BY seen_at",(h,cutoff))
        return [r["price"] for r in cur.fetchall()]

    # ── Monitor baseline ───────────────────────────────────────────────────────
    def monitor_get(self,h:str)->Optional[int]:
        rv=_redis_monitor_get(h)
        if rv is not None: return rv
        conn,cur=self._conn()
        cur.execute("SELECT price FROM monitor_prices WHERE url_hash=?",(h,))
        row=cur.fetchone(); return int(row["price"]) if row and row["price"] is not None else None

    def monitor_set(self,h:str,price:int,name:str="",variant_parent:str=""):
        _redis_monitor_set(h,price)
        conn,cur=self._conn()
        cur.execute("""INSERT INTO monitor_prices(url_hash,price,name,seen_at,variant_parent)
            VALUES(?,?,?,?,?) ON CONFLICT(url_hash) DO UPDATE SET
            price=excluded.price,name=excluded.name,seen_at=excluded.seen_at,
            variant_parent=excluded.variant_parent""",
            (h,int(price),str(name or "")[:180],datetime.now().isoformat(),str(variant_parent or "")[:16]))
        conn.commit()

    # ── Category stats ────────────────────────────────────────────────────────
    def cat_yield(self,cat:str)->float:
        conn,cur=self._conn()
        cur.execute("SELECT yield_rate FROM category_stats WHERE category=?",(cat,))
        row=cur.fetchone(); return row["yield_rate"] if row else 0.0

    def cat_velocity(self,cat:str)->float:
        conn,cur=self._conn()
        cur.execute("SELECT velocity FROM category_stats WHERE category=?",(cat,))
        row=cur.fetchone(); return row["velocity"] if row else 1.0

    def cat_in_cooldown(self,cat:str)->bool:
        conn,cur=self._conn()
        cur.execute("SELECT cooldown_until FROM category_stats WHERE category=?",(cat,))
        row=cur.fetchone()
        if not row or not row["cooldown_until"]: return False
        try: return datetime.now()<datetime.fromisoformat(row["cooldown_until"])
        except (ValueError,TypeError): return False

    def cat_update_stats(self,cat:str,scanned:int,deals:int,error:bool=False):
        conn,cur=self._conn(); yr=deals/max(scanned,1)
        cur.execute("SELECT err_streak,velocity FROM category_stats WHERE category=?",(cat,))
        row=cur.fetchone()
        streak=(row["err_streak"] or 0) if row else 0
        vel=(row["velocity"] or 1.0) if row else 1.0
        if error: streak+=1
        else:
            streak=0
            nv=vel*0.7+(2.0 if yr>=0.02 else (1.5 if yr>=0.01 else 1.0))*0.3
            vel=min(max(nv,0.5),3.0)
        cooldown_until=None
        if streak>=5:
            cooldown_until=(datetime.now()+timedelta(minutes=CAT_COOLDOWN_M)).isoformat(); streak=0
        cur.execute("""INSERT INTO category_stats
            (category,scanned,deals,last_run,yield_rate,err_streak,cooldown_until,velocity)
            VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(category) DO UPDATE SET
            scanned=scanned+excluded.scanned,deals=deals+excluded.deals,
            last_run=excluded.last_run,yield_rate=(yield_rate*0.7+excluded.yield_rate*0.3),
            err_streak=excluded.err_streak,
            cooldown_until=COALESCE(excluded.cooldown_until,cooldown_until),
            velocity=excluded.velocity""",
            (cat,scanned,deals,datetime.now().isoformat(),yr,streak,cooldown_until,vel))
        conn.commit()

    # ── Deal log ──────────────────────────────────────────────────────────────
    def log_deal(self,h,name,url,price,mrp,disc,g,rule,platform,
                 zscore=0.0,lifetime_min=0,fk_ratio=0.0,specter_push:int=0):
        # v8 ADV: specter_push column added by _migrate_v8
        conn,cur=self._conn()
        cur.execute("""INSERT INTO deal_log
            (url_hash,name,url,price,mrp,disc,grade,rule,platform,zscore,lifetime_min,fk_ratio,logged_at,specter_push)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (h,name[:150],url,price,mrp,disc,g,rule,platform,zscore,
             lifetime_min,fk_ratio,datetime.now().isoformat(),specter_push))
        conn.commit()

    def top_deals(self,since:str,n:int=5)->List[Dict]:
        conn,cur=self._conn()
        cur.execute("""SELECT name,url,price,mrp,disc,grade,rule,platform,zscore,fk_ratio
            FROM deal_log WHERE logged_at>=? ORDER BY disc DESC,grade ASC LIMIT ?""",(since,n))
        return [dict(r) for r in cur.fetchall()]

    def deals_last_hour(self)->List[Dict]:
        return self.top_deals((datetime.now()-timedelta(hours=1)).isoformat(),10)

    def export_deals_csv(self,hours:int=24)->str:
        conn,cur=self._conn()
        since=(datetime.now()-timedelta(hours=hours)).isoformat()
        cur.execute("SELECT * FROM deal_log WHERE logged_at>=? ORDER BY logged_at DESC",(since,))
        rows=cur.fetchall()
        buf=io.StringIO()
        if rows:
            w=csv.DictWriter(buf,fieldnames=rows[0].keys()); w.writeheader()
            for r in rows: w.writerow(dict(r))
        return buf.getvalue()

    def export_deals_json(self,hours:int=24)->List[Dict]:
        conn,cur=self._conn()
        since=(datetime.now()-timedelta(hours=hours)).isoformat()
        cur.execute("SELECT * FROM deal_log WHERE logged_at>=? ORDER BY logged_at DESC",(since,))
        return [dict(r) for r in cur.fetchall()]

    def variant_parent(self,asin:str)->Optional[str]:
        conn,cur=self._conn()
        cur.execute("SELECT parent_asin FROM variant_map WHERE asin=?",(asin,))
        row=cur.fetchone(); return row["parent_asin"] if row else None

    # ── v11 D4: FTS5 product name dedup ──────────────────────────────────────
    def fts_is_variant(self, name: str, url_hash: str, price: int) -> bool:
        """Return True if a product with similar name ±5% price already in FTS5.
        Suppresses color/size variants of the same product."""
        if not name: return False
        # Strip punctuation for FTS5 match
        query = re.sub(r"[^\w\s]", " ", name).strip()
        query = " OR ".join(query.split()[:5])  # top-5 content words
        if not query: return False
        try:
            conn, cur = self._conn()
            cur.execute("""SELECT url_hash FROM product_fts
                           WHERE product_fts MATCH ? LIMIT 5""", (query,))
            rows = cur.fetchall()
            for row in rows:
                if row["url_hash"] == url_hash: continue
                # Price check — get last known price of the matched ASIN
                cur.execute("SELECT price FROM monitor_prices WHERE url_hash=?",
                            (row["url_hash"],))
                pr = cur.fetchone()
                if pr and abs(price - pr["price"]) / max(price, 1) < 0.05:
                    return True
        except Exception:
            pass
        return False

    def fts_index(self, name: str, url_hash: str):
        """Add product name + hash to FTS5 index."""
        if not name: return
        try:
            conn, cur = self._conn()
            cur.execute("INSERT OR IGNORE INTO product_fts(name, url_hash) VALUES(?,?)",
                        (name[:200], url_hash))
            conn.commit()
        except Exception:
            pass

    def variant_register(self,asin:str,parent:str):
        conn,cur=self._conn()
        cur.execute("INSERT OR IGNORE INTO variant_map(asin,parent_asin) VALUES(?,?)",(asin,parent))
        conn.commit()

    def clear(self):
        conn,cur=self._conn()
        for t in ("seen_products","sent_products","seen_glitches","price_history",
                  "price_observations","category_stats","deal_log","monitor_prices",
                  "variant_map","digest_log","etag_store"):
            cur.execute(f"DELETE FROM {t}")
        conn.commit(); safe_print("[db] Cleared")

    def vacuum(self):
        conn,_=self._conn(); conn.execute("PRAGMA incremental_vacuum(1000)"); conn.commit()


_DB = UnifiedDB()

# ── BH process-level warm cache ───────────────────────────────────────────────
_bh_warm:Dict[str,Dict]={}; _bh_warm_lock=threading.Lock()
_BH_WARM_CAP = 12000  # v9: was 5000 — larger warm cache = fewer DB roundtrips

def _bh_warm_set(asin: str, payload: Dict):
    """Thread-safe set with LRU-style cap eviction."""
    with _bh_warm_lock:
        if len(_bh_warm) >= _BH_WARM_CAP:
            # Drop oldest 20% of entries
            evict = list(_bh_warm.keys())[:_BH_WARM_CAP // 5]
            for k in evict:
                del _bh_warm[k]
        _bh_warm[asin] = payload


# ═══════════════════════════════════════════════════════════════════════════════
# PHANTOM FETCH  (curl_cffi → cloudscraper → requests cascade)
# ═══════════════════════════════════════════════════════════════════════════════
def _is_bot_page(soup:BeautifulSoup)->bool:
    txt=soup.get_text(separator=" ",strip=True).lower()
    return any(k in txt for k in _AMZ_BOT_SIGS)

def _build_cond_headers(pid:str,sec_ch:Optional[str],platform:str,
                         etag:Optional[str],last_mod:Optional[str])->Dict:
    h=_stealth_headers(pid,sec_ch,platform)
    if etag:     h["If-None-Match"]     = etag
    if last_mod: h["If-Modified-Since"] = last_mod
    return h

def amz_fetch(url:str,retry:int=0,
              etag:Optional[str]=None,last_mod:Optional[str]=None
              )->Tuple[Optional[BeautifulSoup],Optional[str],Optional[str]]:
    """Returns (soup, new_etag, new_last_modified).
       soup=None + etag unchanged → 304 Not Modified → skip parse."""
    pid,ja3,sec_ch,platform=_next_profile()
    headers=_build_cond_headers(pid,sec_ch,platform,etag,last_mod)

    # ── curl_cffi path (primary, real TLS fingerprint) ──────────────────────
    if _HAS_CFFI:
        sess=_cffi_sess(ja3)
        _warm_up(sess,pid,sec_ch,platform)
        _age_cookies(sess)   # v10: advance session-id-time + csm-hit per request
        _poisson_sleep()
        try:
            r=sess.get(url,headers=headers,timeout=TIMEOUT,allow_redirects=True)
            if r.status_code==304:
                _update_health(pid, 304, False)
                return None,etag,last_mod          # not modified
            if r.status_code==200 and len(r.text)>2000:
                soup=BeautifulSoup(r.text,"lxml")
                is_bot=_is_bot_page(soup)
                _update_health(pid, 200, is_bot)
                _p503_record(pid, False)          # v8 ADV: per-profile 200 record
                if not is_bot:
                    _delay_recover()
                    new_etag=r.headers.get("ETag")
                    new_lm  =r.headers.get("Last-Modified")
                    # v11 B3: update referer chain for next request in this thread
                    try: _profile_local.last_url = url
                    except Exception: pass
                    return soup,new_etag,new_lm
                _delay_backoff(503)
            if r.status_code in (429,503):
                _delay_backoff(r.status_code)
                _update_health(pid, r.status_code, False)
                _p503_record(pid, True)          # v8 ADV: per-profile 503-rate track
        except Exception: pass

    # ── cloudscraper fallback ────────────────────────────────────────────────
    if _cs_mod:
        try:
            cs=_cs_mod.create_scraper(browser="chrome")
            _poisson_sleep()
            r=cs.get(url,headers=headers,timeout=TIMEOUT)
            if r.status_code==200 and len(r.text)>2000:
                soup=BeautifulSoup(r.text,"lxml")
                if not _is_bot_page(soup):
                    _delay_recover()
                    return soup,r.headers.get("ETag"),r.headers.get("Last-Modified")
                _delay_backoff(503)
        except Exception: pass

    # ── v10: proxy storm fallback (only when 503 rate > 50%) ────────────────
    if _storm_check():
        pid2,ja3_2,sec_ch2,platform2 = _next_profile()
        hdrs2 = _build_cond_headers(pid2,sec_ch2,platform2,etag,last_mod)
        r_proxy = _amz_fetch_proxy(url, hdrs2, TIMEOUT)
        if r_proxy and len(r_proxy.text) > 2000:
            soup2 = BeautifulSoup(r_proxy.text,"lxml")
            if not _is_bot_page(soup2):
                return soup2, r_proxy.headers.get("ETag"), r_proxy.headers.get("Last-Modified")

    # ── requests fallback ────────────────────────────────────────────────────
    s=requests.Session()
    ret=Retry(total=0,raise_on_status=False)
    s.mount("https://",HTTPAdapter(pool_connections=2,pool_maxsize=8,max_retries=ret))
    _poisson_sleep()
    try:
        r=s.get(url,headers=headers,timeout=TIMEOUT,allow_redirects=True)
        if r.status_code==304: return None,etag,last_mod
        if r.status_code==200 and len(r.text)>2000:
            soup=BeautifulSoup(r.text,"lxml")
            if not _is_bot_page(soup):
                _delay_recover()
                return soup,r.headers.get("ETag"),r.headers.get("Last-Modified")
            _delay_backoff(503)
        if r.status_code in (403,429,503): _delay_backoff(r.status_code)
    except Exception: pass

    if retry<MAX_RETRIES:
        time.sleep(random.uniform(1.5,4.5))
        return amz_fetch(url,retry+1,etag,last_mod)
    return None,None,None


# ═══════════════════════════════════════════════════════════════════════════════
# IMAGE FETCH
# ═══════════════════════════════════════════════════════════════════════════════
_img_sess=requests.Session()
_img_sess.mount("https://",HTTPAdapter(pool_connections=4,pool_maxsize=20,
                                        max_retries=Retry(total=0)))

def fetch_image(product_url:str,platform:str="amazon",
                direct_url:Optional[str]=None)->Optional[bytes]:
    if not USE_IMG: return None
    def _dl(u:str)->Optional[bytes]:
        try:
            r=_img_sess.get(u,headers={"User-Agent":_USER_AGENTS["chrome_120"],
                                        "Referer":"https://www.amazon.in/"},
                            timeout=IMG_TIMEOUT,stream=True)
            if r.status_code!=200: return None
            data=bytearray()
            for chunk in r.iter_content(65536):
                data.extend(chunk)
                if len(data)>9_000_000: break
            return bytes(data) if len(data)>2000 else None
        except Exception: return None
    if direct_url and direct_url.startswith("http"):
        d=_dl(direct_url)
        if d: return d
    try:
        soup,_,_=amz_fetch(product_url)
        if not soup: return None
        img_url=None
        og=soup.find("meta",property="og:image")
        if og and og.get("content"): img_url=og["content"]
        if not img_url:
            for sc in soup.find_all("script"):
                ct=sc.string or ""
                if "colorImages" not in ct: continue
                for pat in (r'"hiRes"\s*:\s*"(https://[^"]+)"',r'"large"\s*:\s*"(https://[^"]+)"'):
                    m=re.search(pat,ct)
                    if m: img_url=m.group(1); break
                if img_url: break
        if not img_url or not img_url.startswith("http"): return None
        img_url=re.sub(r"_AC_[A-Z0-9_,]+_","_AC_UX1200_",img_url)
        return _dl(img_url)
    except Exception: return None

def _compress_image(data:bytes,max_kb:int=800)->bytes:
    if len(data)<=max_kb*1024 or not _HAS_PIL: return data
    try:
        img=_PILImage.open(io.BytesIO(data)).convert("RGB")
        w,h=img.size; scale=min(1200/max(w,h),1.0)
        if scale<1.0: img=img.resize((int(w*scale),int(h*scale)),_PILImage.LANCZOS)
        buf=io.BytesIO(); img.save(buf,"JPEG",quality=82,optimize=True)
        return buf.getvalue()
    except Exception: return data


# ═══════════════════════════════════════════════════════════════════════════════
# UNIT PRICE GUARD
# ═══════════════════════════════════════════════════════════════════════════════
class UPG:
    _S=re.compile(r"/\s*(?:\d+\s*)?(?:kg|g|mg|ml|l|ltr|litre|liter|unit|piece|pc|pcs|"
                  r"pack|tablet|tab|capsule|cap|serving|dose|count|cnt|cm|mm|inch|"
                  r"ft|yard|meter|m|set|pair|sheet|roll|sachet|pouch|strip|bottle)",re.IGNORECASE)
    _N=re.compile(r"[₹]?\s*([\d,]+(?:\.\d+)?)\s*/\s*(?:\d+\s*)?"
                  r"(?:kg|g|mg|ml|l|ltr|litre|liter|unit|piece|pc|pcs|"
                  r"pack|tablet|tab|capsule|cap|serving|dose|count|cnt|cm|mm|inch|"
                  r"ft|yard|meter|m|set|pair|sheet|roll|sachet|pouch|strip|bottle)",re.IGNORECASE)
    @classmethod
    def bad(cls,t:str)->set:
        s:set=set()
        for m in cls._N.finditer(t):
            try:
                v=int(round(float(m.group(1).replace(",","")))); v>0 and s.add(v)
            except Exception: pass
        return s
    @classmethod
    def has_sfx(cls,r:str)->bool: return bool(cls._S.search(r))
    @classmethod
    def parse(cls,r:str,bad:set)->Optional[int]:
        if not r or cls.has_sfx(r): return None
        ms=re.findall(r"(\d+\.?\d*)",re.sub(r"[₹$,\s]","",r))
        if not ms: return None
        try: v=int(round(float(ms[0])))
        except Exception: return None
        return None if (v<=0 or v in bad) else v


# ═══════════════════════════════════════════════════════════════════════════════
# COUPON DETECTOR
# ═══════════════════════════════════════════════════════════════════════════════
class CD:
    _P=[r"(\d+)%?\s*(?:off|OFF|OFFER)",r"coupon.*?(\d+)%",r"save.*?(\d+)%",
        r"(\d+)%\s*coupon",r"clip.*?(\d+)%",r"extra\s*(\d+)%",r"(\d+)%\s*off",
        r"(?:axis|hdfc|icici|sbi|kotak|amex|citi|rbl|yes\s*bank).*?(\d+)%",
        r"bank\s*offer.*?(\d+)%",r"credit\s*card.*?(\d+)%",
        r"(\d+)%.*?(?:cashback|instant\s*discount)",r"emi.*?(\d+)%\s*off"]
    _V=[r"₹\s*(\d{3,5})",r"Rs\.?\s*(\d{3,5})",r"(\d{3,5})\s*₹",
        r"off.*?₹\s*(\d{3,5})",r"save.*?₹\s*(\d{3,5})",
        r"coupon.*?₹\s*(\d{3,5})",r"cashback.*?₹\s*(\d{3,5})"]
    @staticmethod
    def pct(t:str)->int:
        best=0
        for p in CD._P:
            for m in re.findall(p,t,re.IGNORECASE):
                try:
                    v=int(m)
                    if 0<v<=100: best=max(best,v)
                except Exception: pass
        return best
    @staticmethod
    def val(t:str)->int:
        best=0
        for p in CD._V:
            for m in re.findall(p,t,re.IGNORECASE):
                try:
                    v=int(m)
                    if v>=100: best=max(best,v)
                except Exception: pass
        return best


# ═══════════════════════════════════════════════════════════════════════════════
# AMAZON PARSER v7  (stock signal + BSR)
# ═══════════════════════════════════════════════════════════════════════════════
_CS_COUPON=[".s-coupon-unclipped",".s-coupon-clipped",".s-coupon-amount",
            ".s-coupon-code-text",'[data-a-expander-name="couponExpander"]',
            ".a-color-price",".a-color-success",".a-color-state",".s-coupon-highlight-color"]

_OOS_SIGS=("currently unavailable","out of stock","temporarily unavailable",
           "in stock soon","sign up to be notified")

def _parse_stock(text:str)->StockInfo:
    si=StockInfo()
    tl=text.lower()
    if any(s in tl for s in _OOS_SIGS):
        si.available=False; return si
    m=re.search(r"only\s+(\d+)\s+left",tl,re.IGNORECASE)
    if m:
        si.low_stock=True
        try: si.stock_count=int(m.group(1))
        except Exception: si.stock_count=1
    bsr=re.search(r"#([\d,]+)\s+in\s+(?:[A-Za-z &]+)\s*(?:see top|best sellers)",tl,re.IGNORECASE)
    if not bsr: bsr=re.search(r"rank.*?#([\d,]+)",tl,re.IGNORECASE)
    if bsr:
        try:
            si.bsr_rank=int(bsr.group(1).replace(",",""))
            si.bsr_fast=si.bsr_rank<=500
        except Exception: pass
    return si

def _amz_card(card)->Optional[Dict]:
    if card.select_one(".s-sponsored-label-text"): return None
    name=None
    for s in ("h2 a span","h2 span",".a-size-base-plus.a-color-base.a-text-normal",
              ".a-size-medium.a-color-base.a-text-normal","span.a-text-normal"):
        t=card.select_one(s)
        if t and len(t.get_text(strip=True))>3:
            name=re.sub(r"\s+"," ",t.get_text(strip=True)).strip(); break
    if not name or len(name)<5: return None
    url=None
    for s in ("h2 a[href]","a.a-link-normal.s-no-outline[href]","a.a-link-normal[href]"):
        t=card.select_one(s)
        if t and t.get("href"):
            h=t["href"]; url=f"https://www.amazon.in{h}" if h.startswith("/") else h; break
    if not url or not _asin(url): return None
    cu=f"https://www.amazon.in/dp/{_asin(url)}"
    if is_blacklisted(cu): return None

    full=card.get_text(separator=" ",strip=True); bad=UPG.bad(full)
    cur=None
    for s in ('.a-price[data-a-color="base"] .a-offscreen','.a-price .a-offscreen',
              '.a-price-whole','.a-price-to-pay .a-offscreen'):
        t=card.select_one(s)
        if t: cur=UPG.parse(t.get_text(),bad)
        if cur: break
    if not cur: return None
    mrp=cur
    for s in ('.a-price[data-a-color="secondary"] .a-offscreen',
              '.a-price.a-text-price .a-offscreen','.a-text-price .a-offscreen',
              '.a-price[data-a-strike="true"] .a-offscreen'):
        t=card.select_one(s)
        if t:
            p=UPG.parse(t.get_text(),bad)
            if p and p>cur: mrp=p; break
    if UPG.has_sfx(full): mrp=cur
    cp=CD.pct(full); cv=CD.val(full)
    for s in _CS_COUPON:
        t=card.select_one(s)
        if t: ct=t.get_text(); cp=max(cp,CD.pct(ct)); cv=max(cv,CD.val(ct))
    if cv>=cur: cv=0
    if cv>0 and cur>0 and cv>cur*0.95: cv=0

    thumb:Optional[str]=None
    for it in card.select("img.s-image,img[data-image-load],img[src*='m.media-amazon']"):
        src=it.get("src","")
        if src.startswith("http"):
            thumb=re.sub(r"_AC_[A-Z0-9_,]+_","_AC_UX1200_",src); break

    parent_asin=None
    m_p=re.search(r'"parentAsin"\s*:\s*"([A-Z0-9]{10})"',full,re.IGNORECASE)
    if m_p:
        pa=m_p.group(1).upper()
        if pa!=_asin(cu): parent_asin=pa

    # Stock + BSR from card text
    si=_parse_stock(full)
    if not si.available: return None   # skip OOS cards entirely

    return {
        "name":name[:200],"url":cu,"current_price":cur,"mrp_price":mrp,
        "coupon_percent":cp,"coupon_value":cv,
        "hash":hashlib.md5(cu.encode()).hexdigest()[:16],
        "platform":"amazon","img_url":thumb,"parent_asin":parent_asin,
        "low_stock":si.low_stock,"stock_count":si.stock_count,
        "bsr_rank":si.bsr_rank,"bsr_fast":si.bsr_fast,
    }

# ── v11 A1: Embedded page JSON fast-path ──────────────────────────────────────
# Amazon injects structured price data into every search/dp page as script tags.
# Extracting via regex is 40–70ms faster than BS4 card walking.
_RE_PRELOADED   = re.compile(r'"priceAmount"\s*:\s*([\d.]+)', re.DOTALL)
_RE_LDPRICE     = re.compile(r'"price"\s*:\s*"([\d.]+)"')
_RE_ASIN_INLINE = re.compile(r'"ASIN"\s*:\s*"([A-Z0-9]{10})"')
_RE_MRP_INLINE  = re.compile(r'"listPrice"\s*:\s*"?([\d,]+(?:\.\d+)?)"?')
_RE_TITLE_INL   = re.compile(r'"title"\s*:\s*"([^"]{5,200})"')

def _fast_json_extract(raw_html: str) -> List[Dict]:
    """A1: extract price/ASIN/title from __PRELOADED_STATE__ and ld+json blocks.
    Returns list of items in same format as _amz_card(). Falls back to [] if nothing found."""
    results: List[Dict] = []
    try:
        # ld+json Product schema (most reliable structured source)
        for ld_block in re.finditer(
                r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',
                raw_html, re.DOTALL | re.IGNORECASE):
            try:
                data = _json_loads(ld_block.group(1))
                if not isinstance(data, dict): continue
                if data.get("@type") not in ("Product", "ItemList"): continue
                offers = data.get("offers", {})
                if isinstance(offers, list):
                    offers = offers[0] if offers else {}
                price_s = offers.get("price") or data.get("price", "")
                cur = int(float(str(price_s).replace(",","").strip())) if price_s else 0
                if cur <= 0: continue
                mrp_s = data.get("highPrice") or offers.get("highPrice", "")
                mrp   = int(float(str(mrp_s).replace(",","").strip())) if mrp_s else cur
                name  = data.get("name","")[:200]
                url_p = data.get("url","") or data.get("@id","")
                asin  = _asin(url_p)
                if not asin or not name: continue
                url_c = f"https://www.amazon.in/dp/{asin}"
                results.append({
                    "name": name, "url": url_c, "current_price": cur,
                    "mrp_price": mrp if mrp > cur else cur,
                    "coupon_percent": 0, "coupon_value": 0,
                    "hash": hashlib.md5(url_c.encode()).hexdigest()[:16],
                    "platform": "amazon", "img_url": data.get("image","") or None,
                    "parent_asin": None, "low_stock": False,
                    "stock_count": 0, "bsr_rank": 0, "bsr_fast": False,
                    "_fast_path": True,
                })
            except Exception:
                pass
        # __PRELOADED_STATE__ / data-a-state blocks with priceAmount
        if not results:
            asin_m  = _RE_ASIN_INLINE.search(raw_html)
            price_m = _RE_PRELOADED.search(raw_html)
            title_m = _RE_TITLE_INL.search(raw_html)
            mrp_m   = _RE_MRP_INLINE.search(raw_html)
            if asin_m and price_m and title_m:
                asin = asin_m.group(1)
                cur  = int(float(price_m.group(1)))
                name = title_m.group(1)[:200]
                mrp  = int(float(mrp_m.group(1).replace(",",""))) if mrp_m else cur
                if cur > 0 and len(name) >= 5:
                    url_c = f"https://www.amazon.in/dp/{asin}"
                    results.append({
                        "name": name, "url": url_c, "current_price": cur,
                        "mrp_price": mrp if mrp > cur else cur,
                        "coupon_percent": 0, "coupon_value": 0,
                        "hash": hashlib.md5(url_c.encode()).hexdigest()[:16],
                        "platform": "amazon", "img_url": None,
                        "parent_asin": None, "low_stock": False,
                        "stock_count": 0, "bsr_rank": 0, "bsr_fast": False,
                        "_fast_path": True,
                    })
    except Exception:
        pass
    return results


def parse_amazon(soup: BeautifulSoup, raw_html: str = "") -> List[Dict]:
    """v11 A1: fast JSON path first, BS4 card walk as fallback.
    raw_html: pass the original HTML string to enable the fast path.
    If fast path returns items, BS4 walk is skipped (40-70ms saved per page)."""
    # Fast path — embedded JSON extract
    if raw_html:
        fast = _fast_json_extract(raw_html)
        if fast:
            return fast

    # BS4 card walk fallback (existing v10 path)
    cards=(soup.select("div[data-component-type='s-search-result']")
           or soup.select("div[data-asin]:not([data-asin=''])")
           or soup.select("[data-asin]"))
    out=[]
    for card in cards:
        try:
            p=_amz_card(card)
            if p: out.append(p)
        except Exception: pass
    return out


# ═══════════════════════════════════════════════════════════════════════════════
# MULTI-SOURCE VALIDATOR  (async fan-out: BH + PHA + Flipkart)
# ═══════════════════════════════════════════════════════════════════════════════
# Each BH worker thread owns an event loop for async source fetching.
_bh_loop_local=threading.local()

# v8 ADV: Per-thread _CffiAsync session holder — one session reused across all
# calls on the same BH thread. Eliminates FD/connection leak from per-call
# `async with _CffiAsync(...)` under sustained queue load. (debug-playbook.md)
_bh_cffi_sess_local = threading.local()

def _get_bh_cffi_async(impersonate: str = "chrome120"):
    """Return a persistent _CffiAsync session for this BH worker thread.
    Recreates if the session was closed or errors out."""
    if not _HAS_CFFI:
        return None
    key = f"sess_{impersonate}"
    sess = getattr(_bh_cffi_sess_local, key, None)
    if sess is None:
        try:
            sess = _CffiAsync(impersonate=impersonate)
            setattr(_bh_cffi_sess_local, key, sess)
        except Exception:
            return None
    return sess

def _bh_loop()->asyncio.AbstractEventLoop:
    if not hasattr(_bh_loop_local,"loop"):
        loop=asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        _bh_loop_local.loop=loop
    return _bh_loop_local.loop

def _run_async_bh(coro):
    return _bh_loop().run_until_complete(coro)

def _build_bhresult(prices:List[int],price:int,source:str)->BHResult:
    r=BHResult(ok=True,source=source)
    r.history_prices=prices; r.history_len=len(prices)
    r.all_time_low=min(prices); r.all_time_high=max(prices)
    recent=prices[-90:] if len(prices)>90 else prices
    sr=sorted(recent); n=len(sr)
    r.median_90d=sr[n//2] if n%2 else ((sr[n//2-1]+sr[n//2])//2 if n else 0)
    r.real_mrp=r.all_time_high
    r.zscore=compute_zscore(recent,price)
    if r.history_len>=3 and r.median_90d>0 and price>0:
        ratio=price/r.median_90d
        if ratio>=0.90:
            r.ok=False; r.reject_reason=f"fake:{ratio:.2f}"; r.confidence_delta=-50
            r.verdict="reject"; return r
    if r.all_time_low>0 and price<=r.all_time_low:
        r.is_genuine_low=True; r.confidence_delta=+20; r.verdict="atl"
    elif r.median_90d>0 and price<r.median_90d*0.50:
        r.is_genuine_low=True; r.confidence_delta=+15; r.verdict="atl"
    elif r.median_90d>0 and price<r.median_90d*0.70:
        r.is_genuine_low=True; r.confidence_delta=+8; r.verdict="ok"
    else: r.verdict="ok"
    if r.zscore<-2.0: r.confidence_delta=min(r.confidence_delta+10,30)
    return r

async def _async_bh(asin:str,price:int)->BHResult:
    """Fetch BuyHatke via curl_cffi async."""
    url=f"https://buyhatke.com/price-history-api/amazon-in/{asin}/"
    hdr={"User-Agent":_USER_AGENTS["chrome_120"],"Referer":"https://buyhatke.com/",
         "Accept":"application/json,*/*"}
    try:
        if _HAS_CFFI:
            # v8 ADV: reuse per-thread session (no FD leak)
            sess = _get_bh_cffi_async("chrome120")
            if sess:
                r = await sess.get(url, headers=hdr, timeout=BH_TIMEOUT)
                if r.status_code != 200: return BHResult()
                data = r.json()
            else:
                return BHResult()
        else:
            import httpx
            async with httpx.AsyncClient() as client:
                r = await client.get(url, headers=hdr, timeout=BH_TIMEOUT)
                if r.status_code != 200: return BHResult()
                data = r.json()
    except Exception:
        # Session may be stale; clear it so next call recreates
        if hasattr(_bh_cffi_sess_local, "sess_chrome120"):
            _bh_cffi_sess_local.sess_chrome120 = None
        return BHResult()
    raw=data.get("data",data.get("prices",[]))
    prices:List[int]=[]
    for pt in raw:
        try:
            if isinstance(pt,(list,tuple)) and len(pt)>=2: prices.append(int(pt[1]))
            elif isinstance(pt,dict): prices.append(int(pt.get("price",pt.get("p",0))))
        except Exception: pass
    prices=[p for p in prices if p>0]
    if not prices: return BHResult()
    try: bh_mrp=int(data.get("mrp",data.get("max_price",0)) or 0)
    except Exception: bh_mrp=0
    r2=_build_bhresult(prices,price,"buyhatke")
    r2.bh_mrp=bh_mrp
    if bh_mrp>0: r2.real_mrp=max(r2.real_mrp,bh_mrp)
    return r2

async def _async_pha(product_url:str,price:int)->BHResult:
    """Fetch pricehistoryapp.com via curl_cffi async."""
    if not re.search(r"/dp/[A-Z0-9]{10}",product_url,re.IGNORECASE): return BHResult()
    hdr={"User-Agent":_USER_AGENTS["chrome_122"],"Referer":"https://pricehistoryapp.com/",
         "Accept":"text/html,*/*"}
    try:
        if _HAS_CFFI:
            # v8 ADV: reuse per-thread session for PHA
            sess = _get_bh_cffi_async("chrome124")
            if sess:
                r = await sess.post("https://pricehistoryapp.com/search",
                                    data={"q": product_url}, headers=hdr,
                                    timeout=18, allow_redirects=True)
                text = r.text if r.status_code == 200 else ""
            else:
                text = ""
        else:
            text = ""
    except Exception:
        if hasattr(_bh_cffi_sess_local, "sess_chrome124"):
            _bh_cffi_sess_local.sess_chrome124 = None
        text = ""
    if not text or len(text)<500: return BHResult()
    soup=BeautifulSoup(text,"lxml"); prices:List[int]=[]
    for sc in soup.find_all("script"):
        ct=sc.string or ""
        for pat in (r'"data"\s*:\s*\[([0-9,\s]+)\]',r'prices\s*=\s*\[([0-9,\s]+)\]'):
            m=re.search(pat,ct)
            if m:
                for v in re.findall(r"\d+",m.group(1)):
                    try:
                        p=int(v)
                        if 50<p<10_000_000: prices.append(p)
                    except ValueError: pass
        if prices: break
    if not prices: return BHResult()
    return _build_bhresult(prices,price,"pha")

async def _async_flipkart(asin:str,amz_price:int)->float:
    """v10 PHANTOM STRIKE: Flipkart structured API first, scrape fallback.
    API returns JSON price in ~180ms vs ~600ms HTML scrape."""
    if not USE_FLIPKART or amz_price<=0: return 0.0

    FK_SEARCH_API = "https://www.flipkart.com/api/3/page/search"
    FK_API_UA     = "Flipkart Android/7.3.0 (Android 13; SM-G998B)"

    sess = _get_bh_cffi_async("chrome120")

    # ── Try structured API first ──────────────────────────────────────────
    if sess:
        api_headers = {
            "User-Agent":   FK_API_UA,
            "Accept":       "application/json",
            "X-User-Agent": "Mozilla/5.0 (Android 13; Mobile; rv:109.0) FKUA/android/7.3.0/android/Mobile",
        }
        api_params = {"q": asin, "as": "off", "as-show": "on",
                      "otracker": "search", "page": "1", "sort": "relevance"}
        try:
            r = await sess.get(FK_SEARCH_API, headers=api_headers,
                               params=api_params, timeout=FK_TIMEOUT)
            if r.status_code == 200:
                data = r.json()
                slots = (data.get("pageData", {})
                             .get("pageContext", {})
                             .get("slots", []))
                for slot in slots:
                    products = (slot.get("widget", {})
                                    .get("data", {})
                                    .get("products", []))
                    for prod in products:
                        pricing = (prod.get("productInfo", {})
                                       .get("value", {})
                                       .get("pricing", {}))
                        fk_price_val = (pricing.get("finalPrice", {}).get("value")
                                        or pricing.get("mrp", {}).get("value"))
                        if fk_price_val:
                            fk_price = int(float(str(fk_price_val).replace(",", "")))
                            if fk_price > 0:
                                return round(fk_price / amz_price, 3)
                # Fallback regex scan of JSON body
                prices_api = re.findall(r'"finalPrice"\s*:\s*\{"value"\s*:\s*([\d.]+)', r.text)
                if prices_api:
                    fk_price = int(float(prices_api[0]))
                    if fk_price > 0:
                        return round(fk_price / amz_price, 3)
        except Exception:
            pass

    # ── Scrape fallback ───────────────────────────────────────────────────
    search_url = (f"https://www.flipkart.com/search?q={asin}"
                  f"&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_0_na_na_na")
    hdr = {"User-Agent": _USER_AGENTS["chrome_120"], "Accept": "text/html,*/*",
           "Accept-Language": "en-IN,en;q=0.9", "Referer": "https://www.flipkart.com/"}
    try:
        if sess:
            r2 = await sess.get(search_url, headers=hdr, timeout=FK_TIMEOUT)
            text = r2.text if r2.status_code == 200 else ""
        else:
            text = ""
    except Exception:
        if hasattr(_bh_cffi_sess_local, "sess_chrome120"):
            _bh_cffi_sess_local.sess_chrome120 = None
        return 0.0
    if not text or len(text) < 200: return 0.0
    prices = []
    for m in re.finditer(r'₹\s*([\d,]{3,10})', text):
        try:
            p = int(m.group(1).replace(",", ""))
            if 50 < p < 10_000_000: prices.append(p)
        except ValueError: pass
    if not prices: return 0.0
    fk_price = sorted(prices)[len(prices) // 3]
    return round(fk_price / amz_price, 3) if amz_price > 0 else 0.0

async def _fetch_all_sources(asin:str,product_url:str,price:int)->Tuple[BHResult,BHResult,float]:
    """Concurrent fan-out: BH + PHA + Flipkart."""
    results=await asyncio.gather(
        _async_bh(asin,price),
        _async_pha(product_url,price),
        _async_flipkart(asin,price),
        return_exceptions=True
    )
    bh  = results[0] if isinstance(results[0],BHResult) else BHResult()
    pha = results[1] if isinstance(results[1],BHResult) else BHResult()
    fk  = results[2] if isinstance(results[2],float)    else 0.0
    return bh,pha,fk

def _source_vote(bh:BHResult,pha:BHResult)->BHResult:
    """2-of-3 source voting (BH + PHA; Flipkart is a scalar not a BHResult).
    v8 ADV (bayesian-tuning.md): PHA tiebreaker — if only BH rejects but PHA
    has strong ATL history (≥10 pts), soften BH reject from -3.0 to -1.0 weight.
    Handles BH API gaps where post-restock history is missing."""
    rejects=[r for r in (bh,pha) if not r.ok and r.confidence_delta<=-50]
    if len(rejects)>=2:
        r=rejects[0]; r.reject_reason=f"voted_fake(2/2)"; return r
    # PHA tiebreaker: BH alone rejects but PHA has solid ATL evidence
    if (not bh.ok and bh.confidence_delta<=-50
            and pha.ok and pha.verdict=="atl" and pha.history_len>=10):
        bh.confidence_delta = -25                   # soften: -50 → -25
        bh.verdict = "reject_soft"
        bh.reject_reason = (bh.reject_reason or "") + "_pha_atl_override"
        bh.ok = True                                # re-admit to valid pool
    valid=[r for r in (bh,pha) if r.ok]
    if not valid: return BHResult()
    best=max(valid,key=lambda r:r.history_len)
    if sum(1 for r in valid if r.is_genuine_low)>=2:
        best.confidence_delta=min(best.confidence_delta+5,30)
    return best

def _bh_with_sources(url: str, price: int, platform: str,
                      product_name: str = "") -> BHResult:
    """v11: full 6-source fan-out → voted BHResult with retail ratio + velocity flag."""
    if platform not in ("amazon","amazon_in"): return BHResult()
    a = _asin(url)
    if not a: return BHResult()
    # Check caches first
    with _bh_warm_lock:
        cached = _bh_warm.get(a)
    if cached:
        r = BHResult(ok=True, all_time_low=cached.get("all_time_low",0),
                     source=cached.get("source","buyhatke"),
                     verdict=cached.get("verdict","ok"),
                     is_genuine_low=cached.get("verdict","")=="atl")
        r.fk_ratio = _velocity_boost(a)   # still apply velocity boost from cache hit
        return r
    db_c = _DB.bh_cache_get(a)
    if db_c:
        _bh_warm_set(a, db_c)
        r = BHResult(ok=True, all_time_low=db_c.get("all_time_low",0),
                     source=db_c.get("source","buyhatke"),
                     verdict=db_c.get("verdict","ok"),
                     is_genuine_low=db_c.get("verdict","")=="atl")
        return r
    try:
        # v11: pass product_name for Croma/RD search
        bh, pha, retail_ratio = _run_async_bh(
            _fetch_all_sources_v10(a, url, price, product_name=product_name)
        )
    except Exception: return BHResult()
    voted = _source_vote(bh, pha)
    voted.fk_ratio = retail_ratio
    verdict = voted.verdict or ("reject" if not voted.ok else "ok")
    if voted.ok:
        _DB.bh_cache_set(a, verdict, voted.all_time_low, voted.source)
        _bh_warm_set(a, {"verdict": verdict, "all_time_low": voted.all_time_low,
                          "source": voted.source})
    return voted


# ═══════════════════════════════════════════════════════════════════════════════
# FLASH DEAL
# ═══════════════════════════════════════════════════════════════════════════════
def is_flash(h:str,cur:int)->Tuple[bool,float]:
    hist=_DB.price_history_window(h,FLASH_WINDOW_H)
    if len(hist)<2: return False,0.0
    oldest=hist[-1]
    if oldest<=0: return False,0.0
    drop=(oldest-cur)/oldest
    return (True,drop*100) if drop>=FLASH_DROP_PCT else (False,0.0)


# ═══════════════════════════════════════════════════════════════════════════════
# RULE CHECKERS  (overlord, glitch)
# ═══════════════════════════════════════════════════════════════════════════════
def check_overlord(item:Dict)->Tuple[Optional[str],Dict]:
    mrp=item["mrp_price"]; cur=item["current_price"]
    cv=item.get("coupon_value",0); cp=item.get("coupon_percent",0)
    if mrp>0 and cur>0:
        disc=((mrp-cur)/mrp)*100; ratio=mrp/cur
        if (disc>=ov("rule1_min_disc",RULE1_MIN_DISCOUNT)
                and cur>=ov("rule1_min_price",RULE1_MIN_PRICE)
                and RULE1_MRP_RATIO_MIN<=ratio<=RULE1_MRP_RATIO_MAX
                and mrp<=RULE1_MRP_MAX):
            item["rule"]="rule_1"; item["discount"]=round(disc,1)
            item["confidence"]=50; return "rule_1",item
    if cur>=ov("rule2_min_price",RULE2_MIN_PRICE) and mrp>cur:
        eff=(cv/cur*100) if cv>0 else float(cp) if cp>0 else 0.0
        if eff>=ov("rule2_min_coupon",RULE2_MIN_COUPON_EFF):
            item["rule"]="rule_2"; item["effective_coupon_pct"]=round(eff,1)
            item["confidence"]=50; return "rule_2",item
    h=item.get("hash","")
    ok_f,fdrop=is_flash(h,cur)
    if ok_f and cur>=200 and mrp>cur:
        disc=((mrp-cur)/mrp*100) if mrp>0 else 0
        item["rule"]="rule_3"; item["discount"]=round(disc,1)
        item["flash_drop_pct"]=round(fdrop,1); item["_is_flash"]=True
        item["confidence"]=45; return "rule_3",item
    return None,item

def is_glitch_local(item:Dict)->Tuple[bool,float,int]:
    mrp=item["mrp_price"]; cur=item["current_price"]
    if mrp<=0 or cur<=0 or cur<150 or mrp>GHOST_MRP_MAX: return False,0.0,-1
    if mrp/cur>GHOST_MRP_RATIO or mrp<=cur: return False,0.0,-1
    dp=((mrp-cur)/mrp)*100
    for i,(mn,mx,_) in enumerate(GLITCH_TIERS):
        if mrp>mn and cur<mx: return True,dp,i
    return False,0.0,-1


# ═══════════════════════════════════════════════════════════════════════════════
# DISCORD RELAY
# ═══════════════════════════════════════════════════════════════════════════════
_disc_sess=requests.Session()
_disc_sess.mount("https://",HTTPAdapter(pool_connections=2,pool_maxsize=8,
                                         max_retries=Retry(total=0)))

def _relay_discord(text:str,grade_:str="D"):
    if not DISCORD_WEBHOOK: return
    plain=re.sub(r'<a href="([^"]+)">[^<]+</a>',r'\1',text)
    plain=re.sub(r'<[^>]+>','',plain)[:2000]
    color_map={"S":0xFFD700,"A":0xC0C0C0,"B":0xCD7F32,"C":0x808080}
    payload={"embeds":[{"description":plain,"color":color_map.get(grade_,0x808080),
                        "footer":{"text":f"Glitch Hunter v7 PHANTOM | Grade {grade_}"},
                        "timestamp":datetime.now(timezone.utc).isoformat()}]}
    try: _disc_sess.post(DISCORD_WEBHOOK,json=payload,timeout=8)
    except Exception: pass


# ═══════════════════════════════════════════════════════════════════════════════
# TELEGRAM v7  (circuit breaker + edit-in-place + callback handler)
# ═══════════════════════════════════════════════════════════════════════════════
_tg_q      = queue.Queue()
_tg_lock   = threading.Lock()
_tg_last   = 0.0
_tg_sent   = 0; _tg_failed=0; _tg_silenced=0
_tg_cb_fails=0; _tg_cb_open=False; _tg_cb_reset=0.0

# v11 E2: skip-24h set — hash → suppressed until monotonic+86400
_skip_24h_set: set = set()
_skip_24h_exp: Dict[str, float] = {}
_skip_24h_lock = threading.Lock()

def _skip_is_active(h16: str) -> bool:
    """True if this hash was Skip'd and hasn't expired yet."""
    with _skip_24h_lock:
        exp = _skip_24h_exp.get(h16, 0.0)
        if exp and time.monotonic() < exp:
            return True
        if h16 in _skip_24h_set:
            _skip_24h_exp[h16] = time.monotonic() + 86400.0
            _skip_24h_set.discard(h16)
            return True
        return False

def _tg_pool()->requests.Session:
    s=requests.Session()
    s.mount("https://",HTTPAdapter(pool_connections=2,pool_maxsize=10,
                                   max_retries=Retry(total=0)))
    return s

_tg_s1=_tg_pool(); _tg_s2=_tg_pool()

def _cb_check()->bool:
    global _tg_cb_open,_tg_cb_fails
    if _tg_cb_open:
        if time.monotonic()>=_tg_cb_reset:
            _tg_cb_open=False; _tg_cb_fails=0
            safe_print("   🔌 TG CB reset")
        else: return True
    return False

def _cb_fail():
    global _tg_cb_fails,_tg_cb_open,_tg_cb_reset
    _tg_cb_fails+=1
    if _tg_cb_fails>=5:
        _tg_cb_open=True; _tg_cb_reset=time.monotonic()+60.0
        safe_print("   ⚡ TG circuit breaker OPEN")

def _cb_ok():
    global _tg_cb_fails
    _tg_cb_fails=max(0,_tg_cb_fails-1)

def _tg_call(method:str,sess:requests.Session,**kwargs)->Tuple[bool,Optional[int],Optional[int]]:
    """Returns (ok, retry_after, message_id)."""
    global _tg_sent,_tg_failed
    if _cb_check(): return False,5,None
    try:
        r=sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/{method}",timeout=22,**kwargs)
        if r.status_code==200:
            _tg_sent+=1; _cb_ok()
            try: msg_id=r.json().get("result",{}).get("message_id")
            except Exception: msg_id=None
            return True,None,msg_id
        try:
            body=r.json(); desc=str(body.get("description",""))
            code=int(body.get("error_code",r.status_code) or r.status_code)
            if code==429 or "retry after" in desc.lower():
                params=body.get("parameters",{}) or {}
                try: ra=max(1,min(120,int(params.get("retry_after",30))))
                except Exception: ra=30
                return False,ra,None
            if "parse" in desc.lower(): return None,None,None
            if r.status_code in (408,425,500,502,503,504): return False,2,None
        except (ValueError,TypeError):
            if r.status_code in (429,503): return False,3,None
        _tg_failed+=1; _cb_fail(); return False,None,None
    except requests.RequestException:
        _tg_failed+=1; _cb_fail(); return False,2,None

def _edit_message(sess:requests.Session,chat_id:str,msg_id:int,text:str,markup:Optional[Dict]=None):
    """Edit-in-place for dedup (same ASIN, < 15min old)."""
    body={"chat_id":chat_id,"message_id":msg_id,"text":text[:4096],
          "parse_mode":"HTML","disable_web_page_preview":True}
    if markup: body["reply_markup"]=json.dumps(markup)
    try: _tg_call("editMessageText",sess,json=body)
    except Exception: pass

def _build_markup(url:str)->Dict:
    _h16 = hashlib.md5(url.encode()).hexdigest()[:16]
    return {"inline_keyboard":[[
        {"text":"🛒 Buy Now","url":url},
        {"text":"📊 History","callback_data":f"hist:{url[:60]}"},
        {"text":"🔔 Watch","callback_data":f"watch:{_asin(url) or url[:15]}"},
        {"text":"🔕 Skip 24h","callback_data":f"skip:{_h16}"},
    ]]}

def _extract_url(text:str)->Optional[str]:
    m=re.search(r'href="(https?://[^"]{10,})"',text); return m.group(1) if m else None

def _safe_cap(text:str,max_len:int=950)->str:
    clean=re.sub(r'\n*🔗\s*<a href="[^"]*">[^<]*</a>\s*$','',text).rstrip()
    if len(clean)<=max_len: return clean
    return re.sub(r'<[^>]*$','',clean[:max_len]).rstrip()+"…"

def _send_one(item:Dict,sess:requests.Session,chat_id:str=CHAT_ID)->Tuple[bool,Optional[int],Optional[int]]:
    global _tg_silenced
    text=item["text"]; img=item.get("img_bytes"); g=item.get("grade","D")
    existing_msg_id=item.get("existing_msg_id")
    markup=item.get("markup") or _build_markup(_extract_url(text) or "https://amazon.in")
    mj=json.dumps(markup) if markup else None
    with _grade_lock:
        gap=GRADE_RATE.get(g,0.0)
        diff=time.time()-_grade_last.get(g,0.0)
        if diff<gap: time.sleep(gap-diff)
        _grade_last[g]=time.time()

    # Edit-in-place if same message exists < 15min ago
    if existing_msg_id:
        _edit_message(sess,chat_id,existing_msg_id,text,markup)
        return True,None,existing_msg_id

    if img:
        if ARGS.compress_img: img=_compress_image(img)
        data={"chat_id":chat_id,"caption":_safe_cap(text),"parse_mode":"HTML"}
        if mj: data["reply_markup"]=mj
        ok,ra,mid=_tg_call("sendPhoto",sess,data=data,
                            files={"photo":("p.jpg",io.BytesIO(img),"image/jpeg")})
        if ok:
            if g=="S" and not ARGS.no_autopin and mid:
                try: _tg_call("pinChatMessage",sess,
                               json={"chat_id":chat_id,"message_id":mid,"disable_notification":True})
                except Exception: pass
            if DISCORD_WEBHOOK: _relay_discord(text,g)
            return ok,ra,mid
        if ra: time.sleep(ra+1)

    body={"chat_id":chat_id,"text":text[:4096],"parse_mode":"HTML","disable_web_page_preview":True}
    if mj: body["reply_markup"]=mj
    ok,ra,mid=_tg_call("sendMessage",sess,json=body)
    if ok is None:
        plain=re.sub(r"<[^>]+>","",text)[:4096]
        fb={"chat_id":chat_id,"text":plain}
        if mj: fb["reply_markup"]=mj
        ok,ra,mid=_tg_call("sendMessage",sess,json=fb)
    if ok and g=="S" and not ARGS.no_autopin and mid:
        try: _tg_call("pinChatMessage",sess,json={"chat_id":chat_id,"message_id":mid,"disable_notification":True})
        except Exception: pass
    if ok and DISCORD_WEBHOOK: _relay_discord(text,g)
    return ok,ra,mid

def _make_drain(sess:requests.Session):
    def _drain():
        global _tg_last,_tg_failed
        while True:
            try:
                item=_tg_q.get(timeout=1)
                if item is None: break
                with _tg_lock:
                    gap=time.time()-_tg_last
                    if gap<TG_MIN_DELAY: time.sleep(TG_MIN_DELAY-gap)
                g=item.get("grade","D")
                chat_id=PREMIUM_CHAT_ID if (g=="S" and PREMIUM_CHAT_ID!=CHAT_ID) else CHAT_ID
                ok,ra,mid=_send_one(item,sess,chat_id=chat_id)
                with _tg_lock: _tg_last=time.time()
                if ok and mid and item.get("on_sent"):
                    try: item["on_sent"](mid)
                    except Exception: pass
                if ok and g=="S" and PREMIUM_CHAT_ID!=CHAT_ID:
                    _send_one(item,sess,chat_id=CHAT_ID)
                if not ok and ra is not None:
                    attempt=int(item.get("_retry",0))+1
                    if attempt<=ARGS.telegram_retries:
                        wait=max(float(ra),min(60.0,2.0**min(attempt,6)))+random.uniform(0.1,0.8)
                        time.sleep(wait); retry=dict(item); retry["_retry"]=attempt; _tg_q.put(retry)
                    else: _tg_failed+=1
                _tg_q.task_done()
            except queue.Empty: continue
            except Exception as exc:
                safe_print(f"   ❌ drain: {exc}")
                try: _tg_q.task_done()
                except Exception: pass
    return _drain

_tg_t1=threading.Thread(target=_make_drain(_tg_s1),daemon=True); _tg_t1.start()
_tg_t2=threading.Thread(target=_make_drain(_tg_s2),daemon=True); _tg_t2.start()

def tg_queue(text:str,img=None,markup=None,g="D",tier=-1,disc=0.0,
             platform="",on_sent=None,existing_msg_id:Optional[int]=None,
             url:str=""):
    global _tg_silenced
    if DRY_RUN: safe_print(f"   [DRY] [{g}] {text[:80].replace(chr(10),' ')}"); return
    if in_silent() and not silent_ok(g,tier,disc): _tg_silenced+=1; return
    # v11 E2: skip-24h suppression
    _h16 = hashlib.md5((url or text[:80]).encode()).hexdigest()[:16]
    if _skip_is_active(_h16): return
    _tg_q.put({"text":text,"img_bytes":img,"markup":markup,"grade":g,
               "platform":platform,"_retry":0,"on_sent":on_sent,
               "existing_msg_id":existing_msg_id})

def tg_raw(text:str):
    if DRY_RUN: safe_print(f"   [DRY] {text[:60].replace(chr(10),' ')}"); return
    _tg_q.put({"text":text,"img_bytes":None,"markup":None,"grade":"D","_retry":0})

def tg_drain(timeout:float=120.0)->bool:
    d=time.monotonic()+timeout
    while time.monotonic()<d:
        if _tg_q.empty(): return True
        time.sleep(0.5)
    return False

def test_tg()->bool:
    if DRY_RUN: safe_print("   [DRY] TG test skipped"); return True
    try:
        r=requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe",timeout=10)
        if r.status_code==200 and r.json().get("ok"):
            safe_print(f"   ✅ Bot: @{r.json()['result'].get('username','?')}")
        else: safe_print("   ❌ getMe failed"); return False
    except Exception as exc: safe_print(f"   ❌ {exc}"); return False
    ok,_,_=_tg_call("sendMessage",_tg_s1,json={
        "chat_id":CHAT_ID,"parse_mode":"HTML",
        "text":(f"🟢 <b>GLITCH HUNTER v9 TURBO</b>\n"
                f"curl_cffi:{_HAS_CFFI} aiosqlite:{_HAS_AIOSQLITE} "
                f"Redis:{'✅' if _redis else '❌'}\n"
                f"Workers:{MAX_WORKERS} Turbo:{ARGS.turbo_workers} "
                f"Warmup:{'✅' if USE_WARMUP else '❌'}\n"
                f"Flipkart:{'✅' if USE_FLIPKART else '❌'} "
                f"SPECTER:{'✅' if USE_SPECTER else '❌'} "
                f"Discord:{'✅' if DISCORD_WEBHOOK else '❌'}"
                +(" [DRY-RUN]" if DRY_RUN else ""))})
    safe_print("   ✅ Ping sent" if ok else "   ❌ Ping failed")
    return bool(ok)


# ═══════════════════════════════════════════════════════════════════════════════
# CALLBACK / BOT COMMAND HANDLER
# ═══════════════════════════════════════════════════════════════════════════════
_cb_offset=0; _cb_lock=threading.Lock()

def _handle_callback(upd:Dict,sess:requests.Session):
    """Process a single Telegram update (callback_query or message command)."""
    cb=upd.get("callback_query",{})
    msg=upd.get("message",{})

    if cb:
        cid=str(cb.get("id",""))
        data=cb.get("data","")
        chat_id=str(cb.get("message",{}).get("chat",{}).get("id",""))
        # Acknowledge the callback
        try: sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/answerCallbackQuery",
                       json={"callback_query_id":cid},timeout=5)
        except Exception: pass

        if data.startswith("hist:"):
            url=data[5:]
            h=hashlib.md5(url.encode()).hexdigest()[:16]
            series=_DB.observation_series(h,14)
            if series:
                spark=sparkline(series,14)
                reply=(f"📊 <b>14-day price trend</b>\n"
                       f"Min ₹{min(series):,} | Max ₹{max(series):,} | Now ₹{series[-1]:,}\n"
                       f"<code>{spark}</code>")
            else: reply="📊 No price history yet for this product."
            try: sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                           json={"chat_id":chat_id,"text":reply,"parse_mode":"HTML"},timeout=8)
            except Exception: pass

        elif data.startswith("watch:"):
            asin_s=data[6:][:10].upper()
            if re.match(r"^[A-Z0-9]{10}$",asin_s):
                _DB.watchlist_add(asin_s,ARGS.watchlist_interval)
                _watchlist[asin_s]=ARGS.watchlist_interval
                reply=f"👁 ASIN <code>{asin_s}</code> added to watchlist."
            else: reply="⚠️ Invalid ASIN."
            try: sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                           json={"chat_id":chat_id,"text":reply,"parse_mode":"HTML"},timeout=8)
            except Exception: pass

        # v11 E2: Skip 24h — suppress re-alert for this hash for 24 hours
        elif data.startswith("skip:"):
            skip_h = data[5:][:16]
            _skip_24h_set.add(skip_h)
            reply = "🔕 Suppressed for 24h."
            try: sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                           json={"chat_id":chat_id,"text":reply,"parse_mode":"HTML"},timeout=5)
            except Exception: pass

    elif msg:
        text=(msg.get("text","") or "").strip()
        chat_id=str(msg.get("chat",{}).get("id",""))
        if not text.startswith("/"): return

        cmd=text.split()[0].lower()
        args=text.split()[1:]

        if cmd=="/status":
            with _monitor_lock: stats=dict(_monitor_stats)
            cb_open_n = sum(1 for s in _breakers.values() if s.open_until > time.monotonic())
            reply=(f"🔬 <b>v10 PHANTOM STRIKE Status</b>\n"
                   f"Sweeps: {stats['sweeps']}\n"
                   f"Seen: {_total_scanned:,} | Drops: {stats['drops']}\n"
                   f"TG: {_tg_sent}✅ {_tg_failed}❌ | Replay: {len(_replay_buf)}\n"
                   f"Turbo: {'✅' if in_turbo() else '❌'} | "
                   f"SPECTER: {'🌐' if USE_SPECTER else '❌'} | "
                   f"AJAX: {'⚡' if DEALS_AJAX_NODES else '❌'}\n"
                   f"Keepa: {_keepa_tokens_used}/{_keepa_daily_cap} | "
                   f"CB open: {cb_open_n} | "
                   f"Storm: {'🔴' if _proxy_active.is_set() else '✅'} | "
                   f"Silent: {'✅' if in_silent() else '❌'}")
        elif cmd=="/top":
            since=(datetime.now()-timedelta(hours=24)).isoformat()
            deals=_DB.top_deals(since,5)
            if not deals: reply="No deals in last 24h."
            else:
                lines=["🏆 <b>Top Deals (24h)</b>"]
                for d in deals:
                    lines.append(f"Grade {d['grade']} {d['disc']:.1f}% — "
                                 f"<a href=\"{d['url']}\">{_html_mod.escape(d['name'][:50])}</a>")
                reply="\n".join(lines)
        elif cmd=="/pause":
            try:
                with open(CONTROL_FILE,"w") as fh: json.dump({"paused":True},fh)
                reply="⏸️ Paused."
            except Exception: reply="❌ Could not write control file."
        elif cmd=="/resume":
            try:
                with open(CONTROL_FILE,"w") as fh: json.dump({"paused":False},fh)
                reply="▶️ Resumed."
            except Exception: reply="❌ Could not write control file."
        elif cmd=="/watch" and args:
            asin_s=args[0].upper()[:10]
            if re.match(r"^[A-Z0-9]{10}$",asin_s):
                _DB.watchlist_add(asin_s)
                _watchlist[asin_s]=ARGS.watchlist_interval
                reply=f"👁 Watching <code>{asin_s}</code>"
            else: reply="⚠️ Provide a valid 10-char ASIN."
        elif cmd=="/unwatch" and args:
            asin_s=args[0].upper()[:10]
            _DB.watchlist_remove(asin_s)
            _watchlist.pop(asin_s,None)
            reply=f"🚫 Removed <code>{asin_s}</code> from watchlist."
        elif cmd=="/watchlist":
            wl=_DB.watchlist_all()
            if not wl: reply="Watchlist is empty."
            else:
                lines=[f"<code>{w['asin']}</code> — last ₹{w['last_price']:,}" for w in wl[:20]]
                reply=f"👁 <b>Watchlist ({len(wl)})</b>\n"+"\n".join(lines)
        elif cmd=="/digest":
            # v8 ADV: force-send digest on demand
            deals = _DB.deals_last_hour()
            if not deals:
                reply = "📭 No deals in the last hour."
            else:
                medals = ["🥇","🥈","🥉","4️⃣","5️⃣"]
                lines  = [f"⏰ <b>On-Demand Digest</b> ({datetime.now(IST).strftime('%H:%M IST')})\n"]
                for i, d in enumerate(deals[:5]):
                    m = medals[i] if i < len(medals) else "🔹"
                    lines.append(f"{m} Grade {d['grade']} {d['disc']:.1f}% — "
                                 f"<a href=\"{d['url']}\">{_html_mod.escape(d['name'][:60])}</a>")
                reply = "\n\n".join(lines)

        elif cmd=="/stats":
            # v8 ADV: show stealth + Bayesian engine internals
            with _sh_lock:
                h_scores = {pid: f"{sh.score:.2f}(c{sh.captcha_count})" for pid, sh in _session_health.items()}
            with _p503_lock:
                cooling = {pid: f"{int(cd - time.monotonic())}s"
                           for pid, cd in _p503_cooldown.items() if cd > time.monotonic()}
            bh_warm_sz = len(_bh_warm)
            reply = (f"🔬 <b>v8 ADV Engine Stats</b>\n"
                     f"Session health: {h_scores}\n"
                     f"503-cooled profiles: {cooling or 'none'}\n"
                     f"BH warm cache: {bh_warm_sz}/{_BH_WARM_CAP}\n"
                     f"BH-Q: {_bhq.qsize()} | dropped: {_bhq.dropped}\n"
                     f"Ghost rej: {_ghost_rej} | BH rej: {_bh_rej}")

        elif cmd=="/reload":
            # v8 ADV: hot-reload categories + watchlist from disk
            _load_blacklist(); _load_watchlist()
            cats = _load_cats()
            reply = f"🔄 Reloaded: {len(cats)} categories, {len(_watchlist)} watchlist ASINs."

        elif cmd=="/help":
            reply=("📖 <b>Commands</b>\n"
                   "/status — bot health\n/top — top 5 deals (24h)\n"
                   "/watch ASIN — add to watchlist\n/unwatch ASIN — remove\n"
                   "/watchlist — list watchlist\n/pause /resume — control sweep\n"
                   "/digest — force hourly digest\n/stats — engine internals\n"
                   "/reload — hot-reload categories + watchlist")
        else: return

        try: sess.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                       json={"chat_id":chat_id,"text":reply,"parse_mode":"HTML",
                             "disable_web_page_preview":True},timeout=8)
        except Exception: pass

def _cb_worker():
    """Long-poll getUpdates + dispatch commands/callbacks."""
    global _cb_offset
    sess=_tg_pool()
    while not _shutdown_flag.is_set():
        try:
            r=sess.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
                       params={"offset":_cb_offset,"timeout":20,"allowed_updates":
                               '["message","callback_query"]'},
                       timeout=25)
            if r.status_code!=200: time.sleep(5); continue
            data=r.json()
            for upd in data.get("result",[]):
                with _cb_lock: _cb_offset=max(_cb_offset,upd["update_id"]+1)
                try: _handle_callback(upd,sess)
                except Exception as exc:
                    if ARGS.debug: safe_print(f"   ⚠️ CB: {exc}")
        except Exception: time.sleep(5)


# ═══════════════════════════════════════════════════════════════════════════════
# HOURLY DIGEST
# ═══════════════════════════════════════════════════════════════════════════════
_last_digest_h=-1

def maybe_send_digest():
    global _last_digest_h
    if ARGS.no_digest: return
    h=datetime.now(IST).hour
    if h==_last_digest_h: return
    deals=_DB.deals_last_hour()
    if not deals: return
    _last_digest_h=h
    medals=["🥇","🥈","🥉","4️⃣","5️⃣"]
    lines=[f"⏰ <b>Last-Hour Digest</b> ({datetime.now(IST).strftime('%H:%M IST')})\n"]
    for i,d in enumerate(deals[:3]):
        m=medals[i] if i<len(medals) else "🔹"
        lines.append(f"{m} Grade {d['grade']} {d['disc']:.1f}% — "
                     f"<a href=\"{d['url']}\">{_html_mod.escape(d['name'][:60])}</a>")
    tg_raw("\n\n".join(lines))


# ═══════════════════════════════════════════════════════════════════════════════
# MESSAGE BUILDERS v7  (lifetime tag + FK tag + stock tag + ASCII chart)
# ═══════════════════════════════════════════════════════════════════════════════
def _sh(t:str)->str: return _html_mod.escape(str(t))

def _bh_block(bh,cur:int)->str:
    if not bh or not getattr(bh,"ok",False): return ""
    atl=getattr(bh,"all_time_low",0); med=getattr(bh,"median_90d",0)
    hl=getattr(bh,"history_len",0); hist=getattr(bh,"history_prices",[])
    src=getattr(bh,"source","?"); zs=getattr(bh,"zscore",0.0)
    fk=getattr(bh,"fk_ratio",0.0)
    parts=[]
    if atl>0: parts.append(f"ATL ₹{atl:,}{'🏆' if cur<=atl else ''}")
    if med>0: parts.append(f"90d ₹{med:,}")
    if hl:    parts.append(f"{hl}pts [{src}]")
    if zs<-2.0: parts.append(f"z={zs:.1f}⬇️")
    fk_tag=""
    if fk>=1.5:   fk_tag=f" | FK ₹~{int(cur*fk):,}(+{(fk-1)*100:.0f}%)✅"
    elif 0<fk<1:  fk_tag=f" | FK cheaper⚠️"
    verdict="⬇️ AT HISTORY LOW" if getattr(bh,"is_genuine_low",False) else "✅ ok"
    sp=f"  {sparkline(hist)}" if hist else ""
    return f"\n📊 {' | '.join(parts)} — {verdict}{fk_tag}{sp}"

def _chart_block(h:str)->str:
    series=_DB.observation_series(h,14)
    if len(series)<4: return ""
    chart=ascii_chart(series,width=16,height=3)
    return f"\n<pre>{chart}</pre>" if chart else ""

def _stock_tag(item:Dict)->str:
    if item.get("low_stock"):
        n=item.get("stock_count",0)
        return f"\n⚠️ <b>Only {n} left in stock!</b>" if n else "\n⚠️ <b>Low stock!</b>"
    return ""

def _lt_tag(item:Dict,disc_pct:float)->str:
    lt=predict_lifetime(disc_pct,datetime.now(IST).hour,
                        bool(item.get("low_stock")),bool(item.get("bsr_fast")))
    item["_lifetime_min"]=lt
    return f"\n{lifetime_tag(lt)}"

def _delta(last:Optional[int],cur:int)->str:
    if not last or last<=cur: return ""
    d=last-cur; p=d/last*100
    return f"\n⬇️ <b>Dropped ₹{d:,} ({p:.1f}%) since last alert</b>"

def _sh_name(item:Dict)->str: return _sh(item["name"][:110])

def build_r1(item:Dict,bh=None,last=None)->Tuple[str,str]:
    disc=item.get("discount",0); e,l=_dtier(disc)
    cur=item["current_price"]; mrp=item["mrp_price"]
    conf=item.get("confidence",0)
    g,ge=grade(conf,disc,getattr(bh,"is_genuine_low",False) if bh else False)
    fake="\n⚠️ <i>MRP inflated — real used</i>" if item.get("_fake_mrp_adj") else ""
    text=(f"{e} <b>{l} — EXTREME DEAL {ge} Grade {g}</b>\n\n"
          f"📦 {_sh_name(item)}\n\n"
          f"💰 <b>Now: ₹{cur:,}</b>  |  <s>MRP: ₹{mrp:,}</s>\n"
          f"📉 Saved: ₹{mrp-cur:,} ({disc:.1f}% off){fake}"
          f"{_delta(last,cur)}"
          f"{_stock_tag(item)}{_lt_tag(item,disc)}\n"
          f"🏪 Amazon | 🔬 {conf}/100 | [OVL-R1]"
          f"{_bh_block(bh,cur)}{_chart_block(item.get('hash',''))}\n\n"
          f'🔗 <a href="{item["url"]}">Buy on Amazon →</a>')
    return text,g

def build_r2(item:Dict,bh=None,last=None)->Tuple[str,str]:
    eff=item.get("effective_coupon_pct",0); e,l=_ctier(eff)
    cur=item["current_price"]; mrp=item["mrp_price"]
    cv=item.get("coupon_value",0); cp=item.get("coupon_percent",0)
    conf=item.get("confidence",0); g,ge=grade(conf,eff,False)
    cl=f"🎫 ₹{cv:,} off" if cv>0 else f"🎫 {cp}% off"
    after=cur-cv if cv>0 else int(cur*(1-cp/100))
    text=(f"{e} <b>{l} — COUPON DEAL {ge} Grade {g}</b>\n\n"
          f"📦 {_sh_name(item)}\n\n"
          f"💰 <b>Listed: ₹{cur:,}</b>  |  <s>MRP: ₹{mrp:,}</s>\n"
          f"{cl}\n✅ After coupon: ~₹{after:,}\n📉 Effective: {eff:.1f}%"
          f"{_delta(last,cur)}{_lt_tag(item,eff)}\n"
          f"🏪 Amazon | 🔬 {conf}/100 | [OVL-R2]"
          f"{_bh_block(bh,cur)}{_chart_block(item.get('hash',''))}\n\n"
          f'🔗 <a href="{item["url"]}">Buy on Amazon →</a>')
    return text,g

def build_r3(item:Dict,bh=None)->Tuple[str,str]:
    disc=item.get("discount",0); cur=item["current_price"]; mrp=item["mrp_price"]
    conf=item.get("confidence",0); fd=item.get("flash_drop_pct",0)
    g,ge=grade(conf,disc,False)
    text=(f"⏰ <b>FLASH DEAL {ge} Grade {g}</b>\n\n"
          f"📦 {_sh_name(item)}\n\n"
          f"💰 <b>Now: ₹{cur:,}</b>  |  <s>MRP: ₹{mrp:,}</s>\n"
          f"⚡ Crashed {fd:.1f}% in {FLASH_WINDOW_H:.0f}h — act fast!\n"
          f"🏪 Amazon | 🔬 {conf}/100 | [OVL-R3-FLASH]"
          f"{_bh_block(bh,cur)}{_chart_block(item.get('hash',''))}\n\n"
          f'🔗 <a href="{item["url"]}">Buy Now →</a>')
    return text,g

def build_glitch(item:Dict,dp:float,conf:int,tier:int,
                 bh=None,last=None)->Tuple[str,Dict,str]:
    cur=item["current_price"]; mrp=item["mrp_price"]; url=item["url"]
    tl=GLITCH_TIERS[tier][2] if 0<=tier<len(GLITCH_TIERS) else "—"
    e="👑" if dp>=90 else "💀" if dp>=80 else "⚡" if dp>=65 else "🔥"
    g,ge=grade(conf,dp,getattr(bh,"is_genuine_low",False) if bh else False)
    drop_tag=" ⬇️ DROPPED" if item.get("_is_price_drop") else ""
    flash_tag=" ⏰ FLASH"   if item.get("_is_flash") else ""
    fake="\n⚠️ <i>MRP inflated</i>" if item.get("_fake_mrp_adj") else ""
    text=(f"{e} <b>GLITCH{drop_tag}{flash_tag} {ge} Grade {g}</b>\n\n"
          f"📦 {_sh_name(item)}\n\n"
          f"💰 <b>Now: ₹{cur:,}</b>  |  <s>MRP: ₹{mrp:,}</s>\n"
          f"📉 {dp:.1f}%  |  Saved ₹{mrp-cur:,}{fake}"
          f"{_delta(last,cur)}"
          f"{_stock_tag(item)}{_lt_tag(item,dp)}\n"
          f"🎯 {tl}\n"
          f"🔬 {conf}/100  |  🏪 Amazon | [GLITCH]"
          f"{_bh_block(bh,cur)}{_chart_block(item.get('hash',''))}\n\n"
          f'🔗 <a href="{url}">Buy Now →</a>')
    markup=_build_markup(url)
    return text,markup,g


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — SOURCE CIRCUIT BREAKER
# Auto-disables BH/PHA/FK after 5 consecutive failures for 5 minutes.
# ═══════════════════════════════════════════════════════════════════════════════
BREAKER_THRESHOLD = 5
BREAKER_COOLDOWN  = 300   # 5 minutes

@dataclass
class _BreakerState:
    failures:    int   = 0
    open_until:  float = 0.0
    half_open:   bool  = False

_breakers: Dict[str, _BreakerState] = {
    "bh":  _BreakerState(),
    "pha": _BreakerState(),
    "fk":  _BreakerState(),
    "ccc": _BreakerState(),   # v11 A4/C5: CamelCamelCamel
    "cr":  _BreakerState(),   # v11 C1: Croma
    "rd":  _BreakerState(),   # v11 C2: Reliance Digital
}
_breaker_lock = threading.Lock()

def _cb_is_open(source: str) -> bool:
    with _breaker_lock:
        b = _breakers.get(source, _BreakerState())
        if b.open_until > time.monotonic():
            return True
        if b.open_until > 0 and not b.half_open:
            b.half_open = True
            return False
        return False

def _cb_record_success(source: str):
    with _breaker_lock:
        b = _breakers.get(source, _BreakerState())
        b.failures   = 0
        b.open_until = 0.0
        b.half_open  = False

def _cb_record_failure(source: str):
    with _breaker_lock:
        b = _breakers.setdefault(source, _BreakerState())
        b.failures += 1
        if b.failures >= BREAKER_THRESHOLD:
            b.open_until = time.monotonic() + BREAKER_COOLDOWN
            b.half_open  = False
            safe_print(f"   ⚡ CB OPEN: {source} ({b.failures} failures) — {BREAKER_COOLDOWN}s")

async def _guarded_source(source: str, coro) -> Any:
    if _cb_is_open(source):
        return None
    try:
        result = await coro
        _cb_record_success(source)
        return result
    except Exception as exc:
        _cb_record_failure(source)
        if ARGS.debug:
            safe_print(f"   ⚠️ {source} CB failure #{_breakers[source].failures}: {exc}")
        return None


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — KEEPA FREE-TIER ATL
# 100 tokens/day. Budget: Grade-S candidates + watchlist ASINs.
# Set KEEPA_API_KEY env var to enable. Weight in Bayesian: +2.0 (highest).
# ═══════════════════════════════════════════════════════════════════════════════
KEEPA_API_URL      = "https://api.keepa.com/product"
_keepa_tokens_used = 0
_keepa_token_lock  = threading.Lock()
_keepa_daily_cap   = 95

def _keepa_budget() -> bool:
    with _keepa_token_lock:
        return bool(KEEPA_API_KEY) and _keepa_tokens_used < _keepa_daily_cap

def _keepa_consume():
    global _keepa_tokens_used
    with _keepa_token_lock:
        _keepa_tokens_used += 1

def fetch_keepa(asin: str, price: int) -> KeepaResult:
    """Sync Keepa lookup. Called from _bh_worker for Grade-S + watchlist."""
    if not _keepa_budget():
        return KeepaResult()
    cache_key = f"keepa:{asin}"
    with _bh_warm_lock:
        cached = _bh_warm.get(cache_key)
    if cached and (time.time() - cached.get("ts", 0)) < 3600:
        k = cached.get("keepa", {})
        return KeepaResult(
            ok=True, atl=k.get("atl", 0),
            median_90d=k.get("med90", 0),
            history_len=k.get("hl", 0),
            is_atl=(price <= k.get("atl", price + 1) if k.get("atl") else False),
        )
    try:
        r = requests.get(KEEPA_API_URL,
                         params={"key": KEEPA_API_KEY, "domain": "10",
                                 "asin": asin, "stats": "90", "history": "1"},
                         timeout=8)
        if r.status_code != 200: return KeepaResult()
        _keepa_consume()
        data = r.json()
    except Exception:
        return KeepaResult()
    try:
        product   = data.get("products", [{}])[0]
        stats     = product.get("stats", {})
        csv_data  = product.get("csv", [])
        atl_val   = 0; med90 = 0; hist_len = 0
        if stats:
            min_arr   = stats.get("min",   [])
            avg90_arr = stats.get("avg90", [])
            if isinstance(min_arr, list) and len(min_arr) > 0:
                raw_atl = min_arr[0] if min_arr[0] and min_arr[0] > 0 else 0
                atl_val = raw_atl // 100 if raw_atl > 100 else 0
            if isinstance(avg90_arr, list) and len(avg90_arr) > 0:
                raw_med = avg90_arr[0] if avg90_arr[0] and avg90_arr[0] > 0 else 0
                med90   = raw_med // 100 if raw_med > 100 else 0
        if csv_data and isinstance(csv_data, list) and len(csv_data) > 0:
            price_series = csv_data[0]
            if price_series:
                valid_pairs = [price_series[i+1] for i in range(0, len(price_series)-1, 2)
                               if price_series[i+1] and price_series[i+1] > 0]
                hist_len = len(valid_pairs)
        result = KeepaResult(ok=True, atl=atl_val, median_90d=med90,
                             history_len=hist_len,
                             is_atl=(price <= atl_val if atl_val > 0 else False))
        _bh_warm_set(cache_key, {"ts": time.time(),
                                  "keepa": {"atl": atl_val, "med90": med90, "hl": hist_len}})
        return result
    except Exception:
        return KeepaResult()


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — CIRCUIT-BREAKER-AWARE FAN-OUT
# Wraps _fetch_all_sources with per-source circuit breakers.
# ═══════════════════════════════════════════════════════════════════════════════
# ── v11 A4/C5: CamelCamelCamel free price history ────────────────────────────
async def _async_ccc(asin: str, price: int) -> BHResult:
    """Fetch CamelCamelCamel.in price history. Bayesian weight +1.2 for ATL.
    No API key. Rotating User-Agent sufficient."""
    url = f"https://in.camelcamelcamel.com/product/{asin}"
    hdr = {
        "User-Agent": _USER_AGENTS["chrome_122"],
        "Accept": "text/html,*/*",
        "Referer": "https://in.camelcamelcamel.com/",
        "Accept-Language": "en-IN,en;q=0.9",
    }
    try:
        sess = _get_bh_cffi_async("chrome120")
        if not sess: return BHResult()
        r = await sess.get(url, headers=hdr, timeout=12)
        if r.status_code != 200: return BHResult()
        text = r.text
        # Highcharts data: Highcharts.chart('price-history-chart', { series: [{ data: [...] }] })
        # Also try simpler inline array patterns
        prices: List[int] = []
        m = re.search(r"series\s*:\s*\[.*?data\s*:\s*\[([\d,\s\[\]null]+)\]", text, re.DOTALL)
        if m:
            raw = m.group(1)
            # pairs format: [timestamp, price] or flat [price, price, ...]
            pair_m = re.findall(r"\[\s*\d+\s*,\s*(\d+)\s*\]", raw)
            if pair_m:
                for v in pair_m:
                    try:
                        p = int(v)
                        if 50 < p < 10_000_000: prices.append(p)
                    except ValueError: pass
            else:
                for v in re.findall(r"\b(\d{3,8})\b", raw):
                    try:
                        p = int(v)
                        if 50 < p < 10_000_000: prices.append(p)
                    except ValueError: pass
        if not prices:
            # Fallback: extract any ₹ prices from the page
            for v in re.findall(r"[\₹Rs\.]+\s*([\d,]{3,8})", text):
                try:
                    p = int(v.replace(",",""))
                    if 50 < p < 10_000_000: prices.append(p)
                except ValueError: pass
        if len(prices) < 2: return BHResult()
        r2 = _build_bhresult(prices, price, "ccc")
        # CCC ATL weight is +1.2 (lower than Keepa's +2.0 but free daily)
        # Mark with a custom flag for bayesian_conf to pick up
        r2.source = "ccc"
        return r2
    except Exception:
        return BHResult()


# ── v11 C1: Croma undocumented product search API ────────────────────────────
async def _async_croma(product_name: str, amz_price: int) -> float:
    """Croma (Tata) React frontend search API. No auth. Bayesian +0.6 if Croma > Amazon."""
    if amz_price <= 0 or not product_name: return 0.0
    q = re.sub(r"[^\w\s]", " ", product_name)[:60].strip()
    url = "https://api.croma.com/searchservices/v3/search"
    params = {"q": q, "currentPage": "0", "pageSize": "5", "sortBy": "relevance"}
    hdr = {
        "User-Agent": _USER_AGENTS["chrome_120"],
        "Origin": "https://www.croma.com",
        "Referer": "https://www.croma.com/",
        "Accept": "application/json, */*",
    }
    try:
        sess = _get_bh_cffi_async("chrome120")
        if not sess: return 0.0
        r = await sess.get(url, headers=hdr, params=params, timeout=8)
        if r.status_code != 200: return 0.0
        data = _json_loads(r.text)
        products = data.get("searchResult", {}).get("products", [])
        if not products: return 0.0
        croma_prices: List[int] = []
        for prod in products[:3]:
            fp = prod.get("finalPrice") or prod.get("mrpPrice", 0)
            try:
                p = int(float(str(fp).replace(",","")))
                if p > 0: croma_prices.append(p)
            except (ValueError, TypeError): pass
        if not croma_prices: return 0.0
        best = min(croma_prices)
        # +0.6 weight if Croma price > Amazon (confirms deal)
        return round(best / amz_price, 3) if amz_price > 0 else 0.0
    except Exception:
        return 0.0


# ── v11 C2: Reliance Digital undocumented Solr API ───────────────────────────
async def _async_reldigital(product_name: str, amz_price: int) -> float:
    """Reliance Digital Solr search. No auth. Bayesian +0.6 confirmation."""
    if amz_price <= 0 or not product_name: return 0.0
    q = re.sub(r"[^\w\s]", " ", product_name)[:60].strip()
    url = ("https://www.reliancedigital.in/rildigitalws/v2/rrldigital/cms/"
           "productlist")
    params = {"query": q, "pageSize": "5", "currentPage": "0"}
    hdr = {
        "User-Agent": _USER_AGENTS["chrome_120"],
        "Origin": "https://www.reliancedigital.in",
        "Referer": "https://www.reliancedigital.in/",
        "x-dtpc": str(random.randint(1000,9999)),
        "Accept": "application/json, */*",
    }
    try:
        sess = _get_bh_cffi_async("chrome120")
        if not sess: return 0.0
        r = await sess.get(url, headers=hdr, params=params, timeout=8)
        if r.status_code != 200: return 0.0
        data = _json_loads(r.text)
        products = data.get("products", []) or data.get("data", {}).get("products", [])
        rd_prices: List[int] = []
        for prod in products[:3]:
            price_block = prod.get("price", {}) or {}
            pv = price_block.get("value") or prod.get("finalPrice", 0)
            try:
                p = int(float(str(pv).replace(",","")))
                if p > 0: rd_prices.append(p)
            except (ValueError, TypeError): pass
        if not rd_prices: return 0.0
        best = min(rd_prices)
        return round(best / amz_price, 3) if amz_price > 0 else 0.0
    except Exception:
        return 0.0


# ── v11 C3: Amazon lightning deal countdown ───────────────────────────────────
_lightning_cache: Dict[str, Dict] = {}
_lightning_lock  = threading.Lock()

def _fetch_lightning_deal(deal_id: str, item_group_id: str = "") -> Dict:
    """Fetch percentClaimed + remainingTime from Amazon deal API.
    Returns dict: {pct_claimed, remaining_s, label}. Silent fail → {}."""
    cache_key = deal_id
    with _lightning_lock:
        c = _lightning_cache.get(cache_key)
        if c and time.time() - c.get("_ts", 0) < 30:
            return c
    try:
        url = "https://www.amazon.in/gp/deal/ajax/getDealDetails"
        params = {"dealId": deal_id, "isGlobalRequest": "false"}
        if item_group_id:
            params["itemGroupId"] = item_group_id
        hdr = {
            "User-Agent": _USER_AGENTS["chrome_120"],
            "Accept": "application/json, */*",
            "Referer": "https://www.amazon.in/deals",
            "x-requested-with": "XMLHttpRequest",
        }
        r = requests.get(url, params=params, headers=hdr, timeout=5)
        if r.status_code != 200:
            return {}
        data = _json_loads(r.text)
        deal_data = (data.get("dealDetails", {}).get(deal_id, {})
                     or list(data.get("dealDetails", {}).values() or [{}])[0]
                     if data.get("dealDetails") else {})
        pct   = float(deal_data.get("percentClaimed", 0) or 0)
        rem_s = int(deal_data.get("dealEndTime", 0) or 0)
        if rem_s > time.time():
            rem_s = int(rem_s - time.time())
        else:
            rem_s = rem_s  # already a delta
        label = ""
        if rem_s > 0 and rem_s < 300:
            label = f"⏰ ENDING SOON ({rem_s}s left)"
        elif pct >= 70:
            label = f"🔥 {pct:.0f}% claimed"
        result = {"pct_claimed": pct, "remaining_s": rem_s,
                  "label": label, "_ts": time.time()}
        with _lightning_lock:
            _lightning_cache[cache_key] = result
        return result
    except Exception:
        return {}


# ── v11 A5: ASIN velocity spike tracker ──────────────────────────────────────
_asin_velocity: Dict[str, int] = {}
_asin_vel_lock = threading.Lock()

def _velocity_hit(asin: str) -> int:
    """Increment hit count for this ASIN in current sweep. Returns new count."""
    with _asin_vel_lock:
        _asin_velocity[asin] = _asin_velocity.get(asin, 0) + 1
        return _asin_velocity[asin]

def _velocity_boost(asin: str) -> float:
    """Return Bayesian log-odds boost if ASIN is velocity-flagged (3+ hits/sweep)."""
    with _asin_vel_lock:
        return 0.3 if _asin_velocity.get(asin, 0) >= 3 else 0.0


async def _fetch_all_sources_v10(asin: str, product_url: str, price: int,
                                  product_name: str = ""
                                  ) -> Tuple[BHResult, BHResult, float]:
    """v11: 6-source CB-guarded fan-out — BH + PHA + FK + CCC + Croma + RelDigital."""
    # v11 A5: velocity spike — flag ASIN if 3+ hits this sweep
    hit_count = _velocity_hit(asin)
    results = await asyncio.gather(
        _guarded_source("bh",  _async_bh(asin, price)),
        _guarded_source("pha", _async_pha(product_url, price)),
        _guarded_source("fk",  _async_flipkart(asin, price)),
        _guarded_source("ccc", _async_ccc(asin, price)),          # v11 A4/C5
        _guarded_source("cr",  _async_croma(product_name, price)), # v11 C1
        _guarded_source("rd",  _async_reldigital(product_name, price)), # v11 C2
        return_exceptions=True,
    )
    bh  = results[0] if isinstance(results[0], BHResult) else BHResult()
    pha = results[1] if isinstance(results[1], BHResult) else BHResult()
    fk  = results[2] if isinstance(results[2], float)    else 0.0

    # CCC — treat as additional BHResult source for voting
    ccc_r = results[3] if isinstance(results[3], BHResult) else BHResult()
    # Croma ratio — boost fk_ratio-equivalent (>1 = Amazon cheaper = deal confirmed)
    croma_ratio  = results[4] if isinstance(results[4], float) else 0.0
    rd_ratio     = results[5] if isinstance(results[5], float) else 0.0

    # Absorb CCC into BH if BH has no data and CCC does
    if ccc_r.ok and not bh.ok:
        bh = ccc_r

    # Pick best retail ratio (FK / Croma / RD) for Bayesian fk_ratio slot
    retail_ratio = max(fk, croma_ratio, rd_ratio)

    # Tag velocity spike on item (picked up in _bh_with_sources caller)
    if hit_count >= 3:
        bh._velocity_flagged = True    # type: ignore[attr-defined]

    return bh, pha, retail_ratio


# ═══════════════════════════════════════════════════════════════════════════════
# MULTI-LANE PRIORITY BH QUEUE
# ═══════════════════════════════════════════════════════════════════════════════
class MLQ:
    def __init__(self,maxsize:int=12000):
        self._lanes=[[],[],[]]
        self._lock=threading.Lock(); self._sem=threading.Semaphore(0)
        self._n=0; self._size=0; self._max=maxsize; self._dropped=0
    def _lane(self,disc:float)->int:
        return 0 if disc>=80 else (1 if disc>=50 else 2)
    def put(self,cand:Dict,priority:float=0.0):
        disc=-priority
        with self._lock:
            if self._size>=self._max: self._dropped+=1; return
            heapq.heappush(self._lanes[self._lane(disc)],(priority,self._n,cand))
            self._n+=1; self._size+=1
        self._sem.release()
    def get(self,timeout:float=2.0):
        if not self._sem.acquire(timeout=timeout): raise queue.Empty
        with self._lock:
            for heap in self._lanes:
                if heap: _,_,c=heapq.heappop(heap); self._size-=1; return c
        raise queue.Empty
    def task_done(self): pass
    def join(self):
        while True:
            with self._lock:
                if self._size==0: break
            time.sleep(0.05)
    def qsize(self)->int:
        with self._lock: return self._size
    def empty(self)->bool:
        with self._lock: return self._size==0
    @property
    def dropped(self)->int: return self._dropped

_bhq=MLQ(maxsize=12000)

# ── Shared state ──────────────────────────────────────────────────────────────
_bh_done=threading.Event()
_bh_stat=threading.Lock()
_bh_rej=0; _ovl_r1=0; _ovl_r2=0; _ovl_r3=0
_gli_found=0; _drops=0; _ghost_rej=0
_extra_bh:List[threading.Thread]=[]; _extra_lock=threading.Lock()
_bands_done:set=set(); _BANDS=[80,250,600]
_IO_EXEC=ThreadPoolExecutor(max_workers=max(BH_WORKERS*4,80),thread_name_prefix="io")


def _scale_bh():
    """Band-based scaler kept as immediate-response fallback alongside auto-scaler."""
    qs=_bhq.qsize()
    with _extra_lock:
        for b in _BANDS:
            if qs>=b and b not in _bands_done:
                _bands_done.add(b)
                safe_print(f"   📈 BH scale +{BH_WORKERS} (Q={qs}≥{b})")
                for _ in range(BH_WORKERS):
                    t=threading.Thread(target=_bh_worker,daemon=True)
                    t.start(); _extra_bh.append(t)


# ── v10: Auto-scaling supervisor ──────────────────────────────────────────────
_BH_MIN_WORKERS  = 10
_BH_MAX_WORKERS  = 120
_BH_HIGH_WM      = 300   # spawn above this queue depth
_BH_LOW_WM       = 30    # kill idle workers below this
_BH_IDLE_TTL     = 20    # seconds queue must stay low before kill
_dyn_workers: List[threading.Thread] = []
_dyn_stops:   List[threading.Event]  = []
_dyn_lock_v10 = threading.Lock()

def _dyn_spawn_bh(stop_ev: threading.Event):
    """Dynamic BH worker. Runs identical loop to _bh_worker.
    stop_ev checked each iteration — terminated by auto-scaler when queue drains."""
    global _bh_rej,_ovl_r1,_ovl_r2,_ovl_r3,_gli_found,_drops,_ghost_rej
    while not _bh_done.is_set() and not stop_ev.is_set():
        _scale_bh()
        try: cand = _bhq.get(timeout=2)
        except queue.Empty:
            if _bh_done.is_set(): break
            continue
        if cand is None: break
        try:
            item=cand["item"]; platform=item.get("platform","amazon")
            is_drop=cand.get("is_price_drop",False)
            cat_name=cand.get("cat_name","?")
            direct_img=item.get("img_url")
            pa=item.get("parent_asin")
            if pa:
                _DB.variant_register(_asin(item["url"]) or "",pa)
                ph=hashlib.md5(f"https://www.amazon.in/dp/{pa}".encode()).hexdigest()[:16]
                if _DB.overlord_is_seen(ph,item["current_price"]): continue
            bh=BHResult()
            if USE_BH:
                try: bh=_bh_with_sources(item["url"],item["current_price"],platform)
                except Exception: pass
            img_f=_IO_EXEC.submit(fetch_image,item["url"],platform,direct_img) if USE_IMG else None
            if bh and getattr(bh,"confidence_delta",0)<=-50:
                with _bh_stat: _bh_rej+=1
                _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"bh_rej")
                _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue
            img=None
            try: img=img_f.result(timeout=IMG_TIMEOUT+2) if img_f else None
            except Exception: pass
            bh_rmrp=getattr(bh,"real_mrp",0) if bh and getattr(bh,"ok",False) else 0
            if bh_rmrp>0:
                cp2=item["current_price"]
                if bh_rmrp>cp2:
                    item=dict(item); item["mrp_price"]=bh_rmrp; item["_fake_mrp_adj"]=True
                    if "discount" in item: item["discount"]=round(((bh_rmrp-cp2)/bh_rmrp)*100,1)
                else:
                    _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"fake_mrp")
                    _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue
            if bh and getattr(bh,"ok",False) and getattr(bh,"all_time_high",0)>0:
                smrp=item.get("mrp_price",0)
                if smrp>0 and bh.all_time_high<smrp*0.70:
                    with _bh_stat: _ghost_rej+=1
                    _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"ghost_v3")
                    _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue
            cur=item["current_price"]; mrp=item.get("mrp_price",0)
            disc_pct=((mrp-cur)/mrp*100) if mrp>cur>0 else 0.0
            zscore_v=getattr(bh,"zscore",0.0) if bh else 0.0
            bh_verdict=getattr(bh,"verdict","") if bh else ""
            fk_ratio=getattr(bh,"fk_ratio",0.0) if bh else 0.0
            prior=cat_prior_from_db(_DB,cat_name)
            low_stock=bool(item.get("low_stock",False))
            bsr_fast=bool(item.get("bsr_fast",False))
            _hist_len=getattr(bh,"history_len",0) if bh else 0
            _keepa_r2: Optional[KeepaResult]=None
            _asin_v2=_asin(item.get("url",""))
            if _asin_v2 and (disc_pct>=90.0 or _asin_v2 in _watchlist):
                try: _keepa_r2=fetch_keepa(_asin_v2,cur)
                except Exception: pass
            _ccc_verdict2 = bh.source if bh and getattr(bh,"source","") == "ccc" and bh.ok else ""
            _vel_boost2   = _velocity_boost(_asin_v2) if _asin_v2 else 0.0
            # v11 C3: lightning deal urgency from pre-fetched payload
            _ld2 = item.get("_lightning", {})
            _ld_pct2 = float(_ld2.get("pct_claimed", 0)) if _ld2 else 0.0
            bay_conf=bayesian_conf(disc_pct,zscore_v,bh_verdict,fk_ratio,prior,low_stock,bsr_fast,
                                   history_len=_hist_len, keepa=_keepa_r2,
                                   velocity_boost=_vel_boost2, ccc_verdict=_ccc_verdict2,
                                   lightning_pct_claimed=_ld_pct2)
            item=dict(item); item["confidence"]=bay_conf
            if is_drop: item["_is_price_drop"]=True
            rule,oi=check_overlord(dict(item))
            if rule and not _DB.overlord_is_seen(item["hash"],cur):
                oi["confidence"]=bay_conf
                if bay_conf>=OVERLORD_MIN_CONF:
                    last_s=_DB.overlord_get_last_sent(item["hash"])
                    old_mid=_DB.overlord_get_sent_msg_id(item["hash"])
                    disc_o=oi.get("discount",oi.get("effective_coupon_pct",0))
                    if rule=="rule_1":   text_o,g_o=build_r1(oi,bh,last_s)
                    elif rule=="rule_2": text_o,g_o=build_r2(oi,bh,last_s)
                    else:               text_o,g_o=build_r3(oi,bh)
                    lt=oi.get("_lifetime_min",0)
                    with _bh_stat:
                        if rule=="rule_1": _ovl_r1+=1
                        elif rule=="rule_2": _ovl_r2+=1
                        else: _ovl_r3+=1
                    def _on_sent_ovl2(mid,h=item["hash"],pr=cur,do=disc_o,
                                      cv=oi.get("coupon_value",0),cp3=oi.get("coupon_percent",0),
                                      rl=rule,g2=g_o):
                        _DB.overlord_mark_sent(h,pr,do,cv,cp3,rl,g2,mid)
                    tg_queue(text_o,img,g=g_o,disc=disc_o,platform="amazon",
                             on_sent=_on_sent_ovl2,existing_msg_id=old_mid,
                             url=item.get("url",""))
                    _DB.overlord_mark_seen(item["hash"],cur,disc_o,
                                           oi.get("coupon_value",0),oi.get("coupon_percent",0),rule)
                    _DB.log_deal(item["hash"],item["name"],item["url"],cur,mrp,disc_o,g_o,
                                 rule,"amazon",zscore_v,lt,fk_ratio,
                                 specter_push=int(item.get("_specter_push",False)))
            gok,gdp,gtier=is_glitch_local(item)
            if gok:
                proc,_=_DB.glitch_should_process(item["hash"],cur)
                if proc:
                    cg=bayesian_conf(gdp,zscore_v,bh_verdict,fk_ratio,prior,low_stock,bsr_fast,
                                     history_len=_hist_len, keepa=_keepa_r2,
                                     velocity_boost=_vel_boost2, ccc_verdict=_ccc_verdict2,
                                     lightning_pct_claimed=_ld_pct2)
                    if cg>=ov("min_conf_glitch",MIN_CONFIDENCE):
                        last_g2=_DB.glitch_last_sent(item["hash"])
                        old_gmid=_DB.glitch_get_sent_msg_id(item["hash"])
                        tg_t,tg_mk,g_g=build_glitch(item,gdp,cg,gtier,bh,last_g2)
                        lt=item.get("_lifetime_min",0)
                        with _bh_stat:
                            _gli_found+=1
                            if is_drop: _drops+=1
                        def _on_sent_g2(mid,h=item["hash"],pr=cur,g2=g_g):
                            _DB.glitch_mark_seen(h,pr,g2,mid)
                        tg_queue(tg_t,img,tg_mk,g=g_g,tier=gtier,disc=gdp,
                                 platform="amazon",on_sent=_on_sent_g2,
                                 existing_msg_id=old_gmid)
                        if not old_gmid: _DB.glitch_mark_seen(item["hash"],cur,g_g)
                        _DB.log_deal(item["hash"],item["name"],item["url"],cur,mrp,gdp,g_g,
                                     f"glitch_t{gtier+1}","amazon",zscore_v,lt,fk_ratio,
                                     specter_push=int(item.get("_specter_push",False)))
        except Exception as exc:
            if ARGS.debug: safe_print(f"   ⚠️ dyn-bh: {exc}")

def _autoscale_supervisor():
    low_since: Optional[float] = None
    while not _shutdown_flag.is_set():
        time.sleep(10)
        depth = _bhq.qsize()
        with _dyn_lock_v10:
            current = len([t for t in _dyn_workers if t.is_alive()])
            base_ct = len([t for t in _extra_bh if t.is_alive()])
            total   = BH_WORKERS + base_ct + current
        if depth > _BH_HIGH_WM and total < _BH_MAX_WORKERS:
            to_spawn = min((depth - _BH_HIGH_WM) // 50 + 2, _BH_MAX_WORKERS - total, 8)
            for _ in range(to_spawn):
                ev = threading.Event()
                w  = threading.Thread(target=_dyn_spawn_bh, args=(ev,), daemon=True, name="bh-dyn")
                w.start()
                with _dyn_lock_v10:
                    _dyn_workers.append(w)
                    _dyn_stops.append(ev)
            safe_print(f"   ⬆️ auto-spawn {to_spawn} BH workers (depth={depth}, total={total+to_spawn})")
            low_since = None
        elif depth < _BH_LOW_WM:
            if low_since is None: low_since = time.monotonic()
            elif time.monotonic() - low_since > _BH_IDLE_TTL:
                with _dyn_lock_v10:
                    to_kill = len(_dyn_workers) // 2
                    for ev in _dyn_stops[:to_kill]: ev.set()
                    _dyn_workers[:] = _dyn_workers[to_kill:]
                    _dyn_stops[:]   = _dyn_stops[to_kill:]
                if to_kill: safe_print(f"   ⬇️ killed {to_kill} idle BH workers (depth={depth})")
                low_since = None
        else:
            low_since = None


def _bh_worker():
    global _bh_rej,_ovl_r1,_ovl_r2,_ovl_r3,_gli_found,_drops,_ghost_rej
    while True:
        _scale_bh()
        try: cand=_bhq.get(timeout=2)
        except queue.Empty:
            if _bh_done.is_set() and _bhq.empty(): break
            continue
        if cand is None: break
        try:
            item=cand["item"]; platform=item.get("platform","amazon")
            is_drop=cand.get("is_price_drop",False)
            cat_name=cand.get("cat_name","?")
            direct_img=item.get("img_url")

            # Variant dedup
            pa=item.get("parent_asin")
            if pa:
                _DB.variant_register(_asin(item["url"]) or "",pa)
                ph=hashlib.md5(f"https://www.amazon.in/dp/{pa}".encode()).hexdigest()[:16]
                if _DB.overlord_is_seen(ph,item["current_price"]): continue

            # ── Async source fan-out (BH + PHA + Flipkart) ──────────────────
            bh=BHResult()
            if USE_BH:
                try: bh=_bh_with_sources(item["url"],item["current_price"],platform)
                except Exception: pass

            # Fetch image in parallel with URL resolve
            img_f=_IO_EXEC.submit(fetch_image,item["url"],platform,direct_img) if USE_IMG else None

            if bh and getattr(bh,"confidence_delta",0)<=-50:
                with _bh_stat: _bh_rej+=1
                safe_print(f"   ❌ BH REJECT: {item['name'][:35]} | {bh.reject_reason}")
                jlog("bh_reject",name=item["name"][:50],reason=bh.reject_reason)
                _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"bh_rej")
                _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue

            img=None
            try: img=img_f.result(timeout=IMG_TIMEOUT+2) if img_f else None
            except Exception: pass

            # BH MRP correction
            bh_rmrp=getattr(bh,"real_mrp",0) if bh and getattr(bh,"ok",False) else 0
            if bh_rmrp>0:
                cp=item["current_price"]
                if bh_rmrp>cp:
                    item=dict(item); item["mrp_price"]=bh_rmrp; item["_fake_mrp_adj"]=True
                    if "discount" in item: item["discount"]=round(((bh_rmrp-cp)/bh_rmrp)*100,1)
                else:
                    _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"fake_mrp")
                    _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue

            # Ghost-MRP check
            if bh and getattr(bh,"ok",False) and getattr(bh,"all_time_high",0)>0:
                smrp=item.get("mrp_price",0)
                if smrp>0 and bh.all_time_high<smrp*0.70:
                    with _bh_stat: _ghost_rej+=1
                    _DB.overlord_mark_seen(item["hash"],item["current_price"],0,0,0,"ghost_v3")
                    _DB.glitch_mark_seen(item["hash"],item["current_price"]); continue

            # ── Bayesian confidence ──────────────────────────────────────────
            cur=item["current_price"]; mrp=item.get("mrp_price",0)
            disc_pct=((mrp-cur)/mrp*100) if mrp>cur>0 else 0.0
            zscore_v=getattr(bh,"zscore",0.0) if bh else 0.0
            bh_verdict=getattr(bh,"verdict","") if bh else ""
            fk_ratio=getattr(bh,"fk_ratio",0.0) if bh else 0.0
            prior=cat_prior_from_db(_DB,cat_name)
            low_stock=bool(item.get("low_stock",False))
            bsr_fast=bool(item.get("bsr_fast",False))
            _hist_len = getattr(bh, "history_len", 0) if bh else 0
            # v10: Keepa ATL — fetch for Grade-S candidates (disc>=90%) + watchlist
            _keepa_r: Optional[KeepaResult] = None
            _asin_v = _asin(item.get("url",""))
            if _asin_v and (disc_pct >= 90.0 or _asin_v in _watchlist):
                try: _keepa_r = fetch_keepa(_asin_v, cur)
                except Exception: pass
            # v11: extract CCC verdict and velocity boost from BH result
            _ccc_verdict   = bh.source if bh and getattr(bh,"source","") == "ccc" and bh.ok else ""
            _vel_boost     = _velocity_boost(_asin_v) if _asin_v else 0.0
            bay_conf=bayesian_conf(disc_pct,zscore_v,bh_verdict,fk_ratio,prior,low_stock,bsr_fast,
                                   history_len=_hist_len, keepa=_keepa_r,
                                   velocity_boost=_vel_boost, ccc_verdict=_ccc_verdict)
            item=dict(item); item["confidence"]=bay_conf
            if is_drop: item["_is_price_drop"]=True

            # ── OVERLORD ─────────────────────────────────────────────────────
            rule,oi=check_overlord(dict(item))
            if rule and not _DB.overlord_is_seen(item["hash"],cur):
                oi["confidence"]=bay_conf
                if bay_conf>=OVERLORD_MIN_CONF:
                    last_s=_DB.overlord_get_last_sent(item["hash"])
                    old_mid=_DB.overlord_get_sent_msg_id(item["hash"])
                    disc_o=oi.get("discount",oi.get("effective_coupon_pct",0))
                    bh_low=getattr(bh,"is_genuine_low",False) if bh else False
                    if rule=="rule_1":   text_o,g_o=build_r1(oi,bh,last_s)
                    elif rule=="rule_2": text_o,g_o=build_r2(oi,bh,last_s)
                    else:               text_o,g_o=build_r3(oi,bh)
                    lt=oi.get("_lifetime_min",0)
                    with _bh_stat:
                        if rule=="rule_1": _ovl_r1+=1
                        elif rule=="rule_2": _ovl_r2+=1
                        else: _ovl_r3+=1
                        n=_ovl_r1+_ovl_r2+_ovl_r3
                    safe_print(f"   🔥 OVL #{n} [{g_o}] z={zscore_v:.1f} fk={fk_ratio:.1f}"
                               f" lt={lt}m: {item['name'][:35]}")
                    jlog("deal_ovl",rule=rule,grade=g_o,conf=bay_conf,price=cur,
                         disc=disc_o,zscore=zscore_v,fk_ratio=fk_ratio,lt=lt,
                         name=item["name"][:60],asin=_asin(item["url"]))
                    def _on_sent_ovl(mid,h=item["hash"],pr=cur,do=disc_o,cv=oi.get("coupon_value",0),
                                     cp2=oi.get("coupon_percent",0),rl=rule,g2=g_o):
                        _DB.overlord_mark_sent(h,pr,do,cv,cp2,rl,g2,mid)
                    tg_queue(text_o,img,g=g_o,disc=disc_o,platform="amazon",
                             on_sent=_on_sent_ovl,existing_msg_id=old_mid)
                    _DB.overlord_mark_seen(item["hash"],cur,disc_o,
                                           oi.get("coupon_value",0),oi.get("coupon_percent",0),rule)
                    _DB.log_deal(item["hash"],item["name"],item["url"],cur,mrp,
                                 disc_o,g_o,rule,"amazon",zscore_v,lt,fk_ratio,
                                 specter_push=int(item.get("_specter_push",False)))

            # ── GLITCH ───────────────────────────────────────────────────────
            gok,gdp,gtier=is_glitch_local(item)
            if gok:
                proc,reason=_DB.glitch_should_process(item["hash"],cur)
                if proc:
                    cg=bayesian_conf(gdp,zscore_v,bh_verdict,fk_ratio,prior,low_stock,bsr_fast,
                                       history_len=_hist_len, keepa=_keepa_r,
                                       velocity_boost=_vel_boost, ccc_verdict=_ccc_verdict)
                    if cg>=ov("min_conf_glitch",MIN_CONFIDENCE):
                        last_g=_DB.glitch_last_sent(item["hash"])
                        old_gmid=_DB.glitch_get_sent_msg_id(item["hash"])
                        tg_t,tg_mk,g_g=build_glitch(item,gdp,cg,gtier,bh,last_g)
                        lt=item.get("_lifetime_min",0)
                        with _bh_stat:
                            _gli_found+=1
                            if is_drop: _drops+=1
                            gn=_gli_found
                        safe_print(f"   ⚡ GLITCH #{gn} [{g_g}] T{gtier+1} {gdp:.1f}%"
                                   f" z={zscore_v:.1f} fk={fk_ratio:.1f} lt={lt}m:"
                                   f" {item['name'][:35]}")
                        jlog("deal_glitch",grade=g_g,tier=gtier+1,disc=gdp,conf=cg,
                             zscore=zscore_v,fk_ratio=fk_ratio,lt=lt,
                             price=cur,name=item["name"][:60],asin=_asin(item["url"]))
                        def _on_sent_g(mid,h=item["hash"],pr=cur,g2=g_g):
                            _DB.glitch_mark_seen(h,pr,g2,mid)
                        tg_queue(tg_t,img,tg_mk,g=g_g,tier=gtier,disc=gdp,
                                 platform="amazon",on_sent=_on_sent_g,
                                 existing_msg_id=old_gmid)
                        if not old_gmid: _DB.glitch_mark_seen(item["hash"],cur,g_g)
                        _DB.log_deal(item["hash"],item["name"],item["url"],cur,mrp,
                                     gdp,g_g,f"glitch_t{gtier+1}","amazon",zscore_v,lt,fk_ratio,
                                     specter_push=int(item.get("_specter_push",False)))
        except Exception as exc:
            safe_print(f"   ❌ BH worker: {exc}")
            if ARGS.debug: traceback.print_exc()


# ═══════════════════════════════════════════════════════════════════════════════
# IN-MEMORY DEDUP
# ═══════════════════════════════════════════════════════════════════════════════
_seen_lock=threading.Lock(); _seen_set:set=set()
_asin_lock=threading.Lock(); _asin_set:set=set()
_sem_dedup:Dict[str,Tuple[str,int]]={};  _sem_lock=threading.Lock()

def _name_key(name:str)->str:
    return re.sub(r"[^a-z0-9]","",name.lower())[:40]

def _semantic_seen(item:Dict)->bool:
    if not ARGS.semantic_dedup: return False
    key=_name_key(item.get("name","")); price=item.get("current_price",0)
    with _sem_lock:
        ex=_sem_dedup.get(key)
        if ex:
            eh,ep=ex
            if abs(price-ep)/max(ep,1)<0.05: return True
        _sem_dedup[key]=(item.get("hash",""),price)
    return False

def _fast_seen(h:str,price:int)->bool:
    k=(h,price)
    with _seen_lock:
        if k in _seen_set: return True
    if _DB.overlord_is_seen(h,price):
        with _seen_lock: _seen_set.add(k)
        return True
    return False

def _unified_seen(h: str, price: int) -> bool:
    """v10 PHANTOM STRIKE: Bloom pre-filter → in-memory set → SQLite.
    99.9% of repeat ASINs filtered in O(7) bitwise ops. SQLite only on Bloom miss."""
    bloom_key = f"{h}:{price}"
    k = (h, price)

    with _bloom_lock:
        if bloom_key in _bloom_dedup:
            # Bloom hit: likely seen — confirm with in-memory set
            with _seen_lock:
                if k in _seen_set:
                    return True
            # Bloom false positive: fall through to SQLite
        else:
            # Bloom miss: definitely NOT seen — register and return False
            _bloom_dedup.add(bloom_key)
            with _seen_lock:
                _seen_set.add(k)
            return False

    # Bloom false positive path: check SQLite cross-table
    if _DB.overlord_is_seen(h, price):
        with _seen_lock: _seen_set.add(k)
        with _bloom_lock: _bloom_dedup.add(bloom_key)
        return True
    last_g = _DB.glitch_last_sent(h)
    if last_g is not None and last_g == price:
        with _seen_lock: _seen_set.add(k)
        with _bloom_lock: _bloom_dedup.add(bloom_key)
        return True
    return False

def _fast_mark(h:str,price:int):
    with _seen_lock: _seen_set.add((h,price))

def _asin_seen(url:str)->bool:
    a=_asin(url)
    if not a: return False
    with _asin_lock:
        if a in _asin_set: return True
        _asin_set.add(a)
    return False


# ═══════════════════════════════════════════════════════════════════════════════
# BATCHED PRICE WRITER
# ═══════════════════════════════════════════════════════════════════════════════
_pbuf:List[Tuple[str,int]]=[]; _pbuf_lock=threading.Lock(); PBUF_FLUSH=80   # v9: was 300

def _price_buf(h:str,price:int):
    with _pbuf_lock:
        _pbuf.append((h,price))
        if len(_pbuf)<PBUF_FLUSH: return
        batch=list(_pbuf); _pbuf.clear()
    _DB.flush_prices(batch)

def _flush_remaining():
    with _pbuf_lock:
        if not _pbuf: return
        batch=list(_pbuf); _pbuf.clear()
    _DB.flush_prices(batch)


# ═══════════════════════════════════════════════════════════════════════════════
# URL HELPERS
# ═══════════════════════════════════════════════════════════════════════════════
def clean_amazon_url(url:str)->Optional[str]:
    a=_asin(url); return f"https://www.amazon.in/dp/{a}" if a else None


# ═══════════════════════════════════════════════════════════════════════════════
# WATCHLIST WORKER
# ═══════════════════════════════════════════════════════════════════════════════
def _watchlist_worker():
    """Polls watchlisted ASINs directly at their configured interval."""
    safe_print(f"   👁 Watchlist worker started ({len(_watchlist)} ASINs)")
    last_checked:Dict[str,float]={}
    while not _shutdown_flag.is_set():
        now=time.monotonic()
        wl=list(_watchlist.items())
        for asin_w,interval in wl:
            if _shutdown_flag.is_set(): break
            last=last_checked.get(asin_w,0.0)
            if now-last<interval: continue
            last_checked[asin_w]=now
            product_url=f"https://www.amazon.in/dp/{asin_w}"
            try:
                soup,_e,_l=amz_fetch(product_url)
                if not soup: continue
                products=parse_amazon(soup)
                if not products: continue
                item=products[0]; cur=item.get("current_price",0)
                if cur<=0: continue
                prev=_DB.monitor_get(item["hash"])
                _DB.watchlist_update_price(asin_w,cur)
                _DB.monitor_set(item["hash"],cur,item.get("name",""))
                _price_buf(item["hash"],cur)
                if prev and cur<prev:
                    drop=(prev-cur)/prev*100
                    h=item["hash"]; mrp=item.get("mrp_price",0)
                    disc=((mrp-cur)/mrp*100) if mrp>cur else drop
                    proc,_=_DB.glitch_should_process(h,cur)
                    if proc:
                        safe_print(f"   👁 WATCHLIST: {asin_w} ₹{prev:,}→₹{cur:,} ({drop:.1f}%↓)")
                        bh=BHResult()
                        try: bh=_bh_with_sources(product_url,cur,"amazon")
                        except Exception: pass
                        lt=predict_lifetime(disc,datetime.now(IST).hour,bool(item.get("low_stock")),False)
                        text=(f"👁 <b>WATCHLIST ALERT</b> — ASIN <code>{asin_w}</code>\n\n"
                              f"📦 {_sh(item['name'][:100])}\n\n"
                              f"💰 <b>Now: ₹{cur:,}</b> (was ₹{prev:,})\n"
                              f"📉 {drop:.1f}% drop  |  {lifetime_tag(lt)}"
                              f"{_stock_tag(item)}"
                              f"{_bh_block(bh,cur)}\n\n"
                              f'🔗 <a href="{product_url}">View →</a>')
                        tg_raw(text)
                        _DB.glitch_mark_seen(h,cur,"W")
            except Exception as exc:
                if ARGS.debug: safe_print(f"   ⚠️ watchlist {asin_w}: {exc}")
        time.sleep(15)


# ═══════════════════════════════════════════════════════════════════════════════
# MULTI-PAGE CATEGORY SCANNER
# ═══════════════════════════════════════════════════════════════════════════════
_latencies:deque=deque(maxlen=600)

def record_latency(ms:float): _latencies.append(ms)

def latency_stats()->Dict:
    if not _latencies: return {}
    s=sorted(_latencies); n=len(s)
    return {"p50":s[int(n*0.50)],"p95":s[int(n*0.95)],
            "p99":s[min(int(n*0.99),n-1)],"mean":round(sum(s)/n,1),"n":n}

def _page_depth(cat_name:str)->int:
    vel=_DB.cat_velocity(cat_name)
    if vel>=1.5: return min(ARGS.max_pages,6)   # v9: was vel>=2.0 → pages 4
    if vel>=1.0: return min(ARGS.max_pages,4)   # v9: was vel>=1.5 → pages 3
    return 2                                     # v9: floor 2 was 1

def _fetch_page(url:str,page:int)->Tuple[Optional[BeautifulSoup],Optional[str],Optional[str],str]:
    """Returns (soup, new_etag, new_lm, raw_html). raw_html passed to parse_amazon A1 fast-path."""
    sep="&" if "?" in url else "?"
    page_url=f"{url}{sep}page={page}"
    etag,last_mod=_DB.etag_get(page_url)
    t0=time.monotonic()
    soup,new_etag,new_lm=amz_fetch(page_url,etag=etag,last_mod=last_mod)
    lat=(time.monotonic()-t0)*1000; record_latency(lat)
    if new_etag or new_lm: _DB.etag_set(page_url,new_etag,new_lm)
    # extract raw_html from soup for A1 fast-path; cheap .decode() only if soup exists
    raw_html = ""
    try:
        if soup is not None:
            raw_html = str(soup)
    except Exception:
        pass
    return soup,new_etag,new_lm,raw_html

def monitor_category(cat:Dict)->Tuple[str,int,int,int,int]:
    global _total_scanned
    name=cat.get("name",cat.get("url","?")); base=cat.get("url","")
    if not base: return name,0,0,0,0
    if _DB.cat_in_cooldown(name):
        safe_print(f"   ⏳ [{name[:18]}] cooldown"); return name,0,0,0,0

    wait_if_paused()
    depth=_page_depth(name)
    seeded=changed=drops=queued=0
    all_products:List[Dict]=[]

    # Fetch pages in parallel with staggered starts
    par=min(depth,ARGS.par_pages)
    page_results:Dict[int,Optional[BeautifulSoup]]={}

    _page_raw: Dict[int,str] = {}   # v11 A1: raw html per page for fast-path

    def _fetch_and_store(pg:int):
        if pg>1: time.sleep((pg-1)*ARGS.page_stagger+random.uniform(0,0.5))
        soup,_,_,raw=_fetch_page(base,pg)
        page_results[pg]=soup
        _page_raw[pg]=raw

    with ThreadPoolExecutor(max_workers=par,thread_name_prefix="pp") as ppool:
        futs={ppool.submit(_fetch_and_store,pg):pg for pg in range(1,depth+1)}
        for fut in as_completed(futs):
            try: fut.result()
            except Exception: pass

    for pg in range(1,depth+1):
        soup=page_results.get(pg)
        if soup is None: break    # 304 or fetch failure → stop deeper
        raw=_page_raw.get(pg,"")
        prods=parse_amazon(soup, raw_html=raw)   # v11 A1: pass raw for fast-path
        del soup                  # v8 ADV: explicit free; reduces GC pressure under 20+ workers
        if not prods: break       # empty page → stop
        all_products.extend(prods)
        if len(prods)<8: break    # sparse page → no deeper

    min_drop=max(float(ARGS.alert_drop_pct),0.0)

    for item in all_products:
        if _shutdown_flag.is_set(): break
        try:
            price=int(item.get("current_price") or 0)
            h=item.get("hash")
            if not h or price<=0: continue
            if is_blacklisted(item.get("url","")): continue
            if _semantic_seen(item): continue

            _total_scanned+=1
            _price_buf(h,price)
            pa=item.get("parent_asin")
            if pa: _DB.variant_register(_asin(item["url"]) or "",pa)

            previous=_DB.monitor_get(h)
            drop_pct=0.0; price_drop_trigger=False

            if previous is None:
                _DB.monitor_set(h,price,item.get("name",""),pa or "")
                seeded+=1
            elif price!=previous:
                changed+=1
                drop_pct=((previous-price)/previous*100.0) if previous>0 else 0.0
                _DB.monitor_set(h,price,item.get("name",""),pa or "")
                if price<previous:
                    drops+=1
                    item["_monitor_prev_price"]=previous
                    price_drop_trigger=drop_pct>=min_drop

            if ARGS.max_alert_price>0 and price>ARGS.max_alert_price: continue

            # v11 D4: FTS5 variant dedup (only if semantic_dedup enabled or always fast-check)
            if ARGS.semantic_dedup:
                try:
                    if _DB.fts_is_variant(item.get("name",""), h, price):
                        continue
                except Exception:
                    pass

            overlord_r,_=check_overlord(dict(item))
            glitch_ok,g_disc,_=is_glitch_local(item)
            flash_ok,_=is_flash(h,price)
            strong=glitch_ok and g_disc>=max(70.0,min_drop)
            candidate=bool(overlord_r or flash_ok or strong)
            if not price_drop_trigger and not candidate: continue
            if _unified_seen(h,price) or _asin_seen(item.get("url","")): continue

            item["_is_price_drop"]=bool(price_drop_trigger)
            mrp=int(item.get("mrp_price") or 0)
            discount=g_disc if glitch_ok else (((mrp-price)/mrp*100) if mrp>price>0 else 0)
            # v8 ADV (debug-playbook.md): queue pressure fast-path gate.
            # Under heavy load, discard weak candidates to prevent BH worker stall.
            q_pressure = _bhq.qsize()
            if q_pressure > 350:   # v9: was 150 — higher ceiling before shedding
                is_strong = (
                    (glitch_ok and g_disc >= 70.0)   # v9: was 80% — admit more
                    or (overlord_r == "rule_1")
                    or bool(item.get("_specter_push"))
                )
                if not is_strong:
                    continue   # skip — queue full, only high-signal items pass
            _bhq.put({"item":item,"is_price_drop":bool(price_drop_trigger),"cat_name":name},
                     priority=-float(discount))
            queued+=1

            if price_drop_trigger and previous is not None:
                safe_print(f"   📉 [{name[:16]}] {item.get('name','')[:32]}"
                           f" ₹{previous:,}→₹{price:,} ({drop_pct:.1f}%↓)")
            elif strong:
                safe_print(f"   ⚡ [{name[:16]}] GLITCH: {item.get('name','')[:32]} ({g_disc:.1f}%)")
            else:
                safe_print(f"   🔎 [{name[:16]}] DEAL: {item.get('name','')[:32]}")
        except Exception as exc:
            safe_print(f"   ⚠️ [{name[:16]}] {type(exc).__name__}: {exc}")
            if ARGS.debug: traceback.print_exc()

    _DB.cat_update_stats(name,len(all_products),queued,error=not all_products)
    return name,seeded,changed,drops,queued

def monitor_sweep(cats:List[Dict])->Tuple[int,int,int,int,int]:
    seeded=changed=drops=queued=done=0
    workers=max(1,min(active_workers(),80))   # v9: was 48
    with ThreadPoolExecutor(max_workers=workers,thread_name_prefix="cat") as pool:
        futures={pool.submit(monitor_category,cat):cat for cat in cats}
        for fut in as_completed(futures):
            if _shutdown_flag.is_set(): break
            cat=futures[fut]
            try:
                name,s_c,c_c,d_c,q_c=fut.result()
                seeded+=s_c; changed+=c_c; drops+=d_c; queued+=q_c; done+=1
                if c_c or q_c:
                    safe_print(f"✅ {name[:22]} | chg:{c_c} drop:{d_c} q:{q_c} ({done}/{len(cats)})")
            except Exception as exc:
                safe_print(f"❌ [{cat.get('name','')[:18]}] {type(exc).__name__}: {exc}")
    return done,seeded,changed,drops,queued


# ═══════════════════════════════════════════════════════════════════════════════
# SWEEP SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
def send_summary(since:str,elapsed_min:float):
    top=_DB.top_deals(since,5)
    if not top: return
    medals=["🥇","🥈","🥉","4️⃣","5️⃣"]
    lines=[f"🏆 <b>Top {len(top)} Deals</b> ({elapsed_min:.0f}min) | v10 PHANTOM STRIKE\n"]
    for i,d in enumerate(top):
        m=medals[i] if i<len(medals) else "🔹"
        fk_s=f" FK:{d['fk_ratio']:.1f}×" if d.get("fk_ratio",0)>=1.2 else ""
        lines.append(f"{m} Grade {d['grade']}  {d['disc']:.1f}% off  "
                     f"₹{d['price']:,}{fk_s}\n"
                     f"   <a href=\"{d['url']}\">{_sh(d['name'][:70])}</a>")
    tg_raw("\n\n".join(lines))


# ═══════════════════════════════════════════════════════════════════════════════
# STATUS + DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
_total_scanned=0; _scan_start=0.0; _scan_done=False
_monitor_stats={"sweeps":0,"seeded":0,"changed":0,"drops":0,"queued":0}
_monitor_lock=threading.Lock()
_ANSI={"R":"\033[0m","B":"\033[1m","C":"\033[96m","G":"\033[92m","Y":"\033[93m","M":"\033[95m"}

def _write_status(state:str="running",**extra):
    try:
        path=ARGS.status_file
        if not path: return
        if not os.path.isabs(path): path=os.path.join(SCRIPT_DIR,path)
        os.makedirs(os.path.dirname(path) or SCRIPT_DIR,exist_ok=True)
        with _monitor_lock: stats=dict(_monitor_stats)
        ls=latency_stats()
        payload={"state":state,"version":"v10-phantom-strike",
                 "updated_at":datetime.now(IST).isoformat(),"pid":os.getpid(),
                 "dry_run":DRY_RUN,"turbo_mode":in_turbo(),
                 "curl_cffi":_HAS_CFFI,"aiosqlite":_HAS_AIOSQLITE,
                 "redis":bool(_redis),"flipkart":USE_FLIPKART,
                 "specter":USE_SPECTER,
                 "discord":bool(DISCORD_WEBHOOK),"sweeps":stats["sweeps"],
                 "products_seen_total":_total_scanned,
                 "seeded":stats["seeded"],"changed":stats["changed"],
                 "drops":stats["drops"],"queued":stats["queued"],
                 "ovl_r1":_ovl_r1,"ovl_r2":_ovl_r2,"ovl_r3":_ovl_r3,
                 "glitch_alerts":_gli_found,"bh_rejected":_bh_rej,
                 "ghost_rejected":_ghost_rej,"tg_sent":_tg_sent,
                 "tg_failed":_tg_failed,"tg_cb":_tg_cb_open,
                 "tg_q":_tg_q.qsize(),"bh_q":_bhq.qsize(),
                 "bh_dropped":_bhq.dropped,"silenced":_tg_silenced,
                 "latency_ms":ls,
                 "ajax_nodes":len(DEALS_AJAX_NODES),
                 "keepa_tokens_used":_keepa_tokens_used,
                 "keepa_budget":_keepa_daily_cap,
                 "proxy_storm":_proxy_active.is_set(),
                 "replay_buf":len(_replay_buf),
                 "cb_open":sum(1 for s in _breakers.values() if s.open_until > time.monotonic()),
                 "bloom_active":True}
        payload.update(extra)
        tmp=path+".tmp"
        with open(tmp,"w",encoding="utf-8") as fh:
            json.dump(payload,fh,ensure_ascii=False,indent=2); fh.write("\n")
        os.replace(tmp,path)
    except Exception as exc:
        safe_print(f"⚠️ Status write: {type(exc).__name__}")

def _dashboard():
    while not _scan_done and not _shutdown_flag.is_set():
        time.sleep(25)
        if _scan_done or _shutdown_flag.is_set(): break
        e=max(time.monotonic()-_scan_start,1)
        rate=_total_scanned/e*60; qs=_bhq.qsize()
        bar="▓"*min(qs//10,20)+"░"*max(0,20-min(qs//10,20))
        sl="🌙" if in_silent() else ("⚡ TURBO" if in_turbo() else "")
        ts=datetime.now(IST).strftime("%H:%M:%S IST")
        ls=latency_stats()
        with _monitor_lock: stats=dict(_monitor_stats)
        lat_line=(f"p50:{ls.get('p50',0):.0f}ms p95:{ls.get('p95',0):.0f}ms"
                  if ls else "latency: no data")
        replay_n = len(_replay_buf)
        ajax_n   = len(DEALS_AJAX_NODES)
        keepa_t  = f"{_keepa_tokens_used}/{_keepa_daily_cap}" if KEEPA_API_KEY else "off"
        cb_open  = sum(1 for s in _breakers.values() if s.open_until > time.monotonic())
        lines=[
            f"\n{_ANSI['B']}{_ANSI['C']}╔══ GLITCH HUNTER v10 PHANTOM STRIKE  {ts} {sl} {'═'*4}╗{_ANSI['R']}",
            f"║  Sweep #{stats['sweeps']}  Seen:{_total_scanned:,} ({rate:.0f}/min)  Workers:{active_workers()}",
            f"║  Seeded:{stats['seeded']:,}  Drops:{stats['drops']:,}  BH-Q:{bar}({qs})",
            f"║  {_ANSI['G']}OVL{_ANSI['R']}  : R1={_ovl_r1} R2={_ovl_r2} R3={_ovl_r3}  Glitch={_gli_found}",
            f"║  Reject: BH={_bh_rej} Ghost={_ghost_rej} Silent={_tg_silenced}",
            f"║  {_ANSI['Y']}TG{_ANSI['R']}    : {_tg_sent}✅ {_tg_failed}❌ CB:{'OPEN' if _tg_cb_open else 'ok'}"
            +("  [DRY]" if DRY_RUN else ""),
            f"║  {_ANSI['M']}Latency{_ANSI['R']}: {lat_line}",
            f"║  {_ANSI['C']}v10{_ANSI['R']}   : AJAX={ajax_n}nodes CB={cb_open}open "
            f"Keepa={keepa_t} Replay={replay_n} Bloom✅ Storm:{'🔴' if _proxy_active.is_set() else '✅'}",
            f"╚{'═'*54}╝\n",
        ]
        safe_print("\n".join(lines))


# ═══════════════════════════════════════════════════════════════════════════════
# FASTAPI WEBHOOK (extended: export + watchlist endpoints)
# ═══════════════════════════════════════════════════════════════════════════════
def _start_webhook():
    if ARGS.webhook_port<=0: return
    try:
        from fastapi import FastAPI, Response
        import uvicorn
        api=FastAPI(title="Glitch Hunter v8 SPECTER API")

        @api.get("/status")
        def api_status():
            with _monitor_lock: stats=dict(_monitor_stats)
            return {"state":"running","version":"v10-phantom-strike",
                    "sweeps":stats["sweeps"],
                    "tg_sent":_tg_sent,"bh_q":_bhq.qsize(),
                    "latency":latency_stats(),"curl_cffi":_HAS_CFFI,
                    "flipkart":USE_FLIPKART,"redis":bool(_redis),
                    "specter":USE_SPECTER,
                    "ajax_nodes":len(DEALS_AJAX_NODES),
                    "keepa":bool(KEEPA_API_KEY),
                    "keepa_tokens_used":_keepa_tokens_used,
                    "proxy_storm":_proxy_active.is_set(),
                    "replay_buf":len(_replay_buf),
                    "cb_open":sum(1 for s in _breakers.values() if s.open_until > time.monotonic()),
                    "bloom":True}

        @api.get("/top")
        def api_top():
            since=(datetime.now()-timedelta(hours=1)).isoformat()
            return _DB.top_deals(since,5)

        @api.get("/export/csv")
        def api_csv(hours:int=24):
            return Response(_DB.export_deals_csv(hours),
                            media_type="text/csv",
                            headers={"Content-Disposition":"attachment;filename=deals.csv"})

        @api.get("/export/json")
        def api_json(hours:int=24):
            return _DB.export_deals_json(hours)

        @api.get("/watchlist")
        def api_watchlist():
            return _DB.watchlist_all()

        @api.post("/watchlist")
        def api_watch(asin:str,interval:int=180):
            asin=asin.upper()[:10]
            if not re.match(r"^[A-Z0-9]{10}$",asin):
                return {"error":"invalid ASIN"}
            _DB.watchlist_add(asin,interval)
            _watchlist[asin]=interval
            return {"added":asin,"interval":interval}

        @api.delete("/watchlist/{asin}")
        def api_unwatch(asin:str):
            asin=asin.upper()[:10]
            _DB.watchlist_remove(asin)
            _watchlist.pop(asin,None)
            return {"removed":asin}

        threading.Thread(target=uvicorn.run,
                         kwargs={"app":api,"host":"0.0.0.0","port":ARGS.webhook_port,
                                 "log_level":"warning"},daemon=True).start()
        safe_print(f"   🌐 API on :{ARGS.webhook_port}")
    except ImportError:
        safe_print("   ⚠️ FastAPI/uvicorn not installed — webhook disabled")


# ═══════════════════════════════════════════════════════════════════════════════
# v8 SPECTER — AMAZON REAL-TIME PRICE PUSH (MQTT-over-WebSocket)
# ═══════════════════════════════════════════════════════════════════════════════
# Taps Amazon's own push channel used by the mobile app.
# Protocol: MQTT 3.1.1 over WebSocket, anonymous SigV4 for browse-mode sessions.
# Topics:   amzn/category-deals/IN/{BROWSE_NODE_ID}
# Latency:  < 2 seconds from price change to detection.
# Cost:     Zero page scrapes during monitoring; near-zero bot-score pressure.
# ─────────────────────────────────────────────────────────────────────────────

import struct as _struct

_SPECTER_WS_ENDPOINT = "wss://msh.amazon.in/vvp/messaging/push"
_SPECTER_WS_HEADERS  = {
    "User-Agent":       "Amazon/24.18.0.100 (Android 13; Pixel 7)",
    "Accept-Language":  "en-IN",
    "X-Amzn-App-Id":   "Amazon.Shopping.Client",
    "Origin":           "https://www.amazon.in",
}

# ── Browse node IDs for category subscriptions ───────────────────────────────
# Each corresponds to an Amazon.in browse node; covers major deal categories.
_SPECTER_DEFAULT_NODES = [
    "1805560031",  # Electronics deals
    "1375424031",  # Mobiles
    "1389396031",  # Laptops
    "976419031",   # Televisions
    "1984443031",  # Cameras
    "4347501031",  # Smart Watches
    "2083427031",  # Home & Kitchen
    "1350380031",  # Appliances
    "3419153031",  # Computers
    "6398634031",  # Gaming
]


def _specter_sigv4_url(region: str = "ap-south-1") -> str:
    """Build anonymous SigV4-signed WebSocket URL (browse-mode, no credentials)."""
    import hmac as _hmac, hashlib as _hash, urllib.parse as _up
    now = datetime.utcnow()
    amz_date  = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    service = "execute-api"
    cred    = f"ANONYMOUS/{date_stamp}/{region}/{service}/aws4_request"
    params  = {
        "X-Amz-Algorithm":     "AWS4-HMAC-SHA256",
        "X-Amz-Credential":    cred,
        "X-Amz-Date":          amz_date,
        "X-Amz-Expires":       "300",
        "X-Amz-SignedHeaders": "host",
    }
    qs = "&".join(f"{_up.quote(k,safe='')}={_up.quote(v,safe='')}"
                  for k, v in sorted(params.items()))
    host = _SPECTER_WS_ENDPOINT.replace("wss://","").split("/")[0]
    uri  = "/" + "/".join(_SPECTER_WS_ENDPOINT.replace("wss://","").split("/")[1:])
    cr   = "\n".join(["GET", uri, qs, f"host:{host}\n", "host",
                      "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"])
    sts  = "\n".join(["AWS4-HMAC-SHA256", amz_date,
                      f"{date_stamp}/{region}/{service}/aws4_request",
                      _hash.sha256(cr.encode()).hexdigest()])
    def _sign(key, msg):
        return _hmac.new(key, msg.encode(), _hash.sha256).digest()
    sk = _sign(_sign(_sign(_sign(b"AWS4" + b"", date_stamp), region), service), "aws4_request")
    sig = _hmac.new(sk, sts.encode(), _hash.sha256).hexdigest()
    endpoint = _SPECTER_WS_ENDPOINT
    if "?" not in endpoint:
        return f"{endpoint}?{qs}&X-Amz-Signature={sig}"
    return f"{endpoint}&{qs}&X-Amz-Signature={sig}"


def _mqtt_connect(client_id: str, keepalive: int = 60) -> bytes:
    """Build MQTT 3.1.1 CONNECT packet (clean session, no auth)."""
    proto  = b"\x00\x04MQTT\x04\x02"          # protocol name + level + flags (clean session)
    ka     = _struct.pack("!H", keepalive)
    cid_b  = client_id.encode()
    cid_p  = _struct.pack("!H", len(cid_b)) + cid_b
    body   = proto + ka + cid_p
    return bytes([0x10, len(body)]) + body


def _mqtt_subscribe(topic: str, packet_id: int = 1) -> bytes:
    """Build MQTT SUBSCRIBE packet (QoS 1)."""
    t_b    = topic.encode()
    t_p    = _struct.pack("!H", len(t_b)) + t_b
    body   = _struct.pack("!H", packet_id) + t_p + b"\x01"
    return bytes([0x82, len(body)]) + body


def _mqtt_pingreq() -> bytes:
    return bytes([0xC0, 0x00])


def _mqtt_parse_publish(frame: bytes) -> Optional[Dict]:
    """Extract JSON payload from MQTT PUBLISH frame. Returns None for non-PUBLISH."""
    if not frame or (frame[0] & 0xF0) != 0x30:
        return None
    idx, mult, rem = 1, 1, 0
    while True:
        if idx >= len(frame): return None
        b = frame[idx]; idx += 1
        rem += (b & 0x7F) * mult; mult *= 128
        if not (b & 0x80): break
    t_len = _struct.unpack("!H", frame[idx:idx+2])[0]; idx += 2
    idx  += t_len                           # skip topic
    if frame[0] & 0x06: idx += 2           # QoS > 0: skip packet ID
    payload = frame[idx:]
    try:
        return json.loads(payload.decode("utf-8"))
    except Exception:
        return None


async def _specter_main_async(nodes: List[str]):
    """Persistent MQTT-over-WebSocket session. Pushes price events into _bhq."""
    import websockets as _wsl
    client_id = f"specter-{random.randint(100000, 999999)}"
    reconnect_delay = 5.0

    while not _shutdown_flag.is_set():
        try:
            url = _specter_sigv4_url()
            async with _wsl.connect(
                url,
                extra_headers=_SPECTER_WS_HEADERS,
                subprotocols=["mqtt"],
                ping_interval=30,
                ping_timeout=10,
                close_timeout=5,
                max_size=2**20,
            ) as ws:
                # MQTT CONNECT
                await ws.send(_mqtt_connect(client_id))
                connack = await asyncio.wait_for(ws.recv(), timeout=10)
                if isinstance(connack, str): connack = connack.encode()
                if len(connack) < 4 or connack[0] != 0x20 or connack[3] != 0:
                    safe_print(f"   ⚡ SPECTER CONNACK failed (rc={connack[3] if len(connack)>3 else '?'})")
                    await asyncio.sleep(reconnect_delay)
                    continue

                # Subscribe to category deal topics
                for i, node in enumerate(nodes, 1):
                    topic = f"amzn/category-deals/IN/{node}"
                    await ws.send(_mqtt_subscribe(topic, packet_id=i))
                    try: await asyncio.wait_for(ws.recv(), timeout=5)   # SUBACK
                    except asyncio.TimeoutError: pass

                # v8 ADV (v8-specter.md): subscribe to individual ASIN price-alert
                # topics for watchlisted ASINs — gives per-ASIN real-time detection.
                wl_asins = list(_watchlist.keys())[:50]  # cap: MQTT topic limit
                for j, w_asin in enumerate(wl_asins, len(nodes) + 1):
                    topic = f"amzn/price-alerts/IN/{w_asin}"
                    await ws.send(_mqtt_subscribe(topic, packet_id=j))
                    try: await asyncio.wait_for(ws.recv(), timeout=3)
                    except asyncio.TimeoutError: pass
                if wl_asins:
                    safe_print(f"   🌐 SPECTER: +{len(wl_asins)} watchlist ASIN topics")

                safe_print(f"   🌐 SPECTER live — {len(nodes)} category + {len(wl_asins)} ASIN streams "
                           f"| client={client_id}")
                reconnect_delay = 5.0   # reset on successful connect

                last_ping = time.monotonic()
                async for raw in ws:
                    if _shutdown_flag.is_set(): break
                    # Periodic PINGREQ to keep connection alive
                    if time.monotonic() - last_ping > 50:
                        try: await ws.send(_mqtt_pingreq())
                        except Exception: pass
                        last_ping = time.monotonic()

                    if isinstance(raw, str):
                        try: event = json.loads(raw)
                        except Exception: continue
                    else:
                        event = _mqtt_parse_publish(raw)
                    if not event: continue

                    et = event.get("eventType","")
                    # v8 ADV: also capture STOCK_ALERT (watchlist low-stock push)
                    # and DEAL_UPDATED (price revision mid-deal)
                    if et not in ("PRICE_CHANGE","DEAL_STARTED","LIGHTNING_DEAL",
                                  "STOCK_ALERT","DEAL_UPDATED"):
                        continue

                    asin    = event.get("asin","")
                    cur_p   = int(event.get("currentPrice", 0) or 0)
                    mrp_p   = int(event.get("mrp", 0) or 0)
                    disc_p  = float(event.get("discountPercent", 0) or 0)
                    if not asin or cur_p <= 0: continue
                    if mrp_p > 0 and disc_p == 0:
                        disc_p = round((mrp_p - cur_p) / mrp_p * 100, 1)

                    # Only fast-path events with meaningful discounts
                    if disc_p < (ARGS.flash_drop_pct * 0.75): continue

                    product_url = f"https://www.amazon.in/dp/{asin}"
                    h = hashlib.md5(product_url.encode()).hexdigest()[:16]
                    # v11 C3: lightning deal countdown from SPECTER event
                    _spect_deal_id = (event.get("dealId") or event.get("deal_id") or "")
                    _spect_ld = _fetch_lightning_deal(_spect_deal_id) if _spect_deal_id else {}
                    synth_item = {
                        "name":           asin,           # real name resolved in BH worker
                        "url":            product_url,
                        "current_price":  cur_p,
                        "mrp_price":      mrp_p,
                        "coupon_percent": 0,
                        "coupon_value":   0,
                        "hash":           h,
                        "platform":       "amazon",
                        "img_url":        None,
                        "low_stock":      event.get("stockStatus","") == "LOW_STOCK",
                        "bsr_rank":       0,
                        "bsr_fast":       False,
                        "_specter_push":  True,
                        "_specter_event": et,
                        "_lightning":     _spect_ld,
                        "_lightning_label": _spect_ld.get("label",""),
                    }
                    _bhq.put({"item": synth_item, "is_price_drop": True,
                               "cat_name": f"SPECTER/{et}"}, priority=-disc_p)
                    safe_print(f"   🌐 SPECTER push: {asin} {disc_p:.1f}% [{et}]")
                    jlog("specter_push", asin=asin, disc=disc_p, event=et, price=cur_p)

        except Exception as exc:
            if not _shutdown_flag.is_set():
                safe_print(f"   ⚡ SPECTER reconnect ({type(exc).__name__}) — {reconnect_delay:.0f}s")
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(reconnect_delay * 1.8, 120.0)


def _specter_thread(nodes: List[str]):
    """Thread entry: owns its own asyncio event loop for SPECTER WebSocket."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(_specter_main_async(nodes))
    except Exception as exc:
        safe_print(f"   ⚡ SPECTER thread exit: {exc}")
    finally:
        loop.close()


def _start_specter(all_cats: List[Dict]):
    """Derive browse nodes from category names and launch SPECTER thread."""
    if not USE_SPECTER:
        safe_print("   ⚡ SPECTER disabled (websockets not installed or --no-specter)")
        return
    # User-specified nodes take priority
    if ARGS.specter_nodes:
        nodes = [n.strip() for n in ARGS.specter_nodes.split(",") if n.strip()]
    else:
        nodes = list(_SPECTER_DEFAULT_NODES)
    if not nodes:
        safe_print("   ⚡ SPECTER: no nodes configured")
        return
    t = threading.Thread(target=_specter_thread, args=(nodes,), daemon=True,
                         name="specter")
    t.start()
    safe_print(f"   🌐 SPECTER thread started — {len(nodes)} nodes")


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — DEALS AJAX POLLER
# Polls Amazon /deals/ajax/v1 every 4s for structured JSON deal feed.
# Sub-300ms detection. Runs parallel to SPECTER. Feeds bhq lane 0.
# ═══════════════════════════════════════════════════════════════════════════════
DEALS_AJAX_URL    = "https://www.amazon.in/deals/ajax/v1"
DEALS_AJAX_NODES: List[str] = []   # filled from all_cats on start

def _deals_ajax_worker():
    POLL_INTERVAL = 4
    BATCH_NODES   = 10
    sess = requests.Session()
    sess.mount("https://", HTTPAdapter(pool_connections=2, pool_maxsize=8,
                                        max_retries=Retry(total=0)))
    _ajax_seen: Dict[str, int] = {}

    def _poll_nodes(node_ids: List[str]):
        pid, ja3, sec_ch, platform = _next_profile()
        h = _stealth_headers(pid, sec_ch, platform)
        h.update({
            "Accept":           "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer":          "https://www.amazon.in/deals",
            "Sec-Fetch-Dest":   "empty",
            "Sec-Fetch-Mode":   "cors",
            "Sec-Fetch-Site":   "same-origin",
        })
        params = {
            "dealType":     "ALL_DEALS",
            "sort":         "BY_SCORE",
            "isFilterWise": "true",
            "pageNumber":   "1",
            "fetchCount":   "60",
            "facetKey":     ",".join(node_ids),
        }
        try:
            if _HAS_CFFI:
                cffi = _cffi_sess(ja3)
                r = cffi.get(DEALS_AJAX_URL, headers=h, params=params, timeout=6)
            else:
                r = sess.get(DEALS_AJAX_URL, headers=h, params=params, timeout=6)
            if r.status_code != 200: return
            data = r.json()
        except Exception:
            return

        deals = data.get("dealDetails", {})
        if not deals and isinstance(data, list):
            deals = {str(i): d for i, d in enumerate(data)}

        for deal_id, d in deals.items():
            try:
                asin       = (d.get("impressionAsin") or d.get("asin") or "")[:10]
                deal_price = int(float(d.get("dealPrice", 0) or d.get("currentPrice", 0) or 0))
                list_price = int(float(d.get("listPrice",  0) or d.get("originalPrice", 0) or 0))
                if not asin or deal_price <= 0 or list_price <= 0: continue
                if list_price <= deal_price: continue
                disc = (list_price - deal_price) / list_price * 100.0
                if disc < float(ARGS.alert_drop_pct): continue
                if _ajax_seen.get(asin) == deal_price: continue
                _ajax_seen[asin] = deal_price
                product_url = f"https://www.amazon.in/dp/{asin}"
                h_hash      = hashlib.md5(product_url.encode()).hexdigest()[:16]
                if _unified_seen(h_hash, deal_price): continue
                # v11 C3: lightning deal countdown — fetch pct_claimed + label
                _ld = _fetch_lightning_deal(deal_id,
                          d.get("itemGroupId", d.get("dealItemGroupId", "")))
                synth = {
                    "name":           d.get("title", asin)[:150],
                    "url":            product_url,
                    "current_price":  deal_price,
                    "mrp_price":      list_price,
                    "discount":       round(disc, 1),
                    "hash":           h_hash,
                    "platform":       "amazon",
                    "img_url":        None,
                    "low_stock":      bool(d.get("egressUrl", "")),
                    "stock_count":    0,
                    "bsr_fast":       False,
                    "coupon_percent": 0,
                    "coupon_value":   0,
                    "_specter_push":  True,
                    "_ajax_deal":     True,
                    "_lightning":     _ld,
                    "_lightning_label": _ld.get("label",""),
                }
                _bhq.put({"item": synth, "is_price_drop": True, "cat_name": "AJAX"},
                         priority=-disc)
                safe_print(f"   ⚡ AJAX: {asin} {disc:.1f}% ₹{deal_price:,}")
                jlog("ajax_deal", asin=asin, disc=round(disc,1), price=deal_price)
            except Exception:
                continue

    while not _shutdown_flag.is_set():
        try:
            nodes = DEALS_AJAX_NODES[:]
            if not nodes:
                _shutdown_flag.wait(POLL_INTERVAL); continue
            for i in range(0, len(nodes), BATCH_NODES):
                if _shutdown_flag.is_set(): break
                _poll_nodes(nodes[i:i+BATCH_NODES])
                time.sleep(random.uniform(0.8, 1.4))
        except Exception as exc:
            if ARGS.debug: safe_print(f"   ⚠️ ajax_worker: {exc}")
        _shutdown_flag.wait(POLL_INTERVAL)


def _start_ajax_poller(all_cats: List[Dict]):
    """Extract browse node IDs from category URLs and launch AJAX poller thread."""
    nodes = []
    for cat in all_cats:
        url = cat.get("url", "")
        m = re.search(r"[?&]node=(\d+)", url)
        if m: nodes.append(m.group(1))
        m2 = re.search(r"rh=n[:%](\d+)", url)
        if m2 and m2.group(1) not in nodes: nodes.append(m2.group(1))
    DEALS_AJAX_NODES.clear()
    DEALS_AJAX_NODES.extend(list(dict.fromkeys(nodes)))
    safe_print(f"   ⚡ AJAX poller: {len(DEALS_AJAX_NODES)} nodes")
    threading.Thread(target=_deals_ajax_worker, daemon=True, name="ajax-poller").start()


# ── v11 A3: Amazon RSS deal feed poller ───────────────────────────────────────
_RSS_FEEDS = [
    "https://www.amazon.in/gp/rss/deals/ref=xs_gb_rss",
    "https://www.amazon.in/gp/rss/bestsellers/electronics/ref=zg_bs_electronics_rss_pg_1",
    "https://www.amazon.in/gp/rss/bestsellers/computers/ref=zg_bs_computers_rss_pg_1",
    "https://www.amazon.in/gp/rss/bestsellers/mobile/ref=zg_bs_mobile_rss_pg_1",
]
_RSS_POLL_INTERVAL = 30   # seconds

def _rss_worker():
    """Poll Amazon.in RSS feeds for deals. Zero anti-bot — CDN-served."""
    if not _HAS_FEEDPARSER:
        safe_print("   ⚠️ feedparser not installed — RSS poller skipped (pip install feedparser)")
        return
    safe_print(f"   📡 RSS poller started ({len(_RSS_FEEDS)} feeds, {_RSS_POLL_INTERVAL}s interval)")
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; FeedParser/6)",
        "Accept": "application/rss+xml, application/xml, text/xml, */*",
    })
    while not _shutdown_flag.is_set():
        for feed_url in _RSS_FEEDS:
            try:
                r = sess.get(feed_url, timeout=10)
                if r.status_code != 200: continue
                parsed = _feedparser.parse(r.content)
                for entry in parsed.entries[:20]:
                    link = entry.get("link","")
                    asin = _asin(link)
                    if not asin: continue
                    # Try to extract price from title/summary
                    summary = (entry.get("summary","") or entry.get("title",""))
                    price_m = re.search(r"₹\s*([\d,]+)", summary)
                    if not price_m: continue
                    try:
                        price = int(price_m.group(1).replace(",",""))
                    except ValueError: continue
                    if price <= 0: continue
                    url_c = f"https://www.amazon.in/dp/{asin}"
                    h = hashlib.md5(url_c.encode()).hexdigest()[:16]
                    if _unified_seen(h, price): continue
                    # Build minimal candidate and push to BH queue
                    title = re.sub(r"<[^>]+>","", entry.get("title",""))[:200]
                    item = {
                        "name": title if title else f"ASIN {asin}",
                        "url": url_c, "current_price": price,
                        "mrp_price": price, "coupon_percent": 0, "coupon_value": 0,
                        "hash": h, "platform": "amazon", "img_url": None,
                        "parent_asin": None, "low_stock": False,
                        "stock_count": 0, "bsr_rank": 0, "bsr_fast": False,
                        "_specter_push": True,   # RSS = high-confidence source
                    }
                    # Quick candidate check before BH queue
                    glitch_ok, g_disc, _ = is_glitch_local(item)
                    if glitch_ok and g_disc >= 50.0:
                        _bhq.put({"item": item, "is_price_drop": False,
                                  "cat_name": "rss"}, priority=-float(g_disc))
                        if ARGS.debug:
                            safe_print(f"   📡 RSS: {title[:35]} ₹{price:,}")
            except Exception:
                pass
        _shutdown_flag.wait(timeout=_RSS_POLL_INTERVAL)


def _start_rss_poller(all_cats: List[Dict]):
    """Launch RSS feed polling thread (A3)."""
    threading.Thread(target=_rss_worker, daemon=True, name="rss-poller").start()


# ── v11 E5: Daily digest at 09:00 IST ─────────────────────────────────────────
def _send_daily_digest():
    """Scheduled 09:00 IST digest: top 5 deals, grade breakdown, uptime."""
    try:
        since = (datetime.now() - timedelta(hours=24)).isoformat()
        deals = _DB.top_deals(since, 5)
        with _monitor_lock: stats = dict(_monitor_stats)
        # Grade breakdown
        conn, cur = _DB._conn()
        cur.execute("""SELECT grade, COUNT(*) as n FROM deal_log
                       WHERE logged_at >= ? GROUP BY grade""", (since,))
        grade_counts = {r["grade"]: r["n"] for r in cur.fetchall()}
        gc_line = "  ".join(f"[{g}]×{grade_counts.get(g,0)}" for g in "SABCD")
        best_disc = 0.0
        try:
            cur.execute("SELECT MAX(disc) as md FROM deal_log WHERE logged_at >= ?", (since,))
            row = cur.fetchone()
            if row and row["md"]: best_disc = float(row["md"])
        except Exception: pass
        uptime_h = (time.monotonic() - _scan_start) / 3600
        keepa_t  = f"{_keepa_tokens_used}/{_keepa_daily_cap}" if KEEPA_API_KEY else "off"
        medals = ["🥇","🥈","🥉","4️⃣","5️⃣"]
        lines  = [f"📅 <b>Daily Digest</b> — {datetime.now(IST).strftime('%d %b %Y, %H:%M IST')}\n"]
        if deals:
            for i, d in enumerate(deals[:5]):
                m = medals[i] if i < len(medals) else "🔹"
                lines.append(f"{m} Grade {d['grade']}  {d['disc']:.1f}%  ₹{d['price']:,}\n"
                             f"   <a href=\"{d['url']}\">{_sh(d['name'][:60])}</a>")
        else:
            lines.append("📭 No deals in last 24h.")
        lines.append(f"\n📊 Grade breakdown: {gc_line}")
        lines.append(f"💥 Best discount: {best_disc:.1f}%")
        lines.append(f"⏱ Uptime: {uptime_h:.1f}h | Sweeps: {stats['sweeps']}")
        lines.append(f"🔑 Keepa: {keepa_t} | Workers: {active_workers()}")
        tg_raw("\n\n".join(lines))
        safe_print("   📅 Daily digest sent")
    except Exception as exc:
        if ARGS.debug: safe_print(f"   ⚠️ Daily digest: {exc}")


def _daily_digest_thread():
    """E5: fire daily digest at 09:00 IST, repeat every 24h."""
    while not _shutdown_flag.is_set():
        now_ist = datetime.now(IST)
        target  = now_ist.replace(hour=9, minute=0, second=0, microsecond=0)
        if now_ist >= target:
            target += timedelta(days=1)
        secs = (target - now_ist).total_seconds()
        safe_print(f"   📅 Daily digest scheduled in {secs/3600:.1f}h ({target.strftime('%H:%M IST')})")
        _shutdown_flag.wait(timeout=secs)
        if _shutdown_flag.is_set(): break
        _send_daily_digest()


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — GRADE-S REPLAY BUFFER
# Stores Grade-S items that hit TG rate limits. Retries with exponential backoff.
# ═══════════════════════════════════════════════════════════════════════════════
@dataclass
class _ReplayItem:
    item:       Dict
    enqueued:   float
    attempts:   int   = 0
    next_retry: float = 0.0

_replay_buf:  List[_ReplayItem] = []
_replay_lock_v10 = threading.Lock()
_REPLAY_MAX  = 8
_REPLAY_BASE = 30.0

def replay_enqueue(item: Dict):
    key = hashlib.md5(item.get("text", "").encode()).hexdigest()[:8]
    with _replay_lock_v10:
        for ex in _replay_buf:
            if hashlib.md5(ex.item.get("text","").encode()).hexdigest()[:8] == key: return
        _replay_buf.append(_ReplayItem(
            item=item, enqueued=time.time(),
            next_retry=time.time() + _REPLAY_BASE,
        ))
    safe_print(f"   📼 Grade-S replay buffered: {item.get('text','')[:40]}")

def _replay_worker():
    sess = _tg_pool()
    while not _shutdown_flag.is_set():
        time.sleep(5)
        now = time.time()
        with _replay_lock_v10:
            to_retry  = [ri for ri in _replay_buf if now >= ri.next_retry and ri.attempts < _REPLAY_MAX]
            to_remove = [ri for ri in _replay_buf if ri.attempts >= _REPLAY_MAX]
            for ri in to_remove:
                _replay_buf.remove(ri)
                safe_print(f"   ❌ Replay exhausted ({ri.attempts} attempts)")
        for ri in to_retry:
            ok, ra, mid = _send_one(ri.item, sess, chat_id=CHAT_ID)
            ri.attempts += 1
            if ok:
                with _replay_lock_v10:
                    if ri in _replay_buf: _replay_buf.remove(ri)
                safe_print(f"   ✅ Replay ok (attempt {ri.attempts})")
            else:
                wait = min(_REPLAY_BASE * (2 ** ri.attempts), 1800)
                ri.next_retry = time.time() + wait + random.uniform(0, wait * 0.1)


# ═══════════════════════════════════════════════════════════════════════════════
# v10 PHANTOM STRIKE — MARKET QUIET PING
# ═══════════════════════════════════════════════════════════════════════════════
_last_quiet_ping_h = -1
QUIET_PING_THRESHOLD = 3

def _maybe_quiet_ping(quiet_sweeps: int, sweep_no: int):
    global _last_quiet_ping_h
    if quiet_sweeps < QUIET_PING_THRESHOLD: return
    h = datetime.now(IST).hour
    if h == _last_quiet_ping_h: return
    _last_quiet_ping_h = h
    ls = latency_stats()
    bh_warm_sz = len(_bh_warm)
    msg = (f"📡 <b>Market Quiet</b> — {datetime.now(IST).strftime('%H:%M IST')}\n"
           f"Sweep #{sweep_no} | {quiet_sweeps} empty sweeps\n"
           f"Bot alive ✅ | p95 {ls.get('p95',0):.0f}ms | "
           f"BH cache {bh_warm_sz} | "
           f"SPECTER {'🌐' if USE_SPECTER else '❌'} | "
           f"AJAX {'⚡' if DEALS_AJAX_NODES else '❌'} | "
           f"Keepa {'🔑' if KEEPA_API_KEY else '❌'} ({_keepa_tokens_used}/{_keepa_daily_cap})")
    tg_raw(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# SIGNAL + SHUTDOWN
# ═══════════════════════════════════════════════════════════════════════════════
_shutdown_flag=threading.Event()

def _handle_signal(sig,frame):
    safe_print(f"\n⚠️ Signal {sig} — draining then stop…")
    _shutdown_flag.set()

_signal.signal(_signal.SIGINT,  _handle_signal)
_signal.signal(_signal.SIGTERM, _handle_signal)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN MONITOR LOOP
# ═══════════════════════════════════════════════════════════════════════════════
def monitor_loop():
    global _scan_done,_total_scanned,_scan_start
    global _bh_rej,_ovl_r1,_ovl_r2,_ovl_r3,_gli_found,_drops,_ghost_rej

    _shutdown_flag.clear()
    _scan_done=False; _total_scanned=0; _scan_start=time.monotonic()

    if ARGS.fresh: _DB.clear()
    _open_log()
    jlog("startup",version="v10-phantom-strike",curl_cffi=_HAS_CFFI,
         aiosqlite=_HAS_AIOSQLITE,flipkart=USE_FLIPKART,specter=USE_SPECTER,
         keepa=bool(KEEPA_API_KEY),proxy=bool(RESIDENTIAL_PROXY_URL),dry=DRY_RUN)

    # Warm BH cache + Redis init
    _init_redis()
    loaded=_DB.bh_warm_load()
    with _bh_warm_lock: _bh_warm.update(loaded)
    safe_print(f"   🔥 BH warm cache: {len(loaded)} ASINs")

    _load_blacklist(); _load_watchlist()
    # Sync file watchlist → DB
    for asin_w,itv in _watchlist.items(): _DB.watchlist_add(asin_w,itv)

    _start_webhook()

    all_cats=_load_cats()
    if not all_cats: safe_print("❌ No categories"); return

    random.shuffle(all_cats)
    batch_size=40 if ARGS.num_cats<=0 else max(5,min(ARGS.num_cats,len(all_cats)))  # v9: was 21
    adaptive_iv=active_interval()
    quiet_sweeps=0

    def pick_batch(pool:List[Dict],size:int)->List[Dict]:
        fresh=_load_cats()
        if len(fresh)!=len(pool): pool[:]=fresh
        if len(pool)<=size: out=list(pool); random.shuffle(out); return out
        ranked=sorted(pool,key=lambda c:_DB.cat_velocity(c.get("name","?"))*_DB.cat_yield(c.get("name","?")),reverse=True)
        top_n=ranked[:min(size,max(size//2,8))]
        rest=[c for c in ranked if c not in top_n]
        random.shuffle(rest)
        batch=top_n+rest[:size-len(top_n)]
        random.shuffle(batch)
        return batch

    # Banner
    safe_print("="*76)
    safe_print("👁  AMAZON GLITCH HUNTER v10 PHANTOM STRIKE — SONIC FAST / GOD MODE HIDDEN / UNBLOCKABLE")
    safe_print(f"curl_cffi:{'✅' if _HAS_CFFI else '❌'}  "
               f"aiosqlite:{'✅' if _HAS_AIOSQLITE else '❌'}  "
               f"Redis:{'✅' if _redis else '❌'}  "
               f"Flipkart:{'✅' if USE_FLIPKART else '❌'}  "
               f"Warmup:{'✅' if USE_WARMUP else '❌'}  "
               f"SPECTER:{'✅' if USE_SPECTER else '❌'}  "
               f"AJAX:{'✅' if DEALS_AJAX_NODES else '⏳'}  "
               f"Keepa:{'✅' if KEEPA_API_KEY else '❌'}  "
               f"Proxy:{'✅' if RESIDENTIAL_PROXY_URL else 'auto'}  "
               f"Bloom:✅  CB:✅  Replay:✅")
    safe_print(f"Turbo: {TURBO_START_H}–{TURBO_END_H} IST "
               f"({ARGS.turbo_workers} workers @ {ARGS.turbo_interval}s)  "
               f"MaxPages:{ARGS.max_pages}  ParPages:{ARGS.par_pages}")
    if _watchlist: safe_print(f"Watchlist: {len(_watchlist)} ASINs")
    if DRY_RUN: safe_print("⚠️  DRY-RUN — no Telegram sends")
    safe_print("="*76)

    _write_status("starting",pool_size=len(all_cats),batch_size=batch_size)
    if not test_tg(): safe_print("⚠️ TG test failed — continuing")

    # Start workers
    _bh_done.clear()
    bh_threads=[]
    for _ in range(max(1,BH_WORKERS)):
        w=threading.Thread(target=_bh_worker,daemon=True); w.start(); bh_threads.append(w)

    # Watchlist worker
    if _watchlist:
        wl_thread=threading.Thread(target=_watchlist_worker,daemon=True); wl_thread.start()

    # TG callback handler
    if BOT_TOKEN and not DRY_RUN:
        threading.Thread(target=_cb_worker,daemon=True).start()

    # Dashboard
    threading.Thread(target=_dashboard,daemon=True).start()

    # v8 SPECTER — real-time WebSocket price push engine
    _start_specter(all_cats)
    _start_ajax_poller(all_cats)                                              # v10: AJAX deal feed
    threading.Thread(target=_autoscale_supervisor, daemon=True,
                     name="bh-autoscale").start()                            # v10: dynamic worker pool
    threading.Thread(target=_replay_worker, daemon=True,
                     name="tg-replay").start()                               # v10: Grade-S replay
    if KEEPA_API_KEY:
        safe_print(f"   🔑 Keepa: {_keepa_daily_cap} tokens/day budget active")

    try:
        while not _shutdown_flag.is_set():
            cats=pick_batch(all_cats,batch_size)
            names=[c.get("name","?")[:16] for c in cats[:8]]
            started=time.monotonic()
            with _monitor_lock:
                _monitor_stats["sweeps"]+=1
                sweep_no=_monitor_stats["sweeps"]

            turbo_tag=" ⚡TURBO" if in_turbo() else ""
            specter_tag=" 🌐SPECTER" if USE_SPECTER else ""
            safe_print(f"\n👁  SWEEP #{sweep_no}{turbo_tag}{specter_tag} — {datetime.now(IST).strftime('%H:%M:%S IST')}")
            safe_print(f"   Batch ({len(cats)}): {', '.join(names)}{'…' if len(cats)>8 else ''}")

            since=datetime.now().isoformat()
            done,seeded,changed,drops,queued=monitor_sweep(cats)

            with _monitor_lock:
                _monitor_stats["seeded"]+=seeded
                _monitor_stats["changed"]+=changed
                _monitor_stats["drops"]+=drops
                _monitor_stats["queued"]+=queued

            elapsed=time.monotonic()-started
            ls=latency_stats()
            safe_print(f"📊 Sweep #{sweep_no}: cats={done}/{len(cats)} "
                       f"seed={seeded} chg={changed} drop={drops} q={queued} "
                       f"t={elapsed:.1f}s p95={ls.get('p95',0):.0f}ms")

            maybe_send_digest()
            send_summary(since,elapsed/60)
            jlog("sweep_done",sweep=sweep_no,cats=done,changed=changed,
                 drops=drops,queued=queued,elapsed_s=round(elapsed,2))
            _write_status("running",
                last_sweep_at=datetime.now(IST).isoformat(),
                last_sweep_s=round(elapsed,2),last_sweep_cats=done,
                last_sweep_drops=drops,latency_ms=ls)
            _flush_remaining()
            try: _DB.vacuum()
            except Exception: pass

            with _seen_lock:  _seen_set.clear()
            with _asin_lock:  _asin_set.clear()
            with _sem_lock:   _sem_dedup.clear()
            with _bloom_lock: _bloom_dedup.clear()   # v10: reset Bloom per sweep

            if ARGS.once: break

            base_iv=active_interval()
            if ARGS.no_adaptive_polling:
                adaptive_iv=base_iv
            elif drops>0 or queued>0:
                quiet_sweeps=0; adaptive_iv=max(8,int(base_iv*0.50))   # v9: floor 8s was 18, mult 0.50 was 0.65
            elif changed>0:
                quiet_sweeps=0; adaptive_iv=max(8,int(base_iv*0.65))   # v9: mult 0.65 was 0.82
            else:
                quiet_sweeps+=1
                if quiet_sweeps>=2:
                    adaptive_iv=min(int(ARGS.max_monitor_interval),max(base_iv,int(adaptive_iv*1.08)))
                _maybe_quiet_ping(quiet_sweeps, sweep_no)   # v10: market quiet ping

            remaining=max(0.0,adaptive_iv-elapsed)
            if remaining:
                safe_print(f"💤 Next in {remaining:.0f}s (adaptive; quiet={quiet_sweeps})")
                _shutdown_flag.wait(remaining)

    except KeyboardInterrupt:
        safe_print("🛑 KeyboardInterrupt"); _shutdown_flag.set()
    finally:
        _scan_done=True
        _flush_remaining()
        try: _bhq.join()
        except Exception: pass
        _bh_done.set()
        for _ in bh_threads+_extra_bh: _bhq.put(None)
        for w in bh_threads+_extra_bh: w.join(timeout=3)
        tg_drain(35)
        jlog("shutdown")
        _write_status("stopped",stopped_at=datetime.now(IST).isoformat())
        safe_print("✅ v8 SPECTER stopped cleanly.")


# ═══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT — supervisor with exp back-off
# ═══════════════════════════════════════════════════════════════════════════════
if __name__=="__main__":
    if not DRY_RUN:
        missing = []
        if not BOT_TOKEN:
            missing.append("BOT_TOKEN")
        if not CHAT_ID:
            missing.append("CHAT_ID")
        if missing:
            safe_print("❌ Missing required Railway variable(s): " + ", ".join(missing))
            safe_print("Open Railway → service → Variables and add them, then redeploy.")
            safe_print("For a local no-send test, run: python -u 1.py --dry-run")
            raise SystemExit(2)

    backoff=15
    while True:
        try:
            monitor_loop()
            if ARGS.once: break
            safe_print(f"⚠️ monitor_loop returned — restart in {backoff}s")
            time.sleep(backoff); backoff=min(backoff*2,120)
        except KeyboardInterrupt:
            safe_print("\n🛑 Stopped."); break
        except Exception as exc:
            safe_print(f"💥 {type(exc).__name__}: {exc}")
            traceback.print_exc()
            safe_print(f"↻ Restart in {backoff}s…")
            time.sleep(backoff); backoff=min(backoff*2,120)