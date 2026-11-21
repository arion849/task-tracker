# Task Tracker

A small command-line task tracker in Python. Tasks are saved to a local `tasks.json` file, so they persist between runs.

## Features

- Add a task with a description and a status: `todo`, `in-progress` or `done`
- Each task gets a UUID plus created and updated timestamps
- List all tasks with their status and timestamps
- Recovers if `tasks.json` is missing or corrupt by starting a fresh list

## Run

```bash
python main.py
```

No dependencies beyond the Python 3 standard library.

## Task format

```json
{
  "tasks": [
    {
      "id": "3c034668-0b59-41fb-88aa-50a2f4128ae6",
      "status": "todo",
      "created_at": "2025-11-08T16:18:00.303806",
      "updated_at": "2025-11-08T16:18:00.303806",
      "description": "Write the report"
    }
  ]
}
```
