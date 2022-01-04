import research.gscraper
import research.wikisearch


def research(query, qword=[]):
    wiki = wikisearch.research_wiki(query)
    google = gscraper.google_search(query)
    if qword != []:
        for i in qword:
            google += gscraper.google_search(f"{i} {query}")
    return {'wiki': wiki, 'google': google}
