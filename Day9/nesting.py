# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": {"Paris": 5, "Lille": 7, "Dijon": 3}, "total_visited": 15},
    "Germany": {"Berlin": 3, "Hamburg": 12, "Stuttgart": 20}
}

# print(travel_log["France"]["cities_visited"]["Paris"])
# print(travel_log["France"]["total_visited"])


# Nesting Dictionary in a List

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Stuttgart", "Hamburg", "Frankfurt"],
        "total_visits": 15
    },
]


