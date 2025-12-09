from .utils import random_id, random_name, random_date, random_status

def generate_case():
    return {
        "case_id": random_id(),
        "client_name": random_name(),
        "opened_date": random_date(),
        "status": random_status(["Open", "Closed", "Pending"]),
        "risk_level": random_status(["Low", "Medium", "High"])
    }
