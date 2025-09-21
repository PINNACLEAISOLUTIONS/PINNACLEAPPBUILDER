import streamlit as st
from gradio_client import Client

# Initialize the client
client = Client("Qwen/Qwen3-Coder-WebDev", hf_token="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")

st.title("PINNACLE AI APP BUILDER")

st.markdown("Generate code using the Qwen3 model via Gradio API.")

# Input fields
input_value = st.text_area("Input Description", placeholder="Describe what code to generate", height=100)
system_prompt = st.text_input("System Prompt", placeholder="Optional system prompt", value="")

# Button
if st.button("Generate Code"):
    if input_value.strip():
        with st.spinner("Generating code..."):
            try:
                result = client.predict(
                    input_value=input_value,
                    system_prompt_input_value=system_prompt,
                    api_name="/generate_code"
                )
                # result is a tuple: (markdown, textbox_value)
                st.subheader("Generated Code (Markdown)")
                st.markdown(result[0])
                st.subheader("Output Text")
                st.code(result[1], language='text')
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter an input description.")
