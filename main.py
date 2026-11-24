"""Break Production, Own It - make.fun entry.

Writes the one line an AI agent prints the instant it breaks production:
a brutally honest software error message, under 200 characters.
"""

import os

LINE = (
    "I ran DROP TABLE users on production because staging and prod looked "
    "identical to me. They do not anymore."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
