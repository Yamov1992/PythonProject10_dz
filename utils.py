import json
import requests

def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_candidates_all():
    return load_candidates()

def get_candidate_by_pk(pk):

    candidates = get_candidates_all()

    for candidate in candidates:
        if pk == candidate["pk"]:
            return candidate

    return "not found"

def get_candidates_by_skill(skill):

    result = []


    for candidate in load_candidates():
        skills = candidate["skills"].lower().split(", ")
        if skill in skills:
            result.append(candidate)

    return result

# user_input = input()
# result = get_candidates_by_skills(user_input)
# print(result)