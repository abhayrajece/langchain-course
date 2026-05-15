from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def search(query: str) -> str:
    """
    Tools that serarch the web for information about a query and return the results.
    Args:
        query (str): The query to search for.
    Returns:
        The searched Results.
    """
    print(f"searching for {query}")
    return tavily.search(query = query)

llm = ChatOpenAI(model = "gpt-5")
tools = [TavilySearch()]
agent = create_agent(model = llm, tools = tools)

def main():
    print("Hello from agentic-ai!")
    result = agent.invoke({"messages": [HumanMessage(content="Search top 2 job opening on linkedin for Agentic AI in Bangalore, India")]})
    print(result)

    
if __name__ == "__main__":
    main()