import streamlit as st
from gradio_client import Client

st.title("PINNACLE AI APP BUILDER")

st.markdown("Generate code using AI models via Gradio API.")

# Input fields
input_value = st.text_area("Input Description", placeholder="Describe what code to generate", height=100)
system_prompt = st.text_input("System Prompt", placeholder="Optional system prompt", value="")

# Button
if st.button("Generate Code"):
    if input_value.strip():
        with st.spinner("Generating code..."):
            try:
                # Try to connect to a working Hugging Face space
                client = Client("microsoft/DialoGPT-medium")
                result = client.predict(input_value, api_name="/predict")
                
                st.subheader("Generated Response")
                st.write(result)
                
            except Exception as e:
                st.error(f"Error connecting to AI model: {str(e)}")
                st.info("Please check if the Hugging Face space is available or try a different model.")
                
                # Show the input for debugging
                st.subheader("Your Input")
                st.write(f"**Description:** {input_value}")
                if system_prompt:
                    st.write(f"**System Prompt:** {system_prompt}")
    else:
        st.warning("Please enter an input description.")

st.markdown("---")
st.markdown("**Note:** This app connects to Hugging Face models. If you encounter errors, the model space may be unavailable.")
