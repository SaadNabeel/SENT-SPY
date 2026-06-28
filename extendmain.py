import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

name = input("Enter your name: ").strip()

if name == "":
    name = "Mystery Agent"

history = []

positive = 0
negative = 0
neutral = 0

print(f"\nHello, Agent {name}!")
print("Commands: history, stats, reset, exit")

while True:

    text = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if text.lower() == "history":

        if len(history) == 0:
            print("No history available.")
        else:
            print("\nConversation History:")
            for msg, sentiment in history:
                print(msg, "->", sentiment)

    elif text.lower() == "stats":

        print("\nSentiment Statistics")
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)

    elif text.lower() == "reset":

        history.clear()
        positive = 0
        negative = 0
        neutral = 0
        print("All data has been reset.")

    elif text.lower() == "exit":

        total = positive + negative + neutral

        print("\n===== MISSION REPORT =====")
        print("Agent:", name)
        print("Total Messages:", total)
        print("Positive:", positive)
        print("Negative:", negative)
        print("Neutral:", neutral)

        if positive > negative and positive > neutral:
            mood = "Positive"
        elif negative > positive and negative > neutral:
            mood = "Negative"
        else:
            mood = "Neutral"

        print("Overall Mood:", mood)
        print("Mission Complete!")
        break

    elif text == "":
        print("Please enter some text.")

    else:

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.25:
            sentiment = "Positive"
            positive += 1
            print(f"{Fore.GREEN}Positive sentiment detected!{Style.RESET_ALL}")

        elif polarity < -0.25:
            sentiment = "Negative"
            negative += 1
            print(f"{Fore.RED}Negative sentiment detected!{Style.RESET_ALL}")

        else:
            sentiment = "Neutral"
            neutral += 1
            print(f"{Fore.YELLOW}Neutral sentiment detected!{Style.RESET_ALL}")

        history.append((text, sentiment))