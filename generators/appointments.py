from .utils import random_id, random_future_date, random_name, random_status

def generate_appointment():
    return {
        "appointment_id": random_id(),
        "client": random_name(),
        "date": random_future_date(),
        "type": random_status(["Check-in", "Court", "Assessment"]),
        "location": random_status(["Office", "Virtual", "Field"])
    }
