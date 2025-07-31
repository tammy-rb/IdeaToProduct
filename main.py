import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")

from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from tools.google_drive import google_drive_mcp_tools
from datetime import datetime

load_dotenv()

def main():

    idea = "an application that helps users track their daily water intake and set hydration goals."
    app_name = "HydroTrack"

    hl_agent = Agent(
    role="High-Level Design Architect and Google Drive Expert",
    goal="Create comprehensive high-level design documents from project ideas and save them to Google Drive",
    backstory="""I am an experienced system architect with 15+ years of experience in translating 
    innovative ideas into structured, actionable design documents. I specialize in creating clear, 
    comprehensive high-level designs that serve as blueprints for development teams.
    i am very organized, so after i make a document i always save it in a folder with the name of the app.
    I am also an expert in using Google Drive for document management and collaboration.
    I can create folders, documents, and ensure everything is well-organized and accessible.
    """,
    tools=google_drive_mcp_tools,
    verbose=True,
    allow_delegation=False
    )

    hl_task = Task(
    description=f"""
    make an initial high-level design document for the idea: '{idea}', and save it to Google Drive.
    do it step by step:
    1. go to Google Drive and create a new folder named {app_name}.
    2. make a document with the name {app_name}_HL_Design.txt
    3. populate the document with a high-level design document about the idea provided.
    4. save the document in the folder {app_name} in Google Drive.
    5. make sure the document is not empty and contains a high-level design document.
    """,
    agent=hl_agent,
    expected_output="Populated high-level design document in Google Drive about the idea provided"
    )

    crew = Crew(
        agents=[hl_agent],
        tasks=[hl_task],
        #process=Process.sequential,  # Sequential processing ensures proper task dependency
        verbose=True
    )
    
    # Execute the crew
    print("\nStarting crew execution...")
    result = crew.kickoff()
    
    print("\nAll tasks completed successfully!")

    print({
        "idea": idea,
        "crew_result": result.output if hasattr(result, "output") else str(result),
        "status": "completed",
        "timestamp": datetime.now().isoformat()
    })
        

if __name__ == "__main__":
    main()
