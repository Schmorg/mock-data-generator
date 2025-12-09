from generators.cases import generate_case
from generators.appointments import generate_appointment
from generators.timelines import generate_timeline

import json
from pathlib import Path

OUTPUT_PATH = Path("data/generated_mock_data.json")

def main():
    data = {
        "cases": [generate_case() for _ in range(5)],
        "appointments": [generate_appointment() for _ in range(10)],
        "timelines": [generate_timeline() for _ in range(3)]
    }

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Mock data generated at {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
