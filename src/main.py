from langchain_google_genai import ChatGoogleGenerativeAI

from config import get_settings


def main():
    settings = get_settings()

    # Initialize Google Generative AI model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GEMINI_API_KEY,
    )

    # Send a hello world message
    response = llm.invoke("Hello!")

    print(response.content)


if __name__ == "__main__":
    main()
