import json
from typing import Dict, Any
from llm.client import LLMClient


class PlannerAgent:
    def __init__(self):
        self.llm_client = LLMClient()
        self.available_tools = {
            "GitHubTool": ["search_repositories"],
            "WeatherTool": ["get_weather"]
        }

    def create_plan(self, user_task):
        print(f"\n📋 Planner Agent: Processing task: '{user_task}'")

        plan = self.llm_client.generate_plan(user_task)

        # If LLM fails, use fallback plan
        if "error" in plan or "steps" not in plan:
            print("⚠ Using fallback static plan")

            steps = []

            # WEATHER HANDLING
            if "weather" in user_task.lower():
                city = "Mumbai"  # default city

                if "in" in user_task.lower():
                    city = user_task.lower().split("in")[-1].strip()

                steps.append({
                    "tool": "WeatherTool",
                    "action": "get_weather",
                    "parameters": {"city": city.title()}
                })

            # GITHUB HANDLING
            if "github" in user_task.lower() or "repo" in user_task.lower():
                steps.append({
                    "tool": "GitHubTool",
                    "action": "search_repositories",
                    "parameters": {"query": "python"}
                })

            return {
                "task_description": user_task,
                "steps": steps
            }

        return plan

    def _validate_step(self, step: Dict[str, Any]) -> bool:
        required_fields = ["tool", "action", "parameters"]

        for field in required_fields:
            if field not in step:
                return False

        if step["tool"] not in self.available_tools:
            return False

        if step["action"] not in self.available_tools[step["tool"]]:
            return False

        return True
