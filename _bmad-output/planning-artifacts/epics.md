---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories', 'step-04-final-validation']
inputDocuments:
  - '/Users/pbos/Documents/testproject/_bmad-output/planning-artifacts/prd.md'
  - '/Users/pbos/Documents/testproject/_bmad-output/planning-artifacts/architecture.md'
---

# testproject - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for testproject, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

**Call Routing & IVR**
- FR1: System can receive inbound calls from Zendesk Talk dialing platform
- FR2: System can route received calls to Dialfire dialing platform
- FR3: System can query Braze to retrieve lead owner field value during inbound call processing
- FR4: System can query Braze to retrieve lead score tier field value during inbound call processing
- FR5: System can apply routing rule that routes calls to specific dialer based on lead owner value
- FR6: System can apply routing rule that routes calls to specific dialer based on lead score tier value
- FR7: System can present DTMF IVR menu to caller allowing them to select dialer destination
- FR8: System can route call based on DTMF menu selection when Braze data unavailable
- FR9: System can retrieve real-time capacity information from dialing platforms for load balancing
- FR10: System can apply load balancing rule that routes calls to dialer with available agent capacity

**Braze Integration**
- FR11: System can authenticate with Braze API
- FR12: System can retrieve customer record from Braze using caller phone number
- FR13: System can retrieve lead score field from Braze customer record
- FR14: System can cache customer data locally to support fast lookups during call routing
- FR15: System can write call outcome data to Braze customer record after call completion

**Dialing Platform Integration**
- FR16: System can authenticate with Dialfire API
- FR17: System can authenticate with Zendesk Talk API
- FR18: System can place outbound call instruction to dialing platform
- FR19: System can receive call status updates from dialing platform
- FR20: System can query agent availability status from dialer platform
- FR21: System can retrieve capacity information from dialer platform
- FR22: System can detect connectivity failure with dialer platform
- FR23: System can attempt retry when dialer platform API request fails

**Monitoring & Dashboard**
- FR26: System can display real-time count of active calls being processed
- FR27: System can display count of calls routed to each dialer platform
- FR28: System can display count of successful call routing completions
- FR29: System can display count of failed call routing attempts
- FR30: System can display integration health status for each connected platform
- FR31: System can display CRM API response time metrics
- FR32: System can display dialer API response time metrics
- FR33: System can display call routing success rate percentage
- FR34: Admin user can view call routing distribution over time period
- FR35: Sales leadership user can view performance metrics dashboard
- FR36: Admin user can access detailed call trace for individual failed routing attempts

**Alerting & Notifications**
- FR37: System can send email notification when routing failure rate exceeds threshold
- FR38: System can send email notification when integration fails to connect
- FR39: Admin user can configure email addresses for alert notifications
- FR40: Admin user can configure alert threshold values for routing failures

**Configuration & Rules**
- FR41: Admin user can configure which CRM field determines routing destination
- FR42: Admin user can configure lead owner to dialer mapping rules
- FR43: Admin user can configure lead score tier to dialer mapping rules
- FR44: Admin user can configure time-based routing rules
- FR45: Admin user can configure load balancing rules between dialers

**System Administration**
- FR46: System can store dialing platform API credentials securely
- FR47: System can store CRM API credentials securely
- FR48: Admin user can add users with admin permissions
- FR49: Admin user can add users with read-only permissions
- FR50: Admin user can remove user access
- FR51: Read-only user can view dashboard but cannot modify configuration

**Audit & Logging**
- FR52: System can log complete routing decision chain for each call
- FR53: System can log API request to CRM during call routing
- FR54: System can log API response from CRM during call routing
- FR55: System can log API request to dialer during call routing
- FR56: System can log API response from dialer during call routing
- FR57: System can log user configuration changes
- FR58: System can retain audit logs for minimum 90 days
- FR59: Admin user can view audit log entries
- FR60: Admin user can search audit logs by time period
- FR61: Admin user can search audit logs by caller phone number

**Data Management**
- FR62: System can store lead data cached from CRM
- FR63: System can update cached lead data when CRM record changes
- FR64: System can encrypt data at rest for customer information
- FR65: System can encrypt data in transit for all API communications

### NonFunctional Requirements

**Performance**
- NFR-PERF-1: System must complete call setup and routing within 2 seconds from call receipt (includes CRM lookup + routing decision + dialer handoff)
- NFR-PERF-2: System must instrument and track call setup time for every call
- NFR-PERF-3: Alert trigger when call setup time exceeds 1.5 seconds on more than 5% of calls
- NFR-PERF-4: Dashboard pages must load within 5 seconds for standard views
- NFR-PERF-5: Real-time metrics display must update within 3 seconds of data change
- NFR-PERF-6: Historical report generation may take up to 10 seconds
- NFR-PERF-7: System must detect and display integration failures within 1 minute of occurrence
- NFR-PERF-8: API latency monitoring updates must be visible within 5 minutes of data collection
- NFR-PERF-9: Alerting systems must trigger within 1 minute of threshold breach

**Security**
- NFR-SEC-1: All data at rest must be encrypted using AES-256 or equivalent (Phase 2)
- NFR-SEC-2: All data in transit must be encrypted using TLS 1.2 or higher
- NFR-SEC-3: Encryption keys must be managed securely with key rotation capability
- NFR-SEC-4: Dialer API credentials must be stored securely (not plaintext)
- NFR-SEC-5: CRM API credentials must be stored securely (not plaintext)
- NFR-SEC-6: Credentials must be encrypted at rest with access controls limiting who can retrieve decrypted values
- NFR-SEC-7: System must log all routing rule changes with timestamp, user identity, and rule modification details
- NFR-SEC-8: System must log all user permission changes (adds, removes, modifications)
- NFR-SEC-9: System must log all configuration changes to integration credentials
- NFR-SEC-10: Audit logs must be immutable (cannot be modified after creation)
- NFR-SEC-11: Audit logs must be retained for minimum 90 days
- NFR-SEC-12: No additional PII beyond what exists in customer's CRM database
- NFR-SEC-13: System must not store customer's CRM data permanently except for lead data caching
- NFR-SEC-14: Cached lead data must include only fields required for routing (phone number, owner, score)
- NFR-SEC-15: Customer data isolation must be enforced (no data leakage between customers)
- NFR-SEC-16: System design must implement SOC 2 Type I controls from inception

**Integration**
- NFR-INT-1: System must achieve 99% success rate on CRM API calls
- NFR-INT-2: System must achieve 99% success rate on dialer API calls
- NFR-INT-3: System must monitor integration success rates per platform
- NFR-INT-4: Alert trigger when integration success rate falls below 95% over 5-minute window
- NFR-INT-5: System must detect integration failures within 5 minutes of occurrence
- NFR-INT-6: System must display integration health status on dashboard in near real-time
- NFR-INT-7: System must send email alerts when integration failures exceed 5% over 5-minute window

**Integration Failure Handling**
- NFR-FAIL-1: Braze lookup failure - Route to customer-configured default fallback dialer immediately (no retry)
- NFR-FAIL-2: Dialer handoff failure - Immediate retry once, then route to fallback dialer
- NFR-FAIL-3: Both dialers unavailable - Play TTS message, retry, then route to basic hold queue
- NFR-FAIL-4: Dialer capacity query failure - Route to customer-configured preferred dialer
- NFR-FAIL-5: Integration down completely - Declare after 3 consecutive failures within 1-minute window
- NFR-FAIL-6: CRM down routing - Route all calls to customer-configured default dialer
- NFR-FAIL-7: Single dialer down routing - Route 100% of calls to functioning dialer
- NFR-FAIL-8: Recovery detection - Declare recovered after 3 consecutive successful API calls
- NFR-FAIL-9: Partial CRM response - 1.5 second maximum response time cutoff

**Reliability**
- NFR-REL-1: Target uptime 99.5% (realistic for MVP with design partner customer)
- NFR-REL-2: Acceptable downtime 3.6 hours per month
- NFR-REL-3: Downtime must be scheduled during off-peak hours with customer notification
- NFR-REL-4: System must maintain routing failure rate below 1%
- NFR-REL-5: Zero tolerance for silent failures - every failure must be logged
- NFR-REL-6: Every failure must be visible in audit logs and dashboard
- NFR-REL-7: Failed calls must be traceable end-to-end (complete routing decision chain visible)
- NFR-REL-8: System must support graceful degradation when partial failures occur
- NFR-REL-9: Automatic recovery must occur without manual intervention where possible

### Additional Requirements

**From Architecture - Starter Template**
- ARCH-1: Backend must use tiangolo/full-stack-fastapi-template with Python 3.10+ and FastAPI framework
- ARCH-2: Frontend must use Vite + React with TypeScript (template: react-ts)
- ARCH-3: Twilio Programmable Voice as telephony middleware layer (webhook-based architecture)
- ARCH-4: Initialization commands:
  - Backend: `npx create-fastapi-app@latest ivr-backend --docker`
  - Frontend: `npm create vite@latest ivr-dashboard -- --template react-ts`

**From Architecture - Infrastructure**
- ARCH-5: Redis required for Braze customer data caching (<2s SLA requirement)
- ARCH-6: Cache key pattern: `braze:customer:{phone_number}` with TTL 1 hour
- ARCH-7: PostgreSQL database (latest stable LTS)
- ARCH-8: AWS ECS deployment with GitHub Actions CI/CD
- ARCH-9: Single Dev/Prod environment structure (MVP scope)
- ARCH-10: Fixed container scaling (2-4 containers for HA), auto-scaling deferred to Phase 2

**From Architecture - API & Security**
- ARCH-11: RESTful API architecture with structured error handling
- ARCH-12: API key authentication (X-API-Key header)
- ARCH-13: TLS 1.3 for all data in transit
- ARCH-14: CloudWatch Logs and Metrics for observability
- ARCH-15: Structured JSON logging with request_id correlation

**From Architecture - Frontend**
- ARCH-16: React Query for API state management
- ARCH-17: React Router v6 with routes: /, /logs, /settings, /dialers
- ARCH-18: Tailwind CSS recommended for rapid dashboard UI

**From Architecture - Patterns**
- ARCH-19: snake_case for Python/backend code, camelCase for TypeScript/frontend code
- ARCH-20: Consistent API response format: `{ data: ... }` or `{ error: { type, message, details, request_id }}`
- ARCH-21: Use BackgroundTasks for async logging (don't block webhook responses)
- ARCH-22: Never retry Braze API during call routing (caller waiting)
- ARCH-23: Retry dialer API once before routing to fallback

### FR Coverage Map

| FR | Epic | Description |
|----|------|-------------|
| FR1 | Epic 1 | Receive inbound calls from Zendesk Talk |
| FR2 | Epic 1 | Route calls to Dialfire |
| FR3 | Epic 2 | Query Braze for lead owner |
| FR4 | Epic 2 | Query Braze for lead score tier |
| FR5 | Epic 2 | Route based on lead owner value |
| FR6 | Epic 2 | Route based on lead score tier |
| FR7 | Epic 3 | Present DTMF IVR menu |
| FR8 | Epic 3 | Route based on DTMF selection (fallback) |
| FR9 | Epic 3 | Retrieve dialer capacity for load balancing |
| FR10 | Epic 3 | Apply load balancing rules |
| FR11 | Epic 2 | Authenticate with Braze API |
| FR12 | Epic 2 | Retrieve customer from Braze by phone |
| FR13 | Epic 2 | Retrieve lead score from Braze |
| FR14 | Epic 2 | Cache customer data locally |
| FR15 | Epic 8 | Write call outcome to Braze |
| FR16 | Epic 3 | Authenticate with Dialfire API |
| FR17 | Epic 3 | Authenticate with Zendesk Talk API |
| FR18 | Epic 1 | Place outbound call to dialer |
| FR19 | Epic 3 | Receive call status updates |
| FR20 | Epic 3 | Query agent availability |
| FR21 | Epic 3 | Retrieve dialer capacity |
| FR22 | Epic 3 | Detect dialer connectivity failure |
| FR23 | Epic 3 | Retry failed dialer API requests |
| FR26 | Epic 4 | Display active call count |
| FR27 | Epic 4 | Display calls per dialer |
| FR28 | Epic 4 | Display successful routing count |
| FR29 | Epic 4 | Display failed routing count |
| FR30 | Epic 4 | Display integration health status |
| FR31 | Epic 4 | Display CRM API response time |
| FR32 | Epic 4 | Display dialer API response time |
| FR33 | Epic 4 | Display routing success rate |
| FR34 | Epic 4 | View routing distribution over time |
| FR35 | Epic 4 | Sales leadership metrics dashboard |
| FR36 | Epic 4 | Access call trace for failed routes |
| FR37 | Epic 5 | Email alert on routing failure threshold |
| FR38 | Epic 5 | Email alert on integration failure |
| FR39 | Epic 5 | Configure alert email addresses |
| FR40 | Epic 5 | Configure alert thresholds |
| FR41 | Epic 6 | Configure CRM routing field |
| FR42 | Epic 6 | Configure lead owner mappings |
| FR43 | Epic 6 | Configure lead score tier mappings |
| FR44 | Epic 6 | Configure time-based routing |
| FR45 | Epic 6 | Configure load balancing rules |
| FR46 | Epic 7 | Store dialer credentials securely |
| FR47 | Epic 7 | Store CRM credentials securely |
| FR48 | Epic 7 | Add admin users |
| FR49 | Epic 7 | Add read-only users |
| FR50 | Epic 7 | Remove user access |
| FR51 | Epic 7 | Read-only dashboard access |
| FR52 | Epic 8 | Log complete routing decision chain |
| FR53 | Epic 8 | Log CRM API requests |
| FR54 | Epic 8 | Log CRM API responses |
| FR55 | Epic 8 | Log dialer API requests |
| FR56 | Epic 8 | Log dialer API responses |
| FR57 | Epic 8 | Log user configuration changes |
| FR58 | Epic 8 | Retain logs for 90 days |
| FR59 | Epic 8 | View audit log entries |
| FR60 | Epic 8 | Search logs by time period |
| FR61 | Epic 8 | Search logs by phone number |
| FR62 | Epic 2 | Store cached lead data |
| FR63 | Epic 8 | Update cached data on CRM change |
| FR64 | Epic 8 | Encrypt data at rest |
| FR65 | Epic 1 | Encrypt data in transit |

## Epic List

### Epic 1: Project Setup & Core Call Routing Infrastructure
System can receive inbound calls via Twilio and route them to a dialer platform, establishing the foundation using Architecture-specified starter templates (FastAPI backend + Vite React frontend).

**FRs covered:** FR1, FR2, FR18, FR65
**ARCH covered:** ARCH-1 through ARCH-15, ARCH-19-21

---

### Epic 2: Intelligent Data-Driven Routing
Calls route intelligently based on customer data from Braze (lead score, lead owner), with Redis caching to meet the <2s call setup SLA.

**FRs covered:** FR3, FR4, FR5, FR6, FR11, FR12, FR13, FR14, FR62
**ARCH covered:** ARCH-5, ARCH-6, ARCH-22

---

### Epic 3: Dialer Reliability & Failover
Calls always route successfully even when integration issues occur through automatic retry, fallback routing to secondary dialer, load balancing, and DTMF menu backup when data is unavailable.

**FRs covered:** FR7, FR8, FR9, FR10, FR16, FR17, FR19, FR20, FR21, FR22, FR23
**ARCH covered:** ARCH-23
**NFRs addressed:** NFR-FAIL-1 through NFR-FAIL-9

---

### Epic 4: Operations Monitoring Dashboard
Jordan (Sales Ops) and Maya (VP Sales) can monitor call routing in real-time, view routing distribution, track success/failure metrics, and see integration health status at a glance.

**FRs covered:** FR26, FR27, FR28, FR29, FR30, FR31, FR32, FR33, FR34, FR35, FR36
**ARCH covered:** ARCH-16, ARCH-17, ARCH-18

---

### Epic 5: Alerting & Proactive Notifications
Jordan receives email alerts when routing failures exceed thresholds or integrations fail, enabling proactive response before users complain.

**FRs covered:** FR37, FR38, FR39, FR40

---

### Epic 6: Routing Rule Configuration
Jordan can configure routing rules through the admin interface without developer assistance, including lead owner mappings, score tier rules, time-based routing, and load balancing.

**FRs covered:** FR41, FR42, FR43, FR44, FR45

---

### Epic 7: User Management & Access Control
Maya can view dashboards with read-only access while Jordan has full admin control. Integration credentials stored securely with proper access controls.

**FRs covered:** FR46, FR47, FR48, FR49, FR50, FR51
**NFRs addressed:** NFR-SEC-4 through NFR-SEC-6

---

### Epic 8: Audit Trail & Compliance
Complete audit trail for every call enables debugging, compliance reporting, and operational analysis with 90-day retention and searchable logs.

**FRs covered:** FR15, FR52, FR53, FR54, FR55, FR56, FR57, FR58, FR59, FR60, FR61, FR63, FR64

---

## Epic 1: Project Setup & Core Call Routing Infrastructure

System can receive inbound calls via Twilio and route them to a dialer platform, establishing the foundation using Architecture-specified starter templates (FastAPI backend + Vite React frontend).

### Story 1.1: Initialize Backend Project with FastAPI

As a **developer**,
I want to initialize the backend project using the FastAPI starter template with Docker support,
So that I have a properly structured foundation for building the IVR routing system.

**Acceptance Criteria:**

**Given** no existing backend project
**When** I run the initialization command `npx create-fastapi-app@latest ivr-backend --docker`
**Then** a new FastAPI project is created with the following structure:
- `/app/api/` directory for API routes
- `/app/core/` directory for configuration and utilities
- `/app/models/` directory for SQLAlchemy models
- `/app/services/` directory for business logic
- `/app/repositories/` directory for database access
- `/app/schemas/` directory for Pydantic schemas
**And** Docker configuration files are present (Dockerfile, docker-compose.yml)
**And** the project uses Python 3.10+ with async support
**And** environment configuration uses Pydantic Settings pattern in `/app/core/config.py`
**And** `.env.example` file documents all required environment variables:
- `DATABASE_URL` for PostgreSQL connection
- `REDIS_URL` for Redis connection
- `API_KEY` for dashboard authentication
**And** pre-commit hooks are configured with Ruff for linting
**And** pytest is configured for testing with async support
**And** the application starts successfully with `docker-compose up`

**References:** ARCH-1, ARCH-4, ARCH-7, ARCH-11, ARCH-14, ARCH-15, ARCH-19

---

### Story 1.2: Initialize Frontend Project with Vite React

As a **developer**,
I want to initialize the frontend dashboard project using Vite with React and TypeScript,
So that I have a modern, fast development environment for building the monitoring dashboard.

**Acceptance Criteria:**

**Given** no existing frontend project
**When** I run the initialization command `npm create vite@latest ivr-dashboard -- --template react-ts`
**Then** a new React TypeScript project is created with the following structure:
- `/src/pages/` directory for page components
- `/src/components/` directory for reusable UI components
- `/src/hooks/` directory for custom React hooks
- `/src/services/` directory for API client
- `/src/utils/` directory for helper functions
- `/src/types/` directory for TypeScript type definitions
**And** Tailwind CSS is installed and configured
**And** React Query (@tanstack/react-query) is installed for API state management
**And** React Router v6 is installed with routes configured:
- `/` - Dashboard page
- `/logs` - Audit log viewer page
- `/settings` - Settings page
- `/dialers` - Dialer status page
**And** ESLint and Prettier are configured for code quality
**And** `.env.example` file documents required environment variables:
- `VITE_API_BASE_URL` for backend API URL
- `VITE_API_KEY` for authentication
**And** the application starts successfully with `npm run dev`
**And** all component and hook files follow camelCase naming convention

**References:** ARCH-2, ARCH-4, ARCH-16, ARCH-17, ARCH-18, ARCH-19

---

### Story 1.3: Implement Twilio Webhook for Inbound Calls

As a **system**,
I want to receive inbound call webhooks from Twilio,
So that I can process incoming calls and make routing decisions.

**Acceptance Criteria:**

**Given** the backend application is running
**When** Twilio sends a POST request to `/webhooks/twilio` with call data including:
- `From` (caller phone number)
- `To` (Twilio phone number)
- `CallSid` (unique call identifier)
**Then** the endpoint returns a valid TwiML XML response within 2 seconds
**And** the response content-type is `application/xml`
**And** a new call record is created in the `calls` table with:
- `call_sid` from Twilio
- `caller_number` from the `From` field
- `status` set to 'received'
- `created_at` timestamp
**And** the call is logged with structured JSON including `request_id`
**And** the endpoint does not require API key authentication (webhook endpoint)

**Given** Twilio sends a malformed request
**When** the webhook endpoint receives the request
**Then** a 400 error response is returned
**And** the error is logged with details for debugging

**Given** an unexpected server error occurs
**When** processing the webhook
**Then** a 500 error response is returned with consistent error format:
```json
{
  "error": {
    "type": "InternalServerError",
    "message": "An unexpected error occurred",
    "request_id": "<uuid>"
  }
}
```
**And** the error is logged with full stack trace

**References:** FR1, ARCH-11, ARCH-15, ARCH-20, ARCH-21

---

### Story 1.4: Implement Basic Call Routing to Dialer

As a **system**,
I want to route incoming calls to a configured dialer,
So that callers are connected to the appropriate sales agent.

**Acceptance Criteria:**

**Given** a valid inbound call webhook is received
**When** the routing decision is made
**Then** a TwiML response is generated with a `<Dial>` verb containing the Dialfire phone number
**And** the TwiML includes proper caller ID configuration
**And** the call record is updated with:
- `routed_dialer` set to 'dialfire'
- `status` set to 'routed'
- `routed_at` timestamp
**And** the routing decision is logged asynchronously using BackgroundTasks (not blocking the webhook response)
**And** all API communication uses TLS 1.3 encryption

**Given** the dialer phone number is configured in environment variables
**When** generating the TwiML response
**Then** the `<Dial>` verb uses the configured `DIALFIRE_PHONE_NUMBER` value
**And** the TwiML is generated using the `twilio-py` SDK

**Given** a call is successfully routed
**When** viewing the call record
**Then** the complete routing decision chain is visible:
- Call received timestamp
- Routing decision timestamp
- Target dialer
- Response time in milliseconds

**References:** FR2, FR18, FR65, ARCH-3, ARCH-13, ARCH-21

---

### Story 1.5: Create Core Database Schema

As a **developer**,
I want to create the core database tables for calls and dialers,
So that call routing data can be persisted and queried.

**Acceptance Criteria:**

**Given** PostgreSQL database is running
**When** Alembic migrations are executed
**Then** a `calls` table is created with columns:
- `id` (primary key, auto-increment)
- `call_sid` (string, unique, not null) - Twilio call identifier
- `caller_number` (string, not null) - E.164 format phone number
- `routed_dialer` (string, nullable) - target dialer name
- `status` (string, not null) - call status enum
- `routing_decision_ms` (integer, nullable) - routing latency
- `created_at` (timestamp with timezone, not null)
- `routed_at` (timestamp with timezone, nullable)
- `updated_at` (timestamp with timezone, not null)
**And** a `dialers` table is created with columns:
- `id` (primary key, auto-increment)
- `name` (string, unique, not null) - dialer identifier
- `phone_number` (string, not null) - dialer phone number
- `api_key` (string, nullable) - encrypted API key
- `active` (boolean, default true)
- `created_at` (timestamp with timezone, not null)
- `updated_at` (timestamp with timezone, not null)
**And** appropriate indexes are created:
- `idx_calls_call_sid` on `calls.call_sid`
- `idx_calls_caller_number` on `calls.caller_number`
- `idx_calls_created_at` on `calls.created_at`
**And** foreign key constraint exists: `calls.routed_dialer` references `dialers.name`
**And** all table and column names use snake_case convention
**And** migrations can be rolled back without data loss

**References:** ARCH-7, ARCH-19

---

### Story 1.6: Setup CI/CD Pipeline

As a **developer**,
I want to configure GitHub Actions for automated testing and deployment,
So that code changes are validated and deployed consistently.

**Acceptance Criteria:**

**Given** code is pushed to the repository
**When** a pull request is created or updated
**Then** the CI pipeline runs automatically with the following jobs:
- Backend tests (`pytest`)
- Backend linting (`ruff check`)
- Frontend tests (`npm test`)
- Frontend linting (`npm run lint`)
- TypeScript type checking (`tsc --noEmit`)
**And** the pipeline fails if any job fails
**And** test results are visible in the PR

**Given** code is merged to the `main` branch
**When** the merge is complete
**Then** the CD pipeline builds Docker images for backend and frontend
**And** images are tagged with the git commit SHA
**And** images are pushed to Amazon ECR
**And** the ECS task definition is updated with new image tags
**And** deployment to the dev environment happens automatically

**Given** deployment to production is needed
**When** the deployment workflow is triggered
**Then** manual approval is required before proceeding
**And** the production ECS service is updated with the new task definition
**And** deployment status is reported back to GitHub

**Given** the pipeline configuration files
**When** reviewing the repository
**Then** the following workflow files exist:
- `.github/workflows/ci.yml` - test and lint on PR
- `.github/workflows/build-backend.yml` - build backend image
- `.github/workflows/build-frontend.yml` - build frontend image
- `.github/workflows/deploy-prod.yml` - production deployment with approval

**References:** ARCH-8, ARCH-9, ARCH-10

---

**Epic 1 Summary:** 6 stories covering project initialization, core call routing, database schema, and CI/CD pipeline.

## Epic 2: Intelligent Data-Driven Routing

Calls route intelligently based on customer data from Braze (lead score, lead owner), with Redis caching to meet the <2s call setup SLA.

### Story 2.1: Implement Redis Caching Service

As a **developer**,
I want to implement a Redis caching service,
So that customer data can be cached for fast lookups during call routing.

**Acceptance Criteria:**

**Given** Redis is running and accessible
**When** the application starts
**Then** a Redis connection is established using the `REDIS_URL` environment variable
**And** connection failures are logged and the application continues (graceful degradation)

**Given** a cache key and value
**When** calling `redis_service.set(key, value, ttl)`
**Then** the value is stored in Redis with the specified TTL in seconds
**And** the key follows the pattern `braze:customer:{phone_number}`

**Given** a cache key exists in Redis
**When** calling `redis_service.get(key)`
**Then** the cached value is returned as a Python dictionary
**And** cache hits are logged at DEBUG level

**Given** a cache key does not exist in Redis
**When** calling `redis_service.get(key)`
**Then** `None` is returned
**And** cache misses are logged at DEBUG level

**Given** Redis is unavailable
**When** attempting cache operations
**Then** the operation fails gracefully without raising exceptions
**And** the failure is logged at WARNING level
**And** the calling code can continue without cached data

**References:** ARCH-5, ARCH-6

---

### Story 2.2: Implement Braze API Integration

As a **system**,
I want to retrieve customer data from Braze API,
So that I can make intelligent routing decisions based on lead information.

**Acceptance Criteria:**

**Given** valid Braze API credentials in environment variables (`BRAZE_API_KEY`, `BRAZE_API_URL`)
**When** the Braze service is initialized
**Then** the service authenticates successfully with Braze API
**And** authentication failures are logged at ERROR level

**Given** a caller phone number in E.164 format
**When** calling `braze_service.get_customer_record(phone_number)`
**Then** a GET request is made to Braze API to retrieve the customer by phone number
**And** the request includes the API key in the authorization header
**And** the request has a timeout of 1.5 seconds (to fit within <2s routing budget)

**Given** Braze returns a valid customer record
**When** processing the response
**Then** the following fields are extracted:
- `phone_number` - the customer's phone number
- `lead_owner` - the assigned lead owner/sales rep
- `lead_score` - the customer's lead score tier (0-100)
**And** the response is logged at INFO level with timing metrics

**Given** Braze API request times out (>1.5 seconds)
**When** the timeout occurs
**Then** the request is aborted immediately (no retry per ARCH-22)
**And** `None` is returned to allow fallback routing
**And** the timeout is logged at WARNING level with duration

**Given** Braze API returns an error (4xx, 5xx)
**When** processing the error response
**Then** `None` is returned to allow fallback routing
**And** the error is logged at ERROR level with response details
**And** no retry is attempted (caller is waiting)

**Given** the customer is not found in Braze
**When** a 404 response is received
**Then** `None` is returned
**And** the "customer not found" event is logged at INFO level

**References:** FR11, FR12, FR13, ARCH-22

---

### Story 2.3: Implement Customer Data Caching

As a **system**,
I want to cache Braze customer data in Redis,
So that subsequent lookups are fast and meet the <2s SLA.

**Acceptance Criteria:**

**Given** a call routing request for a phone number
**When** customer data is needed
**Then** Redis cache is checked first using key `braze:customer:{phone_number}`
**And** if cache hit, Braze API is NOT called
**And** cache lookup time is logged

**Given** customer data is not in cache (cache miss)
**When** Braze API returns valid customer data
**Then** the data is cached in Redis with TTL of 1 hour (3600 seconds)
**And** only routing-relevant fields are cached:
- `phone_number`
- `lead_owner`
- `lead_score`
**And** the cache write is logged at DEBUG level

**Given** Braze API returns no data or an error
**When** processing the response
**Then** nothing is cached (don't cache failures)
**And** subsequent requests will try Braze API again

**Given** cached customer data exists
**When** checking the cache entry
**Then** the TTL is set to expire after 1 hour
**And** expired entries are automatically removed by Redis

**Given** Redis is unavailable
**When** attempting to cache customer data
**Then** the routing continues without caching
**And** the failure is logged but does not block the call

**References:** FR14, FR62, ARCH-5, ARCH-6

---

### Story 2.4: Implement Lead Score Based Routing

As a **Sales Operations Manager (Jordan)**,
I want calls to be routed based on lead score tier,
So that high-value leads reach the appropriate sales team.

**Acceptance Criteria:**

**Given** customer data with a lead score value
**When** making a routing decision
**Then** the lead score is used to determine the target dialer:
- Score 80-100 (high): Route to configured "high_score_dialer"
- Score 50-79 (medium): Route to configured "medium_score_dialer"
- Score 0-49 (low): Route to configured "low_score_dialer"
**And** the routing rule applied is logged with the score and decision

**Given** lead score routing rules are configured
**When** the routing service processes a call
**Then** the rules are read from the `routing_rules` table or configuration
**And** score thresholds are configurable (not hardcoded)

**Given** a customer has no lead score (null or missing)
**When** making a routing decision
**Then** the call is routed to the configured default fallback dialer
**And** the "missing lead score" condition is logged at INFO level

**Given** lead score routing is successful
**When** the TwiML response is generated
**Then** the response includes `<Dial>` to the determined dialer phone number
**And** the call record is updated with:
- `routing_rule` = 'lead_score'
- `lead_score` = the customer's score
- `routed_dialer` = the selected dialer name

**References:** FR4, FR6

---

### Story 2.5: Implement Lead Owner Based Routing

As a **Sales Operations Manager (Jordan)**,
I want calls to be routed based on lead owner assignment,
So that returning customers reach their assigned sales representative.

**Acceptance Criteria:**

**Given** customer data with a lead owner value
**When** making a routing decision
**Then** the lead owner is mapped to a specific dialer using the `lead_owner_mappings` configuration
**And** the routing decision is logged with owner and target dialer

**Given** lead owner mappings are configured
**When** the routing service processes a call
**Then** the mappings are read from configuration:
```
{
  "owner_a": "dialfire",
  "owner_b": "zendesk_talk",
  "default": "dialfire"
}
```
**And** mappings support multiple owners per dialer

**Given** a customer has a lead owner that is not in the mappings
**When** making a routing decision
**Then** the call is routed to the "default" dialer from the mappings
**And** the "unknown owner" condition is logged at INFO level

**Given** a customer has no lead owner (null or missing)
**When** lead owner routing is attempted
**Then** the routing falls back to lead score based routing (Story 2.4)
**And** if lead score is also missing, route to default fallback dialer
**And** the fallback chain is logged

**Given** both lead owner and lead score are available
**When** determining routing priority
**Then** lead owner takes precedence over lead score
**And** the priority logic is:
1. If lead owner has value → use lead owner routing
2. Else if lead score has value → use lead score routing
3. Else → use default fallback dialer

**Given** lead owner routing is successful
**When** the call record is updated
**Then** it includes:
- `routing_rule` = 'lead_owner'
- `lead_owner` = the customer's owner
- `routed_dialer` = the selected dialer name

**References:** FR3, FR5

---

**Epic 2 Summary:** 5 stories covering Redis caching, Braze integration, customer data caching, and intelligent routing based on lead score and lead owner.

## Epic 3: Dialer Reliability & Failover

Calls always route successfully even when integration issues occur through automatic retry, fallback routing to secondary dialer, load balancing, and DTMF menu backup when data is unavailable.

### Story 3.1: Implement Dialfire API Integration

As a **system**,
I want to integrate with the Dialfire API,
So that I can route calls to Dialfire and monitor its availability.

**Acceptance Criteria:**

**Given** valid Dialfire API credentials in environment variables (`DIALFIRE_API_KEY`, `DIALFIRE_API_URL`)
**When** the Dialfire service is initialized
**Then** the service authenticates successfully with Dialfire API
**And** authentication failures are logged at ERROR level

**Given** a need to check Dialfire availability
**When** calling `dialfire_service.get_agent_availability()`
**Then** a request is made to Dialfire's availability endpoint
**And** the response includes:
- Number of available agents
- Number of busy agents
- Queue depth
**And** the request has a timeout of 2 seconds

**Given** a need to check Dialfire capacity
**When** calling `dialfire_service.get_capacity()`
**Then** the service returns:
- `available_capacity` (integer) - agents ready to take calls
- `total_capacity` (integer) - total agent seats
- `utilization_percent` (float) - current utilization
**And** the capacity data is logged at DEBUG level

**Given** Dialfire API is unreachable
**When** a connection attempt fails
**Then** a `DialerConnectionError` is raised
**And** the failure is logged at ERROR level with:
- Error type (timeout, connection refused, etc.)
- Timestamp
- Request details

**Given** Dialfire API returns an error response
**When** processing the response
**Then** the error is categorized:
- 4xx errors: Client error, log and don't retry
- 5xx errors: Server error, eligible for retry
**And** the error details are logged

**References:** FR16, FR20, FR21, FR22

---

### Story 3.2: Implement Zendesk Talk API Integration

As a **system**,
I want to integrate with the Zendesk Talk API,
So that I can route calls to Zendesk Talk as a secondary dialer and monitor its availability.

**Acceptance Criteria:**

**Given** valid Zendesk Talk API credentials in environment variables (`ZENDESK_TALK_API_KEY`, `ZENDESK_TALK_API_URL`)
**When** the Zendesk Talk service is initialized
**Then** the service authenticates successfully with Zendesk Talk API
**And** authentication failures are logged at ERROR level

**Given** a need to check Zendesk Talk availability
**When** calling `zendesk_talk_service.get_agent_availability()`
**Then** a request is made to Zendesk Talk's availability endpoint
**And** the response includes agent availability status
**And** the request has a timeout of 2 seconds

**Given** a need to check Zendesk Talk capacity
**When** calling `zendesk_talk_service.get_capacity()`
**Then** the service returns:
- `available_capacity` (integer)
- `total_capacity` (integer)
- `utilization_percent` (float)
**And** the capacity data is logged at DEBUG level

**Given** Zendesk Talk API is unreachable
**When** a connection attempt fails
**Then** a `DialerConnectionError` is raised
**And** the failure is logged at ERROR level with error details

**Given** both Dialfire and Zendesk Talk services exist
**When** accessing dialer services
**Then** they implement the same `DialerService` interface:
- `get_agent_availability()`
- `get_capacity()`
- `check_health()`
**And** the routing service can use either interchangeably

**References:** FR17, FR20, FR21, FR22

---

### Story 3.3: Implement Dialer Retry and Fallback Logic

As a **system**,
I want to automatically retry failed dialer connections and fallback to secondary dialer,
So that calls are always routed successfully even when one dialer has issues.

**Acceptance Criteria:**

**Given** a routing decision selects the primary dialer (e.g., Dialfire)
**When** the dialer API call fails (timeout or error)
**Then** the system retries once immediately (no delay)
**And** the retry attempt is logged at WARNING level

**Given** the retry to the primary dialer succeeds
**When** generating the TwiML response
**Then** the call is routed to the primary dialer as normal
**And** the successful retry is logged at INFO level

**Given** the retry to the primary dialer also fails
**When** the second failure occurs
**Then** the system automatically routes to the fallback dialer (e.g., Zendesk Talk)
**And** the fallback decision is logged at WARNING level with:
- Primary dialer name
- Failure reason
- Fallback dialer name

**Given** the fallback dialer also fails
**When** both dialers are unavailable
**Then** the system executes the catastrophic fallback:
1. Play TTS message: "Please hold while we connect you"
2. Wait 2 seconds
3. Retry primary dialer one more time
4. If still failed, play: "We're experiencing technical difficulties. Press 1 to leave a callback number or hold for the next available agent."
**And** an immediate email alert is sent to configured admin addresses
**And** the double-failure event is logged at CRITICAL level

**Given** retry and fallback configuration
**When** reviewing the system configuration
**Then** the following are configurable:
- `PRIMARY_DIALER` - default primary dialer name
- `FALLBACK_DIALER` - fallback dialer name
- `MAX_RETRY_ATTEMPTS` - number of retries (default: 1)

**References:** FR23, NFR-FAIL-2, NFR-FAIL-3, ARCH-23

---

### Story 3.4: Implement Load Balancing Between Dialers

As a **Sales Operations Manager (Jordan)**,
I want calls to be load balanced between dialers based on capacity,
So that calls are routed to agents who are available to take them.

**Acceptance Criteria:**

**Given** load balancing is enabled in routing configuration
**When** making a routing decision
**Then** the system queries capacity from both dialers before routing
**And** capacity queries happen in parallel (async)
**And** total query time is under 500ms

**Given** both dialers have available capacity
**When** applying load balancing rules
**Then** calls are routed to the dialer with:
- Higher available agent count, OR
- Lower utilization percentage (configurable strategy)
**And** the load balancing decision is logged with both dialers' capacity

**Given** one dialer has no available capacity
**When** making a routing decision
**Then** the call is routed to the dialer with available capacity
**And** the "no capacity" condition is logged at INFO level

**Given** both dialers have no available capacity
**When** making a routing decision
**Then** the call is routed to the preferred dialer (from configuration)
**And** a WARNING is logged indicating potential queue delay

**Given** capacity query fails for one dialer
**When** the query times out or returns an error
**Then** the call is routed to the functioning dialer
**And** the capacity query failure is logged at WARNING level
**And** no retry is attempted for capacity queries (not critical path)

**Given** load balancing is applied
**When** the call record is updated
**Then** it includes:
- `routing_rule` = 'load_balance'
- `dialfire_capacity` = capacity at decision time
- `zendesk_capacity` = capacity at decision time
- `routed_dialer` = selected dialer

**References:** FR9, FR10, NFR-FAIL-4

---

### Story 3.5: Implement DTMF IVR Fallback Menu

As a **caller**,
I want to select my routing destination via phone keypad,
So that I can reach the right team even when automatic routing data is unavailable.

**Acceptance Criteria:**

**Given** Braze customer data lookup fails or returns no data
**When** the routing decision cannot be made automatically
**Then** a DTMF IVR menu is presented to the caller via TwiML:
```xml
<Response>
  <Gather input="dtmf" numDigits="1" action="/webhooks/twilio/gather" method="POST">
    <Say>Press 1 for sales. Press 2 for support.</Say>
  </Gather>
  <Say>We didn't receive any input. Connecting you to our main line.</Say>
  <Dial>{DEFAULT_DIALER_NUMBER}</Dial>
</Response>
```
**And** the IVR presentation is logged at INFO level

**Given** the caller presses a DTMF digit
**When** Twilio sends the gather result to `/webhooks/twilio/gather`
**Then** the digit is processed:
- Press 1: Route to Dialfire (sales)
- Press 2: Route to Zendesk Talk (support)
**And** the DTMF selection is logged with the digit pressed

**Given** the caller does not press any digit (timeout)
**When** the gather timeout occurs
**Then** the call is routed to the default dialer
**And** the "no input" condition is logged at INFO level

**Given** the caller presses an invalid digit
**When** processing the DTMF input
**Then** the call is routed to the default dialer
**And** the "invalid input" is logged with the digit pressed

**Given** DTMF routing is used
**When** the call record is updated
**Then** it includes:
- `routing_rule` = 'dtmf_ivr'
- `dtmf_digit` = the digit pressed (or 'timeout'/'invalid')
- `routed_dialer` = the selected dialer

**References:** FR7, FR8, NFR-FAIL-1

---

### Story 3.6: Implement Call Status Tracking

As a **system**,
I want to receive and track call status updates,
So that the complete call lifecycle is captured for monitoring and reporting.

**Acceptance Criteria:**

**Given** a call is routed to a dialer
**When** Twilio sends status callback webhooks
**Then** the system receives updates at `/webhooks/twilio/status`
**And** the following statuses are tracked:
- `initiated` - call routing started
- `ringing` - dialer phone is ringing
- `in-progress` - call connected to agent
- `completed` - call ended normally
- `busy` - dialer line busy
- `no-answer` - dialer didn't answer
- `failed` - call routing failed

**Given** a status update is received
**When** processing the webhook
**Then** the `calls` table is updated with:
- `status` = new status value
- `status_updated_at` = current timestamp
- `call_duration` = duration in seconds (if completed)
**And** the status transition is logged at INFO level

**Given** a call reaches 'completed' status
**When** updating the call record
**Then** the final call record includes:
- Complete timeline (received → routed → connected → completed)
- Total duration in seconds
- Agent connection time (time from routing to in-progress)

**Given** a call reaches 'failed', 'busy', or 'no-answer' status
**When** updating the call record
**Then** the failure is logged at WARNING level
**And** the failure reason is captured for reporting
**And** failure counts are incremented for alerting thresholds

**Given** the status webhook endpoint
**When** Twilio sends a request
**Then** the endpoint validates the request is from Twilio (IP allowlist)
**And** returns 200 OK quickly (status processing is async via BackgroundTasks)

**References:** FR19

---

**Epic 3 Summary:** 6 stories covering dialer integrations, retry/fallback logic, load balancing, DTMF IVR, and call status tracking.

## Epic 4: Operations Monitoring Dashboard

Jordan (Sales Ops) and Maya (VP Sales) can monitor call routing in real-time, view routing distribution, track success/failure metrics, and see integration health status at a glance.

### Story 4.1: Implement Call Metrics API Endpoints

As a **developer**,
I want to create API endpoints for call metrics,
So that the dashboard can display real-time call statistics.

**Acceptance Criteria:**

**Given** the backend API is running
**When** a GET request is made to `/api/v1/calls/active`
**Then** the response includes:
```json
{
  "data": {
    "active_count": 5,
    "calls": [
      {
        "call_sid": "CA123...",
        "caller_number": "+15551234567",
        "routed_dialer": "dialfire",
        "status": "in-progress",
        "duration_seconds": 45,
        "started_at": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```
**And** the response is returned within 3 seconds
**And** the endpoint requires X-API-Key authentication

**Given** the backend API is running
**When** a GET request is made to `/api/v1/calls/metrics` with optional query params:
- `start_date` (ISO 8601)
- `end_date` (ISO 8601)
- `dialer` (filter by dialer name)
**Then** the response includes aggregated metrics:
```json
{
  "data": {
    "total_calls": 1500,
    "successful_routes": 1485,
    "failed_routes": 15,
    "success_rate": 99.0,
    "by_dialer": {
      "dialfire": { "count": 900, "success_rate": 99.2 },
      "zendesk_talk": { "count": 600, "success_rate": 98.5 }
    },
    "avg_routing_time_ms": 1250
  }
}
```
**And** the response is returned within 5 seconds

**Given** no date range is specified
**When** fetching metrics
**Then** the default range is the last 24 hours

**Given** an invalid date format is provided
**When** the request is processed
**Then** a 400 error is returned with validation details

**References:** FR26, FR27, FR28, FR29, FR33

---

### Story 4.2: Implement Integration Health API Endpoints

As a **developer**,
I want to create API endpoints for integration health status,
So that the dashboard can display the health of connected systems.

**Acceptance Criteria:**

**Given** the backend API is running
**When** a GET request is made to `/api/v1/dialers/status`
**Then** the response includes health status for all integrations:
```json
{
  "data": {
    "dialers": [
      {
        "name": "dialfire",
        "status": "healthy",
        "last_check": "2024-01-15T10:30:00Z",
        "response_time_ms": 150,
        "available_capacity": 10
      },
      {
        "name": "zendesk_talk",
        "status": "healthy",
        "last_check": "2024-01-15T10:30:00Z",
        "response_time_ms": 200,
        "available_capacity": 8
      }
    ],
    "crm": {
      "name": "braze",
      "status": "healthy",
      "last_check": "2024-01-15T10:30:00Z",
      "response_time_ms": 250,
      "cache_hit_rate": 85.5
    }
  }
}
```
**And** the endpoint requires X-API-Key authentication

**Given** an integration is unhealthy
**When** checking its status
**Then** the status field shows:
- `healthy` - responding normally (<1s response time)
- `degraded` - slow responses (1-2s response time)
- `unhealthy` - failing or timeout (>2s or errors)
**And** the `last_error` field contains the most recent error message

**Given** health checks are performed
**When** the system monitors integrations
**Then** health checks run every 30 seconds in the background
**And** results are cached to avoid blocking API responses
**And** the `health_status` table stores historical health data

**Given** API response times are tracked
**When** viewing health status
**Then** the following metrics are available:
- Current response time (last check)
- Average response time (last 5 minutes)
- p95 response time (last 5 minutes)

**References:** FR30, FR31, FR32

---

### Story 4.3: Build Dashboard Home Page

As a **Sales Operations Manager (Jordan)**,
I want to see key call metrics on the dashboard home page,
So that I can monitor system health at a glance.

**Acceptance Criteria:**

**Given** the user navigates to the dashboard (/)
**When** the page loads
**Then** the following metrics are displayed:
- Active calls count (large, prominent display)
- Total calls today
- Success rate percentage
- Average routing time
**And** the page loads within 5 seconds

**Given** the dashboard is displayed
**When** new data is available
**Then** metrics automatically refresh every 5 seconds using React Query polling
**And** no full page reload is required
**And** loading states are shown during data fetches

**Given** the user is viewing the dashboard
**When** metrics update
**Then** visual indicators show:
- Green: Success rate > 99%
- Yellow: Success rate 95-99%
- Red: Success rate < 95%
**And** the active calls count updates in real-time

**Given** an API error occurs
**When** fetching dashboard data
**Then** an error message is displayed using the ErrorAlert component
**And** the last successful data remains visible
**And** a retry button is available

**Given** the dashboard layout
**When** viewing on desktop
**Then** metrics are displayed in MetricCard components arranged in a grid
**And** the layout follows the simple flat structure (no atomic design complexity)

**References:** FR26, FR35, ARCH-16, ARCH-17, ARCH-18

---

### Story 4.4: Build Routing Distribution View

As a **VP of Sales (Maya)**,
I want to see call routing distribution over time,
So that I can understand how calls are being distributed across dialers.

**Acceptance Criteria:**

**Given** the user is on the dashboard
**When** viewing the routing distribution section
**Then** a breakdown is displayed showing:
- Calls to Dialfire (count and percentage)
- Calls to Zendesk Talk (count and percentage)
- Calls via DTMF IVR (count and percentage)
**And** the data is visualized in a clear format (table or simple chart)

**Given** the routing distribution view
**When** selecting a time period filter
**Then** the following options are available:
- Last hour
- Last 24 hours
- Last 7 days
- Custom date range
**And** the display updates to show data for the selected period

**Given** routing data is displayed
**When** viewing success/failure breakdown
**Then** each dialer shows:
- Total calls routed
- Successful connections
- Failed connections
- Success rate percentage
**And** failed routes are highlighted for attention

**Given** the admin user wants more detail
**When** clicking on a dialer's metrics
**Then** a detailed view shows:
- Calls over time (hourly buckets)
- Common failure reasons
- Average connection time

**Given** the data is loading
**When** the API request is in progress
**Then** a LoadingSpinner component is displayed
**And** the previous data remains visible (stale-while-revalidate pattern)

**References:** FR27, FR34

---

### Story 4.5: Build Integration Health Status Display

As a **Sales Operations Manager (Jordan)**,
I want to see the health status of all integrations,
So that I can quickly identify and respond to system issues.

**Acceptance Criteria:**

**Given** the user navigates to the Dialers page (/dialers)
**When** the page loads
**Then** a list of all integrations is displayed:
- Dialfire with health status
- Zendesk Talk with health status
- Braze (CRM) with health status
**And** each integration shows a StatusIndicator component (green/yellow/red)

**Given** an integration is healthy
**When** viewing its status
**Then** a green StatusIndicator is shown
**And** the current response time is displayed
**And** the available capacity is shown (for dialers)

**Given** an integration is degraded or unhealthy
**When** viewing its status
**Then** a yellow or red StatusIndicator is shown
**And** the last error message is displayed
**And** the time since last successful check is shown

**Given** the health status display
**When** viewing API response times
**Then** the following are shown for each integration:
- Current response time
- Average (last 5 min)
- Trend indicator (improving/stable/degrading)
**And** response times over 1 second are highlighted in yellow
**And** response times over 2 seconds are highlighted in red

**Given** cache statistics are available
**When** viewing Braze (CRM) status
**Then** the cache hit rate is displayed
**And** cache effectiveness is indicated:
- Green: >80% hit rate
- Yellow: 50-80% hit rate
- Red: <50% hit rate

**Given** the user wants to test connectivity
**When** clicking "Test Connection" button on a dialer
**Then** an API call is made to POST `/api/v1/dialers/{id}/test`
**And** the result (success/failure) is displayed
**And** the health status refreshes after the test

**References:** FR30, FR31, FR32

---

### Story 4.6: Build Call Trace View for Debugging

As a **Sales Operations Manager (Jordan)**,
I want to view detailed call trace for failed routes,
So that I can debug issues and understand what went wrong.

**Acceptance Criteria:**

**Given** the user navigates to the Logs page (/logs)
**When** viewing call records
**Then** a list of recent calls is displayed with:
- Call SID
- Caller number (masked: +1555***4567)
- Routed dialer
- Status (with color coding)
- Timestamp
**And** failed routes are highlighted in red
**And** the list supports pagination

**Given** a list of calls is displayed
**When** clicking on a specific call row
**Then** the detailed call trace is shown with the complete routing decision chain:
```
10:30:00.000 - Call received from +15551234567
10:30:00.050 - Cache lookup: braze:customer:+15551234567
10:30:00.051 - Cache HIT - customer data found
10:30:00.052 - Lead score: 85, Lead owner: "sales_team_a"
10:30:00.053 - Routing rule: lead_owner -> dialfire
10:30:00.100 - Dialer capacity check: dialfire=10, zendesk=8
10:30:00.150 - TwiML generated for dialfire
10:30:00.200 - Response sent to Twilio (150ms total)
10:30:02.500 - Status update: ringing
10:30:05.000 - Status update: in-progress
10:32:30.000 - Status update: completed (duration: 150s)
```
**And** timestamps show millisecond precision
**And** each step is clearly labeled

**Given** a call failed to route
**When** viewing its trace
**Then** the failure point is highlighted in red
**And** the error message is displayed
**And** any retry attempts are shown
**And** the fallback path (if taken) is documented

**Given** the user wants to find specific calls
**When** using the search/filter functionality
**Then** calls can be filtered by:
- Phone number (partial match)
- Date range
- Status (success/failed)
- Dialer
**And** search results update in real-time

**Given** API request/response logging is captured
**When** viewing a call trace
**Then** the trace includes:
- Braze API request timestamp and response time
- Dialer API request timestamp and response time
- Any errors with full error messages
**And** sensitive data (API keys) is NOT displayed

**References:** FR36

---

**Epic 4 Summary:** 6 stories covering metrics API, health API, dashboard home, routing distribution, health display, and call trace debugging.

## Epic 5: Alerting & Proactive Notifications

Jordan receives email alerts when routing failures exceed thresholds or integrations fail, enabling proactive response before users complain.

### Story 5.1: Implement Alert Service and Email Notifications

As a **developer**,
I want to create an alert service that sends email notifications,
So that administrators can be notified of system issues proactively.

**Acceptance Criteria:**

**Given** email configuration in environment variables:
- `SMTP_HOST` - SMTP server hostname
- `SMTP_PORT` - SMTP server port
- `SMTP_USERNAME` - SMTP authentication username
- `SMTP_PASSWORD` - SMTP authentication password
- `ALERT_FROM_EMAIL` - sender email address
**When** the alert service is initialized
**Then** the service connects to the SMTP server successfully
**And** connection failures are logged at ERROR level

**Given** an alert needs to be sent
**When** calling `alert_service.send_alert(alert_type, message, recipients)`
**Then** an email is sent with:
- Subject: "[IVR Alert] {alert_type}: {brief_summary}"
- Body: Detailed alert message with timestamp
- To: List of recipient email addresses
**And** the email is sent asynchronously (non-blocking)
**And** the send attempt is logged at INFO level

**Given** the email send fails
**When** an SMTP error occurs
**Then** the failure is logged at ERROR level with details
**And** the alert is stored in database for retry
**And** retry is attempted up to 3 times with exponential backoff

**Given** an alert is triggered
**When** the email is sent successfully
**Then** an alert record is created in the `alerts` table with:
- `alert_type` - type of alert
- `message` - alert details
- `recipients` - list of email addresses
- `sent_at` - timestamp
- `status` - 'sent' or 'failed'

**Given** the alerts table
**When** querying alert history
**Then** the API endpoint `/api/v1/alerts/history` returns recent alerts
**And** alerts can be filtered by type, date range, and status

**References:** FR37, FR38

---

### Story 5.2: Implement Routing Failure Rate Monitoring

As a **Sales Operations Manager (Jordan)**,
I want to be alerted when routing failures exceed a threshold,
So that I can respond to issues before they impact too many calls.

**Acceptance Criteria:**

**Given** calls are being processed
**When** the system monitors routing outcomes
**Then** a rolling 5-minute window tracks:
- Total calls attempted
- Successful routes
- Failed routes
- Failure rate percentage
**And** the window slides every 30 seconds

**Given** the routing failure rate exceeds the configured threshold (default: 5%)
**When** the threshold is breached
**Then** an email alert is sent to configured recipients with:
- Subject: "[IVR Alert] High Routing Failure Rate: X%"
- Body containing:
  - Current failure rate
  - Number of failed calls in window
  - Number of total calls in window
  - Time window (last 5 minutes)
  - Most common failure reasons
**And** the alert is logged at WARNING level

**Given** an alert has been sent for high failure rate
**When** the failure rate remains above threshold
**Then** no duplicate alerts are sent within 15 minutes (alert cooldown)
**And** a "still elevated" reminder is sent after 15 minutes if still above threshold

**Given** the failure rate drops below threshold
**When** recovery is detected
**Then** a recovery notification is sent:
- Subject: "[IVR Alert] Routing Failure Rate Recovered"
- Body: Current rate and recovery timestamp
**And** the alert cooldown is reset

**Given** failure rate monitoring configuration
**When** reviewing system settings
**Then** the following are configurable:
- `ROUTING_FAILURE_THRESHOLD_PERCENT` (default: 5)
- `ROUTING_ALERT_WINDOW_MINUTES` (default: 5)
- `ROUTING_ALERT_COOLDOWN_MINUTES` (default: 15)

**References:** FR37

---

### Story 5.3: Implement Integration Failure Alerting

As a **Sales Operations Manager (Jordan)**,
I want to be alerted when an integration fails to connect,
So that I can coordinate with IT or take manual action.

**Acceptance Criteria:**

**Given** integration health checks run every 30 seconds
**When** an integration (Dialfire, Zendesk Talk, or Braze) fails 3 consecutive checks
**Then** the integration is declared "down"
**And** an email alert is sent immediately with:
- Subject: "[IVR Alert] Integration Down: {integration_name}"
- Body containing:
  - Integration name
  - Last successful connection time
  - Error message from failed attempts
  - Impact assessment (e.g., "Calls cannot be routed to Dialfire")

**Given** a single integration is down
**When** describing the impact
**Then** the alert explains:
- Dialfire down: "Calls will failover to Zendesk Talk"
- Zendesk Talk down: "Calls will failover to Dialfire"
- Braze down: "Calls will route using DTMF IVR menu"

**Given** both dialers are down
**When** this critical condition occurs
**Then** a CRITICAL alert is sent immediately with:
- Subject: "[IVR CRITICAL] All Dialers Unavailable"
- Body: Urgent notification that call routing is severely impacted
**And** the alert bypasses normal cooldown
**And** SMS alert is sent if configured (optional)

**Given** an integration recovers
**When** 3 consecutive health checks succeed
**Then** the integration is declared "recovered"
**And** a recovery notification is sent:
- Subject: "[IVR Alert] Integration Recovered: {integration_name}"
- Body: Recovery timestamp and current health status

**Given** integration alerting configuration
**When** reviewing system settings
**Then** the following are configurable:
- `INTEGRATION_FAILURE_THRESHOLD` (default: 3 consecutive failures)
- `INTEGRATION_CHECK_INTERVAL_SECONDS` (default: 30)
- `INTEGRATION_ALERT_COOLDOWN_MINUTES` (default: 15)

**References:** FR38

---

### Story 5.4: Build Alert Configuration UI

As a **Sales Operations Manager (Jordan)**,
I want to configure alert recipients and thresholds through the UI,
So that I can customize alerting without developer assistance.

**Acceptance Criteria:**

**Given** the user navigates to Settings page (/settings)
**When** viewing the Alerts section
**Then** the following configuration options are displayed:
- Email recipients list (add/remove)
- Routing failure threshold percentage
- Integration failure threshold (consecutive failures)
- Alert cooldown period

**Given** the alert configuration form
**When** adding a new email recipient
**Then** the email address is validated for proper format
**And** duplicate emails are prevented
**And** the new recipient is saved to configuration
**And** a confirmation message is displayed

**Given** the alert configuration form
**When** removing an email recipient
**Then** a confirmation dialog is shown
**And** the recipient is removed from the list
**And** at least one recipient must remain (cannot remove all)

**Given** the threshold configuration
**When** adjusting the routing failure threshold
**Then** a slider or input allows values from 1% to 20%
**And** the current value is clearly displayed
**And** changes are saved when clicking "Save"
**And** the backend validates the value is within range

**Given** configuration changes are made
**When** saving the configuration
**Then** a POST request is made to `/api/v1/settings/alerts`
**And** the response confirms success or shows validation errors
**And** changes take effect immediately (no restart required)

**Given** the current alert configuration
**When** loading the Settings page
**Then** all current values are pre-populated in the form
**And** a "Reset to Defaults" button is available
**And** default values are documented next to each field

**Given** API endpoint for alert configuration
**When** a GET request is made to `/api/v1/settings/alerts`
**Then** the current configuration is returned:
```json
{
  "data": {
    "recipients": ["jordan@company.com", "ops@company.com"],
    "routing_failure_threshold_percent": 5,
    "integration_failure_threshold": 3,
    "alert_cooldown_minutes": 15
  }
}
```

**References:** FR39, FR40

---

**Epic 5 Summary:** 4 stories covering alert service, failure rate monitoring, integration alerting, and configuration UI.

## Epic 6: Routing Rule Configuration

Jordan can configure routing rules through the admin interface without developer assistance, including lead owner mappings, score tier rules, time-based routing, and load balancing.

### Story 6.1: Create Routing Rules Data Model and API

As a **developer**,
I want to create a data model and API for routing rules,
So that routing configuration can be stored and managed dynamically.

**Acceptance Criteria:**

**Given** the database schema needs to support routing rules
**When** migrations are run
**Then** a `routing_rules` table is created with:
- `id` (primary key, auto-increment)
- `rule_type` (enum: 'lead_owner', 'lead_score', 'time_based', 'load_balance')
- `name` (string, unique, not null) - human-readable rule name
- `priority` (integer, not null) - rule evaluation order
- `config` (JSONB) - rule-specific configuration
- `active` (boolean, default true)
- `created_at` (timestamp with timezone)
- `updated_at` (timestamp with timezone)
- `created_by` (string) - user who created the rule
**And** indexes are created on `rule_type` and `priority`

**Given** the API for routing rules
**When** a GET request is made to `/api/v1/routing-rules`
**Then** all active routing rules are returned ordered by priority:
```json
{
  "data": [
    {
      "id": 1,
      "rule_type": "lead_owner",
      "name": "Owner-based routing",
      "priority": 1,
      "config": { "mappings": { "team_a": "dialfire" } },
      "active": true
    }
  ]
}
```

**Given** creating a new routing rule
**When** a POST request is made to `/api/v1/routing-rules`
**Then** the rule is validated and saved
**And** the response includes the created rule with ID
**And** the creation is logged in the audit trail

**Given** updating a routing rule
**When** a PUT request is made to `/api/v1/routing-rules/{id}`
**Then** the rule is updated
**And** the update is logged in the audit trail with before/after values

**Given** deleting a routing rule
**When** a DELETE request is made to `/api/v1/routing-rules/{id}`
**Then** the rule is soft-deleted (active = false)
**And** the deletion is logged in the audit trail

**Given** the routing service needs current rules
**When** evaluating a routing decision
**Then** rules are loaded from database (with caching)
**And** rules are evaluated in priority order
**And** the first matching rule determines the routing

**References:** FR41

---

### Story 6.2: Implement Lead Owner Mapping Configuration

As a **Sales Operations Manager (Jordan)**,
I want to configure lead owner to dialer mappings,
So that calls from specific owners route to their designated dialers.

**Acceptance Criteria:**

**Given** the user navigates to Settings > Routing Rules
**When** selecting "Lead Owner Mapping" rule type
**Then** a configuration form is displayed showing:
- Current owner-to-dialer mappings
- Add new mapping button
- Default dialer for unmapped owners

**Given** the lead owner mapping form
**When** adding a new mapping
**Then** the user can:
- Enter or select a lead owner name/ID
- Select target dialer from dropdown (Dialfire, Zendesk Talk)
**And** the mapping is validated (no duplicate owners)
**And** the mapping is added to the list

**Given** existing mappings are displayed
**When** viewing the mappings list
**Then** each mapping shows:
- Lead owner name
- Target dialer
- Edit and Delete buttons
**And** mappings can be reordered by drag-and-drop

**Given** a mapping is edited
**When** saving the changes
**Then** the routing rule config is updated:
```json
{
  "mappings": {
    "sales_team_a": "dialfire",
    "sales_team_b": "zendesk_talk",
    "enterprise": "dialfire"
  },
  "default_dialer": "dialfire"
}
```
**And** changes take effect immediately for new calls

**Given** the default dialer configuration
**When** a call has an owner not in the mappings
**Then** the call routes to the configured default dialer
**And** the "unmapped owner" event is logged

**Given** lead owner mapping is saved
**When** the configuration change is persisted
**Then** an audit log entry is created with:
- User who made the change
- Timestamp
- Before and after configuration
- Rule type: 'lead_owner'

**References:** FR42

---

### Story 6.3: Implement Lead Score Tier Configuration

As a **Sales Operations Manager (Jordan)**,
I want to configure lead score tier routing rules,
So that high-value leads are routed to the appropriate sales team.

**Acceptance Criteria:**

**Given** the user navigates to Settings > Routing Rules
**When** selecting "Lead Score Tiers" rule type
**Then** a configuration form is displayed showing:
- List of score tiers with ranges and target dialers
- Add new tier button
- Default dialer for scores not matching any tier

**Given** the lead score tier form
**When** adding a new tier
**Then** the user can:
- Enter tier name (e.g., "High Value", "Medium", "Low")
- Enter minimum score (0-100)
- Enter maximum score (0-100)
- Select target dialer
**And** score ranges are validated (no overlaps)
**And** min must be less than or equal to max

**Given** score tier configuration
**When** saving the configuration
**Then** the routing rule config is updated:
```json
{
  "tiers": [
    { "name": "High Value", "min": 80, "max": 100, "dialer": "dialfire" },
    { "name": "Medium", "min": 50, "max": 79, "dialer": "dialfire" },
    { "name": "Low", "min": 0, "max": 49, "dialer": "zendesk_talk" }
  ],
  "default_dialer": "zendesk_talk"
}
```
**And** tiers are sorted by min score descending

**Given** overlapping score ranges are entered
**When** attempting to save
**Then** validation error is displayed: "Score ranges cannot overlap"
**And** the conflicting ranges are highlighted

**Given** a call has a lead score
**When** the routing service evaluates score tiers
**Then** the first tier where min <= score <= max is selected
**And** the call routes to that tier's dialer
**And** the tier name is logged with the routing decision

**Given** a call has no lead score
**When** score tier routing is evaluated
**Then** the call routes to the configured default dialer
**And** "no score available" is logged

**References:** FR43

---

### Story 6.4: Implement Time-Based Routing Rules

As a **Sales Operations Manager (Jordan)**,
I want to configure time-based routing rules,
So that calls are routed differently during business hours vs after hours.

**Acceptance Criteria:**

**Given** the user navigates to Settings > Routing Rules
**When** selecting "Time-Based Routing" rule type
**Then** a configuration form is displayed showing:
- Business hours schedule (start time, end time)
- Days of week selection
- Business hours dialer
- After hours dialer
- Timezone selection

**Given** the time-based routing form
**When** configuring business hours
**Then** the user can:
- Set start time (e.g., 9:00 AM)
- Set end time (e.g., 5:00 PM)
- Select active days (checkboxes for Mon-Sun)
- Select timezone from dropdown
**And** times are displayed in 12-hour or 24-hour format (user preference)

**Given** time-based routing configuration
**When** saving the configuration
**Then** the routing rule config is updated:
```json
{
  "timezone": "America/New_York",
  "schedules": [
    {
      "name": "Business Hours",
      "days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
      "start_time": "09:00",
      "end_time": "17:00",
      "dialer": "dialfire"
    }
  ],
  "default_dialer": "zendesk_talk"
}
```

**Given** a call comes in during business hours
**When** time-based routing is evaluated
**Then** the call routes to the business hours dialer
**And** the current time and matched schedule are logged

**Given** a call comes in outside business hours
**When** time-based routing is evaluated
**Then** the call routes to the after-hours/default dialer
**And** "after hours" routing is logged

**Given** multiple time schedules are configured
**When** evaluating routing
**Then** schedules are checked in order
**And** the first matching schedule is used
**And** holidays can be configured as exceptions (optional enhancement)

**Given** timezone configuration
**When** evaluating the current time
**Then** the server uses the configured timezone (not UTC)
**And** daylight saving time is handled automatically

**References:** FR44

---

### Story 6.5: Implement Load Balancing Configuration

As a **Sales Operations Manager (Jordan)**,
I want to configure load balancing between dialers,
So that calls are distributed based on agent availability.

**Acceptance Criteria:**

**Given** the user navigates to Settings > Routing Rules
**When** selecting "Load Balancing" rule type
**Then** a configuration form is displayed showing:
- Enable/disable toggle
- Load balancing strategy selection
- Preferred dialer (for fallback)

**Given** load balancing configuration
**When** viewing strategy options
**Then** the following strategies are available:
- **Capacity-based**: Route to dialer with most available agents
- **Round-robin**: Alternate between dialers
- **Weighted**: Split traffic by percentage (e.g., 70/30)
**And** each strategy has a description explaining its behavior

**Given** capacity-based strategy is selected
**When** saving the configuration
**Then** the routing rule config is updated:
```json
{
  "enabled": true,
  "strategy": "capacity",
  "preferred_dialer": "dialfire",
  "fallback_on_equal": "dialfire"
}
```

**Given** weighted strategy is selected
**When** configuring weights
**Then** the user can:
- Set Dialfire weight (e.g., 70%)
- Set Zendesk Talk weight (e.g., 30%)
**And** weights must sum to 100%
**And** validation prevents invalid totals

**Given** load balancing is enabled
**When** routing a call
**Then** the selected strategy is applied:
- Capacity: Query both dialers, route to higher capacity
- Round-robin: Alternate based on counter
- Weighted: Random selection based on weights
**And** the strategy and decision are logged

**Given** load balancing is disabled
**When** routing a call
**Then** other routing rules (owner, score, time) take precedence
**And** load balancing logic is skipped

**Given** capacity queries fail for one dialer
**When** using capacity-based strategy
**Then** the call routes to the functioning dialer
**And** the failure is logged but doesn't block routing

**References:** FR45

---

**Epic 6 Summary:** 5 stories covering routing rules data model, lead owner mappings, score tiers, time-based routing, and load balancing configuration.

## Epic 7: User Management & Access Control

Maya can view dashboards with read-only access while Jordan has full admin control. Integration credentials stored securely with proper access controls.

### Story 7.1: Implement Secure Credential Storage

As a **system administrator**,
I want integration credentials to be stored securely,
So that API keys and secrets are protected from unauthorized access.

**Acceptance Criteria:**

**Given** dialer API credentials need to be stored
**When** credentials are saved via the settings API
**Then** the credentials are encrypted before storage using:
- AES-256 encryption for the credential value
- Encryption key stored in AWS Secrets Manager (or environment variable for dev)
**And** plaintext credentials are never written to database
**And** plaintext credentials are never logged

**Given** CRM (Braze) API credentials need to be stored
**When** credentials are saved via the settings API
**Then** the same encryption approach is applied
**And** credentials are stored in the `integration_credentials` table:
- `id` (primary key)
- `integration_name` (string: 'dialfire', 'zendesk_talk', 'braze')
- `credential_type` (string: 'api_key', 'api_secret', 'oauth_token')
- `encrypted_value` (binary) - encrypted credential
- `created_at` (timestamp)
- `updated_at` (timestamp)
- `updated_by` (string) - user who last updated

**Given** credentials need to be retrieved
**When** the integration service requests credentials
**Then** credentials are decrypted in memory only when needed
**And** decrypted values are not cached (re-decrypt each time)
**And** credential access is logged at INFO level (without the value)

**Given** viewing credentials in the UI
**When** the settings page displays integration configuration
**Then** credentials are masked (e.g., "sk-****...****abc")
**And** a "Reveal" option requires re-authentication (optional for MVP)
**And** full credentials are never sent to the frontend

**Given** credential rotation is needed
**When** updating an integration credential
**Then** the old credential is kept for 24 hours (rollback period)
**And** the new credential is used immediately
**And** the rotation event is logged in the audit trail

**Given** the database or backups are compromised
**When** an attacker accesses the data
**Then** credentials remain encrypted and unusable without the encryption key
**And** encryption keys are stored separately from the database

**References:** FR46, FR47, NFR-SEC-4, NFR-SEC-5, NFR-SEC-6

---

### Story 7.2: Create User Management Data Model and API

As a **developer**,
I want to create a user management data model and API,
So that users can be created, managed, and assigned roles.

**Acceptance Criteria:**

**Given** the database schema needs to support users
**When** migrations are run
**Then** a `users` table is created with:
- `id` (primary key, auto-increment)
- `email` (string, unique, not null)
- `name` (string, not null)
- `role` (enum: 'admin', 'read_only')
- `api_key` (string, unique) - for API authentication
- `api_key_hash` (string) - hashed version for secure storage
- `active` (boolean, default true)
- `last_login_at` (timestamp, nullable)
- `created_at` (timestamp)
- `updated_at` (timestamp)
- `created_by` (string) - admin who created the user

**Given** the user management API
**When** a GET request is made to `/api/v1/users`
**Then** all users are returned (admin only):
```json
{
  "data": [
    {
      "id": 1,
      "email": "jordan@company.com",
      "name": "Jordan Chen",
      "role": "admin",
      "active": true,
      "last_login_at": "2024-01-15T10:00:00Z"
    }
  ]
}
```
**And** API keys are never included in the response

**Given** creating a new user
**When** a POST request is made to `/api/v1/users` with:
```json
{
  "email": "maya@company.com",
  "name": "Maya Patel",
  "role": "read_only"
}
```
**Then** a new user is created with a generated API key
**And** the API key is returned ONLY in the creation response (one-time view)
**And** the API key hash is stored in the database
**And** a welcome email is sent to the user (optional for MVP)

**Given** updating a user
**When** a PUT request is made to `/api/v1/users/{id}`
**Then** the user details can be updated (name, role, active status)
**And** email cannot be changed (immutable identifier)
**And** the update is logged in the audit trail

**Given** deactivating a user
**When** a DELETE request is made to `/api/v1/users/{id}`
**Then** the user is soft-deleted (active = false)
**And** the user's API key is invalidated immediately
**And** the deactivation is logged in the audit trail

**Given** regenerating an API key
**When** a POST request is made to `/api/v1/users/{id}/regenerate-key`
**Then** a new API key is generated
**And** the old API key is invalidated immediately
**And** the new key is returned (one-time view)
**And** the key regeneration is logged

**References:** FR48, FR49, FR50

---

### Story 7.3: Implement Role-Based Access Control

As a **read-only user (Maya)**,
I want to view dashboards without being able to modify configuration,
So that I can monitor performance without risk of accidental changes.

**Acceptance Criteria:**

**Given** two roles exist: 'admin' and 'read_only'
**When** a user authenticates with their API key
**Then** their role is determined from the users table
**And** the role is attached to the request context

**Given** an admin user makes a request
**When** accessing any API endpoint
**Then** full access is granted to:
- All GET endpoints (read)
- All POST endpoints (create)
- All PUT endpoints (update)
- All DELETE endpoints (delete)

**Given** a read-only user makes a request
**When** accessing GET endpoints
**Then** access is granted to:
- `/api/v1/calls/*` - view calls and metrics
- `/api/v1/dialers/status` - view dialer health
- `/api/v1/alerts/history` - view alert history
- `/api/v1/logs/*` - view audit logs

**Given** a read-only user makes a request
**When** accessing modification endpoints (POST, PUT, DELETE)
**Then** a 403 Forbidden response is returned:
```json
{
  "error": {
    "type": "AuthorizationError",
    "message": "Insufficient permissions. Admin role required.",
    "request_id": "<uuid>"
  }
}
```
**And** the unauthorized attempt is logged at WARNING level

**Given** the frontend application
**When** a read-only user is logged in
**Then** modification UI elements are hidden or disabled:
- Settings page shows "View Only" badge
- Edit/Save buttons are disabled
- Add/Delete buttons are hidden
**And** the user role is available via `/api/v1/users/me`

**Given** role-based access control
**When** implementing endpoint authorization
**Then** a decorator/middleware pattern is used:
```python
@require_role('admin')
async def update_routing_rules(...):
    ...
```
**And** authorization checks happen after authentication

**Given** an unauthenticated request
**When** no API key is provided
**Then** a 401 Unauthorized response is returned
**And** the request is logged at WARNING level

**References:** FR51

---

### Story 7.4: Build User Management UI

As a **Sales Operations Manager (Jordan)**,
I want to manage users through the admin interface,
So that I can add team members and control their access levels.

**Acceptance Criteria:**

**Given** the user is an admin
**When** navigating to Settings > Users
**Then** a list of all users is displayed showing:
- Name
- Email
- Role (Admin/Read-Only)
- Status (Active/Inactive)
- Last login date
- Actions (Edit, Deactivate)

**Given** the user management page
**When** clicking "Add User" button
**Then** a form is displayed with:
- Email field (required, validated)
- Name field (required)
- Role dropdown (Admin, Read-Only)
**And** the form has Save and Cancel buttons

**Given** a new user is created
**When** the form is submitted successfully
**Then** a modal displays the generated API key:
- "API Key created. Copy it now - it won't be shown again."
- Copy button for the API key
- Acknowledge checkbox before closing
**And** the user is added to the list

**Given** editing an existing user
**When** clicking Edit on a user row
**Then** a form is displayed with current values
**And** the name and role can be modified
**And** email is shown but not editable
**And** "Regenerate API Key" button is available

**Given** deactivating a user
**When** clicking Deactivate on a user row
**Then** a confirmation dialog is shown:
- "Are you sure you want to deactivate {user_name}?"
- "They will immediately lose access to the system."
**And** confirming sets the user to inactive
**And** the row shows "Inactive" status in gray

**Given** reactivating a user
**When** clicking Activate on an inactive user
**Then** a confirmation dialog is shown
**And** confirming sets the user to active
**And** their existing API key becomes valid again

**Given** the current user
**When** viewing their own user row
**Then** the Deactivate button is disabled
**And** a tooltip explains "Cannot deactivate yourself"

**Given** only one admin exists
**When** attempting to change their role to read-only
**Then** validation prevents the change:
- "At least one admin user is required"
**And** the save button is disabled

**References:** FR48, FR49, FR50

---

**Epic 7 Summary:** 4 stories covering secure credential storage, user data model, role-based access control, and user management UI.

## Epic 8: Audit Trail & Compliance

Complete audit trail for every call enables debugging, compliance reporting, and operational analysis with 90-day retention and searchable logs.

### Story 8.1: Implement Routing Decision Audit Logging

As a **system**,
I want to log the complete routing decision chain for each call,
So that every routing decision can be traced and debugged.

**Acceptance Criteria:**

**Given** a call is being processed
**When** a routing decision is made
**Then** a `routing_decisions` audit record is created with:
- `id` (primary key)
- `call_sid` (foreign key to calls)
- `request_id` (UUID for correlation)
- `timestamp` (millisecond precision)
- `decision_chain` (JSONB) - complete decision sequence
- `final_dialer` (string) - selected dialer
- `routing_rule` (string) - rule that determined routing
- `total_duration_ms` (integer) - routing processing time

**Given** a routing decision is logged
**When** viewing the decision chain
**Then** it contains a complete sequence of events:
```json
{
  "steps": [
    { "ts": "10:30:00.000", "event": "call_received", "caller": "+15551234567" },
    { "ts": "10:30:00.050", "event": "cache_lookup", "key": "braze:customer:+15551234567", "result": "hit" },
    { "ts": "10:30:00.051", "event": "customer_data", "lead_score": 85, "lead_owner": "team_a" },
    { "ts": "10:30:00.052", "event": "rule_evaluated", "rule": "lead_owner", "match": true },
    { "ts": "10:30:00.053", "event": "dialer_selected", "dialer": "dialfire" },
    { "ts": "10:30:00.150", "event": "twiml_generated", "duration_ms": 150 }
  ]
}
```

**Given** a routing decision fails
**When** logging the failure
**Then** the decision chain includes:
- The failure point with error details
- Any retry attempts
- Fallback decision (if applicable)
- Final outcome (success via fallback or failure)

**Given** multiple routing rules are evaluated
**When** determining the route
**Then** each rule evaluation is logged:
- Rule name and type
- Whether it matched
- Why it matched or didn't match
- Processing time for the rule

**Given** routing audit logs exist
**When** querying by call_sid
**Then** the complete routing history for that call is returned
**And** logs are immutable (cannot be modified after creation)

**References:** FR52

---

### Story 8.2: Implement API Request/Response Logging

As a **system**,
I want to log all external API requests and responses,
So that integration issues can be debugged and audited.

**Acceptance Criteria:**

**Given** a Braze API request is made
**When** the request is sent
**Then** an `api_logs` record is created with:
- `id` (primary key)
- `request_id` (UUID for correlation)
- `call_sid` (nullable - if associated with a call)
- `integration` (string: 'braze', 'dialfire', 'zendesk_talk')
- `method` (string: 'GET', 'POST')
- `url` (string - endpoint called)
- `request_headers` (JSONB - sanitized, no auth tokens)
- `request_body` (JSONB - sanitized)
- `timestamp` (millisecond precision)

**Given** a Braze API response is received
**When** the response is logged
**Then** the same record is updated with:
- `response_status` (integer: HTTP status code)
- `response_headers` (JSONB - relevant headers)
- `response_body` (JSONB - sanitized, truncated if large)
- `duration_ms` (integer - request duration)
- `success` (boolean)
- `error_message` (string - if failed)

**Given** a dialer API request is made (Dialfire or Zendesk Talk)
**When** the request/response cycle completes
**Then** the same logging structure is used
**And** capacity queries and call placement requests are both logged

**Given** sensitive data is in request/response
**When** creating log records
**Then** the following are sanitized:
- API keys replaced with "[REDACTED]"
- Full phone numbers masked: "+1555***4567"
- Large response bodies truncated to 10KB with "[TRUNCATED]" marker

**Given** API logging is performed
**When** during call routing
**Then** logging uses BackgroundTasks (async)
**And** logging never blocks the webhook response
**And** logging failures don't affect call routing

**Given** API logs exist
**When** querying by request_id
**Then** all API calls for that request are returned in chronological order
**And** the complete request/response cycle is visible

**References:** FR53, FR54, FR55, FR56

---

### Story 8.3: Implement Configuration Change Logging

As a **system**,
I want to log all configuration changes made by users,
So that there's an audit trail of who changed what and when.

**Acceptance Criteria:**

**Given** a user modifies routing rules
**When** the change is saved
**Then** a `config_audit_logs` record is created with:
- `id` (primary key)
- `user_id` (foreign key to users)
- `user_email` (string - denormalized for easy querying)
- `action` (enum: 'create', 'update', 'delete')
- `entity_type` (string: 'routing_rule', 'user', 'alert_config', 'integration')
- `entity_id` (string - ID of modified entity)
- `before_value` (JSONB - state before change, null for create)
- `after_value` (JSONB - state after change, null for delete)
- `timestamp` (timestamp with timezone)
- `ip_address` (string - request origin)

**Given** a routing rule is updated
**When** logging the change
**Then** the before/after values show the diff:
```json
{
  "before_value": {
    "name": "Lead Score Routing",
    "config": { "tiers": [{ "min": 80, "max": 100, "dialer": "dialfire" }] }
  },
  "after_value": {
    "name": "Lead Score Routing",
    "config": { "tiers": [{ "min": 70, "max": 100, "dialer": "dialfire" }] }
  }
}
```

**Given** a user is created or deactivated
**When** the change is saved
**Then** the action is logged with:
- User who made the change
- Target user details
- Action taken (create/deactivate)

**Given** alert configuration is changed
**When** saving the new settings
**Then** the change is logged showing:
- Previous threshold values
- New threshold values
- Recipients added/removed

**Given** integration credentials are updated
**When** logging the change
**Then** credential values are NOT logged
**And** only metadata is recorded: "Dialfire API key updated by jordan@company.com"

**Given** configuration audit logs exist
**When** querying by user or time range
**Then** all matching changes are returned
**And** logs can be filtered by entity_type

**References:** FR57

---

### Story 8.4: Implement Log Retention and Management

As a **system administrator**,
I want logs to be automatically retained for 90 days,
So that compliance requirements are met and storage is managed.

**Acceptance Criteria:**

**Given** audit logs are stored in the database
**When** logs are older than 90 days
**Then** they are automatically deleted by a scheduled job
**And** the retention period is configurable via `LOG_RETENTION_DAYS` (default: 90)

**Given** log retention cleanup runs
**When** the scheduled job executes
**Then** the following tables are cleaned:
- `routing_decisions` - records older than 90 days
- `api_logs` - records older than 90 days
- `config_audit_logs` - records older than 90 days
**And** cleanup runs daily during off-peak hours (configurable)
**And** cleanup progress is logged

**Given** large volumes of logs exist
**When** cleanup runs
**Then** deletion happens in batches (1000 records at a time)
**And** the database is not locked during cleanup
**And** cleanup completes within reasonable time

**Given** logs are immutable
**When** any attempt is made to modify existing logs
**Then** the operation is rejected
**And** only deletion via retention policy is allowed
**And** manual deletion requires superadmin access

**Given** compliance requirements
**When** logs are retained
**Then** the following are guaranteed:
- Minimum 90-day retention (can be longer)
- Logs cannot be modified after creation
- Deletion only via automated retention policy
- Deleted logs are permanently removed (no soft delete)

**Given** retention policy execution
**When** the cleanup job runs
**Then** a summary is logged:
- Number of records deleted per table
- Time taken for cleanup
- Any errors encountered

**References:** FR58

---

### Story 8.5: Build Audit Log Search and Query UI

As a **Sales Operations Manager (Jordan)**,
I want to search and view audit logs,
So that I can investigate issues and review system activity.

**Acceptance Criteria:**

**Given** the user navigates to the Logs page (/logs)
**When** the page loads
**Then** the most recent audit logs are displayed (last 24 hours)
**And** logs are paginated (50 per page)
**And** logs show: timestamp, type, summary, user (if applicable)

**Given** the audit log viewer
**When** searching by time period
**Then** the user can:
- Select preset ranges: Last hour, Last 24 hours, Last 7 days, Last 30 days
- Enter custom date range with date pickers
**And** results update to show logs within the selected period

**Given** the audit log viewer
**When** searching by phone number
**Then** the user can:
- Enter a full or partial phone number
- Search finds all calls and routing decisions for matching numbers
**And** phone numbers are matched using partial/wildcard matching
**And** results show all related audit entries

**Given** audit log search
**When** applying filters
**Then** the following filter options are available:
- Log type: Routing decisions, API calls, Configuration changes
- Integration: Braze, Dialfire, Zendesk Talk
- Status: Success, Failed
- User: (for config changes) dropdown of users
**And** multiple filters can be combined

**Given** a log entry is displayed
**When** clicking on the row
**Then** expanded details are shown:
- Full decision chain (for routing logs)
- Complete request/response (for API logs)
- Before/after values (for config changes)
**And** JSON data is formatted and syntax highlighted

**Given** search results are displayed
**When** the user wants to export
**Then** an "Export CSV" button is available
**And** export includes all filtered results (up to 10,000 records)
**And** export respects data masking (phone numbers masked)

**Given** the API endpoint for audit logs
**When** a GET request is made to `/api/v1/logs` with query params:
- `start_date`, `end_date`
- `phone_number`
- `log_type`
- `page`, `page_size`
**Then** matching logs are returned with pagination metadata

**References:** FR59, FR60, FR61

---

### Story 8.6: Implement Call Outcome Logging to Braze

As a **system**,
I want to write call outcomes back to Braze,
So that customer records are updated with call history.

**Acceptance Criteria:**

**Given** a call reaches 'completed' status
**When** the call outcome is finalized
**Then** a Braze API call is made to update the customer record with:
- `last_call_date` - timestamp of the call
- `last_call_outcome` - 'completed', 'no_answer', 'busy', 'failed'
- `last_call_duration` - duration in seconds
- `last_call_dialer` - which dialer handled the call
- `total_calls` - incremented counter

**Given** call outcome data needs to be sent to Braze
**When** the update is triggered
**Then** the update is processed asynchronously (BackgroundTasks)
**And** the webhook response is not blocked
**And** the Braze update is logged in api_logs

**Given** the Braze update fails
**When** the API call returns an error
**Then** the failure is logged at ERROR level
**And** the update is queued for retry (up to 3 attempts)
**And** retry uses exponential backoff (1s, 5s, 30s)
**And** permanent failures are logged but don't affect call routing

**Given** a call fails before completion
**When** logging the outcome to Braze
**Then** the outcome reflects the failure:
- `last_call_outcome` = 'failed' or 'no_answer'
- `last_call_duration` = 0 or partial duration
**And** failure reasons are not sent to Braze (internal only)

**Given** cached customer data exists
**When** a call outcome is logged
**Then** the local cache is updated with new values
**And** cache TTL is reset to 1 hour
**And** subsequent calls reflect the updated data

**Given** Braze webhook integration (Phase 2)
**When** Braze sends customer update webhooks
**Then** the cache can be invalidated proactively
**And** this feature is stubbed for future implementation

**References:** FR15, FR63

---

### Story 8.7: Implement Data Encryption at Rest

As a **system administrator**,
I want sensitive data encrypted at rest,
So that compliance requirements are met and data is protected.

**Acceptance Criteria:**

**Given** the PostgreSQL database contains sensitive data
**When** configuring the database
**Then** AWS RDS encryption is enabled using:
- AES-256 encryption
- AWS managed keys (or customer managed keys)
**And** encryption is transparent to the application

**Given** Redis contains cached customer data
**When** configuring ElastiCache
**Then** encryption at rest is enabled
**And** encryption in transit is enabled (TLS)
**And** AUTH password is required for connections

**Given** application-level encryption is needed
**When** storing highly sensitive fields
**Then** the following are encrypted at the application level:
- Integration credentials (Story 7.1)
- API keys in users table
**And** database-level encryption provides defense in depth

**Given** encryption keys are used
**When** managing key lifecycle
**Then** keys are:
- Stored in AWS Secrets Manager (not in code or config files)
- Rotated annually (or on demand)
- Access-logged via CloudTrail
**And** key access is restricted to the application role

**Given** compliance requirements
**When** auditing encryption status
**Then** the following can be verified:
- RDS encryption enabled: `aws rds describe-db-instances`
- ElastiCache encryption enabled: `aws elasticache describe-cache-clusters`
- Application encryption: audit logs show credential access patterns

**Given** backup and recovery
**When** database backups are created
**Then** backups are also encrypted
**And** encryption keys are backed up separately
**And** recovery procedures are documented

**Note:** This story implements Phase 2 compliance requirements. For MVP, TLS in transit (FR65) and credential encryption (Story 7.1) provide baseline security.

**References:** FR64, NFR-SEC-1

---

**Epic 8 Summary:** 7 stories covering routing decision logging, API logging, configuration change logging, retention management, audit log UI, Braze outcome logging, and data encryption at rest.

---

## Document Complete

All 8 epics with 43 total stories have been created, covering all 61 functional requirements and relevant non-functional requirements.
