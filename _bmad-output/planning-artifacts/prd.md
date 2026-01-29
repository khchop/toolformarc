---
stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-03-success', 'step-04-journeys', 'step-05-domain', 'step-06-innovation', 'step-07-project-type', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish']
inputDocuments: ['/Users/pbos/Documents/testproject/product-brief.md']
documentCounts:
  briefCount: 1
  researchCount: 0
  brainstormingCount: 0
  projectDocsCount: 0
workflowType: 'prd'
project_name: 'testproject'
user_name: 'Pbos'
date: '2026-01-29'
classification:
  projectType: SaaS B2B (web-based platform for sales teams)
  domain: General (telecom/sales operations)
  complexity: Low (standard requirements, technical complexity with telephony)
  projectContext: Greenfield
---

# Product Requirements Document - testproject

**Author:** Pbocos
**Date:** 2026-01-29

## Executive Summary

**Product Vision:** Standalone IVR platform enabling mid-market sales teams to intelligently route calls between multiple dialing systems via real-time customer data integration.

**Core Differentiator:** Centralized routing management with single-pane-of-glass visibility across competing telephony platforms, eliminating manual routing chaos and operational overhead. Real-time decisions based on Braze customer data, with complete audit trails and integration health monitoring.

**Target Customers:** Mid-market sales teams (20-50 agents) using multiple dialing systems (e.g., Zendesk Talk + Dialfire) who experience fragmentation between phone systems and manual routing workarounds. Primary user: Sales Operations Manager responsible for call routing.

**Business Impact:** 15-20% reduction in call abandonment rates, 10% increase in agent utilization, elimination of 2-3 hours daily manual routing work for sales operations teams, and data-driven routing decisions replacing guesswork.

**MVP Strategy:** Problem-solving MVP validating technical viability with 1 design partner customer. Binary success gate: route 500+ calls with <1% failure rate and <2 second call setup time. Revenue generation deferred to Phase 2 after proof-of-concept validation.

---

## Success Criteria

### User Success

**"This is working" moments:**
- **Immediate:** First call routes correctly to the right dialer based on configured rules - validates core routing logic
- **Validation (1 week post-deployment):** Dashboard shows routing distribution working as intended across two dialer systems - confirms predictable behavior

**Quantitative outcomes:**
- **15-20% reduction in call abandonment rate** within first 30 days of deployment (statistical significance requires sufficient call volume)
- **10% increase in calls per agent** - minimum threshold for perceived value ("worth paying for")

### Business Success

**MVP phase (8-10 weeks):**
- Technical viability validation with 1 design partner customer
- 500+ calls routed over 2-week validation period with <1% routing failure rate
- Zero dropped calls attributable to IVR system failure (differentiate from dialer outages)
- Target market validation: Mid-market sales teams (20-50 agents) with actual multi-dialer integration pain

**Growth phase (post-MVP):**
- Revenue from paying customers in mid-market segment
- Expansion to additional dialing system connectors
- Achievement of target customer acquisition numbers

**ROI measurement:**
- Primary metric: Agent utilization improvement (10% calls/agent gain pays for itself)
- Secondary: Conversion rate improvement from faster routing to appropriate specialists
- Qualitative: Reduction in operational overhead for manual routing or system switching

### Technical Success

**Performance SLAs:**
- **Call setup time:** <2 seconds (prevents awkward silences and caller hang-ups)
- **Routing API latency:** <500ms for external API-based decisions
- **System uptime:** 99.9% availability (downtime = missed calls = lost revenue)

**Integration reliability:**
- Stable connections to two different dialer systems simultaneously
- Successful external API request handling (with timeout, fallback, and retry logic)
- Zero dropped calls due to IVR system failure during validation period

### Measurable Outcomes

**MVP validation gate (binary - must achieve to proceed):**
- [ ] 500+ calls successfully routed over 14 consecutive days
- [ ] <1% routing failure rate (calls that failed to route to valid destination)
- [ ] 0 dropped calls attributable to IVR system failure
- [ ] Successful operation across two different dialer systems

**Ongoing success metrics:**
- Call abandonment rate reduction (target: 15-20% improvement)
- Agent utilization increase (target: 10% more calls per agent)
- Dashboard usage (validates week-1 "aha" moment)
- Routing quality feedback (implementation-dependent)

---

## User Journeys

### Jordan Chen - Sales Operations Manager

**Opening Scene:**
It's 8:30 AM and Jordan's already behind. Marketing just dropped 200 hot leads into the CRM, and yesterday's callbacks are sitting in queues. Jordan opens three windows: CRM export, Dialer A dashboard, and Dialer B upload page. This is the next 2-3 hours - manual list segregation, upload juggling, and the constant "Jordan, where did that call go?" Slack messages. Jordan's day isn't about strategy; it's about keeping the leaky routing boat afloat.

**Rising Action:**
A design partner call introduces the IVR routing system. Jordan's skeptical but desperate. Setup takes two days - connecting the two dialers, configuring basic routing rules based on lead scoring. The first call comes in at 10:15 AM. Jordan watches the dashboard pulse: "Call received → Lead score 85 → Routed to Dialer A → Connected to Agent Sarah." Jordan holds their breath until Sarah's status updates to "Call in progress." It worked.

Over the next week, Jordan refines the rules - time-of-day routing, load balancing between dialers when one is near capacity, priority queues for scores above 80. The interruptions stop. Reps stop complaining about wrong-queue assignments. The hot lead scramble becomes an automated rule instead of a frantic manual push.

**Climax:**
One week post-deployment, Jordan opens the dashboard during the morning coffee habit. The past 7 days are laid out: 1,400 calls routed, 68% to Dialer A (warm leads), 32% to Dialer B (cold outreach), zero failed routes. The routing distribution exactly matches Jordan's intended split. Jordan realizes the 2-3 hours of daily manual work is gone. What used to take all morning now happens automatically.

**Resolution:**
Jordan's role has transformed from router mechanic to routing architect. Instead of constantly fixing, Jordan's optimizing. Week 2 brings experimentation - what happens if we route high-score warm leads through Dialer B's better availability? What if we push cold calls through Dialer A during off-peak hours? The dashboard gives instant feedback. Jordan pulls those routing metrics into the Monday sales meeting for the first time - not "I think this is working," but "Here's the data." The purchasing decision is made before the conversation even starts. Jordan is the hero, and the system becomes indispensable.

**This journey reveals requirements for:** Rule-based routing engine with load balancing and time-based rules, real-time monitoring dashboard, routing analytics and distribution reporting, alerting system for routing anomalies, integration with CRM for lead scoring, call flow configuration interface.

---

### Maya Patel - VP of Sales

**Opening Scene:**
Monday morning sales meeting. The leadership team wants to know why conversion dropped 12% on high-value leads last quarter. Maya starts the diagnosis journey: "Jordan, pull the routing breakdown from last quarter." Jordan disappears for 30 minutes, then returns with two spreadsheets - one from Dialer A, one from Dialer B. Maya's team watches while she manually aligns dates and tries to reconcile which leads went where. The answer is unclear. Was it routing? Rep performance? Lead quality? Maya can't definitively say. The conversation moves to speculation, not data-driven decisions.

**Rising Action:**
The IVR system appears as a solution, but Maya doesn't engage with the technical setup - that's Jordan's domain. Maya's journey is about the data. Two weeks after deployment, Jordan invites Maya to look at the new dashboard. Maya sees a single view: call volume by lead score, routing destinations, and conversion rates per pathway. The conversation shifts from speculation to insight.

**Climax:**
Three weeks later, Maya pulls up the dashboard herself before a board meeting. In two minutes, Maya answers the question that used to require a 30-minute manual data extraction: "High-value lead conversion is down because routing to Dialer A dropped 15% during peak hours - we're missing premium lead opportunities." Maya makes a data-driven decision to adjust time-based routing rules and measure the impact next week.

**Resolution:**
Maya's Monday mornings have transformed from data reconciliation time to strategic decision time. The team asks "how did we perform?" and Maya has the answer instantly. The routing system becomes a competitive differentiator - Maya can show prospects "we route every lead to the optimal agent" and back it with data. When Maya discusses metrics with the CEO, it's no longer about call volume - it's about routing optimization driving revenue efficiency. The purchase justification is built on clear, measurable ROI that Maya can defend in any budget conversation.

**This journey reveals requirements for:** Role-based dashboard views (sales leadership vs. ops), aggregated performance metrics, conversion tracking by routing pathway, export capabilities for reporting, historical data analysis, trend visualization, executive summary views.

---

### Integration Support Team (Phase 1) / Customer IT (Phase 3)

**Opening Scene:**
2:47 PM on a Tuesday, the first support ticket arrives: "Calls aren't routing. Nothing coming through." The product team starts the diagnostic journey. Log into Dialer A - it shows no inbound calls. Log into Dialer B - same. Check the IVR logs - activity stopped 3 hours ago. Why? Dialer A released an API update without notification. Calls are being sent but rejected silently. No alerts, no error messages, teams waited 3+ hours to discover the break. The scramble begins - emergency patch, notify customers, apologize for missed calls.

**Rising Action:**
The team builds better monitoring - heartbeat checks on API endpoints, alert thresholds for failed routes. The next integration issue is caught in 12 minutes. But debugging still means logging into multiple systems independently - no single view of what happened when. A customer reports "High-priority lead went to wrong dialer" and the team can't see the routing decision chain - only that the call arrived and was delivered somewhere. Was the IVR decision correct? Did the dialer interpret it correctly? No audit trail exists.

**Climax:**
The single log view arrives. The team opens the call trace screen: "2024-01-15 14:23:07 - Call received from +15551234567 → Lead score lookup via API: 87 → Routing rule: High-score warm → Sent to Dialer A → Dialer A response: Agent line busy → Fallback: Dialer B → Connected." The entire chain is visible in one place. The team can see exactly what happened, when, and why.

**Resolution:**
**Phase 1 (Product Team Support):** The team can now respond to support tickets with precise diagnosis. When a customer reports an issue, the team pulls the call trace and says "I can see exactly what happened - here's the breakdown." Support time drops from 45 minutes of multi-system investigation to 5 minutes of log analysis. The team gains visibility into which integration points are most problematic, informing future connector development priorities.

**Phase 3 (Customer IT + Your Support):** Clear boundaries emerge. Customer IT team configures their dialer credentials and monitors their dialer health. Your team provides a "integration health dashboard" showing API response times, error rates, and connectivity status across all connected systems. When issues arise, your team points to a specific endpoint failure; customer IT fixes their dialer and your team watches the health dashboard return to green. The collaboration becomes transparent rather than adversarial.

**This journey reveals requirements for:** Centralized call log and audit trail, API integration health monitoring, alerting system for integration failures, call trace/debugging interface, integration status dashboard, error reporting and categorization, timeout and retry logs, webhook notification system.

---

## Product Scope

### MVP - Minimum Viable Product

**Core capabilities (gates everything else):**
- Basic call routing between exactly 2 dialing systems (Zendesk Talk + Dialfire)
- Simple rule-based routing engine (load balancing, time-based, or custom rules)
- Web-based administration interface for configuration
- Basic IVR with DTMF input handling
- External API capability for routing decisions with timeout and retry handling
- Call flow designer (code-based or simple visual interface)
- Real-time monitoring dashboard showing active calls and routing distribution
- **Technical validation:** Execute 500+ calls with <1% failure rate, 0 system-caused drops

**Excluded from MVP:**
- More than 2 dialing system connectors
- Advanced analytics or reporting
- Call recording
- Quality metrics (routing success feedback loop)
- Multi-tenant architecture

### Growth Features (Post-MVP)

**System capabilities:**
- Multi-system load balancing across 3+ dialer platforms
- Priority queuing and time-based routing
- Routing quality measurement with agent feedback loop
- Outcome correlation (conversion rates per routing destination)
- A/B testing framework for routing rules
- Advanced analytics dashboard with rule refinement insights
- Webhook notifications for external systems
- Enhanced IVR capabilities (text-to-speech, advanced call flow designer)

**Business features:**
- Multi-tenant support in admin interface
- Integration marketplace for popular dialer platforms
- Call recording and archival
- Advanced reporting and export capabilities

### Vision (Future)

**Complete solution:**
- Multi-data center deployment with global availability
- AI-driven routing optimization (learn from outcomes)
- Voice biometrics and advanced caller identification
- Natural language IVR integration
- Real-time sentiment analysis for routing
- Enterprise-grade compliance and security certifications
- Analytics as a differentiator - helping customers understand calling patterns
- Platform expansion beyond sales (support, service routing)

---

## SaaS B2B Specific Requirements

### Project-Type Overview

This is a managed cloud SaaS B2B platform serving mid-market sales teams (20-50 agents) with intelligent IVR call routing between multiple dialing systems. The platform delivers value through centralized routing management, real-time monitoring, and unified audit trails across competing telephony platforms.

### Multi-Tenant Architecture

**MVP Approach (Single-Instance Per Customer):**
- Dedicated infrastructure per customer deployment
- No shared database or resources across customers
- Simplified operations and security isolation
- Trade-off: Higher cost structure, less automated scaling
- Migration to multi-tenant planned for Growth phase (5+ customers milestone)

**Growth Phase (Shared Infrastructure):**
- Multi-tenant database with customer data isolation
- Shared application instances with customer context
- Cost optimization for scale
- Data partitioning strategies (customer ID-based sharding)

### Permission & Access Control Model

**MVP Role Structure:**

1. **Admin Role (Sales Ops Manager):**
   - Full configuration access (routing rules, call flows, integrations)
   - Dashboard access to all metrics and analytics
   - User management (add/remove team members)
   - Integration credentials management
   - System settings and preferences

2. **Read-Only Role (Sales Leadership):**
   - Dashboard viewing only
   - Performance metrics access
   - Historical reports and trend analysis
   - No configuration or modification permissions

**MVP Limitations:**
- No granular permissions within roles
- Multiple admins permitted at same level
- No audit trail of permission changes
- No delegation or approval workflows

**Growth Phase Enhancements:**
- Support direct login access role
- Customer IT credentials management role
- Granular permission scoping within roles
- Audit logging for all permission changes

### Subscription & Pricing Model

**Tier Structure based on Call Volume and Integration Count:**

| Tier | Call Volume | Dialer Integrations | Target Customers |
|------|------------|-------------------|-----------------|
| Starter | Up to 5,000 calls/month | 2 dialers maximum | Small teams (10-20 agents) |
| Growth | Up to 25,000 calls/month | 4 dialers maximum | Mid-market (20-50 agents) |
| Enterprise | Unlimited | Custom integrations | Large teams (50+ agents) |

**Pricing Rationale:**
- Call volume as primary driver: Aligns with infrastructure costs and value delivered
- Dialer integration as gate: Prevents customers from "gaming" subscriptions with unlimited setups
- Agent count excluded: Hard to enforce and doesn't correlate to system costs

**MVP Scope:** Starter and Growth tiers only, with manual billing/plan changes
**Growth Phase:** Enterprise tier with custom pricing, automated tier upgrades/downgrades

### Integration Requirements

**MVP Baseline (Minimum Viable Surface Area):**

1. **Dialing System Integrations (Required):**
   - Exactly 2 dialer systems per customer
   - Real-time call routing to/from dialers
   - Dialer heartbeat monitoring for availability
   - API-based call placement and status updates
   - Dialer capacity querying for load balancing

2. **Customer Data Integration (Required):**
    - Braze integration for customer lookups
    - Lead scoring extraction for routing decisions
    - Real-time API calls during call routing
    - Customer data enrichment (caller ID, account history)
    - Routing feedback to Braze (call outcome logging)

**Phase 2 Integrations (Post-MVP):**

3. **PBX/System Integration (Conditional):**
   - Required only for customers with existing PBX infrastructure
   - SIP trunk connectivity
   - On-premise PBX support
   - Legacy phone system bridging

4. **Notification Systems:**
   - Slack alerting for routing failures and system issues
   - Email notifications for critical events
   - Webhook notifications for external systems

5. **Custom Integration Framework:**
   - Customer-defined webhook endpoints
   - Self-service integration configuration
   - Integration testing and validation tools

### Compliance & Security Requirements

**Immediate Requirements:**

1. **Audit Log Retention:**
   - Minimum 90-day retention period
   - Complete routing decision chain capture per call
   - User action logging (configuration changes, permission grants/revokes)
   - System event logging (API failures, integration issues)
   - Immutable audit trail (no modification of historical logs)

2. **Security Baseline:**
   - TLS encryption for all data in transit
   - Encryption at rest for customer data
   - Role-based access control enforcement
   - Network segmentation and firewall rules
   - Regular security patching

**SOC 2 Compliance (Planning Required):**

**MVP Phase:**
- Design with SOC 2 controls in mind (don't build tech debt)
- Implement core security controls (access logging, change management, incident response)
- Document policies and procedures
- Prepare for future Type II audit

**Growth Phase:**
- SOC 2 Type I certification (as sales requirement for mid-market)
- Third-party security assessment
- Customer security questionnaire support

**Data Residency:**

**MVP Response to EU Customer Inquiries:**
- "US-only infrastructure currently"
- Document data flow transparency
- EU data transfer compliance planning (if applicable)

**Growth Phase:**
- EU region deployment option (AWS Frankfurt, GCP europe-west)
- Data residency by customer choice
- GDPR compliance checklist

### Implementation Considerations

**Infrastructure Scalability:**
- Start with simple single-instance architecture
- Design data models to be multi-tenant capable from beginning (tenant_id columns, etc.)
- Plan migration path for Growth phase
- Customer onboarding automation vs. manual setup

**Cost Management:**
- Monitor infrastructure costs per customer closely in MVP
- Validate call volume pricing model against actual costs
- Identify cost drivers (API requests, database storage, bandwidth)
- Build cost dashboard for internal visibility

**Customer Isolation:**
- Even with single-instance architecture, ensure customer data isolation
- Test data leakage prevention during development
- Implement secure credential storage (each customer's dialer API keys)

**Operational Implications:**
- Support overhead scales with customer count manually initially
- Each customer has 2 dialer integrations = integration surface area doubles per customer
- Troubleshooting requires access to customer's dialer logs initially
- Onboarding complexity: Help customer integrate both dialers and CRM

---

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Problem-Solving MVP with Technical Validation Focus

**Resource Requirements:** 2 developers minimum for MVP (telephony/backend specialist + integrations/frontend specialist), 8-10 week development timeline

**MVP Philosophy:**
- Validate technical feasibility with design partner first
- Revenue/closed business comes in Phase 2 after proof of concept
- Binary gate: Either we can route calls reliably (<2s, <1% failures) or we can't
- Simplify integration surface to one dialer pair to reduce complexity
- Hardcoded customer configuration (no self-service rule builder yet)

### MVP Feature Set (Phase 1)

**Core User Journeys Supported:**
- Jordan (Sales Ops): Configure routing with our team help, monitor basic call metrics, validate routing accuracy
- Design Partner Validation: Execute 500+ calls with measurable before/after comparison

**Must-Have Capabilities:**

**Call Routing Core:**
- Inbound call routing from one dialer pair (Zendesk Talk → Dialfire)
- Single customer data field lookup for routing decisions (lead score tier)
- Hardcoded routing rules configured by product team (no customer rule builder)
- Basic DTMF IVR (press 1 for X, press 2 for Y) as fallback
- <2 second call setup time SLA compliance

**Monitoring & Observability:**
- Real-time dashboard showing active call count
- Basic reporting: call count by route destination, success/failure breakdown
- Call trace for individual failed routes (debugging)
- Integration health status (dialer connectivity, Braze API status)

**CRM Integration:**
- Braze support for customer data
- Single field lookup per call (lead score tier)
- Potential caching strategy for latency mitigation
- Basic authentication and error handling

**Dialer Integration:**
- Zendesk Talk + Dialfire only (one specific dialer pair)
- Real-time call placement and status updates
- Capacity querying for load balancing
- Integration testing tools

**Admin Interface:**
- Simple dashboard with call metrics (read-only views for both admin and leadership)
- Basic system health monitoring
- Alert configuration (email notifications only)

**Excluded from MVP:**
- Visual rule builder for customers
- Custom audio prompts (TTS-only)
- Role-based permissions (single admin level)
- Multiple dialer pair support
- Advanced analytics or historical reporting
- Call recording
- Webhooks or Slack notifications
- Multi-tenant architecture

### Post-MVP Features

**Phase 2 (Growth):**

**Product Capabilities:**
- Visual rule builder allowing self-service configuration
- Support for additional dialer pairs (expand beyond Zendesk Talk/Dialfire)
- Lead data caching strategy (if latency issues in MVP)
- Enhanced reporting with historical trend analysis
- Conversion tracking per routing pathway
- Advanced IVR features (custom audio prompts, text-to-speech)
- Role-based permissions (admin vs read-only)
- Integration health dashboard with alerting

**Business Development:**
- 2-3 paying customers validating market fit
- Revenue from starter/growth tier subscriptions
- Customer onboarding automation
- Multi-tenant database architecture (shared infrastructure)
- SOC 2 Type I certification preparation

**Phase 3 (Expansion):**

**Platform Capabilities:**
- Any-dialer integrations (connector marketplace approach)
- Advanced routing logic (multi-field CRM lookups, decision trees)
- Routing quality measurement with agent feedback
- A/B testing framework for routing rules
- Call recording and archival
- Webhooks and custom integrations framework
- Slack notifications for system alerts
- Multi-dialer load balancing across 3+ platforms

**Enterprise Readiness:**
- Enterprise tier with unlimited call volume
- Multi-data center deployment (EU region support)
- SOC 2 Type II certification
- Advanced security features (SSO, IP allowlisting)
- Dedicated support and SLAs

### Risk Mitigation Strategy

**Technical Risks:**

**Braze API Latency (<2s SLA Risk):**
- **Risk:** Braze API responses may exceed 2 seconds, causing caller hang-up
- **Mitigation Strategy:**
  - **MVP Approach:** Implement customer data caching - sync important customer fields to local database overnight or on change events
  - **Backup Plan:** If caching still can't meet <2s, relax to <3s and monitor abandon rate impact
  - **Measurement:** Instrument API latency from day 1, set up alerts at 1s to catch issues early
- **Fallback Architecture:** Design system to support rule-based routing when Braze data unavailable (route to default dialer)

**Integration Complexity Risk:**
- **Risk:** Dialfire/Zendesk Talk API changes or undocumented edge cases cause routing failures
- **Mitigation:** 8-10 week MVP buffer includes 2 weeks for integration debugging with design partner
- **Validation:** Use design partner's actual environment for integration testing, not sandbox

**Real-time System Reliability Risk:**
- **Risk:** System failures during peak calling hours cause immediate lost revenue
- **Mitigation:** Comprehensive monitoring/alerting from MVP launch, manual support response (no automated failover yet)

**Market Risks:**

**No Design Partner Found:**
- **Risk:** Cannot identify a mid-market company with genuine multi-dialer pain
- **Mitigation:** Conduct prospect interviews before starting development - if minimum 3 companies express strong pain, proceed. If not, pivot or reconsider market
- **Learning Goal:** During pre-development interviews, refine understanding of current workarounds and intensity of pain

**Pricing/Value Proposition Risk:**
- **Risk:** Companies won't pay for routing optimization - they view it as "nice to have" not "must have"
- **Mitigation:** Focus validation on measurable before/after metrics from design partner ("we used to lose X callbacks/week, now zero"). Quantify actual operational time saved (Jordan's 2-3 hours/day manual routing eliminated)
- **Phase 2 Validation:** Before building Growth features, get 2-3 signed LOIs or pre-pay commitments

**Resource Risks:**

**8-Week Timeline Too Tight:**
- **Risk:** Technical unknowns (CRM latency, integration quirks) cause slips
- **Mitigation:** Strict scope discipline - absolutely no feature creep. If a feature isn't in MVP scope, it doesn't get done
- **Contingency Plan:** Cut dialer integration to ONE platform (just Zendesk Talk) if needed - still proves routing concept
- **Minimum Viable:** If timeline stretches to 12 weeks, proceed with same scope using extended timeline

**Developer Skill Gaps:**
- **Risk:** 2-person team lacks specialized telephony or integration experience
- **Mitigation:** During MVP kickoff, identify skill gaps and upskill or bring in consultant for specific integration work
- **Alternative:** Expand to 3-person team if telephony specialist proves necessary

---

## Functional Requirements

### Call Routing & IVR

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

### Braze Integration

- FR11: System can authenticate with Braze API
- FR12: System can retrieve customer record from Braze using caller phone number
- FR13: System can retrieve lead score field from Braze customer record
- FR14: System can cache customer data locally to support fast lookups during call routing
- FR15: System can write call outcome data to Braze customer record after call completion

### Dialing Platform Integration

- FR16: System can authenticate with Dialfire API
- FR17: System can authenticate with Zendesk Talk API
- FR18: System can place outbound call instruction to dialing platform
- FR19: System can receive call status updates from dialing platform
- FR20: System can query agent availability status from dialer platform
- FR21: System can retrieve capacity information from dialer platform
- FR22: System can detect connectivity failure with dialer platform
- FR23: System can attempt retry when dialer platform API request fails

### Monitoring & Dashboard

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

### Alerting & Notifications

- FR37: System can send email notification when routing failure rate exceeds threshold
- FR38: System can send email notification when integration fails to connect
- FR39: Admin user can configure email addresses for alert notifications
- FR40: Admin user can configure alert threshold values for routing failures

### Configuration & Rules

- FR41: Admin user can configure which CRM field determines routing destination
- FR42: Admin user can configure lead owner to dialer mapping rules
- FR43: Admin user can configure lead score tier to dialer mapping rules
- FR44: Admin user can configure time-based routing rules
- FR45: Admin user can configure load balancing rules between dialers

### System Administration

- FR46: System can store dialing platform API credentials securely
- FR47: System can store CRM API credentials securely
- FR48: Admin user can add users with admin permissions
- FR49: Admin user can add users with read-only permissions
- FR50: Admin user can remove user access
- FR51: Read-only user can view dashboard but cannot modify configuration

### Audit & Logging

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

### Data Management

- FR62: System can store lead data cached from CRM
- FR63: System can update cached lead data when CRM record changes
- FR64: System can encrypt data at rest for customer information
- FR65: System can encrypt data in transit for all API communications

---

## Non-Functional Requirements

### Performance

**Call Setup Time SLA:**
- System must complete call setup and routing within 2 seconds from call receipt
- This SLA applies to end-to-end routing: CRM lookup + routing decision + dialer handoff
- System must instrument and track call setup time for every call
- Alert trigger: Call setup time exceeding 1.5 seconds on more than 5% of calls

**Dashboard Response Time:**
- Dashboard pages must load within 5 seconds for standard views
- Real-time metrics display must update within 3 seconds of data change
- Historical report generation may take up to 10 seconds

**API Monitoring Latency:**
- System must detect and display integration failures within 1 minute of occurrence
- API latency monitoring updates must be visible within 5 minutes of data collection
- Alerting systems must trigger within 1 minute of threshold breach

### Security

**Data Encryption:**
- All data at rest must be encrypted using AES-256 or equivalent
- All data in transit must be encrypted using TLS 1.2 or higher
- Encryption keys must be managed securely with key rotation capability

**Credential Storage:**
- Dialer API credentials must be stored securely (not plaintext)
- CRM API credentials must be stored securely (not plaintext)
- Credentials must be encrypted at rest with access controls limiting who can retrieve decrypted values

**Audit Logging for Security Events:**
- System must log all routing rule changes with timestamp, user identity, and rule modification details
- System must log all user permission changes (adds, removes, modifications)
- System must log all configuration changes to integration credentials
- Audit logs must be immutable (cannot be modified after creation)
- Audit logs must be retained for minimum 90 days

**Data Handling:**
- No additional PII beyond what exists in customer's CRM database
- System must not store customer's CRM data permanently except for lead data caching
- Cached lead data must include only fields required for routing (phone number, owner, score)
- Customer data isolation must be enforced (no data leakage between customers)

**SOC 2 Preparation (MVP):**
- System design must implement SOC 2 Type I controls from inception
- Access control logging must capture all user actions
- Change management processes must be documented
- Incident response procedures must be defined
- Security policies must be documented

### Integration

**Integration Success Rate:**
- System must achieve 99% success rate on CRM API calls
- System must achieve 99% success rate on dialer API calls
- System must monitor integration success rates per platform
- Alert trigger: Integration success rate falls below 95% over 5-minute window

**Integration Failure Detection:**
- System must detect integration failures within 5 minutes of occurrence
- System must display integration health status on dashboard in near real-time
- System must send email alerts when integration failures exceed 5% over 5-minute window

**Integration Failure Handling - Complete Scenarios:**

**Scenario 1: Braze Lookup Fails (Braze API timeout or error)**
- **Immediate Action:** Route to customer-configured default fallback dialer
- **Retry Logic:** Do not retry Braze lookup - caller is waiting, proceed immediately to fallback
- **Logging:** Log Braze failure type, attempted call, customer identifier, timestamp, final routing decision
- **Alerting:** Alert if Braze failure rate exceeds 5% over 5-minute window
- **Caller Experience:** Call routes successfully to appropriate dialer, caller unaware of Braze lookup failure

**Scenario 2: Dialer Handoff Fails (Dialfire/Zendesk Talk API returns error or timeout)**
- **Immediate Action:** Immediate retry to same dialer (no delay)
- **Retry Logic:** One immediate retry attempt. If retry succeeds, proceed normally
- **Both Dialers Fallback:** If both dialers fail, execute cascade:
  1. Play TTS message: "Please hold while we connect you"
  2. Wait 2 seconds, retry primary dialer one more time
  3. If still failed, play apology: "We're experiencing technical difficulties. Press 1 to leave a callback number or hold for the next available agent."
  4. Last resort: route to basic hold queue that rings any available agent in either system
- **Emergency Alerting:** Send SMS alert to Jordan immediately when both dialers fail
- **Logging:** Log primary dialer failure, retry outcome, backup dialer failure, all API responses, fallback strategy executed
- **Caller Experience:** Minimal delay (retry), then guided fallback options

**Scenario 3: Dialer Capacity Query Fails**
- **Immediate Action:** Route to customer-configured preferred dialer (customer knows operation better than algorithm)
- **Retry Logic:** Retry capacity query once immediately, then proceed to preferred dialer fallback
- **Logging:** Log capacity query failure, retry attempt, fallback dialer selected
- **Alerting:** Alert if capacity query failures exceed 5% over 5-minute window
- **Caller Experience:** No visible impact if fallback routing works transparently

**Scenario 4: Integration Goes Down Completely (connection failure, API 500s, sustained failures)**
- **Declaration Threshold:** Declare integration "down" after 3 consecutive failures within 1-minute window
- **CRM Down Routing:** Route all calls to customer-configured default dialer (no CRM data enrichment)
- **Single Dialer Down Routing:** Route 100% of calls to the functioning dialer
- **Both Dialers Down Routing:** Execute catastrophic fallback cascade (Scenario 2 logic)
- **Recovery Detection:** Declare integration "recovered" after 3 consecutive successful API calls
- **Normalization:** Auto-resume normal routing operations upon recovery, do not require manual intervention
- **Recovery Notification:** Send email notification to Jordan that integration has recovered
- **Dashboard Display:** Show outage window clearly in timeline view with start/end times
- **Logging:** Log outage start/end, duration, calls affected, routing behavior during outage, recovery event

**Scenario 5: Partial CRM Response (slow response, incomplete data, missing fields)**
- **Response Time Cutoff:** 1.5 second maximum CRM response time. If exceeded, abort request and use fallback
- **Missing Field Handling:**
  - If lead owner field has value: Use lead owner for routing (regardless of lead score presence)
  - If lead owner is null/null but lead score has value: Use lead score for routing
  - If both lead owner and lead score are null: Route to customer-configured default dialer
- **Degradation Monitoring:** Log CRM response time trends, do not alert unless degradation causes fallbacks
- **Logging:** Log partial response, missing fields, cutoff reason, routing decision made
- **Caller Experience:** Seamless - caller unaware of partial response unless fallback executed

### Reliability

**System Availability:**
- Target uptime: 99.5% (realistic for MVP with design partner customer)
- Acceptable downtime: 3.6 hours per month
- Downtime must be scheduled during off-peak hours with customer notification
- Aspirational goal for Growth phase: 99.9% uptime

**Routing Failure Rate:**
- System must maintain routing failure rate below 1%
- Routing failures defined as calls that fail to reach a valid dialer destination
- This includes CRM lookup failures, dialer handoff failures, and integration failures
- Alert trigger: Routing failure rate exceeds 1% over 5-minute window

**Silent Failure Tolerance:**
- Zero tolerance for silent failures
- Every failure must be logged with detailed information
- Every failure must be visible in audit logs and dashboard
- Failed calls must be traceable end-to-end (complete routing decision chain visible)

**Failure Recovery:**
- System must support graceful degradation when partial failures occur
- System must continue operating with reduced functionality during outages
- Automatic recovery must occur without manual intervention where possible
- Critical failures must trigger manual review and corrective action
