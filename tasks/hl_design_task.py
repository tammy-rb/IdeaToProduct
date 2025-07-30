from crewai import Task

def create_hl_design_template(idea: str) -> str:
    """Generate a concise high-level design document template"""
    return f"""# High-Level Design Document

**Project:** {idea}

## 1. Executive Summary
Brief project overview and main objectives.

## 2. System Architecture
### Components
- Core modules and responsibilities
- Data flow and dependencies

### Technology Stack
- Frontend: [Framework recommendation]
- Backend: [Architecture recommendation]
- Database: [Storage solution]
- APIs: [Third-party services]

## 3. Core Features
### Primary Features
- Essential functionality list
- User workflows

### Secondary Features
- Enhancement features
- Future releases

## 4. Data & API Design
- Key data entities and relationships
- RESTful endpoints structure
- Authentication approach

## 5. Implementation Phases
### Phase 1 (Weeks 1-4): Foundation
- Infrastructure setup
- Core APIs

### Phase 2 (Weeks 5-8): Features
- Primary features
- UI implementation

### Phase 3 (Weeks 9-12): Enhancement
- Optimization
- Testing & deployment

## 6. Risk Assessment
- Technical challenges
- Timeline risks
- Mitigation strategies

## 7. Success Metrics
- Performance KPIs
- User adoption targets

---
*Foundation document for detailed specifications.*"""

def create_hl_design_task(agent, idea: str):
    """Create the high-level design task"""
    design_template = create_hl_design_template(idea)
    
    return Task(
        description=f"""
        Create a comprehensive high-level design document for: "{idea}"
        
        Requirements:
        1. Analyze the idea and create a tailored design document
        2. Use the template below as a starting point and enhance with specific details
        3. Save the document to Google Drive with filename: "HL_Design_[ProjectName]_[Timestamp].md"
        
        Template to customize:
        {design_template}
        
        Focus on:
        - Technology stack appropriate for this specific idea
        - Realistic implementation timeline
        - Specific feature breakdown
        - Project-specific risks and challenges
        """,
        agent=agent,
        expected_output="High-level design document uploaded to Google Drive with confirmation and filename"
    )
