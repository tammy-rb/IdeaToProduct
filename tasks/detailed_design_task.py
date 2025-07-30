from crewai import Task

def create_detailed_design_template() -> str:
    """Generate a concise detailed design document template"""
    return """# Detailed Design Document

## Phase 1: Foundation
### Database Design
- Entity models with key attributes
- Relationships and constraints
- Schema scripts

### API Specification
- Endpoint definitions (CRUD operations)
- Request/response formats
- Authentication & error handling

### Infrastructure
- Development environment setup
- CI/CD pipeline basics
- Docker configuration

## Phase 2: Core Implementation
### Frontend Architecture
- Component hierarchy
- State management
- UI/UX specifications

### Backend Services
- Business logic layer
- Data validation
- Integration patterns

### Testing Strategy
- Unit testing (80% coverage)
- Integration testing
- API testing

## Phase 3: Advanced Features
### Performance & Security
- Caching strategy
- Authentication/authorization
- Monitoring & logging

### Deployment
- Production setup
- Performance monitoring
- Error tracking

## Development Tasks Breakdown
### Epic: [Project Name]

#### Phase 1 Stories:
1. Database setup & schema
2. API framework & endpoints
3. Infrastructure & CI/CD
4. Development environment

#### Phase 2 Stories:
5. Frontend components
6. Backend services
7. API integration
8. UI implementation

#### Phase 3 Stories:
9. Performance optimization
10. Security implementation
11. Monitoring setup
12. Production deployment

Each story includes acceptance criteria, estimates, and dependencies."""

def create_detailed_design_task(agent, hl_task):
    """Create the detailed design task"""
    template = create_detailed_design_template()
    
    return Task(
        description=f"""
        Create detailed design and Jira tasks based on the high-level design from the previous task.
        
        Steps:
        1. Retrieve the high-level design document from Google Drive
        2. Create comprehensive detailed design expanding on the high-level design
        3. Save detailed design to Google Drive as "Detailed_Design_[ProjectName]_[Timestamp].md"
        4. Create Jira Epic and development tasks:
           - Epic for overall project
           - 12 development stories across 3 phases
           - Detailed acceptance criteria for each
           - Time estimates and priorities
           - Proper task linking and dependencies
        
        Template structure:
        {template}
        
        Ensure tasks are actionable and ready for development teams.
        """,
        agent=agent,
        expected_output="Detailed design document in Google Drive and complete Jira task structure with Epic and Stories",
        context=[hl_task]
    )
