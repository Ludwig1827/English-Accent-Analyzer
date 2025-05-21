@tool
def summarize_text(text: str) -> str:

    """Summarizes a given block of text using a language model."""
    llm = ChatOpenAI(model_name="gpt-4o-mini")
    prompt = (
        "Please provide a short, clear summary of the following text:\n\n"
        f"{text}\n\n"
        "Summary:"
    )
    
    return llm.invoke(prompt)
