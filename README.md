AI Personal Finance Planner

An intelligent tool designed to help users manage their finances by creating personalized budgets, investment plans, and saving strategies. Leveraging the power of GPT-4, the planner assists users in setting financial goals and provides tailored financial plans based on their current financial situation.

Libraries Used
textwrap: For managing string formatting.
phi.assistant: Utilized to create assistant instances for interacting with GPT-4.
phi.tools.serpapi_tools: Tools for integrating SerpAPI functionalities.
streamlit: Used to create an interactive web application interface.
phi.llm.openai: Interfaces with OpenAI's GPT-4 to generate financial plans.

Pip installs that were used:
1. pip install streamlit
2. pip install phidata
3. pip install openai
4. pip install google-search-results
   
How It Works:

Setup Streamlit Interface:

The application uses Streamlit to create a user-friendly web interface.
Users are prompted to input their OpenAI API key and SerpAPI key to access GPT-4 functionalities.
User Input:

Users provide their financial goals and current financial situation through text inputs.
Generating Financial Plan:

Upon clicking the "Generate Financial Plan" button, the application processes the inputs.

1. It uses the phi.assistant module to create instances of assistants.
   
2. The assistants run the provided financial goals and current situation through GPT-4.
   
3. The generated financial plan is then displayed to the user.
   
4. Usage:
   After you've downloaded the code and installed the libraries, open the terminal and use "streamlit run LLMfin.py"

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
