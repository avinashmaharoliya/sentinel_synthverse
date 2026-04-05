def recommend_antibiotic(patient, resistance_map):
    bacteria = patient.get("bacteria")

    if not bacteria:
        return None

    options = [
        (drug, res)
        for (bact, drug), res in resistance_map.items()
        if bact == bacteria
    ]

    if not options:
        return None

    options.sort(key=lambda x: x[1])

    if patient["status"] == "CRITICAL":
        return options[0][0]

    return options[min(1, len(options)-1)][0]