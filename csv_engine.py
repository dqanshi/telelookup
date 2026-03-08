from config import CSV_PATH, MAX_RESULTS


def search_csv(query):

    results = []

    with open(CSV_PATH, "r", encoding="utf-8", errors="ignore") as f:

        for line in f:

            if query in line:

                results.append(line.strip())

                if len(results) >= MAX_RESULTS:
                    break

    return results
