
import json

from memory import logger


def test_save_and_load_memory(tmp_path, monkeypatch):
    memory_file = tmp_path / "agent_logs.json"
    monkeypatch.setattr(logger, "MEMORY_FILE", memory_file)

    logger.save_memory(
        "Explain a Python loop",
        "A loop repeats a block of code.",
        8,
        "Add a simple example."
    )

    memory = logger.load_memory()

    assert len(memory) == 1
    assert memory[0]["task"] == "Explain a Python loop"
    assert memory[0]["score"] == 8
    assert memory[0]["feedback"] == "Add a simple example."

    with open(memory_file, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == memory
