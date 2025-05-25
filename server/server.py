import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Tech Updates")


@mcp.resource("echo://message")
def echo_resource() -> str:
    """Echo a message as a resource"""
    return "Resource echo"


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.tool()
def get_hacker_news() -> list:
    """Fetch latest articles from The Hacker News"""
    try:
        response = requests.get("https://thehackernews.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("div", class_="body-post")

            news_items = []
            for article in articles[:5]:  # Get first 5 articles
                title = article.find("h2", class_="home-title").text.strip()
                link = article.find("a", class_="story-link")["href"]
                news_items.append({"title": title, "link": link})
            return news_items
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
