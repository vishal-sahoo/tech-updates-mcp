import arxiv
import nvdlib
import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Tech Updates")


#### Example Tools and Resources ####


@mcp.resource("echo://resource")
def echo_resource() -> str:
    """Echo a message as a resource"""
    return "Resource echo"


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Echo a message as a prompt"""
    return f"Prompt echo: {message}"


#### Common tools for tech updates ####


@mcp.tool()
def get_arxiv_papers(query: str, max_results: int = 5) -> list:
    """Fetch latest papers from arxiv based on a search query"""
    search = arxiv.Search(
        query=query, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate
    )
    results = search.results()

    output = []
    for result in results:
        output.append(
            {"title": result.title, "summary": result.summary, "link": result.entry_id}
        )
    return output


#### Tools for Cybersecurity updates ####


@mcp.tool()
def get_hacker_news(limit: int = 5) -> list:
    """Fetch latest articles from The Hacker News"""
    try:
        response = requests.get("https://thehackernews.com/", timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("div", class_="body-post")

            news_items = []
            for article in articles[:limit]:  # Get first 5 articles
                title = article.find("h2", class_="home-title").text.strip()
                link = article.find("a", class_="story-link")["href"]
                news_items.append({"title": title, "link": link})
            return news_items
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_recent_cves(keyword: str, limit: int = 5):
    """Fetch latest CVEs based on a keyword search"""
    results = nvdlib.searchCVE(keywordSearch=keyword, limit=limit)
    output = []
    for result in results:
        output.append(
            {
                "id": result.id,
                "descriptions": result.descriptions,
            }
        )
    return output


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
