# Asset paths

Assets are loaded by bare filename, which only works when running from the repo root.
Using `os.path.join(os.path.dirname(__file__), ...)` would make it run from anywhere.