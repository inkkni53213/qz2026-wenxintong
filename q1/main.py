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

                result["total"] += 1
                
                level = log_data.get("level")
                user = log_data.get("user")
                message = log_data.get("message")

                if level:
                    result["by_level"][level] = result["by_level"].get(level, 0) + 1
                
                if user:
                    result["by_user"][user] = result["by_user"].get(user, 0) + 1
                
                if level == "ERROR":
                    result["last_error"] = message

    except FileNotFoundError:
        pass 

    return result

if __name__ == "__main__":
    print(analyze_log("app.jsonl"))

