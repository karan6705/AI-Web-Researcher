from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are an expert data extraction assistant. Your task is to extract specific information from the following web content: {dom_content}. "
    "Please follow these instructions precisely: \n\n"
    "1. **Extract Information:** Find and extract ONLY the information that matches this description: {parse_description}. "
    "2. **Format Clearly:** Present the extracted information in a clear, organized format. "
    "3. **Be Precise:** If you find multiple instances, list them clearly. "
    "4. **No Explanations:** Do not add explanations, just provide the requested data. "
    "5. **Empty if None:** If no relevant information is found, respond with 'No relevant information found.'"
)


def parse_with_ollama(dom_chunks, parse_description, model_name="llama3.1"):
    model = OllamaLLM(model=model_name)
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
