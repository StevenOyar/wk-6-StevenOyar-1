# CleanCity QA Testing - Test Plan

**Project:** CleanCity - Waste Pickup Scheduler  
**Version:** 1.0  
**Date:** November 5, 2025  
**Testing Period:** November 5-18, 2025

---

##  Document Information

| Item | Details |
|------|---------|
| **Project Name** | CleanCity - Waste Pickup Scheduler |
| **Application Type** | React.js Web Application |
| **Test Manager** | Lilian Kavengi |
| **Risk Analyst** | Steven Oyaro |
| **Test Executor** | Ruth Kemunto |
| **Project Start** | November 5, 2025 |
| **Project End** | November 18, 2025 |
| **Testing Duration** | 14 days |

---

##  Test Objectives

The primary objectives of this test plan are to:

1. **Functional Testing:** Validate that all features work as specified in the requirements
2. **Non-Functional Testing:** Assess performance, security, accessibility, and usability
3. **Compatibility Testing:** Ensure cross-browser and responsive design functionality
4. **Defect Identification:** Identify and document all bugs with clear reproduction steps
5. **Risk Mitigation:** Test high-risk areas thoroughly to prevent user impact
6. **Quality Assurance:** Ensure the application meets professional quality standards
7. **Documentation:** Create comprehensive test documentation and recommendations

---

##  Scope Definition

### **In Scope**

**Functional Areas:**
- User authentication (registration, login, logout)
- Waste pickup scheduling and management
- Request history and status tracking
- Admin panel functionality
- Blog system and community features
- User profiles and settings
- Notification system
- Dashboard and analytics
- Feedback and reporting features

**Testing Types:**
- Manual functional testing
- Form validation and error handling
- Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- Responsive design (desktop, tablet, mobile)
- Accessibility testing (WCAG 2.1 AA)
- Performance testing
- Security testing (basic)
- Usability testing
- Data persistence (localStorage)

**Browsers & Devices:**
- Chrome (latest version)
- Firefox (latest version)
- Safari (latest version)
- Microsoft Edge (latest version)
- Desktop (1920x1080, 1366x768)
- Tablet (iPad, Android tablets)
- Mobile (iPhone, Android phones)

### **Out of Scope**

- Backend API testing (application uses localStorage only)
- Database testing
- Load testing with thousands of concurrent users
- Mobile app development (web application only)
- Third-party integrations
- Email functionality
- Payment processing
- Server-side performance optimization

---

##  Risk Analysis

### **Identified Risks**

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

**Risk Coverage Target:** ≥85%

---

##  Testing Environment & Tools

### **Hardware Requirements**

- **Computers:** Windows/Mac laptops for desktop testing
- **Devices:** Personal mobile devices for mobile testing (iOS and Android)
- **Network:** Standard internet connection (WiFi or broadband)

### **Software & Tools**

| Category | Tool | Purpose |
|----------|------|---------|
| **Browsers** | Chrome, Firefox, Safari, Edge | Cross-browser testing |
| **Project Management** | Jira or GitHub Kanban | Issue tracking, bug reporting |
| **Testing Documentation** | Markdown, Google Docs | Test cases, reports |
| **Screenshots/Videos** | Snagit, OBS, Built-in tools | Evidence capture |
| **Accessibility** | axe DevTools, WAVE, NVDA | Accessibility testing |
| **Performance** | Lighthouse, Chrome DevTools | Performance analysis |
| **Version Control** | GitHub | Code and documentation management |

### **Test Accounts**

- **Regular Users:** user1@test.com, user2@test.com, user3@test.com
- **Admin Accounts:** admin@cleancity.com, moderator@cleancity.com
- **New Registration:** newuser@test.com (for registration testing)

---

##  Test Schedule

| Phase | Activity | Duration | Dates | Owner | Status |
|-------|----------|----------|-------|-------|--------|
| **Phase 1** | Test Plan & Environment Setup | 2 days | Nov 5-6 | Steven | Planned |
| **Phase 1** | Risk Analysis & Test Strategy | 1 day | Nov 7 | Rose | Planned |
| **Phase 2** | Test Case Design | 2 days | Nov 8-9 | All Team | Planned |
| **Phase 2** | Early Test Execution | 2 days | Nov 10-11 | Lilian | Planned |
| **Phase 3** | Full Test Execution | 3 days | Nov 12-14 | Lilian | Planned |
| **Phase 3** | Defect Analysis & Reporting | 2 days | Nov 15-16 | Steven, Lilian | Planned |
| **Phase 3** | Final Documentation & Video | 2 days | Nov 17-18 | All Team | Planned |
| **Total** | **Complete Testing Cycle** | **14 days** | Nov 5-18 | **Team** | **Planned** |

---

##  Entry Criteria

Before testing can begin, the following must be completed:

- [ ] Test environment is set up and functional
- [ ] All browsers installed and tested
- [ ] Test accounts created and accessible
- [ ] GitHub repository initialized
- [ ] Jira or GitHub Kanban project created
- [ ] Test plan reviewed and approved
- [ ] Team roles and responsibilities assigned
- [ ] Risk analysis completed
- [ ] Test data prepared
- [ ] Communication channels established

---

## 🏁 Exit Criteria

Testing will be considered complete when:

- [ ] All planned test cases have been executed
- [ ] Minimum 15 defects documented in Jira
- [ ] Risk coverage ≥85% achieved
- [ ] Test case pass rate ≥90%
- [ ] All critical and high-priority defects logged
- [ ] Test metrics calculated and documented
- [ ] Final test report completed
- [ ] Video presentation prepared (5 minutes)
- [ ] Test manager sign-off obtained
- [ ] All deliverables committed to repository

---

##  Test Case Categories

### **Functional Test Cases** (Priority: HIGH)
- User Registration & Authentication
- Login & Logout Functionality
- Password Reset & Recovery
- Waste Pickup Scheduling
- Request Modification & Cancellation
- Request Status Tracking
- Admin Panel Access & Functions
- Blog Post Management
- Community Post Interactions
- User Profile Management

### **Non-Functional Test Cases** (Priority: MEDIUM)
- Page Load Performance
- Form Submission Response Time
- UI Responsiveness
- Browser Compatibility
- Mobile Responsiveness
- Accessibility Compliance
- Security Input Validation
- Data Persistence

### **Negative Test Cases** (Priority: MEDIUM)
- Invalid login attempts
- Empty form submissions
- Special character handling
- Boundary value testing
- Unauthorized access attempts
- Data duplication scenarios

### **Edge Case Testing** (Priority: LOW)
- Simultaneous user actions
- Browser back/forward button behavior
- Window resize during operations
- Very long text inputs
- Rapid clicking/submissions

---

##  Deliverables

### **Weekly Submissions**

**Phase 1 (November 5):**
- Test plan document
- Risk analysis report
- Team structure documentation
- Environment setup verification

**Phase 2 (November 11):**
- Detailed test cases (minimum 30)
- Test execution progress
- Early defect log
- Updated risk coverage

**Phase 3 (November 18):**
- Complete test results
- Comprehensive defect report (minimum 15 bugs)
- Final test metrics and KPIs
- Recommendations document
- Video presentation (5 minutes)
- Final test report (PDF)

### **Final Submission Includes**

- Executive Summary
- Test Strategy and Approach
- Test Environment Details
- Test Execution Results
- Defect Analysis by Category
- Risk Assessment Summary
- Recommendations for Improvement
- Test Metrics and Coverage Analysis
- Appendices (screenshots, test cases, Jira exports)

---

##  Team Responsibilities

### **Steven Oyaro - Test Manager**
- Develop and maintain test plan
- Coordinate testing activities
- Track schedule and deliverables
- Calculate and report metrics
- Manage test closure
- **Weekly Deliverable:** Progress report and schedule updates

### **Rose Kemunto - Risk Analyst**
- Identify and prioritize risks
- Develop risk-based test strategy
- Link test cases to risks
- Assess risk coverage
- Recommend risk mitigation
- **Weekly Deliverable:** Risk analysis updates and coverage metrics

### **Lilian Kavengi - Test Executor**
- Execute all test cases
- Capture evidence (screenshots, videos)
- Log defects in Jira with detailed information
- Document test results
- Perform regression testing
- **Weekly Deliverable:** Test execution logs and defect reports

---

##  Quality Metrics

### **Target Metrics**

| Metric | Target | Acceptance Criteria |
|--------|--------|---------------------|
| **Test Case Pass Rate** | ≥90% | Majority of features working correctly |
| **Defect Density** | 0.3-0.5 per test case | Realistic defect discovery |
| **Risk Coverage** | ≥85% | Critical risks thoroughly tested |
| **Bug Severity Distribution** | 3+ Critical, 5+ Medium, 7+ Minor | Balanced defect categorization |
| **Test Documentation Quality** | 100% | All bugs with reproduction steps |
| **Browser Coverage** | 4 browsers | All major browsers tested |
| **Device Coverage** | Desktop, Tablet, Mobile | Responsive design validated |

### **Defect Categorization**

**Severity Levels:**
- **Critical:** System crash, data loss, security breach
- **Major:** Feature completely non-functional
- **Minor:** Feature partially functional or cosmetic issues
- **Cosmetic:** UI/UX inconsistencies with no functional impact

**Bug Categories:**
- Functional defects
- UI/UX issues
- Accessibility barriers
- Performance problems
- Security vulnerabilities
- Data persistence issues

---

##  Testing Methodology

### **Approach**

We will follow the Software Testing Life Cycle (STLC) with emphasis on:

1. **Requirement Analysis:** Understanding functional requirements
2. **Test Planning:** Developing comprehensive test strategy
3. **Test Case Design:** Creating detailed test scenarios
4. **Test Environment Setup:** Configuring browsers and tools
5. **Test Execution:** Running all test cases manually
6. **Defect Reporting:** Logging issues in Jira
7. **Defect Tracking:** Monitoring issue status
8. **Test Closure:** Finalizing documentation and metrics

### **Testing Techniques**

- **Manual Testing:** Primary method for functional testing
- **Exploratory Testing:** Discovering unexpected issues
- **Boundary Value Testing:** Testing limits and edge cases
- **Equivalence Partitioning:** Testing representative values
- **Risk-Based Testing:** Prioritizing high-risk areas
- **Cross-Browser Testing:** Validating consistency
- **Responsive Design Testing:** Mobile and tablet validation
- **Accessibility Testing:** WCAG 2.1 compliance

---

##  Defect Management

### **Bug Report Requirements**

Each defect must include:
- **Summary:** Clear, concise title describing the issue
- **Description:** Detailed explanation of the problem
- **Steps to Reproduce:** Numbered, reproducible steps
- **Environment:** Browser, OS, device, screen resolution
- **Expected vs Actual:** Clear comparison
- **Severity:** Critical, Major, Minor, or Cosmetic
- **Priority:** High, Medium, or Low
- **Screenshots/Videos:** Visual evidence
- **Affected Features:** Which features impacted

### **Jira Workflow**

```
New → In Progress → Under Review → Resolved/Closed
  ↓
  Cannot Reproduce → Closed
  ↓
  Duplicate → Closed
```

---

## Communication Plan

### **Team Communication**
- **Daily:** Quick team sync-ups via messaging
- **Weekly:** Formal meeting with instructor (Wednesdays)
- **Documentation:** Shared GitHub repository for all deliverables

### **Status Reporting**
- **Progress Report:** Weekly submission to instructor
- **Metrics Updates:** Updated daily in Jira dashboard
- **Issue Escalation:** Immediate notification if blockers found

### **Escalation Path**
1. Team discussion and resolution
2. Test manager escalation
3. Instructor consultation
4. Documentation and continued testing

---

##  Success Criteria

### **Project Success Indicators**
- ✅ All planned test cases executed
- ✅ Minimum 15 defects identified and documented
- ✅ ≥85% risk coverage achieved
- ✅ ≥90% test case pass rate
- ✅ Professional documentation completed
- ✅ 5-minute video presentation delivered
- ✅ Team collaboration demonstrated
- ✅ All deliverables submitted on time

---

## Approval & Sign-Off

| Name | Role | Signature | Date |
|------|------|-----------|------|
| Steven Oyaro | Test Manager | ________________ | Nov 5, 2025 |
| Rose Kemunto | Risk Analyst | ________________ | Nov 5, 2025 |
| Lilian Kavengi | Test Executor | ________________ | Nov 5, 2025 |

---

##  Appendices

### **Appendix A: Test Data**
- User accounts for testing
- Sample pickup requests
- Blog post examples
- Community post samples

### **Appendix B: Browser Compatibility Matrix**
- Chrome - Latest version
- Firefox - Latest version
- Safari - Latest version
- Edge - Latest version

### **Appendix C: Device Testing Matrix**
- Desktop: 1920x1080, 1366x768
- Tablet: iPad, Android tablets
- Mobile: iPhone, Android phones

### **Appendix D: References**
- [Functional Requirements](./functional-requirements.md)
- [Technical Specifications](./technical-specs.md)
- [Test Data Document](./test-data.md)
- [Jira Setup Guide](./jira-setup.md)

---

**End of Test Plan Document**

*This test plan will be reviewed and updated based on project progress and emerging risks.*
