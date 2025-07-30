from crewai import Crew, Task, Process
from agents.HL_Design_agent import HighLevelDesignAgent
from agents.Detailed_Design_agent import DetailedDesignAgent
from datetime import datetime
from tasks.hl_design_task import create_hl_design_task
from tasks.detailed_design_task import create_detailed_design_task

class IdeaToProductionCrew:
    def __init__(self):
        self.hl_agent = HighLevelDesignAgent()
        self.detailed_agent = DetailedDesignAgent()
        
    def process_idea_to_production(self, idea: str):
        """Main orchestration method to process an idea through both agents"""
        print(f"🚀 Starting Idea to Production process for: {idea[:100]}...")
        
        try:
            # Create agents using their create_agent methods
            hl_agent = self.hl_agent.create_agent()
            detailed_agent = self.detailed_agent.create_agent()
            
            # Create HL Design Task (Agent 1)
            hl_task = create_hl_design_task(hl_agent, idea)
            
            # Create Detailed Design Task (Agent 2)
            detailed_task = create_detailed_design_task(detailed_agent, hl_task)
            
            # Create crew with both agents and tasks
            crew = Crew(
                agents=[hl_agent, detailed_agent],
                tasks=[hl_task, detailed_task],
                process=Process.sequential,  # Sequential processing ensures proper task dependency
                verbose=True
            )
            
            # Execute the crew
            print("\n🚀 Starting crew execution...")
            result = crew.kickoff()
            
            print("\n✅ All tasks completed successfully!")
            print("✅ High-Level Design document created and uploaded to Google Drive")
            print("✅ Detailed Design document created and uploaded to Google Drive") 
            print("✅ Development Epic and Stories created in Jira")
            
            return {
                "idea": idea,
                "crew_result": result,
                "status": "completed",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Error in crew execution: {str(e)}")
            raise
