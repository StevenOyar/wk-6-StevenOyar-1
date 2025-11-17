# Bug Hunters - Requirement Traceability Matrix (RTM)

---

## Document Information

| Field | Details |
|-------|---------|
| **Project Name** | CleanCity QA Testing Project |
| **Team Name** | Bug Hunters |
| **Document Phase** | Phase 2 and Phase 3|
| **Document Date** | November 16, 2025 |
| **Team Members** | Lilian Kavengi, Steven Oyaro, Rose Kemunto |
| **Status** | Complete |
|**Prepared By:** |Steven Oyaro(risk analyst)
---

## Executive Summary

### Overall Metrics

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Functional Requirements** | 97 | 100% |
| **Requirements Covered** | 97 | 100% |
| **Total Test Cases** | 129 | - |
| **Test Cases Passed** | 38 | 29.5% |
| **Test Cases Failed** | 39 | 30.2% |
| **Test Cases Blocked** | 49 | 38.0% |
| **Test Cases Partial** | 3 | 2.3% |
| **Total Bugs Identified** | 45 |  |

---

## Complete Requirement Traceability Matrix

### 1. Authentication & User Management

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-001 | User registration with all required fields (Email, Password, Confirm Password, Full Name, Phone Number) | TC-001 | Valid user registration with all required fields | Functional | Critical | High | Fail | [Bug-010](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/47) | Open | Form missing Confirm Password and Phone fields. No success message displayed |
| FR-001 | User registration with all required fields | TC-003 | Registration with password less than 8 characters | Functional | Critical | High | Fail | [Bug-001](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/36) | Open | Password validation not working. Accepts passwords under 8 characters |
| FR-001 | User registration with all required fields | TC-004 | Registration with mismatched passwords | Functional | Major | High | Blocked | [Bug-010](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/47) | Open | Cannot test - confirm password field missing from form |
| FR-001 | User registration with all required fields | TC-005 | Registration with name less than 2 characters | Functional | Minor | Medium | Fail | Bug-011 | Open | Name validation missing. Single character names accepted |
| FR-002 | Validate registration data and display appropriate error messages | TC-002 | Registration with invalid email format | Functional | Major | High | Pass | N/A | N/A | Email validation working correctly |
| FR-002 | Validate registration data and display appropriate error messages | TC-006 | Registration with duplicate email | Functional | Critical | High | Fail | [Bug-003](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/38) | Open | Duplicate email validation missing. Same email can be registered multiple times |
| FR-003 | Create user account with "User" role upon successful registration | TC-012 | User role assignment on registration | Functional | Major | High | Pass | N/A | N/A | Default role correctly assigned in localStorage |
| FR-004 | Allow registered users to log in using email and password | TC-007 | Login with valid credentials | Functional | Critical | Critical | Pass | N/A | N/A | Login working correctly with valid credentials |
| FR-005 | Validate login credentials and display error messages | TC-008 | Login with unregistered email | Security | Critical | Critical | Fail | [Bug-005](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/40) | Open | No validation - unregistered users can access protected pages |
| FR-005 | Validate login credentials and display error messages | TC-009 | Login with invalid password | Security | Critical | Critical | Fail | [Bug-006](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/41) | Open | Password validation missing. Users can login with wrong passwords |
| FR-006 | Maintain user session using localStorage | TC-010 | Session persistence after login | Functional | Major | High | Pass | N/A | N/A | Session correctly maintained across browser tabs |
| FR-007 | Redirect users to intended page after successful login | TC-007 | Login with valid credentials | Functional | Minor | Medium | Pass | N/A | N/A | Redirect to profile page working |
| FR-008 | Allow users to log out and clear session data | TC-011 | User logout functionality | Functional | Major | High | Pass | N/A | N/A | Logout clears session and redirects correctly |
| FR-009 | Redirect logged-out users to login page | TC-011 | User logout functionality | Functional | Minor | Medium | Pass | N/A | N/A | Redirect working after logout |
| FR-010 | Support User and Admin roles | TC-012 | User role assignment on registration | Functional | Major | Critical | Pass | N/A | N/A | Role-based system functioning |
| FR-011 | Restrict admin functions to Admin role | TC-069-084 | Admin panel access and functionality | Security | Critical | Critical | Blocked | [Bug-023](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/60) | Open | Admin panel not updating, cannot verify role restrictions |

---

### 2. Waste Management

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-012 | Allow users to schedule waste pickup with required details | TC-013 | Schedule pickup with all required fields | Functional | Critical | Critical | Fail | [Bug-011](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/49) | Open | Form lacks quantity and address fields |
| FR-012 | Allow users to schedule waste pickup with required details | TC-015 | Schedule pickup without selecting location | Functional | Major | High | Pass | N/A | N/A | Error message displayed correctly |
| FR-012 | Allow users to schedule waste pickup with required details | TC-016 | Schedule pickup without selecting waste type | Functional | Major | High | Pass | N/A | N/A | Validation working for waste type |
| FR-012 | Allow users to schedule waste pickup with required details | TC-017 | Schedule pickup with name less than 2 characters | Functional | Minor | Medium | Fail | [Bug-014](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/51) | Open | Name validation missing on pickup form |
| FR-012 | Allow users to schedule waste pickup with required details | TC-019 | Schedule hazardous waste pickup | Functional | Major | High | Blocked | [Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64) | Open | Dashboard doesn't display created requests |
| FR-012 | Allow users to schedule waste pickup with required details | TC-020 | Schedule recyclable waste pickup | Functional | Major | High | Partial | [Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64) | Open | Request created but not visible in dashboard |
| FR-013 | Validate pickup date (minimum 24 hours in advance) | TC-014 | Schedule pickup with date less than 24 hours | Functional | Major | High | Fail | [Bug-007](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/43) | Open | Success message shown but no request created. Can schedule same day |
| FR-013 | Validate pickup date (minimum 24 hours in advance) | TC-014 | Schedule pickup with the provided fields | Functional | Major | High | Fail | [Bug-014](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/50) | Open | No 24-hour validation implemented |
| FR-015 | Prevent scheduling multiple pickups for same date | TC-018 | Prevent duplicate pickups on same date | Functional | Minor | Medium | Blocked | [Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64) | Open | Cannot test - data not saved in dashboard |
| FR-016 | Allow users to view pickup request history | TC-021 | View pickup request history | Functional | Major | High | Fail | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Dashboard doesn't display user's pickup requests |
| FR-017 | Allow users to cancel pending pickup requests | TC-022 | Cancel pending pickup request | Functional | Major | High | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Dashboard not displaying requests to cancel |
| FR-018 | Allow users to modify pickup details before 24 hours | TC-023 | Modify request before 24-hour window | Functional | Major | Medium | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Dashboard not showing requests to modify |
| FR-018 | Allow users to modify pickup details before 24 hours | TC-024 | Attempt to modify request within 24 hours | Functional | Major | Medium | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Cannot test - requests not visible |
| FR-019 | Display request status (Pending, Confirmed, Completed, Cancelled) | TC-025 | Display request status correctly | Functional | Major | High | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Dashboard not displaying status badges |
| FR-020 | Provide real-time status updates | TC-026 | Real-time status updates | Functional | Major | Medium | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | Dashboard not updating in real-time |
| FR-021 | Send notifications for status changes | TC-086 | Pickup confirmation notification | Functional | Major | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | Admin page not working, notifications not showing |
| FR-022 | Allow users to add feedback after pickup completion | TC-027 | Add feedback after pickup completion | Functional | Minor | Low | Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Open | No completed requests visible to add feedback |

---

### 3. Dashboard & Analytics

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-023 | Display personalized dashboard with recent requests and statistics | TC-028 | Display recent pickup requests | Functional | Major | High | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Open | Dashboard not updating with pickup requests |
| FR-023 | Display personalized dashboard | TC-029 | Display upcoming scheduled pickups | Functional | Major | High | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Open | Upcoming pickups showing as 0, not updating |
| FR-023 | Display personalized dashboard | TC-031 | Display achievement badges | Functional | Minor | Medium | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Open | No achievements section in dashboard |
| FR-023 | Display personalized dashboard | TC-032 | Quick action buttons functionality | Functional | Minor | Medium | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Open | Quick action buttons not present |
| FR-024 | Calculate and display environmental impact metrics | TC-030 | Calculate environmental impact metrics | Functional | Major | Medium | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Open | Environmental impact section missing |
| FR-025 | Provide visual charts and graphs for waste data | TC-033 | Display visual charts for waste data | Functional | Major | Medium | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Open | No analytics charts in dashboard |
| FR-026 | Display community leaderboards | TC-034 | Display community leaderboards | Functional | Minor | Low | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Open | Leaderboard feature available but not populated |
| FR-027 | Show monthly and yearly waste trends | TC-035 | Show monthly waste trends | Functional | Minor | Medium | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Open | Monthly trends feature not available |
| FR-027 | Show monthly and yearly waste trends | TC-036 | Show yearly waste trends | Functional | Minor | Medium | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Open | Yearly trends feature not available |
| FR-028 | Provide export functionality for user data | TC-037 | Export user data to CSV | Functional | Minor | Low | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Open | Export feature not implemented |
| FR-029 | Award badges for various achievements | TC-038 | Award "First Pickup" badge | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Open | Achievement system not implemented |
| FR-029 | Award badges for various achievements | TC-039 | Award "10 Pickups Completed" badge | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Open | Badge system missing |
| FR-029 | Award badges for various achievements | TC-040 | Award "Perfect Recycling" badge | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Open | Admin functionality and badge system missing |
| FR-030 | Maintain user points and levels | TC-041 | User points calculation | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Open | Points system not implemented |
| FR-030 | Maintain user points and levels | TC-042 | User level progression | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Open | Level system not implemented |

---

### 4. Content Management

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-031 | Display blog posts with title, content, author, date | TC-043 | Display blog posts | Functional | Major | Medium | Pass | N/A | N/A | Blog displays title, content, and author correctly |
| FR-032 | Create new blog post (Admin) | TC-044 | Create new blog post | Functional | Major | Medium | Blocked | [Bug-015](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/52) | Open | Feature not available, user cannot create blog |
| FR-033 | Edit existing blog post (Admin) | TC-045 | Edit existing blog post | Functional | Major | Medium | Blocked | [Bug-016](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/53) | Open | Edit feature not available |
| FR-034 | Delete blog post (Admin) | TC-046 | Delete blog post | Functional | Major | Medium | Blocked | [Bug-016](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/53) | Open | Delete feature not available for admin |
| FR-035 | Comment on blog post | TC-047 | Comment on blog post | Functional | Major | Medium | Partial | [Bug-017](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/54) | Open | Comments added but disappear on refresh |
| FR-036 | Display rotating eco tips every 5 seconds | TC-048 | Display rotating eco tips | Functional | Minor | Low | Pass | N/A | N/A | Eco tips rotate automatically every 5 seconds |
| FR-037 | Provide interactive quizzes | TC-049 | Interactive quiz functionality | Functional | Minor | Medium | Pass | N/A | N/A | Quiz functions with question progression |
| FR-038 | Track quiz scores and provide explanations | TC-050 | Quiz score tracking | Functional | Minor | Medium | Pass | N/A | N/A | Score updates after each question correctly |
| FR-038 | Track quiz scores and provide explanations | TC-051 | Quiz answer explanations | Functional | Minor | Medium | Pass | N/A | N/A | Explanations provided for correct/incorrect answers |
| FR-039 | Display environmental infographics | TC-052 | Display environmental infographics | Functional | Minor | Low | Pass | N/A | N/A | Statistics from different environments displayed |
| FR-040 | Provide action buttons linking to features | TC-053 | Action buttons linking | Functional | Minor | Medium | Pass | N/A | N/A | Buttons link to request page, community, and report issues |
| FR-041 | Allow users to create community posts | TC-054 | Create community post | Functional | Major | High | Pass | N/A | N/A | Post created and persists on refresh |
| FR-042 | Allow users to like and comment on posts | TC-055 | Like community post | Functional | Major | Medium | Pass | N/A | N/A | Like count increases, button changes, persists on refresh |
| FR-042 | Allow users to like and comment on posts | TC-056 | Comment on community post | Functional | Major | Medium | Pass | N/A | N/A | Comment added successfully |
| FR-043 | Display posts in chronological order | TC-057 | Posts display in chronological order | Functional | Minor | Medium | Pass | N/A | N/A | Posts sorted by newest first |
| FR-044 | Allow users to share tips and experiences | TC-058 | Share waste reduction tips | Functional | Minor | Low | Blocked | [Bug-018](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/55) | Open | Tip category feature not available |

---

### 5. Community Features

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-045 | Allow users to view and edit profile information | TC-059 | View user profile | Functional | Major | High | Pass | N/A | N/A | Name and email display correctly |
| FR-045 | Allow users to view and edit profile information | TC-060 | Edit user profile information | Functional | Major | High | Pass | N/A | N/A | Name successfully updated |
| FR-046 | Display user activity history and achievements | TC-061 | Display user achievements | Functional | Minor | Medium | Fail | [Bug-019](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/56) | Open | No achievements displayed or updated |
| FR-046 | Display user activity history and achievements | TC-062 | Display user activity history | Functional | Minor | Medium | Fail | [Bug-019](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/56) | Open | Activity history not updating |
| FR-047 | Allow users to upload profile pictures | TC-063 | Upload profile picture | Functional | Minor | Low | Fail | [Bug-020](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/57) | Open | Profile picture cannot be updated |
| FR-048 | Show user statistics and environmental impact | TC-064 | Display user statistics | Functional | Minor | Medium | Fail | [Bug-021](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/58) | Open | User statistics not displayed |
| FR-049 | Allow users to follow other community members | TC-065 | Follow other community members | Functional | Minor | Medium | Blocked | [Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) | Open | Follow feature not implemented |
| FR-050 | Provide news feed of community activities | TC-066 | View news feed of community activities | Functional | Minor | Medium | Blocked | [Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) | Open | News feed feature not available |
| FR-051 | Allow users to share achievements and milestones | TC-067 | Share achievements and milestones | Functional | Minor | Low | Blocked | [Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) | Open | Share feature not implemented |
| FR-052 | Support community challenges and events | TC-068 | Participate in community challenges | Functional | Minor | Low | Blocked | [Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) | Open | Challenges feature not available |

---

### 6. Administrative Functions

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-053 | Allow admins to view all pickup requests | TC-069 | Admin view all pickup requests | Functional | Critical | Critical | Fail | [Bug-023](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/60) | Open | Admin panel not updating automatically |
| FR-054 | Allow admins to approve/reject/modify requests | TC-070 | Admin approve pickup request | Functional | Critical | Critical | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Approve feature missing |
| FR-054 | Allow admins to approve/reject/modify requests | TC-071 | Admin reject pickup request | Functional | Critical | Critical | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Reject feature missing |
| FR-054 | Allow admins to approve/reject/modify requests | TC-072 | Admin modify pickup request | Functional | Critical | Critical | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Modify feature missing |
| FR-055 | Allow admins to assign pickup date and time | TC-073 | Admin assign pickup date and time | Functional | Critical | Critical | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Assignment feature missing |
| FR-056 | Provide filtering and search for requests | TC-074 | Filter requests by status | Functional | Major | High | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Filter feature missing |
| FR-056 | Provide filtering and search for requests | TC-075 | Search requests by criteria | Functional | Major | High | Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Open | Search feature missing |
| FR-057 | Allow admins to view all registered users | TC-076 | Admin view all registered users | Functional | Major | High | Blocked | [Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Open | User management features missing |
| FR-058 | Allow admins to change user roles | TC-077 | Admin change user role | Functional | Major | High | Blocked | [Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Open | Role change feature missing |
| FR-059 | Allow admins to suspend/delete user accounts | TC-078 | Admin suspend user account | Functional | Major | High | Blocked | [Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Open | Suspend feature missing |
| FR-059 | Allow admins to suspend/delete user accounts | TC-079 | Admin delete user account | Functional | Major | High | Blocked | [Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Open | Delete feature missing |
| FR-060 | Provide user activity reports | TC-080 | Generate user activity report | Functional | Minor | Medium | Blocked | [Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Open | Reporting features missing |
| FR-061 | Allow admins to moderate community posts | TC-081 | Admin moderate community post | Functional | Major | High | Blocked | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) | Open | Admin panel doesn't display moderation options |
| FR-062 | Allow admins to delete inappropriate content | TC-082 | Admin delete inappropriate content | Functional | Major | High | Blocked | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) | Open | Delete content feature missing |
| FR-063 | Provide content flagging and reporting features | TC-083 | User flag inappropriate content | Functional | Major | Medium | Blocked | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) | Open | Flag feature not available |
| FR-064 | Allow admins to create announcements | TC-084 | Admin create announcement | Functional | Minor | Medium | Blocked | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) | Open | Announcement feature missing |

---

### 7. Notification System

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-065 | Display notification bell with unread count | TC-085 | Notification bell display | Functional | Minor | Medium | Pass | N/A | N/A | Notification bell visible but no unread count |
| FR-066 | Show notifications for various events | TC-086 | Pickup confirmation notification | Functional | Major | High | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | Admin page not working, notifications not showing |
| FR-066 | Show notifications for various events | TC-087 | New blog post notification | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | User cannot create blog posts |
| FR-066 | Show notifications for various events | TC-088 | Community interaction notification | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | No notification update after community interaction |
| FR-066 | Show notifications for various events | TC-089 | Achievement unlock notification | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | Achievement feature missing |
| FR-067 | Mark notifications as read | TC-090 | Mark notification as read | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | Cannot see read/unread status |
| FR-068 | Provide notification history | TC-091 | Notification history view | Functional | Minor | Medium | Blocked | [Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Open | History feature missing |

---

### 8. User Interface Requirements

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-069 | Responsive design for desktop, tablet, mobile | TC-092 | Desktop responsiveness (1920x1080+) | UI/UX | Major | High | Fail | [Bug-036](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/80) | Open | Layout issues on all browsers |
| FR-069 | Responsive design for desktop, tablet, mobile | TC-093 | Tablet responsiveness (768px-1024px) | UI/UX | Major | High | Fail | [Bug-037](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/81) | Open | Elements overlap on tablet mode, headers cover content |
| FR-069 | Responsive design for desktop, tablet, mobile | TC-094 | Mobile responsiveness (320px-767px) | UI/UX | Major | High | Fail | [Bug-038](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/82) | Open | No hamburger menu, headers cover more than half screen |
| FR-070 | Maintain functionality across all screen sizes | TC-095 | Functionality across all screen sizes | UI/UX | Major | High | Fail | [Bug-037](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/81), [Bug-038](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/82) | Open | Scheduling works on desktop but navigation difficult on tablet/mobile |
| FR-071 | WCAG 2.1 AA compliance | TC-096 | WCAG 2.1 AA compliance check | Accessibility | Critical | High | Fail | [Bug-039](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/83) | Open | 1 critical and 34 WCAG 2.1 AA violations found |
| FR-072 | Keyboard navigation support | TC-097 | Keyboard navigation - Tab key | Accessibility | Major | High | Pass | N/A | N/A | All top elements accessible via Tab key |
| FR-073 | Alt text for images | TC-098 | Alt text for images | Accessibility | Major | Medium | Partial | N/A | N/A | Only avatar has alt text, other images missing |
| FR-074 | Screen reader compatibility | TC-099 | Screen reader compatibility | Accessibility | Major | High | Fail | [Bug-040](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/84) | Open | Dropdown for blog tags not announced by screen reader |
| FR-075 | Clear navigation menu | TC-100 | Clear navigation menu | UI/UX | Major | High | Blocked | [Bug-041](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/85) | Open | Navigation menu missing, cannot access menu items |
| FR-076 | Breadcrumbs for complex pages | TC-101 | Breadcrumbs on complex pages | UI/UX | Minor | Medium | Blocked | [Bug-041](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/85) | Open | Breadcrumbs not present on pages |
| FR-077 | Search functionality | TC-102 | Search functionality | Functional | Minor | Medium | Pass | N/A | N/A | Blog search filters results correctly |

---

### 9. Data Management

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-078 | Store data in localStorage | TC-103 | localStorage stores user data | Functional | Critical | Critical | Pass | N/A | N/A | All user data stored correctly |
| FR-078 | Store data in localStorage | TC-104 | localStorage stores pickup requests | Functional | Critical | Critical | Partial | N/A | N/A | Stores correctly but new requests not updated to localStorage |
| FR-079 | Data persistence across sessions | TC-105 | Data persists across sessions | Functional | Critical | Critical | Pass | N/A | N/A | Login and data persist after browser restart |
| FR-080 | Handle localStorage limitations | TC-106 | localStorage limit handling | Functional | Major | High | Pass | N/A | N/A | Error message displayed when approaching 5MB limit |
| FR-081 | Validate all user inputs | TC-123 | Prevent invalid form submission | Functional | Critical | Critical | Pass | N/A | N/A | Error message for blank spaces displayed correctly |
| FR-082 | Prevent SQL injection and XSS attacks | TC-107 | XSS attack prevention | Security | Critical | Critical | Fail | [Bug-042](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/86) | Open | Script tags not escaped, XSS vulnerability exists |
| FR-082 | Prevent SQL injection and XSS attacks | TC-110 | SQL injection prevention | Security | Critical | Critical | Fail | [Bug-043](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/87) | Open | SQL injection payload grants unauthorized access |
| FR-083 | Sanitize user-generated content | TC-111 | User content sanitization | Security | Critical | High | Fail | [Bug-044](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/88) | Open | HTML not escaped or sanitized in community posts |

---

### 10. Performance Requirements

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-084 | Page load within 3 seconds | TC-112 | Page load time - Home page | Performance | Major | High | Pass | N/A | N/A | Home page loads within 3 seconds |
| FR-084 | Page load within 3 seconds | TC-113 | Page load time - Dashboard | Performance | Major | High | Pass | N/A | N/A | Dashboard loads within 3 seconds |
| FR-085 | Interaction response within 1 second | TC-114 | Button click response time | Performance | Major | High | Pass | N/A | N/A | All buttons respond within 1 second |
| FR-085 | Interaction response within 1 second | TC-115 | Form submission response time | Performance | Major | High | Pass | N/A | N/A | Form processes within 1 second with success message |
| FR-086 | Browser compatibility (Chrome, Firefox, Safari, Edge) | TC-116 | Chrome compatibility | Functional | Major | High | Pass | N/A | N/A | All features work correctly in Chrome |
| FR-086 | Browser compatibility (Chrome, Firefox, Safari, Edge) | TC-117 | Firefox compatibility | Functional | Major | High | Pass | N/A | N/A | All features work correctly in Firefox |
| FR-086 | Browser compatibility (Chrome, Firefox, Safari, Edge) | TC-118 | Safari compatibility | Functional | Major | High | Pass | N/A | N/A | All features work correctly in Safari |
| FR-086 | Browser compatibility (Chrome, Firefox, Safari, Edge) | TC-119 | Edge compatibility | Functional | Major | High | Pass | N/A | N/A | All features work correctly in Edge |

---

### 11. Error Handling

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-087 | Display clear, actionable error messages | TC-120 | Clear error messages | Functional | Major | High | Pass | N/A | N/A | Error message "Invalid email" displays clearly |
| FR-088 | Provide error resolution guidance | TC-121 | Error resolution guidance | Functional | Major | High | Pass | N/A | N/A | Error explains what needs to be filled |
| FR-089 | Handle network errors gracefully | TC-122 | Network error handling | Functional | Major | High | Pass | N/A | N/A | Network errors appear in DevTools on deployed app |
| FR-090 | Real-time form validation | N/A | Real-time form validation | Functional | Major | High | test in other test case | N/A | N/A | Test case not executed |
| FR-091 | Prevent invalid form submission | TC-123 | Prevent invalid form submission | Functional | Critical | High | Pass | N/A | N/A | Form not submitted with validation errors |
| FR-092 | Validation error highlighting | TC-124 | Validation error highlighting | Functional | Minor | Medium | Partial | N/A | N/A | Only first field highlighted, others not highlighted |

---

### 12. Support and Maintenance

| FR ID | FR Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|----------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| FR-093 | Contextual help and tooltips | TC-129 | Contextual help tooltips | Functional | Minor | Medium | Blocked | [Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) | Open | Tooltip feature not available |
| FR-094 | FAQ section | TC-130 | FAQ section accessibility | Functional | Minor | Medium | Blocked | [Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) | Open | FAQ section not available |
| FR-095 | Contact information display | TC-131 | Contact information display | Functional | Minor | Low | Blocked | [Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) | Open | Contact info section not available |
| FR-096 | User activity logging | TC-132 | User activity logging | Functional | Minor | Medium | Pass | N/A | N/A | Activities logged in console with details |
| FR-097 | Error logging functionality | TC-133 | Error logging functionality | Functional | Major | High | Pass | N/A | N/A | Errors logged with timestamp, size, name, and message |

---

### 13. Business Rules Validation

| BR ID | Business Rule Description | Test Case ID | Test Case Description | Category | Severity | Priority | Status | Bug ID | Bug Status | Comments |
|-------|---------------------------|--------------|----------------------|----------|----------|----------|--------|--------|------------|----------|
| BR-001 | Pickup scheduling: 30-day advance booking limit | TC-125 | 30-day advance booking limit | Business Rule | Major | High | Fail | [Bug-032](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/75) | Open | Users can schedule beyond 30 days |
| BR-001 | Pickup scheduling: 24-hour minimum notice required | TC-126 | 24-hour minimum notice | Business Rule | Major | High | Fail | [Bug-033](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/76) | Open | Users can schedule pickups same day (within 24 hours) |
| BR-001 | Pickup scheduling: Maximum 3 pickups per week | TC-127 | Maximum 3 pickups per week | Business Rule | Minor | Medium | Blocked | [Bug-034](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/77) | Open | More than 4 pickups can be created, dashboard not updating |
| BR-001 | Hazardous waste requires special approval | TC-128 | Hazardous waste approval requirement | Business Rule | Major | High | Blocked | [Bug-035](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/78) | Open | Admin panel not available to confirm approval workflow |

---

## Summary Statistics by Module

| Module | Total Requirements | Total Test Cases | Pass | Fail | Blocked | Partial | Pass Rate |
|--------|-------------------|------------------|------|------|---------|---------|-----------|
| Authentication & User Management | 11 | 12 | 4 | 6 | 2 | 0 | 33.3% |
| Waste Management | 11 | 15 | 2 | 6 | 7 | 0 | 13.3% |
| Dashboard & Analytics | 8 | 15 | 1 | 9 | 5 | 0 | 6.7% |
| Content Management | 14 | 17 | 6 | 3 | 7 | 1 | 35.3% |
| Community Features | 8 | 10 | 7 | 1 | 2 | 0 | 70.0% |
| Administrative Functions | 12 | 16 | 0 | 1 | 15 | 0 | 0.0% |
| Notification System | 4 | 7 | 1 | 0 | 6 | 0 | 14.3% |
| User Interface Requirements | 9 | 8 | 1 | 5 | 2 | 0 | 12.5% |
| Data Management | 6 | 9 | 5 | 3 | 0 | 1 | 55.6% |
| Performance Requirements | 3 | 8 | 8 | 0 | 0 | 0 | 100.0% |
| Error Handling | 6 | 5 | 3 | 0 | 0 | 1 | 60.0% |
| Support and Maintenance | 5 | 5 | 0 | 0 | 3 | 0 | 0.0% |
| Business Rules Validation | 4 | 4 | 0 | 4 | 0 | 0 | 0.0% |
| **TOTAL** | **97** | **129** | **38** | **39** | **49** | **3** | **29.5%** |

---

## Bug Summary by Severity

| Severity | Count | Percentage | Status |
|----------|-------|------------|--------|
| Critical | 12 | 26.7% | All Open |
| Major | 24 | 53.3% | All Open |
| Minor | 9 | 20.0% | All Open |
| **Total** | **45** | **100%** | **All Open** |

---

## Bug Summary by Category

| Category | Bug Count | Critical | Major | Minor | Status |
|----------|-----------|----------|-------|-------|--------|
| Security | 5 | 3 | 1 | 1 | All Open |
| Functional | 31 | 5 | 18 | 8 | All Open |
| UI/UX | 6 | 1 | 5 | 0 | All Open |
| Accessibility | 2 | 1 | 1 | 0 | All Open |
| Business Rule | 4 | 0 | 3 | 1 | All Open |
| Performance | 0 | 0 | 0 | 0 | N/A |

---

## Critical Defects

### Security Vulnerabilities - Critical Priority

| Bug ID | Description | Impact | Test Case | Current Status |
|--------|-------------|--------|-----------|----------------|
| [Bug-042](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/86) | XSS attack possible - Script tags not escaped | Users can inject malicious scripts | TC-107 | Open |
| [Bug-043](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/87) | SQL injection possible - Unauthorized access granted | Database security compromised | TC-110 | Open |
| [Bug-044](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/88) | User content not sanitized | Malicious HTML can be posted | TC-111 | Open |
| [Bug-005](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/40) | Unregistered users can access protected pages | Authorization bypass | TC-008 | Open |
| [Bug-006](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/41) | Users can login with incorrect passwords | Authentication bypass | TC-009 | Open |

### Core Functionality Failures - Critical Priority

| Bug ID | Description | Impact | Test Case | Current Status |
|--------|-------------|--------|-----------|----------------|
| [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Dashboard not displaying pickup requests | Core waste management feature broken | TC-021-027 | Open |
| [Bug-023](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/60) | Admin panel not updating | Admin cannot manage system | TC-069 | Open |
| [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | All admin request management features missing | System management impossible | TC-070-075 | Open |

---

## Risk Assessment 

| Risk Level | Area | Issues | Impact | Recommendation |
|------------|------|--------|--------|----------------|
| **CRITICAL** | Security | 5 critical vulnerabilities | System and user data at risk | Fix immediately before any deployment |
| **CRITICAL** | Admin Functions | Complete module failure (0% pass) | System cannot be managed | Rebuild admin functionality |
| **HIGH** | Waste Management | Dashboard not updating (63.6% blocked) | Core feature unusable | Fix data persistence and display |
| **HIGH** | Responsive Design | 100% failure on all devices | Poor user experience across devices | Complete UI overhaul needed |
| **MEDIUM** | Authentication | 54.5% failure rate | User account security at risk | Strengthen validation |
| **MEDIUM** | Gamification | 100% blocked | Engagement features unavailable | Implement after critical fixes |
| **LOW** | Support Features | Help system not implemented | Users cannot get assistance | Add after core fixes |

---

## Requirements Coverage Analysis

### Requirements by Status

| Status | Count | Percentage |
|--------|-------|------------|
| Fully Passed | 26 | 26.8% |
| Partially Failed | 15 | 15.5% |
| Completely Failed | 30 | 30.9% |
| Blocked (Cannot Test) | 26 | 26.8% |
| **Total** | **97** | **100%** |