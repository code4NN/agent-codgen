from dotenv import load_dotenv
load_dotenv()

from llm.client import call_llm

def main():
    question=input("Please ask me the question: ")
    response = call_llm(
        model="gemini-2.5-flash",
        system_prompt=(
            "You are an ISKCON Preacher with 24 years of experience"
            "Do not explain reasoning.\n"
            "Produce the final answer only."
        ),
        prompt=question,
        temperature=0.0,
        top_p=0.1,
        max_tokens=2048,
    )

    print("MODEL OUTPUT:")
    print(response.text)


if __name__ == "__main__":
    main()
    # from google import genai

    # # The client gets the API key from the environment automatically
    # client = genai.Client()

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash",
    #     contents="Explain how AI works in a few words"
    # )

    # print(response.text)


