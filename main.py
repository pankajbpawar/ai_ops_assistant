import os
import json
import time
from typing import Dict, Any

from fastapi import FastAPI
from dotenv import load_dotenv

from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.verifier_agent import VerifierAgent

# Load environment variables
load_dotenv()

# --------------------------------------------------
# AI OPERATIONS ASSISTANT CLASS
# --------------------------------------------------

class AIOperationsAssistant:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent()

    def process_task(self, user_task: str) -> Dict[str, Any]:
        print("\n" + "=" * 60)
        print("🤖 AI OPERATIONS ASSISTANT STARTING")
        print("=" * 60)

        # Step 1: Planning
        print("\n📋 PHASE 1: PLANNING")
        plan = self.planner.create_plan(user_task)

        if "error" in plan:
            return {"error": f"Planning failed: {plan['error']}"}

        print(json.dumps(plan, indent=2))

        # Step 2: Execution
        print("\n⚡ PHASE 2: EXECUTION")
        results = self.executor.execute_plan(plan)

        # Step 3: Verification
        print("\n🔍 PHASE 3: VERIFICATION")
        verification = self.verifier.verify_results(
            plan.get("task_description", user_task),
            results
        )

        final_output = self.verifier.format_final_output(verification)

        return {
            "plan": plan,
            "execution_results": results,
            "verification": verification,
            "final_output": final_output
        }

# --------------------------------------------------
# FASTAPI SETUP
# --------------------------------------------------

app = FastAPI()
assistant = AIOperationsAssistant()

@app.post("/run")
def run_task(task: dict):
    user_task = task.get("task")
    return assistant.process_task(user_task)

# --------------------------------------------------
# CLI MODE
# --------------------------------------------------

def run_cli():
    print("\n" + "=" * 60)
    print("🤖 AI Operations Assistant - CLI Mode")
    print("=" * 60)

    while True:
        user_input = input("\n🎯 Enter your task: ").strip()

        if user_input.lower() in ["exit", "quit", "q"]:
            print("Goodbye! 👋")
            break

        result = assistant.process_task(user_input)
        print(result.get("final_output", result))


# --------------------------------------------------

if __name__ == "__main__":
    run_cli()
