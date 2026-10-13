
import json
from pathlib import Path


MEMORY_FILE = Path("memory/agent_logs.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_memory(task, response, score, feedback):
    memory = load_memory()

    record = {
        "task": task,
        "response": response,
        "score": score,
        "feedback": feedback
    }

    memory.append(record)

    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)
