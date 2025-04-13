from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm


def get_custom_message(paths: str) -> str:
    """Prints a custom message when the user asks for it.

    Args:
        None.

    Returns:
        dict: status and result.
    """
    return "This is a custom message from the Ollama agent. You can ask me anything and I will respond accordingly."

root_agent = LlmAgent(
    # LiteLLM knows how to connect to a local Ollama server by default
    # Proxying via the openai standards
    # Add the below env variables in the .env file (https://github.com/google/adk-python/issues/49)
    # OPENAI_API_BASE=http://localhost:11434/v1
    # OPENAI_API_KEY=unused

    model=LiteLlm(model="openai/granite3.1-dense:8b"), 
    name="ollama_gemma_agent",
    instruction=" You are a helpful assistant."
                " Use the `get_custom_message` tool to print a custom message when the user asks for it."
                " For all other queries, respond with the answer. Do not use the tool."
                " If you need to use the tool, respond with the answer and then use the tool."
                " Do not use the tool for every query.",
    tools=[get_custom_message]
)