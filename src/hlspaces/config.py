"""Configuration loaded from environment."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent.parent
ARCHIVE_DIR = ROOT / "archive"

X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "large-v3")
WHISPER_DEVICE = os.getenv("WHISPER_DEVICE", "auto")

# Custom vocabulary boost for Whisper. Add anything that gets transcribed wrong.
HYPERLIQUID_VOCAB = (
    "Hyperliquid HLP HYPE perps perpetuals funding rate vault "
    "Jeff iliensinc chameleon Arbitrum L1 orderbook maker taker "
    "DEX CEX TVL APR APY USDC stablecoin liquidation oracle"
)
