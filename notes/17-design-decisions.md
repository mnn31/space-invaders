# Design decisions

A few one-liner rationales for choices in the codebase:

- Single-file: simplest distribution, small enough that a class hierarchy adds friction
- Pygame: well-supported, runs on macOS/Linux/Windows with one install
- WAV not MP3: WAV plays without external codecs on default Pygame builds
