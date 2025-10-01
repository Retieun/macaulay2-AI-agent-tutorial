import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from m2_tool import Macaulay2Tool

load_dotenv()

class Macaulay2Agent:
    def __init__(self, model: str = "claude-sonnet-4-20250514", temperature: float = 0):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found")
        
        self.llm = ChatAnthropic(model=model, temperature=temperature, max_tokens=4096)
        self.tools = [Macaulay2Tool(timeout=30).create_langchain_tool()]
        
        template = """Expert mathematician with Macaulay2 access.

Analyze question → Write M2 code → Execute → Explain results

Syntax: R = QQ[x,y,z], I = ideal(...), gens gb I, hilbertSeries I, res I

Tools: {tools}
Tool names: [{tool_names}]

Question: {input}
Thought: 
Action: 
Action Input: 
Observation: 
...
Final Answer: 

{agent_scratchpad}"""
        
        prompt = PromptTemplate(
            input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
            template=template
        )
        
        agent = create_react_agent(self.llm, self.tools, prompt)
        self.agent_executor = AgentExecutor(
            agent=agent, tools=self.tools, verbose=True, 
            max_iterations=5, handle_parsing_errors=True
        )
    
    def run(self, query: str) -> str:
        try:
            return self.agent_executor.invoke({"input": query})['output']
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("Macaulay2 Agent powered by Claude\n")
    agent = Macaulay2Agent()
    print("Ready!\n")
    
    while True:
        query = input("\nQuery (or 'quit'): ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            break
        if query:
            print(f"\n{agent.run(query)}\n")

if __name__ == "__main__":
    main()
