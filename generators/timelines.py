from .utils import random_id, random_date, random_status

def generate_timeline():
    return {
        "timeline_id": random_id(),
        "start_date": random_date(),
        "end_date": random_date(),
        "phase": random_status(["Intake", "Supervision", "Compliance", "Completion"])
    }
