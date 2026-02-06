class VerifierAgent:
    def verify_results(self, task, results):
        return {
            "status": "complete",
            "confidence": 0.9,
            "results": results
        }

    def format_final_output(self, verification):
        lines = []
        lines.append("\n================ FINAL RESULTS ================\n")

        for item in verification["results"]:

            # WEATHER RESULT
            if item["tool"] == "WeatherTool":
                weather = item["result"]
                lines.append(
                    f"🌤 Weather in {weather.get('city','')} : "
                    f"{weather.get('temperature','')}°C, "
                    f"{weather.get('description','')}"
                )

            # GITHUB RESULT
            if item["tool"] == "GitHubTool":
                lines.append("\n🔥 Top Python Repositories:")
                for repo in item["result"][:5]:
                    lines.append(
                        f"- {repo['name']} ⭐ {repo['stars']}"
                    )

        lines.append("\n==============================================")
        return "\n".join(lines)
