class StressManagement:
    def __init__(self):
        self.suggestions = {
            "low": [
                "Take a short walk in nature.",
                "Listen to calming music.",
                "Practice deep breathing exercises."
            ],
            "medium": [
                "Try yoga or meditation for at least 20 minutes.",
                "Engage in a creative hobby like painting or writing.",
                "Talk to a close friend or family member about your feelings."
            ],
            "high": [
                "Consult a mental health professional for guidance.",
                "Consider stress-relief medication under medical supervision.",
                "Practice intensive relaxation techniques like progressive muscle relaxation."
            ]
        }

    def get_suggestions(self, stress_level):
        stress_level = stress_level.lower()
        return self.suggestions.get(stress_level, ["Invalid stress level. Please enter low, medium, or high."])

# Example Usage
if __name__ == "__main__":
    sm = StressManagement()
    user_stress_level = input("Enter your stress level (low/medium/high): ")
    suggestions = sm.get_suggestions(user_stress_level)
    print("\nSuggested stress management techniques:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
