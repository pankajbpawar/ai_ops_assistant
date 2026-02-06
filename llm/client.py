import os
import json
from typing import Dict, Any, List
from groq import Groq

class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.1-8b-instant"

    def generate_plan(self, user_task: str) -> Dict[str, Any]:
        prompt = f"""
Convert user task into JSON steps using GitHubTool and WeatherTool.

Task: {user_task}

Return JSON:
{{
 "task_description":"...",
 "steps":[
   {{
     "tool":"GitHubTool",
     "action":"search_repositories",
     "parameters":{{"query":"python"}}
   }}
 ]
}}
"""

        try:
            res = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role":"user","content":prompt}]
            )
            return json.loads(res.choices[0].message.content)
        except Exception as e:
            print("LLM planning error:", e)
            return {"error":"planning failed"}

    def verify_output(self, task_description: str, results: List[Dict[str, Any]]):
        return {"final_answer": str(results)}
