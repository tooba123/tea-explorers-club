import subprocess

result = subprocess.run(
    [
        "uv",
        "run",
        "tea-explorers-club",
        "subscribers",
        "--since",
        "2026-10-01",
        "--run-date",
        "2026-11-20",
    ],
    capture_output=True,
    text=True,
)

assert result.stdout.strip() == "12"
print("ok")
