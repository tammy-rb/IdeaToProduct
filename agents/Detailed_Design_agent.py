from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os
import json
from datetime import datetime

class DetailedDesignAgent:
    def __init__(self):
        # Load MCP configuration
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'mcp_config.json')
        try:
            with open(config_path, 'r') as f:
                mcp_config = json.load(f)
        except FileNotFoundError:
            print(f"Configuration file not found at {config_path}")
            exit(1)

        # Get both Google Drive and Jira MCP server configurations
        gdrive_config = mcp_config['mcpServers']['gdrive']
        jira_config = mcp_config['mcpServers']['jira']

        # Configure Google Drive MCP server parameters
        self.gdrive_params = StdioServerParameters(
            command=gdrive_config['command'],
            args=gdrive_config['args'],
            env={**gdrive_config.get('env', {}), **os.environ}
        )

        # Configure Jira MCP server parameters
        self.jira_params = StdioServerParameters(
            command=jira_config['command'],
            args=jira_config['args'],
            env={**jira_config.get('env', {}), **os.environ}
        )

    def create_agent(self):
        """Create agent with MCP tools using context managers for both Google Drive and Jira"""
        with MCPServerAdapter(self.gdrive_params) as gdrivetool, MCPServerAdapter(self.jira_params) as jiratool:
            all_tools = [*gdrivetool, *jiratool]
            print(f"Available Google Drive tools: {[tool.name for tool in gdrivetool]}")
            print(f"Available Jira tools: {[tool.name for tool in jiratool]}")
            print(f"Total combined tools: {len(all_tools)}")

            agent = Agent(
            role="Detailed Design Specialist",
            goal="Transform high-level designs into comprehensive detailed specifications and create development tasks in Jira",
            backstory="""I am a senior technical architect and project manager with expertise in breaking down 
            high-level designs into detailed technical specifications. I excel at creating comprehensive 
            documentation and organizing development work into manageable tasks with clear requirements and 
            acceptance criteria.""",
            tools=all_tools,
            verbose=True,
            allow_delegation=False
            )
        
        return agent

    def create_detailed_design_template(self, hl_design: str) -> str:
        """Generate a detailed design document from high-level design"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return f"""# Detailed Design Document

            **Based on High-Level Design**
            **Generated on:** {timestamp}

            ## Phase 1: Foundation & Infrastructure

            ### 1.1 Database Design
            #### Entity Relationship Diagram
            - Detailed data models with attributes and constraints
            - Relationship mappings and cardinalities
            - Database schema with indexes and constraints

            #### Database Schema Scripts
            - Table creation scripts
            - Initial data migration scripts
            - Database configuration settings

            ### 1.2 API Specification
            #### RESTful Endpoints
            - Detailed endpoint specifications with request/response formats
            - Authentication and authorization for each endpoint
            - Error handling and status codes

            #### Data Transfer Objects (DTOs)
            - Request and response model specifications
            - Validation rules and constraints
            - Serialization/deserialization requirements

            ### 1.3 Infrastructure Setup
            #### Development Environment
            - Local development setup requirements
            - Docker containerization specifications
            - Development tools and IDE configurations

            #### CI/CD Pipeline
            - Build pipeline configuration
            - Testing automation setup
            - Deployment pipeline specifications

            ## Phase 2: Core Feature Implementation

            ### 2.1 Frontend Components
            #### Component Architecture
            - React/Vue/Angular component hierarchy
            - State management implementation
            - Component interaction patterns

            #### UI/UX Implementation
            - Detailed wireframes and mockups
            - Responsive design specifications
            - Accessibility implementation guidelines

            ### 2.2 Backend Services
            #### Business Logic Layer
            - Service class specifications
            - Business rule implementations
            - Data validation and processing logic

            #### Integration Layer
            - Third-party API integration specifications
            - Message queue implementations
            - Event handling and notifications

            ### 2.3 Testing Strategy
            #### Unit Testing
            - Test coverage requirements (minimum 80%)
            - Mock and stub implementations
            - Test data management

            #### Integration Testing
            - API endpoint testing specifications
            - Database integration test scenarios
            - Third-party service integration tests

            ## Phase 3: Advanced Features & Optimization

            ### 3.1 Performance Optimization
            #### Caching Strategy
            - Redis/Memcached implementation
            - Cache invalidation strategies
            - Performance monitoring setup

            #### Database Optimization
            - Query optimization techniques
            - Index strategies
            - Connection pooling configuration

            ### 3.2 Security Implementation
            #### Authentication System
            - JWT token implementation
            - OAuth2 integration specifications
            - Session management requirements

            #### Authorization Framework
            - Role-based access control (RBAC)
            - Permission management system
            - Security audit logging

            ### 3.3 Monitoring and Logging
            #### Application Monitoring
            - Health check endpoints
            - Performance metrics collection
            - Error tracking and alerting

            #### Logging Framework
            - Structured logging implementation
            - Log aggregation and analysis
            - Audit trail requirements

            ## Implementation Guidelines

            ### Code Standards
            - Coding style guides and linting rules
            - Code review requirements
            - Documentation standards

            ### Development Workflow
            - Git branching strategy
            - Pull request process
            - Code deployment procedures

            ### Quality Assurance
            - Testing protocols and standards
            - Bug tracking and resolution process
            - Performance benchmarking requirements

            ## Risk Mitigation Strategies
            - Technical risk assessments with mitigation plans
            - Contingency planning for critical dependencies
            - Resource allocation and timeline buffers

            ---
            *This detailed design document provides comprehensive specifications for implementation teams.*

            ---

            ## Development Tasks Summary

            The following tasks will be created in Jira based on this detailed design:

            ### Epic: {hl_design[:100]}...

            #### Phase 1 Tasks:
            1. Database schema design and implementation
            2. API framework setup and basic endpoints
            3. Infrastructure and CI/CD pipeline setup
            4. Development environment configuration

            #### Phase 2 Tasks:
            5. Frontend component development
            6. Backend service implementation
            7. API integration and testing
            8. UI/UX implementation and testing

            #### Phase 3 Tasks:
            9. Performance optimization implementation
            10. Security framework integration
            11. Monitoring and logging setup
            12. Final testing and deployment preparation

            Each task will include detailed acceptance criteria, time estimates, and dependencies.
            """