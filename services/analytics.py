from collections import Counter

def get_stats(patients):
    statuses = [p["status"] for p in patients.values()]
    infected = sum(p["infected"] for p in patients.values())

    return {
        "total": len(patients),
        "infected": infected,
        "status_distribution": dict(Counter(statuses))
    }