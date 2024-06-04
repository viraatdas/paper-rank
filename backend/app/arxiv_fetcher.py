import requests
from xml.etree import ElementTree

ARXIV_API_URL = "http://export.arxiv.org/api/query?search_query={query}&start={start}&max_results={max_results}"

def fetch_papers(query="all", start=0, max_results=10):
    url = ARXIV_API_URL.format(query=query, start=start, max_results=max_results)
    response = requests.get(url)
    if response.status_code != 200:
        return []

    root = ElementTree.fromstring(response.content)
    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
        arxiv_id = entry.find("{http://www.w3.org/2005/Atom}id").text.split("/")[-1]
        link = entry.find("{http://www.w3.org/2005/Atom}link[@type='text/html']").attrib['href']
        papers.append({
            "title": title,
            "abstract": summary,
            "url": link,
            "arxiv_id": arxiv_id
        })
    return papers
