from gradio_client import Client

client = Client("Qwen/Qwen3-Coder-WebDev", hf_token="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")

def lambda_example():
    result = client.predict(api_name="/lambda")
    print(result)

def lambda_1_example():
    result = client.predict(api_name="/lambda_1")
    print(result)

def lambda_2_example():
    result = client.predict(api_name="/lambda_2")
    print(result)

def lambda_3_example():
    result = client.predict(api_name="/lambda_3")
    print(result)

def close_modal_example():
    result = client.predict(api_name="/close_modal")
    print(result)

def open_modal_example():
    result = client.predict(api_name="/open_modal")
    print(result)

def update_system_prompt_example(system_prompt=""):
    result = client.predict(system_prompt_input_value=system_prompt, api_name="/update_system_prompt")
    print(result)

def close_modal_1_example():
    result = client.predict(api_name="/close_modal_1")
    print(result)

def close_modal_2_example():
    result = client.predict(api_name="/close_modal_2")
    print(result)

def reset_system_prompt_example():
    result = client.predict(api_name="/reset_system_prompt")
    print(result)

def close_modal_3_example():
    result = client.predict(api_name="/close_modal_3")
    print(result)

def clear_history_example():
    result = client.predict(api_name="/clear_history")
    print(result)

def open_modal_1_example():
    result = client.predict(api_name="/open_modal_1")
    print(result)

def render_history_example():
    result = client.predict(api_name="/render_history")
    print(result)

def close_modal_4_example():
    result = client.predict(api_name="/close_modal_4")
    print(result)

def open_modal_2_example():
    result = client.predict(api_name="/open_modal_2")
    print(result)

def open_modal_3_example():
    result = client.predict(api_name="/open_modal_3")
    print(result)

def lambda_4_example():
    result = client.predict(api_name="/lambda_4")
    print(result)

def generate_code_example(input_value="Hello World", system_prompt=""):
    result = client.predict(
        input_value=input_value,
        system_prompt_input_value=system_prompt,
        api_name="/generate_code"
    )
    print(result)

def lambda_5_example():
    result = client.predict(api_name="/lambda_5")
    print(result)

def close_modal_5_example():
    result = client.predict(api_name="/close_modal_5")
    print(result)

# Example usage
if __name__ == "__main__":
    # Example: Generate code
    generate_code_example("Create a Python function to calculate factorial", "You are a coding assistant.")