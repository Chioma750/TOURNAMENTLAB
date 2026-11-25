def validate_team_names(names):
    for name in names:
        cleaned = name.strip()

        if not cleaned:
            raise ValueError("Team name cannot be empty.")
        print(cleaned)

print(validate_team_names(["Lions", " ", "Hawks"]))