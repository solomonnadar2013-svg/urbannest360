from pathlib import Path
import re

state = Path("docs/development/PROJECT_STATE.md")
if not state.exists():
    raise SystemExit("PROJECT_STATE.md not found")

text = state.read_text(encoding="utf-8")
for key in ["Current Phase", "Current Feature", "Current Task", "Global Status", "Next Task"]:
    m = re.search(rf"^##? {re.escape(key)}\s*\n([^\n]+)", text, re.M)
    if m:
        print(f"{key}: {m.group(1).strip()}")
