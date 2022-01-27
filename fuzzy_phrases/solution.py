import json
import logging

logging.basicConfig(
    level="INFO",
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logfile.log",
    filemode="a",
)


def phrase_in_query(phrase, query):
    """
    This function get a specific phrase and checks if it is in a specific query.
    Returns True if that phrase is contained in the query and False in the opposite case
    """
    try:
        j_temp = phrase.split()
        quer = query.split()
        for word in j_temp:
            # Split para coger la palabra especifica
            if word not in quer:
                return False
        return True
    except Exception as e:
        logging.error("Error encountered while looking for a phrase in a query. %s", e)


def phrasel_search(P, Queries):
    """
    This function gets the phrases and the queries and returns a list with the phrases that are used in those queries
    """
    # Write your solution here
    if len(P) <= 1 or len(P) >= 1000000:
        return "Incorrect P length"
    elif len(Queries) <= 1 or len(Queries) >= 1000:
        return "Incorrect Queries length"

    else:
        ans = []
        for query in Queries:
            if len(query) <= 1 or len(query) >= 100000:
                return "Incorrect Querie length"
            temp = []
            for phrase in P:
                all_in = phrase_in_query(phrase, query)

                if all_in == True:
                    phrase_split = phrase.split()
                    query_split = query.split()
                    index_list = [
                        index
                        for index, word in enumerate(query_split)
                        if word == phrase_split[0]
                    ]
                    for pos in index_list:
                        count = 0
                        final_str = ""
                        if len(phrase_split) == 2:
                            try:
                                final_str = ""
                                if phrase_split[0] == query_split[pos]:
                                    final_str += query_split[pos]
                                    if phrase_split[1] != query_split[pos + 1]:
                                        final_str += " " + query_split[pos + 1]
                                        if phrase_split[1] == query_split[pos + 2]:
                                            final_str += " " + query_split[pos + 2]
                                        else:
                                            final_str = ""
                                            break
                                    else:
                                        final_str += " " + query_split[pos + 1]
                            except Exception as e:
                                logging.error(
                                    "Error encountered while adding words with lenght two. %s",
                                    e,
                                )
                        else:
                            for phrase_pos, phrase_word in enumerate(phrase_split):
                                if count > 1:
                                    final_str = ""
                                    break
                                elif query_split[pos + phrase_pos] != phrase_word:
                                    count += 1
                                    if final_str == "":
                                        final_str += query_split[pos + phrase_pos]
                                    else:
                                        final_str += " " + query_split[pos + phrase_pos]
                                    if query_split[pos + phrase_pos + 1] == phrase_word:
                                        final_str += (
                                            " " + query_split[pos + phrase_pos + 1]
                                        )
                                else:
                                    if final_str == "":
                                        final_str += query_split[pos + phrase_pos]
                                    else:
                                        final_str += " " + query_split[pos + phrase_pos]

                        temp.append(final_str)

            ans.append(temp)
        return ans


if __name__ == "__main__":
    with open("sample.json", "r") as f:
        sample_data = json.loads(f.read())
        P, Queries = (
            sample_data["phrases"],
            sample_data["queries"],
        )
        returned_ans = phrasel_search(P, Queries)

        print("============= ALL TEST PASSED SUCCESSFULLY ===============")
