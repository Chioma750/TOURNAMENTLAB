def validate_team_names(names):
    seen = set()
    
    for name in names:
        cleaned = name.strip()

        if not cleaned:
            raise ValueError("Team name cannot be empty.")
        print(cleaned)

        lowered = cleaned.lower() 
        
        if lowered in seen:
            raise ValueError(f"A duplicate team name, you already have {cleaned} working.")
        seen.add(lowered)

print(validate_team_names(["Hawks", "Lions", "lions"]))