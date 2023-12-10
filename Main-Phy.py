class Health:
    def __init__(self, questions, recommendation_video_good, recommendation_video_struggle):
        self.questions = questions
        self.score = 0
        self.recommendation_video_good = recommendation_video_good
        self.recommendation_video_struggle = recommendation_video_struggle


    def assess(self):
        for question in self.questions:
            answer = input(question + " (Yes or No): ")
            if "Yes" in answer or "yes" in answer:
                self.score += 1
            

    def display_result(self):
        print(f"{self.__class__.__name__} Assessment Completed!")
        print(f"Your {self.__class__.__name__} Score: {self.score}")
        if self.score <= 6:
            print(f"Seems like you struggling in this aspect of health.")
            print(f"We would like you to watch this: {self.recommendation_video_struggle}")
        else:
            print(f"Your {self.__class__.__name__} is fine! Watch: {self.recommendation_video_good}")

class MentalHealth(Health):
    def __init__(self):
        questions = [
            "Do you often practice stress-reducing activities?",
            "Do you maintain a healthy sleep routine?",
            "Have you experienced positive changes in your mood recently?",
            "Do you prioritize self-care to avoid constant fatigue?",
            "Do you actively challenge and replace negative thoughts?",
            "Do you enjoy moments of solitude for self-reflection?",
            "Are you mindful and intentional in your thinking?",
            "Do you practice self-compassion?",
            "Do you focus on your personal growth rather than comparisons?",
            "Do you recognize and appreciate your strengths?"
        ]
        super().__init__(questions, "https://www.youtube.com/watch?v=-OAjfrhuwRk",
                         "https://www.youtube.com/watch?v=qT4CwQW0ltw")

class PhysicalHealth(Health):
    def __init__(self):
        questions = [
            "Do you play any physical sports?",
            "Do you have a balanced diet.",
            "Do you get enough quality sleep?",
            "Do you manage stress physically?",
            "Do you take breaks when working physically?",
            "Do you exercise or workout?",
            "Do you have enough energy for the day?",
            "Does your body sweat more often from physical activities than from heat?",
            "Do you practice proper hygiene?",
            "Are you attentive to any signs of discomfort or pain in your body, seeking appropriate care when needed?"
        ]
        super().__init__(questions, "https://www.youtube.com/watch?v=qTHVnGA5rzU",
                         "https://www.youtube.com/watch?v=Srvnee0ha3g")

class Nutrition(Health):
    def __init__(self):
        questions = [
            "Do you avoid daily intake of junk foods?",
            "Do you consume a balanced diet?",
            "Do you include variety of fruits and vegetables in your regular meals?",
            "Are you mindful of portion sizes?",
            "Do you stay hydrated throughout the day?",
            "Do you have a daily meal plan?",
            "Do you stop eating when you're full?",
            "Are you taking any food supplement?",
            "Do you always eat at the right time?",
            "Do you avoid drinking alcohol?"
        ]
        super().__init__(questions, "https://www.youtube.com/watch?v=9G6qttNNYVo",
                         "https://www.youtube.com/watch?v=jwWpTAXu-Sg")


def main():
    while True:
        print("**********************************************")
        print("Choose what aspect of health you want to assess:")
        print("1. Mental Health")
        print("2. Physical Health")
        print("3. Nutrition")
        print("4. Exit")
        print("**********************************************")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting the program. Goodbye!")
            break

        selected_aspect_class = None
        if choice == '1':
            selected_aspect_class = MentalHealth
        elif choice == '2':
            selected_aspect_class = PhysicalHealth
        elif choice == '3':
            selected_aspect_class = Nutrition

        if selected_aspect_class:
            health_aspect = selected_aspect_class()
            health_aspect.assess()
            health_aspect.display_result()
        
        print("\nPress Enter to go to the main menu...")
        input()

if __name__ == "__main__":
    main()