import os
import json
import solution

folder = os.getcwd() + os.sep


def test_phrase_in_query():
    with open(folder + "sample.json", "r") as f:
        sample_data = json.loads(f.read())
        phrases, queries = sample_data["phrases"][0], sample_data["queries"][1]

    assert solution.phrase_in_query(phrases, queries) == True


def test_sample():
    with open(folder + "sample.json", "r") as f:
        sample_data = json.loads(f.read())
        phrases, queries = sample_data["phrases"], sample_data["queries"]
        returned_ans = solution.phrasel_search(phrases, queries)
        solutions = sample_data["solution"]
        for i in returned_ans:
            i.sort()
        for i in solutions:
            i.sort()
        assert returned_ans == solutions


def test_20_points():
    with open(folder + "20_points.json", "r") as f:
        sample_data = json.loads(f.read())
        phrases, queries = sample_data["phrases"], sample_data["queries"]
        returned_ans = solution.phrasel_search(phrases, queries)
        solutions = sample_data["solution"]
        for i in returned_ans:
            i.sort()
        for i in solutions:
            i.sort()
        assert returned_ans == solutions


def test_30_points():
    with open(folder + "30_points.json", "r") as f:
        sample_data = json.loads(f.read())
        phrases, queries = sample_data["phrases"], sample_data["queries"]
        returned_ans = solution.phrasel_search(phrases, queries)
        solutions = sample_data["solution"]
        for i in returned_ans:
            i.sort()
        for i in solutions:
            i.sort()
        assert returned_ans == solutions


def test_50_points():
    with open(folder + "50_points.json", "r") as f:
        sample_data = json.loads(f.read())
        phrases, queries = sample_data["phrases"], sample_data["queries"]
        returned_ans = solution.phrasel_search(phrases, queries)
        solutions = sample_data["solution"]
        for i in returned_ans:
            i.sort()
        for i in solutions:
            i.sort()
        assert returned_ans == solutions
