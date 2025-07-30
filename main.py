from dotenv import load_dotenv
from crew_manager import IdeaToProductionCrew

load_dotenv()

def main():
    """Main execution function"""
    print("🚀 Welcome to Idea to Production System!")
    print("=" * 50)
    
    # Initialize the crew manager
    crew_manager = IdeaToProductionCrew()
    
    # Get user input for the idea
    #print("\n💡 Please enter your project idea:")
    #user_idea = input().strip()
    user_idea = "an application that helps users track their daily water intake and set hydration goals."
    
    try:
        # Start the crew process
        result = crew_manager.process_idea_to_production(user_idea)
        
        print("\n" + "=" * 50)
        print("🎉 PROCESS COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print(f"📋 Status: {result['status']}")
        print(f"⏰ Completed at: {result.get('timestamp', 'N/A')}")
        print("\n📊 Deliverables:")
        print("  ✅ High-Level Design document uploaded to Google Drive")
        print("  ✅ Detailed Design document uploaded to Google Drive")
        print("  ✅ Development Epic and Stories created in Jira")
        print("\n🚀 Your idea is now ready for development!")
        
    except Exception as e:
        print("\n" + "=" * 50)
        print("💥 PROCESS FAILED!")
        print("=" * 50)
        print(f"❌ Error: {str(e)}")
        print("\n🔍 Please check:")
        print("  - MCP server configurations")
        print("  - Google Drive credentials")
        print("  - Jira API credentials")
        print("  - Network connectivity")

if __name__ == "__main__":
    main()
