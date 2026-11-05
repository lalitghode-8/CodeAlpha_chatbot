import string


def clean_input(user_text: str) -> str:
    """
    Cleans and standardizes user input:
    1. Removes leading/trailing spaces (.strip())
    2. Converts text to lowercase (.lower())
    3. Removes punctuation like '!', '?', '.' (.translate())
    """
    text = user_text.strip().lower()
    # Remove all punctuation marks so "Hello!" becomes "hello"
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def get_bot_response(user_message: str) -> str:
    """
    Determines the chatbot's reply using if-elif-else rules.
    Takes raw user input and returns a predefined string response.
    """
    cleaned_msg = clean_input(user_message)

    # Rule 1: Empty input check
    if not cleaned_msg:
        return "Please type a message so we can chat!"

    # Rule 2: Greetings
    elif cleaned_msg in ["hello", "hi", "hey", "greetings"]:
        return "Hi!"

    # Rule 3: Status inquiries
    elif cleaned_msg in ["how are you", "how are you doing", "hows it going"]:
        return "I'm fine, thanks!"

    # Rule 4: Identity / Name check
    elif cleaned_msg in ["what is your name", "who are you"]:
        return "I am a simple rule-based Python Chatbot."

    # Rule 5: Help command
    elif cleaned_msg == "help":
        return "You can say 'hello', 'how are you', 'what is your name', or 'bye'."

    # Rule 6: Exit / Goodbye
    elif cleaned_msg in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"

    # Fallback Rule: Unrecognized input
    else:
        return "I'm sorry, I don't understand that. Type 'help' to see what I can answer."


def run_tests() -> None:
    """
    Automated test suite to verify the chatbot's logic and edge cases
    before starting the interactive conversation.
    """
    test_cases = [
        ("hello", "Hi!"),
        ("  HELLO!  ", "Hi!"),               # Tests spaces, uppercase, punctuation
        ("how are you?", "I'm fine, thanks!"), # Tests question mark removal
        ("bye", "Goodbye!"),
        ("", "Please type a message so we can chat!"), # Tests empty input
        ("random text", "I'm sorry, I don't understand that. Type 'help' to see what I can answer.")
    ]

    for test_input, expected_output in test_cases:
        actual_output = get_bot_response(test_input)
        assert actual_output == expected_output, f"Test failed for input: '{test_input}'"

    print("[System Check] All 6 unit tests passed successfully!\n")


def start_chat() -> None:
    """
    Main loop that handles user Input/Output until the user exits.
    """
    print("=" * 45)
    print("       Welcome to the Python Chatbot!        ")
    print("   (Type 'help' for options or 'bye' to exit) ")
    print("=" * 45)

    # Infinite loop to keep the conversation running
    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            # Gracefully handles Ctrl+C or unexpected terminal closure
            print("\nBot: Goodbye!")
            break

        # Get reply from the logic function
        reply = get_bot_response(user_input)
        print(f"Bot: {reply}")

        # Break the loop if the user said goodbye
        if reply == "Goodbye!":
            break


# Entry point of the program
if __name__ == "__main__":
    run_tests()   # Step 1: Verify code quality with automated tests
    start_chat()  # Step 2: Launch interactive chat