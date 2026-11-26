#!/usr/bin/env python3
"""Write the GPS's excuse to /output/entry.txt."""
import os

LINE = "You have arrived at your destination. If this is a lake, the lake arrived after my last update, and I do not negotiate with new lakes."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
