def validate_team_names(names):
    for name in names:
        cleaned = name.strip()
        print(cleaned)

print(validate_team_names(["  Red Lions  ", "Hawks"]))