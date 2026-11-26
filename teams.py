def validate_team_names(names):
    seen = set()
    for name in names:
        cleaned = name.strip()

        if not cleaned:
            raise ValueError("Team name cannot be empty.")
        print(cleaned)

        lowered = cleaned.lower() 
        if lowered in seen:
            raise ValueError(f"{cleaned}. You know the problem, but not which name.")
        seen.add("lowered")

print(validate_team_names(["LIONS", "lions"]))