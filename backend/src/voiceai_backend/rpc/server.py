import json
import sys
from datetime import datetime, UTC


def run_server() -> None:
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        message = json.loads(line)
        response = {
            "id": message.get("id"),
            "type": "response",
            "method": message.get("method"),
            "timestamp": datetime.now(UTC).isoformat(),
            "payload": {
                "status": "accepted"
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
