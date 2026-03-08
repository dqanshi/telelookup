def format_results(results):

    if not results:
        return "❌ No results found."

    text = "🔎 Results\n\n"

    for r in results:
        text += f"`{r}`\n\n"

    return text
