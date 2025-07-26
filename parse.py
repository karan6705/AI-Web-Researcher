import os
import google.generativeai as genai
from langchain_core.prompts import ChatPromptTemplate

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

template = (
    "You are an expert data extraction assistant. Your task is to extract specific information from the following web content: {dom_content}. "
    "Please follow these instructions precisely: \n\n"
    "1. **Extract Information:** Find and extract ONLY the information that matches this description: {parse_description}. "
    "2. **Format Clearly:** Present the extracted information in a clear, organized format. "
    "3. **Be Precise:** If you find multiple instances, list them clearly. "
    "4. **No Explanations:** Do not add explanations, just provide the requested data. "
    "5. **Empty if None:** If no relevant information is found, respond with 'No relevant information found.'"
)


def parse_with_gemini(dom_chunks, parse_description, model_name="gemini-1.5-flash"):
    """
    Parse content using Google Gemini API
    """
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel(model_name)

        parsed_results = []

        for i, chunk in enumerate(dom_chunks, start=1):
            try:
                # Create the prompt
                prompt = template.format(
                    dom_content=chunk,
                    parse_description=parse_description
                )

                # Generate response
                response = model.generate_content(prompt)

                if response.text:
                    parsed_results.append(response.text)
                else:
                    parsed_results.append("No relevant information found.")

                print(f"Parsed batch: {i} of {len(dom_chunks)}")

            except Exception as e:
                print(f"Error parsing chunk {i}: {str(e)}")
                parsed_results.append(f"Error processing chunk {i}: {str(e)}")

        return "\n\n---\n\n".join(parsed_results)

    except Exception as e:
        return f"Error initializing Gemini API: {str(e)}"
