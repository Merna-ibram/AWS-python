sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_extract = ["name", "salary"]

result_dict = {key: sample_dict[key] for key in keys_to_extract if key in sample_dict}

print(result_dict)
