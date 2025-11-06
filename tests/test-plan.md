# Test Plan - Phase 1: Planning & Setup
## CleanCity QA Testing Project

---
| **Field** | **Details** |
|-----------|------------|
| **Document Title** | Risk Analysis & Test Strategy Document |
| **Document Phase** | Phase 1 |
| **Document Date** | November 5, 2025 |
| **Project Name** | CleanCity QA Testing Project |
| **Team Name** | Bug Hunters |
| **Prepared By** | Steven Oyaro (Risk Analyst) |
| **Role** | Risk Analyst & Test Strategy Designer |
| **Status** | Phase 1 - Done |

---

## Introduction

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
| **OBJ-003** | Ensure cross-browser compatibility | Application works in Chrome, Firefox, Safari, Edge, Brave|
| **OBJ-004** | Verify accessibility compliance | WCAG 2.1 AA standards met |
| **OBJ-005** | Assess security vulnerabilities | Input validation, XSS, session security tested |

---

## Scope of Testing

### In-Scope Features for Risk Analysis

| **Module** | **Features to Test** | **Priority** | **Risk Level** |
|------------|---------------------|--------------|--------------------------|
| **Authentication** | Registration, Login, Logout, Session Management | P1 - Critical | HIGH |
| **Waste Management** | Pickup Scheduling, Request Management, Status Tracking | P1 - Critical | HIGH |
| **Dashboard** | User Statistics, Charts, Request History | P2 - High | MEDIUM |
| **Admin Panel** | User Management, Request Approval, Moderation | P1 - Critical | HIGH |
| **Feedback System** | Report Missed Pickup, Feedback Submission | P2 - High | MEDIUM |

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

## Test Environment Setup (Risk Analyst Part)

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
| Brave | Latest (v17+) | Installed |
| Edge | Latest (v119+) | Installed |

### Testing Tools for Risk Analysis

| Tool Category | Tool Name | Version | Purpose | Status |
|-------------------|---------------|-------------|-------------|------------|
| Accessibility | axe DevTools | Latest | Automated accessibility scanning |   Ready |
| Performance | Chrome DevTools | Built-in | Performance analysis, debugging |   Built-in |
| Performance | Lighthouse | Built-in | Performance, accessibility scoring |   Built-in |
| Project Management | GitHub Projects (Kanban) | Cloud | Risk tracking, task assignment |   Configured |

---

## Test Schedule

| **Phase** | **Start Date** | **End Date** | **Duration** | **Status** |
|-----------|----------------|--------------|--------------|------------|
| **Phase 1: Planning & Setup** | Nov 5, 2025 | Nov 5, 2025 | 1 day |  **Done** |
| **Phase 2: Test Design & Execution** | Nov 6, 2025 | Nov 12, 2025 | 7 days |  Planned |
| **Phase 3: Reporting & Closure** | Nov 13, 2025 | Nov 18, 2025 | 6 days |  Planned |

---

## Steven Oyaro's Responsibilities

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

