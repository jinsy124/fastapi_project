import redis.asyncio as aioredis
from src.config import Config

# JWT blacklist expiry (seconds)
JTI_EXPIRY = 3600

# ✅ Async Redis client
token_blocklist = aioredis.from_url(
    Config.REDIS_URL,
    decode_responses=True
)


async def add_jti_to_blocklist(jti: str) -> None:
    """
    Store JWT JTI in Redis blocklist
    """
    await token_blocklist.set(
        name=jti,
        value="blocked",
        ex=JTI_EXPIRY
    )


async def token_in_blocklist(jti: str) -> bool:
    """
    Check if JWT JTI exists in Redis blocklist
    """
    return await token_blocklist.exists(jti) == 1
