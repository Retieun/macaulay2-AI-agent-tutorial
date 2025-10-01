from langchain.tools import Tool
from macaulay2_executor import Macaulay2Executor

class Macaulay2Tool:
    def __init__(self, timeout: int = 30):
        self.executor = Macaulay2Executor(timeout=timeout)
    
    def _run(self, code: str) -> str:
        result = self.executor.execute(code, verbose=True)
        if result['success']:
            return f"Success:\n{result['output']}" if result['output'] else "Success (no output)"
        return f"Error:\n{result['error']}"
    
    def create_langchain_tool(self) -> Tool:
        return Tool(
            name="Macaulay2_Executor",
            func=self._run,
            description="""Execute Macaulay2 code for algebraic computations.
            
Syntax:
- Rings: R = QQ[x,y,z]
- Ideals: I = ideal(f1, f2, ...)
- Gröbner basis: gens gb I
- Hilbert series: hilbertSeries I
- Resolution: res I
- Display: toString
"""
        )
