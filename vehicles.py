"""
Simple vehicles data and helper to diagnose 401 (Unauthorized) responses.

Note: a 401 from an API means the server requires valid credentials. If the
API truly needs no auth, check that the request is sent to the correct URL,
that no proxy or gateway is inserting auth requirements, and that any
Authorization header is omitted.
"""

VEHICLES = [
    {"TaskID": "264e638f-1c7a-4d67-9f9c-53f3d1766d37", "Duration": 1, "Impact": 5},
    {"TaskID": "f3e1c8b0-2d4a-4f5e-9c6b-1e2f3d4a5b6c", "Duration": 2, "Impact": 3},
    {"TaskID": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6", "Duration": 3, "Impact": 4},
    {"TaskID": "b2c3d4e5-f6g7-8h9i-0j1k-l2m3n4o5p6q7", "Duration": 4, "Impact": 2},
    {"TaskID": "c3d4e5f6-g7h8-9i0j-1k2l-m3n4o5p6q7r8", "Duration": 5, "Impact": 1},
]


def diagnose_401(request_url, headers=None, response_status=None):
    """Return brief checks to run when you get a 401 despite expecting no auth.

    Args:
        request_url (str): URL you called.
        headers (dict|None): headers you sent (if any).
        response_status (int|None): status code received.

    Returns:
        list[str]: short checklist to investigate.
    """
    tips = []
    tips.append("Verify the URL is correct and uses http/https as intended.")
    tips.append("Ensure no Authorization header or invalid credentials are being sent.")
    tips.append("Check if a proxy, gateway, or API management layer enforces auth.")
    tips.append("Inspect response body for WWW-Authenticate or error details from server.")
    tips.append("Try curl or Postman with no auth to reproduce: curl -v <URL>")
    if headers:
        if "Authorization" in (k.title() for k in headers):
            tips.append("Remove Authorization header or correct its value.")
    if response_status and response_status != 401:
        tips.append(f"Received {response_status}; server may return different code.")
    return tips
