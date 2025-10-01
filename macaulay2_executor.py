import subprocess
import tempfile
import os
import re
from typing import Dict, Optional, Tuple

class Macaulay2Executor:
    def __init__(self, timeout: int = 30, max_code_length: int = 10000):
        self.timeout = timeout
        self.max_code_length = max_code_length
        
    def _validate_code(self, code: str) -> Tuple[bool, Optional[str]]:
        if len(code) > self.max_code_length:
            return False, f"Code too long. Max {self.max_code_length} chars."
        
        forbidden = [r'!\s*"', r'run\s*"', r'exec\s*"', r'system\s*"']
        for pattern in forbidden:
            if re.search(pattern, code, re.IGNORECASE):
                return False, "Forbidden system operations detected."
        return True, None
    
    def execute(self, code: str, verbose: bool = False) -> Dict:
        is_valid, error_msg = self._validate_code(code)
        if not is_valid:
            return {'success': False, 'output': '', 'error': error_msg}
        
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.m2', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            result = subprocess.run(
                ['M2', '--script', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            if temp_file:
                os.unlink(temp_file)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout.strip(),
                'error': result.stderr.strip() if result.returncode != 0 else ''
            }
            
        except subprocess.TimeoutExpired:
            if temp_file:
                os.unlink(temp_file)
            return {'success': False, 'output': '', 'error': f'Timeout after {self.timeout}s'}
        except FileNotFoundError:
            return {'success': False, 'output': '', 'error': 'M2 not found in PATH'}
        except Exception as e:
            if temp_file:
                os.unlink(temp_file)
            return {'success': False, 'output': '', 'error': str(e)}
