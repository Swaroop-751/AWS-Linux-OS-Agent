import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import ShellTool
from langchain.agents import initialize_agent

# ✅ Set Google Gemini API Key
os.environ["GOOGLE_API_KEY"] = "<--YourKey-->"

# ✅ Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

# ✅ Shell Tool
shell_tool = ShellTool()

# ✅ Initialize Agent
myagent = initialize_agent(
    llm=llm,
    tools=[shell_tool],
    verbose=True
)

# ✅ Interactive Agent Loop (no output.log instruction)
while True:
    myprompt = input("Enter your requirement: ")

    if myprompt.lower() in ["exit", "quit"]:
        print("Exiting agent...")
        break

    input_message = {
        "role": "user",
        "content": (
            "You are a Linux administrator. "
            "Execute the required Linux command or logic and only print the final output. "
            "Do not save or write to any file. "
            "Prompt: " + myprompt
        )
    }

    # Run the agent and print output only
    response = myagent.run({"input": input_message})
    print("\n🧩 Final Output:\n", response)

