import json
import os

def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }

try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip() 
                
                if not line:
                    continue

try:
                    log_data = json.loads(line)
                except json.JSONDecodeError:
                    continue
