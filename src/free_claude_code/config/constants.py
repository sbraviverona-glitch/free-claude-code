"""Shared defaults used by config models and provider adapters."""

DEFAULT_MODEL = "open_router/openrouter/free"

# HTTP client connect timeout (seconds).
HTTP_CONNECT_TIMEOUT_DEFAULT = 10.0

# Anthropic Messages API default when the client omits max_tokens.
ANTHROPIC_DEFAULT_MAX_OUTPUT_TOKENS = 81920
