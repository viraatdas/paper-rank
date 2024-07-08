import feedparser
from urllib.parse import urlencode, quote

def fetch_papers(query, max_results=10):
    base_url = 'http://export.arxiv.org/api/query?'
    query_params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results
    }
    query_url = base_url + urlencode(query_params, quote_via=quote)
    
    feed = feedparser.parse(query_url)
    papers = []

    for entry in feed.entries:
        paper = {
            'title': entry.title,
            'abstract': entry.summary,
            'url': entry.link,
            'arxiv_id': entry.id.split('/')[-1],
            'published': entry.published,
        }
        papers.append(paper)

    return papers

# Example usage
papers = fetch_papers('machine learning', max_results=10)
for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"Abstract: {paper['abstract']}")
    print(f"URL: {paper['url']}")
    print(f"arxiv_id: {paper['arxiv_id']}")
    print(f"Published: {paper['published']}\n")
