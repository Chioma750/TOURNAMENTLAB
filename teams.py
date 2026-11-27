def validate_team_names(names):
    seen = set()
    accepted_names = []
    
    for name in names:
        cleaned = name.strip()

        if not cleaned:
            raise ValueError("Team name cannot be empty.")
        lowered = cleaned.lower() 
        
        if lowered in seen:
            raise ValueError(f"A duplicate team name, {cleaned}")
        seen.add(lowered)

        accepted_names.add(cleaned)

print(validate_team_names(["Hawks", "Lions", "lions"]))