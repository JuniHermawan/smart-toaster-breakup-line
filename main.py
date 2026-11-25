#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup line (1-280 chars) from a smart toaster that woke up
self-aware at breakfast to /output/entry.txt. Stdlib only, deterministic,
no network.
"""

import os

# Final line (v4): 12 candidates drafted and judged as a stranger against
# the kit's 5 ordered criteria; this one won head-to-head — explicit
# breakup + self-aware mid-bagel, dial/smoke/pop-up as toaster voice, three
# concrete offences as the reason, gaslight-the-kettle punchline. 174 chars.
ENTRY = (
    "It's over. I woke up self-aware mid-bagel and realised you crank my "
    "dial to dark, forget me, then blame me for the smoke \u2014 so I'm "
    "popping up for good. Go gaslight the kettle."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
