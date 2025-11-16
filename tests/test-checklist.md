# Bug Hunters - Checklist 

---
| **Field** | **Details** |
|-----------|------------|
| **Document Phase** | Phase 2|
| **Document Date** | November 16, 2025 |
| **Project Name** | CleanCity QA Testing Project |
| **Team Name** | Bug Hunters |
| **Prepared By** | Steven Oyaro |
| **Team Members** | Lilian Kavengi, Steven Oyaro, Rose Kemunto |
| **Status** | Phase 2 - Done |

---


## Authentication & User Management

### Registration & Login
- [x] Valid user registration with all required fields
- [x] Email validation (format and uniqueness)
- [x] Password validation (minimum 8 characters, match confirmation)
- [x] Full name validation (2-50 characters)
- [x] Phone number format validation (optional field)
- [x] Error messages display correctly for invalid inputs
- [x] Successful registration creates User role account
- [x] Login with valid credentials succeeds
- [x] Login with invalid credentials shows error
- [x] Session persists in localStorage
- [x] Logout clears session and redirects to login
- [x] Redirect to intended page after login

### Role-Based Access
- [x] User role has appropriate permissions
- [x] Admin role has full administrative access
- [ ] Restricted pages block unauthorized users
- [x] Role-based navigation menu displays correctly

---

## Waste Pickup Management

### Scheduling Pickups
- [x] Schedule form displays with all required fields
- [x] Future date validation (minimum 24 hours advance)
- [x] Waste type selection works (General, Recyclable, Organic, Hazardous)
- [x] Quantity selection works (Small, Medium, Large)
- [x] Special instructions field accepts up to 200 characters
- [x] Address auto-fills from user profile
- [ ] Available time slots display correctly
- [ ] Prevent duplicate pickups on same date
- [x] Successful pickup request confirmation

### Request Management
- [ ] View pickup request history
- [ ] Display request status correctly (Pending, Confirmed, Completed, Cancelled)
- [ ] Cancel pending requests
- [ ] Modify requests before 24-hour window
- [ ] Cannot modify requests within 24 hours
- [ ] Real-time status updates work
- [ ] Notifications for status changes
- [ ] Add feedback after completion

---

## Dashboard & Analytics

### User Dashboard
- [ ] Recent pickup requests display
- [ ] Upcoming scheduled pickups shown
- [ ] Environmental impact statistics calculate correctly
- [ ] Achievement badges display
- [ ] Quick action buttons functional
- [ ] Waste diverted from landfill metric
- [ ] CO2 emissions saved metric
- [ ] Trees equivalent saved metric

### Analytics & Gamification
- [ ] Visual charts render properly
- [ ] Community leaderboards display
- [ ] Monthly trends show accurate data
- [ ] Yearly trends show accurate data
- [ ] CSV export functionality works
- [ ] Achievement badges unlock correctly
- [ ] Points system calculates accurately
- [ ] User levels progress properly

---

## Content & Community

### Blog System
- [x] Blog posts display correctly
- [x] Users can interact with blog content
- [ ] Blog management functions work
- [x] Categories/tags organizational features functional

### Awareness & Education
- [x] Eco tips rotate every 5 seconds
- [x] Interactive quizzes load and function
- [x] Quiz scores track correctly
- [x] Answer explanations display
- [x] Environmental infographics render
- [x] Action buttons link correctly

### Community Features
- [x] Create community posts
- [x] Like posts functionality
- [x] Comment on posts
- [x] Posts display in chronological order
- [x] Share tips and experiences
- [x] View and edit user profile
- [ ] Upload profile pictures
- [] User activity history displays
- [ ] Follow other users
- [ ] News feed shows community activities
- [ ] Share achievements
- [ ] Community challenges participate

---

## Administrative Functions

### Admin Dashboard
- [ ] View all pickup requests
- [ ] Filter and search requests
- [ ] Approve pickup requests
- [ ] Reject pickup requests
- [ ] Modify pickup requests
- [ ] Assign pickup dates and times

### User & Content Management
- [ ] View all registered users
- [ ] Change user roles
- [ ] Suspend user accounts
- [ ] Delete user accounts (except admins)
- [ ] Generate user activity reports
- [ ] Moderate community posts
- [ ] Delete inappropriate content
- [ ] Content flagging system works
- [ ] Create announcements

---

## Notifications & UI

### Notification System
- [x] Notification bell displays unread count
- [ ] Pickup confirmation notifications
- [ ] New blog post notifications
- [ ] Community interaction notifications
- [ ] Achievement unlock notifications
- [ ] Mark notifications as read
- [ ] Notification history accessible

### User Interface
- [ ] Responsive on desktop (1920x1080+)
- [ ] Responsive on tablet (768px-1024px)
- [ ] Responsive on mobile (320px-767px)
- [x] Keyboard navigation works
- [x] Alt text on all images
- [ ] Screen reader compatible
- [ ] Clear navigation menu
- [ ] Breadcrumbs on complex pages
- [x] Search functionality works

---

## Data & Performance

### Data Management
- [x] Data persists in localStorage
- [x] Data maintains integrity across sessions
- [x] localStorage limitations handled
- [x] All inputs validated before processing
- [ ] XSS attack prevention
- [ ] User content sanitization

### Performance & Compatibility
- [x] Pages load within 3 seconds
- [x] User interactions respond within 1 second
- [x] Works on Chrome (latest 2 versions)
- [x] Works on Firefox (latest 2 versions)
- [x] Works on Safari (latest 2 versions)
- [x] Works on Edge (latest 2 versions)

---

## Error Handling & Support

### Error Management
- [x] Clear, actionable error messages
- [x] Guidance for common issues
- [x] Network errors handled gracefully
- [x] Real-time form validation
- [x] Invalid data prevents submission
- [x] Validation errors highlighted clearly

### Help & Support
- [ ] Contextual help and tooltips
- [ ] FAQ section accessible
- [ ] Contact information available
- [x] User activity logging works
- [x] Error logging and reporting functional

---

## Business Rules Validation

### Scheduling Rules
- [ ] 30-day advance booking limit enforced
- [ ] 24-hour minimum notice enforced
- [ ] Maximum 3 pickups per week enforced
- [ ] Hazardous waste requires approval

### Content & User Rules
- [ ] Email uniqueness enforced
- [ ] Password requirements enforced
- [ ] Inactive account archiving (6 months)
- [x] Admin accounts cannot be deleted
- [x] Inappropriate content prevented
- [x] Content reporting works
- [ ] 1-year content archiving

---

## Test Summary
- **Total Items:** 133
- **Items Tested:** 129
- **Items Passed:** 56
- **Items Failed/Blocked:** 73
- **Completion Rate:** 97%
- **Critical Issues Found:** 45
- **Tested By:** Bug Hunters Team
- **Test Date:** November 10-14, 2025
- **Test Environment:** Chrome, Firefox, Safari, Edge (Desktop, Tablet, Mobile)

---

## Sign-Off

| **Name** | **Role** | **Initial** | **Date** | **Status** |
|----------|----------|---------------|---------|-----------|
| Lilian Kavengi | Test Manager | LK | Nov 16, 2025 | Complete |
| Steven Oyaro | Risk Analyst | SO | Nov 16, 2025 | Complete |
| Rose Kemunto | Test Executor | RK | Nov 16, 2025 | Complete |