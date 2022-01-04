import research.gscraper
import research.wikisearch


def research(query, qword=[]):
    wiki = wikisearch.research_wiki(query)
    if qword != []:
        for i in qword:
            google = gscraper.google_search(f"{i} {query}")
    else:
        google = gscraper.google_search(query)
    return {'wiki': wiki, 'google': google}
