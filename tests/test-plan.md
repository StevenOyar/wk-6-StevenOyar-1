# Test Plan - Phase 1: Planning & Setup
## CleanCity QA Testing Project

---
| **Field** | **Details** |
|-----------|------------|
| **Document Phase** | Phase 1 |
| **Document Date** | November 5, 2025 |
| **Project Name** | CleanCity QA Testing Project |
| **Team Name** | Bug Hunters |
| **Prepared By** | Lilian Kavengi (Test Manager) |
| **Team Members** | Lilian Kavengi, Steven Oyaro, Rose Kemunto |
| **Status** | Phase 1 - Done |

---

## Introduction

## Summary

This test plan outlines a comprehensive quality assurance testing approach for the CleanCity waste pickup scheduler web application. The testing will span 14 days (November 1-18, 2025), involving a team of 3 QA group members from PLP July Cohort that are utilizing risk-based testing methodologies and GitHub Kanban for project management and sometimes Jira for task assigment.

**Key Objectives:**
- Identify and document minimum 15 defects
- Achieve 100% feature coverage
- Validate cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- Ensure WCAG 2.1 AA accessibility compliance
- Deliver comprehensive test report and video presentation per the predefined conditions.

---
### Project Overview

| **Aspect** | **Description** |
|------------|-----------------|
| **Application Name** | CleanCity - Waste Pickup Scheduler |
| **Application Type** | React.js Web Application |
| **Purpose** | Waste management and pickup scheduling system for communities |
| **Target Users** | Residents, administrators, community members |
| **Technology Stack** | React.js, HTML5, CSS3, localStorage |
| **Testing Period** | November 1 - November 11, 2025 |
| **Testing Type** | Functional, Non-Functional, Compatibility, Accessibility |

---

## Test Objectives

### Primary Objectives

| **Objective ID** | **Objective** | **Success Criteria** |
|------------------|---------------|----------------------|
| **OBJ-001** | Identify and document minimum 15 bugs | ≥15 bugs logged in GitHub Kanban with full details |
| **OBJ-002** | Validate all functional requirements | 100% of features tested against FRS |
| **OBJ-003** | Ensure cross-browser compatibility | Application works in Chrome, Firefox, Safari, Edge|
| **OBJ-004** | Verify accessibility compliance | WCAG 2.1 AA standards met |
| **OBJ-005** | Assess security vulnerabilities | Input validation, XSS, session security tested |
| **OBJ-006** | Evaluate performance | Page load times < 3 seconds |
| **OBJ-007** | Test responsive design | Works on desktop and mobile devices |
| **OBJ-008** | Validate data persistence | localStorage functionality verified |


### Testing Goals

| **Category** | **Goal** | **Target** |
|--------------|----------|------------|
| **Test Coverage** | Complete feature coverage | 95% |
| **Test Cases** | Create comprehensive test cases | 90+ test cases |
| **Test Execution** | Execute all priority test cases | 100% |
| **Bug Detection** | Find and document defects | ≥15 bugs (3+ critical, 5+ major, 7+ minor) |
| **Documentation** | Professional test documentation | Complete test report |
| **Video Presentation** | Professional demonstration | 5-minute video |
| **Browser Coverage** | Test on all major browsers | 5 browsers (100%) |
| **Device Coverage** | Test responsive design | Desktop, Tablet, Mobile (100%) |
---

## Scope of Testing

### In-Scope 

| **Module** | **Features to Test** | **Priority** | **Risk Level** |
|------------|---------------------|--------------|--------------------------|
| **Authentication** | Registration, Login, Logout, Session Management | Critical | HIGH |
| **Waste Management** | Pickup Scheduling, Request Management, Status Tracking | P1 - Critical | HIGH |
| **Dashboard** | User Statistics, Charts, Request History |  High | MEDIUM |
| **Admin Panel** | User Management, Request Approval, Moderation |  Critical | HIGH |
| **Feedback System** | Report Missed Pickup, Feedback Submission |  High | MEDIUM |
| **Community** | Posts, Interactions, Feed | Medium |
| **Blog System** | Posts, Comments, Content Management | High |
| **Feedback System** | Report Missed Pickup, Feedback Submission | High |
| **Awareness Content** | Educational Content, Tips, Quizzes | Medium |
| **Non-Functional** | Performance, Accessibility, Usability, Security | High |

**Total In-Scope Test Cases: not done yet**   

### Out-of-Scope

| **Item** | **Reason** |
|---------|------------|
| Backend API Testing | Application uses localStorage only (no backend) |
| Database Testing | Data stored in browser localStorage |
| Payment Gateway | Not implemented in application |
| Email Notifications | Not implemented |
| Third-party Integrations | None present in application |
| Load Testing (1000+ users) | Single user application |
| Native Mobile App | Web application and mobile simulations only |

---


---

## Risk Analysis

### Identified Risks & Mitigation Strategies

| Risk ID | Feature | Description | Likelihood | Impact | Priority | Mitigation |
|---------|---------|-------------|-----------|--------|----------|-----------|
| R-01 | Authentication | Session data loss or authentication bypass | Medium | High | **Critical** | Test login/logout flows, session persistence, role-based access |
| R-02 | Waste Management | Pickup scheduling conflicts or double bookings | Medium | High | **Critical** | Test date/time validation, duplicate prevention |
| R-03 | Data Persistence | localStorage corruption or data loss | Low | High | **High** | Test data after browser clear, cookie handling |
| R-04 | Admin Functions | Unauthorized admin access or privilege escalation | Medium | High | **High** | Test role restrictions, permission validation |
| R-05 | Form Validation | Invalid input causes crashes or unexpected behavior | Medium | Medium | **High** | Test empty fields, special characters, boundary values |
| R-06 | Responsive Design | Layout breaks on mobile devices | Low | Medium | **Medium** | Test all screen sizes, orientation changes |
| R-07 | Accessibility | Screen reader incompatibility or keyboard navigation issues | Low | Medium | **Medium** | Test with accessibility tools, keyboard only navigation |
| R-08 | Performance | Slow page loads or UI freezes | Low | Medium | **Medium** | Monitor load times, browser performance |

---

## Test Strategy Based on Risks

### High-Risk Areas (Priority Testing)
- Authentication system comprehensive testing
- Waste management module validation
- Data persistence and localStorage functionality
- Admin access control mechanisms

### Medium-Risk Areas (Standard Testing)
- Form validation across all modules
- Responsive design on various devices
- Accessibility compliance verification
- Performance metrics monitoring

### Low-Risk Areas (Exploratory Testing)
- UI/UX improvements and cosmetic issues
- Minor feature enhancements
- Edge case scenarios

---
### Defect Severity Levels

| **Severity** | **Definition** | **Examples** | **Impact** | **Response** |
|--------------|----------------|--------------|-----------|------------|
| **CRITICAL** | System crash, data loss, security vulnerability, complete feature failure | • Cannot login<br>• Data deleted<br>• XSS vulnerability<br>• Admin access bypass | Blocks all users | Fix immediately |
| **MAJOR** | Significant functionality broken, incorrect business data | • Scheduling fails<br>• Wrong dashboard data<br>• Form not validating | Impacts core workflow | Fix ASAP |
| **MINOR** | Feature partially functional, has workaround | • Button misaligned<br>• Tooltip wrong<br>• Minor validation issue | User frustration | Fix soon |
| **COSMETIC** | Visual inconsistencies, no functional impact | • Typo in text<br>• Spacing issue<br>• Icon misaligned | Aesthetic only | Fix later |

### Defect Reporting Requirements

Each bug report MUST include:
- **Summary:** Clear 1-line description
- **Description:** Detailed explanation
- **Steps to Reproduce:** Numbered list (minimum 3 steps)
- **Expected Result:** What should happen
- **Actual Result:** What actually happens
- **Environment:** Browser, OS, device, screen resolution
- **Severity:** Critical/Major/Minor/Cosmetic
- **Priority:** High/Medium/Low
- **Screenshots/Video:** Visual evidence
- **Test Data Used:** Specific inputs that trigger bug
- **Impact Analysis:** User/business impact

---

## Test Environment 

### Hardware Requirements

| Component | Specification | Purpose | Status |
|---------------|-------------------|-------------|-----------|
| Laptop | Windows/Mac with 8GB+ RAM | Primary testing machine |   Ready |
| RAM | Minimum 8GB | Run application and tools simultaneously |   Ready |
| Storage | 20GB available | Store test data, screenshots, videos |   Ready |
| Internet | Stable connection | Access application and documentation |   Ready |

### Browser Requirements for Cross-Browser Testing

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | Latest (v119+) | Installed |
| Firefox | Latest (v120+) | Installed |
| Safari | Latest (v17+) | Installed |
| Edge | Latest (v119+) | Installed |

### Testing Tools for Risk Analysis

| Tool Category | Tool Name | Version | Purpose | Status |
|-------------------|---------------|-------------|-------------|------------|
| Project Management | GitHub Projects (Kanban) & Jira | Cloud | Issue tracking, bug reporting, progress |   Configured |
| Accessibility | axe DevTools | Latest | Automated accessibility scanning |   Ready |
| Accessibility | WAVE (WebAIM) | Latest | Web accessibility evaluation |   Ready |
| Accessibility | NVDA | Latest | Screen reader testing (Windows) |   Ready |
| Accessibility | VoiceOver | Built-in | Screen reader testing (macOS/iOS) |   Ready |
| Performance | Chrome DevTools | Built-in | Performance analysis, debugging |   Built-in |
| Performance | Lighthouse | Built-in | Performance, accessibility scoring |   Built-in |
| Screen Recording | OBS Studio | Latest | Bug recording, video presentation |  Ready |
| Screenshots | Built-in tools + Snagit | Latest | Evidence capture |   Ready |
| Collaboration | GitHub, Google Drive | Cloud | Documentation, task assignment, file sharing |   Active |
---

### Test Data Available

### Test Data Available

| Data Type | Details | Source | Status |
|---------------|-------------|-----------|-----------|
| Regular Users | user1@test.com, user2@test.com, user3@test.com | Project provided | Ready |
| Admin Accounts | admin@cleancity.com, moderator@cleancity.com | Project provided | Ready |
| Test Locations | Nairobi, Kisumu, Mombasa, Eldoret | Project provided | Ready |
| Waste Types | General, Recyclable, Organic, Hazardous | Project provided | Ready |
| Invalid Data | Special characters, XSS attempts | Team prepared | Ready |
| Boundary Data | Min/max values, empty fields | Team prepared | Ready |


---


## Test Team Structure & Roles

### Team Members

| **Role** | **Name** | **Email** | **Availability** |
|----------|----------|-----------|------------------|
| **Test Manager** | Lilian Kavengi | kavengililian14@gmail.com | Mon-Sun 8:00pm to 12:00am |
| **Risk Analyst** | Steven Oyaro | stvnoyaro@gmail.com | Mon-Sun 9am to 12:00am |
| **Test Executor** | Rose Kemunto | ivorywehner2@gmail.com | Mon-Sun 11am - 11pm |

### Team Environment Status

| Team Member | Role | OS | Browsers Setup | Tools | Status |
|-----------------|----------|---------|-------------------|-----------|------------|
| Lilian Kavengi | Test Manager | Windows |  All 5 configured | Complete |  Ready |
| Steven Oyaro | Risk Analyst | Windows and Mac |  All 5 configured |  Complete |  Ready |
| Rose Kemunto | Test Executor | Windows |  All 5 configured |  Complete |  Ready |

### Roles & Responsibilities

#### LILIAN KAVENGI - Test Manager

**Primary Responsibilities:**
- Develop and maintain comprehensive test plan and strategy
- Coordinate all testing activities across the team
- Track project schedule, milestones, and deliverables
- Oversee all team member work to ensure quality required standards are met
- Review and approve all test cases, bug reports, and documentation
- Calculate and report test metrics
- Manage risk mitigation and escalation procedures
- Prepare final test report and closure documentation
- Lead communication with instructor (Gerald) and communicate the weekly meeting pitch
- Ensure all deliverables meet  quality standards
- Conduct quality reviews of all team outputs before submission
- Approves the team has done all the tasks and moves the project milestone to the next phase

**Testing Focus Areas:**
- Authentication and User Management
- Admin Panel Functionality
- Security Testing
- Overall Test Strategy and Planning

#### STEVEN OYARO - Risk Analyst

**Primary Responsibilities:**
- Identify, analyze, and prioritize all testing risks
- Develop comprehensive risk-based test strategy
- Design functional test cases for core features
- Link test cases to identified risks for traceability
- Assess and report risk coverage percentage
- Recommend risk mitigation approaches and strategies
- Perform cross-browser compatibility testing
- Conduct exploratory testing for edge cases
- Submit all work to Test Manager for review and approval
- Document risk analysis findings and updates
- Writing automation tests for the team

**Testing Focus Areas:**
- Waste Management Module
- Dashboard and Analytics
- Blog System
- Cross-Browser Compatibility Testing
- Risk Assessment and Coverage

#### ROSE KEMUNTO - Test Executor

**Primary Responsibilities:**
- Execute all test cases systematically and thoroughly
- Capture comprehensive evidence (screenshots, videos, screen recordings)
- Log all defects in GitHub Kanban with complete details
- Document test results and execution logs
- Perform accessibility testing using WCAG 2.1 AA standards
- Conduct performance testing and analysis
- Perform regression testing
- Submit all bug reports and test results to Test Manager for validation
- Update detailed execution logs and evidence repository

**Testing Focus Areas:**
- Community Features and Interactions
- Feedback System
- Awareness Content
- Performance Testing
- Accessibility Testing (WCAG 2.1 AA)

### Quality Assurance Process

**Work Review Flow:**
1. Team member completes assigned work
2. Schedule a meeting with other team members for discussion and presentation of assigned work
3. After the meeting, the assigned work is shared with other team members for review
4. Test Manager reviews for quality, completeness, and standards
5. If approved: Work is finalized and committed to repository
6. If revisions needed: Test Manager provides feedback via a Whatsapp call, team member revises
7. Final approval by Test Manager before any submission to instructor

**Quality Standards Enforced by Test Manager:**
- All test cases have clear steps and expected results
- All bug reports include reproduction steps, screenshots and severity
- All documentation is complete, meets best practice and well formatted
- All deliverables meet the project requirements
- Consistency in formatting and terminology across all documents



---
### Milestone

| **Milestone** | **Date** | **Deliverables** | **Status** |
|---------------|----------|------------------|------------|
| **Phase 1 Complete** | Nov 5, 2025 | • Repository initialized<br>• GitHub Kanban configured<br>• Test plan finalized<br>• Team ready for Phase 2 | Done |
| **Phase 2 Ready** | Nov 6, 2025 | • All test cases prepared<br>• Testing begins <br> •Early automation testing |  In Progress |
| **Phase 3 Reporting** | Nov 13, 2025 | • Final test report<br>• Video presentation |  Planned |

---

## Communication Plan

| **Communication Type** | **Platform** | **Frequency** | **Participants** | **Purpose** |
|------------------------|--------------|---------------|------------------|------------|
| **Daily Team Meeting** | Google Meet | Daily 8:00 PM | All team members | Status updates, blockers, coordination |
| **Quick Updates** | WhatsApp Group | Real time | All team members | Urgent issues, quick questions, task updates |
| **Formal Communication** | Email | Daily | All team members | Official updates, document sharing |
| **Instructor Meeting** | Zoom | Wednesdays | Any member + Instructor Gerald | Formal progress review, guidance per phase |
| **Progress Tracking** | GitHub Kanban & Jira | Continuous | All team members | Task status, bug tracking, deliverables |
| **Document Sharing** | GitHub + Google Drive + Email | Daily | All team members | Test docs, evidence, reports |



## Test Schedule

| **Phase** | **Start Date** | **End Date** | **Duration** | **Status** |
|-----------|----------------|--------------|--------------|------------|
| **Phase 1: Planning & Setup** | Nov 1, 2025 | Nov 5, 2025 | 1 day |  **Done** |
| **Phase 2: Test Design & Execution** | Nov 6, 2025 | Nov 11, 2025 | 6 days |  In Progress |
| **Phase 3: Reporting & Closure** | Nov 11, 2025 | Nov 18, 2025 | 7 days | In Progress   |



## Approval & Sign-Off
### Phase 1:  PLanning and Setup

### Instructor Acknowledgment
| **Field** | **Details** |
|-----------|------------|
| **Instructor Name** | Gerald |
| **Percentage % earned** | 5% |
| **Review Date** | 5/11/2025|
| **Comments** | Proceed to Phase 2 |
---
### Phase 2: 

### Instructor Acknowledgment
| **Field** | **Details** |
|-----------|------------|
| **Instructor Name** | Gerald |
| **Percentage % earned** | 5%|
| **Review Date** |11/11/2025 |
| **Comments** | good work we work on the report and finish execution |

---
| **Name** | **Role** | **Initial** | **Date** | **Status** |
|----------|----------|---------------|---------|-----------|
| Lilian Kavengi | Test Manager |  | Nov 5, 2025 | Done |
| Steven Oyaro | Risk Analyst |  | Nov 5, 2025 |  |
| Rose Kemunto | Test Executor |  | Nov 5, 2025 |  |