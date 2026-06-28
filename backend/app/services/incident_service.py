def calculate_priority(severity: str) -> str:

    severity = severity.lower()

    if severity == "critical":
        return "P1"

    if severity == "high":
        return "P2"

    if severity == "medium":
        return "P3"

    return "P4"


def assign_team(service: str) -> str:

    service = service.lower()

    mapping = {
        "payment-service": "Payments Team",
        "auth-service": "Identity Team",
        "search-service": "Search Team",
    }

    return mapping.get(service, "Platform Team")