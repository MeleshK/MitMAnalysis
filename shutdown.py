"""
A simple way of shutting down the mitmproxy instance to stop everything.

Usage:

    mitmproxy -s shutdown.py

    and then send a HTTP request to trigger the shutdown:
    curl --proxy localhost:8080 http://example.com/path
"""
from mitmproxy import ctx, http


def request(flow: http.HTTPFlow) -> None:
    ctx.log.info("Shutting down everything...")
    ctx.master.shutdown()