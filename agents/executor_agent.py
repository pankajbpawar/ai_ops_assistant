import time
from typing import Dict, Any, List

from tools.weather_tool import get_weather
from tools.github_tool import search_repositories


class ExecutorAgent:
    def __init__(self):
        self.max_retries = 3

    def execute_plan(self, plan: Dict[str, Any]) -> List[Dict[str, Any]]:
        print(f"\n⚡ Executor Agent: Executing {len(plan.get('steps', []))} steps")

        results = []

        for step in plan.get("steps", []):
            step_result = self._execute_step(step)

            results.append({
                "tool": step["tool"],
                "action": step["action"],
                "result": step_result,
                "status": "success" if step_result is not None else "failed"
            })

            time.sleep(1)

        print("✅ Executor: Completed all steps")
        return results

    def _execute_step(self, step: Dict[str, Any]):
        tool = step.get("tool")
        action = step.get("action")
        params = step.get("parameters", {})

        print(f"   Step: {tool}.{action}({params})")

        try:
            if tool == "WeatherTool":
                return get_weather(**params)

            elif tool == "GitHubTool":
                return search_repositories(**params)

            else:
                return {"error": f"Unknown tool {tool}"}

        except Exception as e:
            return {"error": str(e)}
