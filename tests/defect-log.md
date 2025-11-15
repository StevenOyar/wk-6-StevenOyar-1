# CleanCity Application - Defect Log

**Project:** CleanCity Waste Management System  
**Test Cycle:** Phase 2 Testing  
**Testing Period:** November 14, 2025  
**Tester Team:** Bug Hunters (Lilian Kavengi, Steven Oyaro, Rose Kemunto)  
**Status:** Done  

---

##  Complete Defect Log Table

| Bug ID | Summary | Severity | Priority | Environment | Affected FR(s) | Steps to Reproduce | Expected Result | Actual Result | Attachments | Status | Notes |
|--------|---------|----------|----------|-------------|----------------|-------------------|-----------------|---------------|-------------|--------|-------|
| [BUG-001](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/36) | Password length validation bypassed on registration | Critical | High | Chrome 120.0, Firefox 121.0, Safari 17.0 / Windows 11, macOS 14 / Local dev server | FR-001 | 1. Navigate to registration page<br>2. Fill Name: "John Doe"<br>3. Fill Email: "user1@test.com"<br>4. Fill Password: "12" (2 chars)<br>5. Click Register | Error: "Password must be at least 8 characters long". Form blocked. | Password accepted, user registered, redirected to login. No validation error. | `/screenshots/bug-001-weak-password.png`<br>`/videos/bug-001-bypass.mp4` | Open | Security vulnerability. No client/server validation. Allows weak passwords. Workaround: None. Impact: Accounts vulnerable to brute force. Related: BUG-006. |
| [BUG-003](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/38) | Duplicate email addresses allowed during registration | Critical | High | Chrome 120.0 / Windows 11 / Local dev server | FR-002 | 1. Register user: user@cleancity.com<br>2. Logout<br>3. Register again with same email<br>4. Click Register | Error: "User with this email already exists". Registration blocked. | No error. Email registered twice. Both accounts exist in localStorage. | `/screenshots/bug-003-duplicate.png`<br>`/screenshots/bug-003-localstorage.png` | Open | Data integrity issue. Violates unique constraint. Causes auth conflicts. Workaround: None. Impact: Authentication conflicts, data inconsistency. |
| [BUG-005](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/40) | Authentication bypass - unregistered emails can login | Critical | High | Chrome 120.0, Firefox 121.0, Safari 17.0, Edge 120.0 / Windows 11, macOS 14, Android 13, Local dev | FR-005 | 1. Navigate to login<br>2. Enter unregistered email: invalid@test.com<br>3. Enter any password<br>4. Click Sign In<br>5. Observe result | Error: "Invalid email or password". Access denied. | No error. User logged in. Access to all protected pages granted. | `/screenshots/bug-005-login-bypass.png`<br>`/videos/bug-005-auth-bypass.mp4` | Open | **CRITICAL SECURITY VULNERABILITY**. Auth system broken. No email validation. Allows unauthorized access to entire application. Workaround: None. Impact: Complete security breach. Related: BUG-006. Blocks production. |
| [BUG-006](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/41) | Authentication bypass - any password accepted for login | Critical | High | Chrome 120.0, Firefox 121.0, Safari 17.0, Edge 120.0 / Windows 11, macOS 14 / Local dev | FR-005 | 1. Navigate to login<br>2. Enter valid email: user@cleancity.com<br>3. Enter wrong password: "123"<br>4. Click Sign In | Error: "Invalid email or password". Login denied. | No error. User logged in with wrong password. Access granted. | `/screenshots/bug-006-password-bypass.png`<br>`/videos/bug-006-wrong-password.mp4` | Open | **CRITICAL SECURITY VULNERABILITY**. Password validation missing. Any password works. Auth fundamentally broken. Workaround: None. Impact: Any account accessible. Related: BUG-005, BUG-001. |
| [BUG-007](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/43) | Pickup requests fail to persist to dashboard | Critical | High | Chrome 120.0, Firefox 121.0, Safari 17.0 / Windows 11, macOS 14, Local dev | FR-013 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Fill: Name, Email, Location, Waste Type, Date (3 days ahead)<br>4. Click Submit<br>5. Navigate to Dashboard | Success message. Request saved to localStorage. Displayed in dashboard with "Pending" status. | Success message shows. Dashboard empty. No request displayed. localStorage not updated. Data lost. | `/screenshots/bug-007-empty-dashboard.png`<br>`/screenshots/bug-007-localstorage.png`<br>`/videos/bug-007-data-lost.mp4` | Open | **CRITICAL**. Core feature broken. Data persistence failing. localStorage.setItem() not called or failing. Workaround: None. Impact: Blocks 7 test cases (TC-021 to TC-027). Users cannot track requests. Related: BUG-027, BUG-028. |
| [BUG-010](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/47) | Registration form missing Confirm Password and Phone fields | Major | High | All browsers / All OS / Local dev | FR-001, FR-003 | 1. Navigate to registration page<br>2. Observe form fields<br>3. Compare with FRS requirements | Form displays: Name, Email, Phone, Password, Confirm Password. Success message after registration. | Form only has: Name, Email, Password. Missing: Phone and Confirm Password. No success message. | `/screenshots/bug-010-missing-fields.png`<br>`/docs/requirements-fr-001-003.pdf` | Open | Form incomplete per requirements. Cannot test password matching (TC-004 blocked). Cannot collect phone numbers. Workaround: None. Impact: Incomplete user data. Blocks: TC-001, TC-004. |
| BUG-011a | Name field validation missing on registration | Minor | Low | All browsers / All OS / Local dev | FR-001 | 1. Navigate to registration<br>2. Enter single char "J" in Name<br>3. Fill valid email and password<br>4. Click Register | Error: "Name must be at least 2 characters". Form blocked. | Name accepted. No error. Registration proceeds with single character name. | `/screenshots/bug-011a-single-char.png` | Open | Data quality issue. Minor impact. Workaround: Users self-correct. Impact: Poor data quality. Blocks: TC-005. Fix: Add minLength validation. |
| [BUG-011b](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/49) | Pickup form missing Quantity and Address fields | Major | High | All browsers / All OS / Local dev | FR-012 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Observe form fields<br>4. Compare with requirements | Form includes: Name, Email, Location, Waste Type, Quantity, Address, Date. | Form missing: Quantity field and Address field. | `/screenshots/bug-011b-missing-fields.png` | Open | Form incomplete. Quantity needed for resource planning. Address needed for navigation. Workaround: None. Impact: Incomplete pickup info, operational issues. Blocks: TC-013. |
| [BUG-014a](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/50) | 24-hour advance notice validation not enforced | Major | Medium | All browsers / All OS / Local dev | FR-013 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Fill all fields<br>4. Select today's date<br>5. Click Submit | Error: "Pickup date must be at least 24 hours in advance". Form blocked. | No error. Same-day pickups allowed. Request created successfully with today's date. | `/screenshots/bug-014a-same-day.png`<br>`/videos/bug-014a-validation-bypass.mp4` | Open | Business rule violation. Operational risk for crews. Workaround: Manual checking. Impact: Crew scheduling problems. Related: BUG-033 (duplicate). Blocks: TC-014. |
| [BUG-014b](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/51) | Name validation missing on pickup form | Minor | Low | All browsers / All OS / Local dev | FR-012 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Enter single char "J" in Name<br>4. Fill other fields<br>5. Submit | Error: "Name must be at least 2 characters". Blocked. | Success message. Request scheduled with invalid name. | `/screenshots/bug-014b-pickup-single-char.png` | Open | Data quality issue. Consistent with BUG-011a. Workaround: Users provide proper names. Impact: Minor. Blocks: TC-017. |
| [BUG-015](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/52) | Admin blog post creation feature not implemented | Major | Medium | All browsers / All OS / Local dev | FR-032 | 1. Login as admin<br>2. Navigate to Blog<br>3. Look for "Create Post" button<br>4. Try to create new post | Admin can create blog posts with title, content, publish. | No creation feature. Users/admins cannot create blogs. | `/screenshots/bug-015-no-create.png` | Open | Admin content management missing. Workaround: None. Impact: Cannot add new content. Blocks: TC-044. |
| [BUG-016](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/53) | Admin cannot edit or delete blog posts | Major | Medium | All browsers / All OS / Local dev | FR-033, FR-034 | 1. Login as admin<br>2. Navigate to Blog<br>3. Select existing post<br>4. Look for Edit/Delete buttons | Admin can edit and delete blog posts. | No edit or delete options available for admins. | `/screenshots/bug-016-no-edit-delete.png` | Open | Admin content controls missing. Cannot manage inappropriate content. Workaround: Manual localStorage editing. Impact: Cannot update/remove content. Blocks: TC-045, TC-046. |
| [BUG-017](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/54) | Blog comments do not persist after refresh | Major | Medium | All browsers / All OS / Local dev | FR-035 | 1. Navigate to blog post<br>2. Add comment<br>3. Comment displays<br>4. Refresh page or navigate away<br>5. Return to post | Comment persists and remains visible. | Comment displays initially but disappears on refresh or navigation. | `/screenshots/bug-017-comment-lost.png`<br>`/videos/bug-017-no-persist.mp4` | Open | Data persistence issue. Poor UX. Comments must be stored permanently. Workaround: Don't refresh. Impact: Users lose comments. Blocks: TC-047 (partial pass). |
| [BUG-018](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/55) | Waste reduction tip categorization missing | Minor | Low | All browsers / All OS / Local dev | FR-044 | 1. Login as user<br>2. Navigate to Community<br>3. Create post<br>4. Look for "Tip" tag option | Posts can be tagged as tips with categories. Tips have special badge. | Tip feature not available. Cannot categorize posts as tips. | `/screenshots/bug-018-no-tip-feature.png` | Open | Community feature missing. Reduces content organization. Workaround: Use hashtags in text. Impact: Tips not highlighted. Blocks: TC-058. |
| [BUG-019](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/56) | Profile achievements and activity history not updating | Major | Medium | All browsers / All OS / Local dev | FR-046 | 1. Complete activities (pickups, posts)<br>2. Navigate to Profile<br>3. Check achievements section<br>4. Check activity section | Achievements displayed. Activity history shown chronologically. | No achievements displayed. Activity not updated after creating pickup or posts. | `/screenshots/bug-019-no-achievements.png`<br>`/screenshots/bug-019-no-activity.png` | Open | Profile functionality incomplete. Users cannot see progress. Workaround: None. Impact: No visibility of contributions. Blocks: TC-061, TC-062. Related: BUG-031a. |
| [BUG-020](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/57) | Profile picture upload not functional | Minor | Low | All browsers / All OS / Local dev | FR-047 | 1. Login as user<br>2. Navigate to Profile<br>3. Look for profile picture<br>4. Try to click/edit<br>5. Look for upload button | Profile picture with edit icon. Click opens file dialog. Can upload and update. | Picture appears permanent. No upload or edit option. Cannot change picture. | `/screenshots/bug-020-no-upload.png` | Open | Personalization feature missing. Minor UX issue. Workaround: Use default avatar. Impact: Cannot personalize profile. Blocks: TC-063. |
| [BUG-021](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/58) | User statistics not displayed on profile | Major | Medium | All browsers / All OS / Local dev | FR-048 | 1. Complete activities<br>2. Navigate to Profile<br>3. Check statistics section | Statistics show: total pickups, points earned, environmental impact. | No user statistics displayed. Features not updated with activity. | `/screenshots/bug-021-no-stats.png` | Open | Profile analytics missing. Users cannot track contributions. Workaround: None. Impact: No progress visibility. Blocks: TC-064. |
| [BUG-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) | Social features not implemented (follow, feed, share, challenges) | Major | Medium | All browsers / All OS / Local dev | FR-049, FR-050, FR-051, FR-052 | 1. Navigate to user profile<br>2. Look for Follow button<br>3. Check for news feed<br>4. Look for share/challenges features | Can follow users, view feed, share achievements, join challenges. | No social features available. Cannot follow, share, or participate in challenges. | `/screenshots/bug-022-no-social.png` | Open | Major community features missing. Reduces social aspect. Workaround: None. Impact: Limited engagement. Blocks: TC-065, TC-066, TC-067, TC-068 (4 test cases). |
| [BUG-023](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/60) | Admin panel does not display pickup requests | Critical | High | All browsers / All OS / Local dev | FR-053 | 1. Login as admin (admin@cleancity.com/admin123)<br>2. Navigate to Admin Panel<br>3. Click Pickup Requests<br>4. Observe table | All pickup requests from all users displayed with details and status. | Admin panel requests table empty. No user requests visible. Panel not updating. | `/screenshots/bug-023-admin-empty.png`<br>`/videos/bug-023-no-requests.mp4` | Open | **CRITICAL**. Admin cannot perform core function. Not reading from localStorage or filtering incorrectly. Workaround: None. Impact: Admin workflow blocked. Blocks: TC-069. Related: BUG-024, BUG-025. |
| [BUG-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) | Admin request management features missing | Critical | High | All browsers / All OS / Local dev | FR-054, FR-055, FR-056 | 1. Login as admin<br>2. Navigate to Admin Panel<br>3. Look for: Approve, Reject, Edit, Assign date, Filter, Search | Admin can approve, reject, modify, assign dates, filter by status, search requests. | All features missing: No approve/reject, no edit, no date assignment, no filters, no search. | `/screenshots/bug-024-missing-features.png`<br>`/screenshots/bug-024-expected.png` | Open | **CRITICAL**. Core admin workflow blocked. Cannot manage pickup lifecycle. Workaround: None. Impact: Cannot confirm pickups, schedule crews, process requests. Blocks: TC-070, TC-071, TC-072, TC-073, TC-074, TC-075 (6 test cases). |
| [BUG-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) | Admin user management and reporting missing | Critical | High | All browsers / All OS / Local dev | FR-057, FR-058, FR-059, FR-060 | 1. Login as admin<br>2. Navigate to Admin Panel<br>3. Look for User Management section<br>4. Look for Reports section<br>5. Try user/report actions | User Management section with list. Can change roles, suspend, delete accounts. Can generate reports. | No User Management section. No Reports section. Cannot view/manage users or generate reports. | `/screenshots/bug-025-admin-sections.png`<br>`/screenshots/bug-025-missing.png` | Open | **CRITICAL**. Cannot manage users or generate reports. Major admin gap. Workaround: Manual localStorage editing (impractical). Impact: Cannot manage accounts, track usage. Security risk: Cannot suspend malicious users. Blocks: TC-076, TC-077, TC-078, TC-079, TC-080 (5 test cases). |
| [BUG-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) | Content moderation features not implemented | Major | Medium | All browsers / All OS / Local dev | FR-061, FR-062, FR-063, FR-064 | 1. Login as admin<br>2. Look for Content Moderation section<br>3. Try to: view flagged posts, moderate, delete content, create announcements<br>4. Login as user, try to flag content | Admin can moderate posts, delete inappropriate content, handle flags, create announcements. Users can flag content. | No Content Moderation section. Cannot view flagged posts, moderate, delete content, or create announcements. Users cannot flag. | `/screenshots/bug-026-no-moderation.png` | Open | Platform vulnerable to inappropriate content. Cannot manage community safety. Workaround: Manual localStorage editing (impractical). Impact: Content safety risk. Security concern. Blocks: TC-081, TC-082, TC-083, TC-084 (4 test cases). |
| [BUG-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64) | Pickup data persistence failure blocks duplicate detection | Critical | High | All browsers / All OS / Local dev | FR-015, FR-012 | 1. Login as user<br>2. Schedule pickup for tomorrow<br>3. Check dashboard<br>4. Try to schedule 2nd pickup same date | First pickup visible. Second attempt shows error: "You already have a pickup scheduled for this date". Hazardous waste marked "Pending Approval". | Cannot test - data not saved in dashboard (BUG-007). First pickup not visible. Cannot verify duplicate detection or hazardous workflow. | `/screenshots/bug-027-cannot-test.png` | Open | Blocked by BUG-007 and BUG-028. Core data persistence issue. Workaround: None. Impact: Cannot test 3 test cases. Blocks: TC-018, TC-019, TC-020. Related: BUG-007, BUG-028. |
| [BUG-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) | Dashboard request table remains empty - data not displayed | Critical | High | All browsers / All OS / Local dev | FR-016, FR-017, FR-018, FR-019, FR-020, FR-022 | 1. Login to application<br>2. Schedule pickup requests<br>3. Navigate to Dashboard<br>4. Check "My Requests" section<br>5. Observe table | All user's requests displayed with: Request ID, Date, Location, Waste Type, Status. Action buttons: View, Cancel, Edit. Status badges color-coded. | Dashboard table completely empty. Shows "0" for all counts. No data displayed even if localStorage has data. Cannot view/cancel/modify requests. | `/screenshots/bug-028-empty-table.png`<br>`/screenshots/bug-028-localstorage-data.png`<br>`/videos/bug-028-not-updating.mp4` | Open | **CRITICAL**. Users cannot manage requests. Data may exist in localStorage but not rendered. Component not reading correctly. Workaround: None. Impact: Cannot cancel, view status, add feedback. Blocks: TC-021, TC-022, TC-023, TC-024, TC-025, TC-026, TC-027 (7 test cases). Related: BUG-007, BUG-027. |
| [BUG-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) | Dashboard missing environmental metrics and features | Major | Medium | All browsers / All OS / Local dev | FR-023, FR-024 | 1. Login with completed pickups<br>2. Navigate to Dashboard<br>3. Look for environmental impact section<br>4. Look for achievement badges<br>5. Look for quick action buttons | Dashboard shows: recent/upcoming pickups, environmental impact (waste diverted, CO2, trees), achievement badges, quick action buttons. | Dashboard shows 0 pickups. Missing: environmental impacts section, achievements section, quick action buttons. | `/screenshots/bug-029-missing-features.png`<br>`/screenshots/bug-029-expected.png` | Open | Multiple dashboard features not implemented. Poor UX. Users cannot see environmental contribution. Workaround: None. Impact: Reduced engagement, missing gamification. Blocks: TC-028, TC-029, TC-030, TC-031, TC-032 (5 test cases). Related: BUG-030, BUG-031a. |
| [BUG-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) | Analytics and reporting features not implemented | Major | Medium | All browsers / All OS / Local dev | FR-025, FR-026, FR-027, FR-028 | 1. Login as user<br>2. Navigate to Dashboard<br>3. Look for: visual charts, leaderboard, trends (monthly/yearly), CSV export | Visual charts for waste data. Community leaderboard populated. Monthly/yearly trend graphs. CSV export button. | No charts/analytics. Leaderboard exists but empty. No trends section. No export functionality. | `/screenshots/bug-030-no-analytics.png`<br>`/screenshots/bug-030-empty-leaderboard.png` | Open | Analytics module incomplete. Reduces app value. Users cannot track progress over time. Workaround: None. Impact: Missing insights, no competitive engagement. Blocks: TC-033, TC-034, TC-035, TC-036, TC-037 (5 test cases). Fix: Implement Chart.js, add trend calculation, add CSV export. |
| [BUG-031a](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) | Gamification system not implemented (badges, points, levels) | Major | Medium | All browsers / All OS / Local dev | FR-029, FR-030 | 1. Register new account<br>2. Schedule first pickup<br>3. Check for "First Pickup" badge<br>4. Complete activities<br>5. Check profile for points/level | Badges awarded: First Pickup, 10 Pickups, Perfect Recycling. Points calculated. Level progression system. Achievements in profile. | No badge system. No points calculation. No level progression. Gamification completely missing. | `/screenshots/bug-031a-no-badges.png`<br>`/screenshots/bug-031a-no-points.png` | Open | Major engagement feature missing. Reduces user motivation. Workaround: None. Impact: Lower retention, no competitive element. Blocks: TC-038, TC-039, TC-040, TC-041, TC-042 (5 test cases). Related: BUG-019, BUG-029. |
| [BUG-031b](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) | Notification system completely non-functional | Major | Medium | All browsers / All OS / Local dev | FR-066, FR-067, FR-068 | 1. Login as user<br>2. Schedule pickup<br>3. Have admin confirm<br>4. Check notification bell<br>5. Have user like your post<br>6. Try to mark as read<br>7. Try to view history | Notification bell shows unread count. Notifications for: pickup confirmation, blog posts, interactions, achievements. Can mark as read. History accessible. | Bell visible with no count. No notifications triggered. Admin page not working. Community interactions don't trigger. Cannot mark as read. No history view. | `/screenshots/bug-031b-no-notifications.png`<br>`/screenshots/bug-031b-bell-icon.png` | Open | Full notification system not implemented. Users miss important updates. Workaround: Manual page checking. Impact: Poor communication, unaware of status changes. Blocks: TC-086, TC-087, TC-088, TC-089, TC-090, TC-091 (6 test cases). Related: BUG-024, BUG-031a. |
| [BUG-032](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/75) | 30-day advance booking limit not enforced | Major | Medium | All browsers / All OS / Local dev | BR-001 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Select date 31+ days from today<br>4. Fill fields<br>5. Click Submit | Error: "Cannot schedule more than 30 days in advance". Form blocked. User prompted for earlier date. | No error. Request submitted for dates 31+ days ahead. No business rule enforcement. | `/screenshots/bug-032-far-future-date.png` | Open | Business rule violation. Resource planning issues. May cause long-term scheduling conflicts. Workaround: Manual checking. Impact: Operational planning difficulties. Blocks: TC-125. Fix: Add validation: selectedDate <= currentDate + 30 days. |
| [BUG-033](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/76) | 24-hour minimum notice business rule not enforced | Major | Medium | All browsers / All OS / Local dev | BR-001 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Select today's date<br>4. Fill form<br>5. Submit | Error: "Minimum 24-hour notice required". Submission blocked. | Request submitted same day. No validation error. Business rule not enforced. | `/screenshots/bug-033-same-day-allowed.png` | Open | Business rule violation. Duplicate of BUG-014a. Operational issues. Workaround: None. Impact: Crew scheduling problems. Blocks: TC-126. Related: BUG-014a. |
| [BUG-034](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/77) | Maximum 3 pickups per week limit not enforced | Major | Medium | All browsers / All OS / Local dev | BR-001 | 1. Login as user<br>2. Schedule 3 pickups in current week<br>3. Attempt 4th pickup same week<br>4. Submit | Error: "Maximum 3 pickups per week reached". 4th pickup blocked. | More than 4 pickups can be created in same week. No validation. Unlimited pickups allowed. | `/screenshots/bug-034-unlimited-pickups.png` | Open | Business rule violation. Resource capacity management broken. Workaround: None. Impact: Overload risk for crews. Blocks: TC-127. Blocked by: BUG-028 (cannot see pickups to test). |
| [BUG-035](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/78) | Hazardous waste approval requirement not implemented | Major | Medium | All browsers / All OS / Local dev | BR-001 | 1. Login as user<br>2. Navigate to Schedule Pickup<br>3. Select "Hazardous" waste type<br>4. Fill fields<br>5. Submit<br>6. Check status<br>7. Login as admin to verify | Status shows "Pending Approval" (not "Pending"). Admin notified. Admin must approve. Special handling flagged. | Cannot verify status (BUG-028 blocks dashboard). Admin panel not working (BUG-024). Cannot test approval workflow. | `/screenshots/bug-035-cannot-verify.png` | Open | Business rule enforcement unclear. Safety risk if not flagged. Workaround: None. Impact: Safety concern for hazardous materials. Blocks: TC-128. Blocked by: BUG-024, BUG-028. |
| [BUG-036](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/80) | Desktop layout issues across all browsers | Major | Medium | Chrome 120.0, Firefox 121.0, Safari 17.0, Edge 120.0 / 1920x1080 / Windows 11, macOS 14 / Local dev | FR-069 | 1. Set browser to 1920x1080<br>2. Navigate through all pages<br>3. Observe layout, spacing, alignment<br>4. Test features<br>5. Check visual consistency | All features display correctly. Proper spacing and alignment. Professional appearance. Consistent layout. No overlapping. | Layout issues on all browsers. Inconsistent spacing. Some elements misaligned. Visual appearance issues. Not professionally polished. | `/screenshots/bug-036-desktop-chrome.png`<br>`/screenshots/bug-036-firefox.png`<br>`/screenshots/bug-036-safari.png` | Open | UI/UX polish needed. Professional appearance compromised. Workaround: None. Impact: Poor first impression, unprofessional. Blocks: TC-092. Related: BUG-037, BUG-038. |
| [BUG-037](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/81) | Tablet responsive design broken - headers overlap | Major | High | Chrome 120.0, Safari 17.0 / iPad Air, iPad Pro, Android tablets / 768px-1024px / WiFi | FR-069, FR-070 | 1. Open on tablet or resize to 768px<br>2. Navigate through pages<br>3. Try to fill forms<br>4. Observe header behavior<br>5. Test scheduling | Layout adapts to tablet. Headers properly sized, no overlap. Navigation accessible. Forms properly sized. Touch-friendly. | Layout not adaptive. Element headers overlap. Headers cover significant screen space. Navigation difficult. Forms extend beyond viewport. User faces difficulty navigating. | `/screenshots/bug-037-tablet-overlap-ipad.png`<br>`/screenshots/bug-037-android.png`<br>`/videos/bug-037-unusable.mp4` | Open | Tablet users significantly affected. CSS media queries missing/incorrect. Workaround: Use desktop mode. Impact: Poor tablet UX, 20-30% users affected. Blocks: TC-093, TC-095. Related: BUG-038, BUG-036. |
| [BUG-038](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/82) | Mobile responsiveness completely broken - no hamburger menu | Critical | High | Chrome Mobile 120.0, Safari, Firefox Mobile 121.0 / iPhone 13 Pro, Samsung Galaxy S23, iPad Air / 320px-768px / WiFi, 4G | FR-069, FR-070 | 1. Open on mobile or resize to 375px<br>2. Observe navigation<br>3. Try to access pages<br>4. Try to fill forms<br>5. Navigate through pages | Hamburger menu (☰) in top-right. Click opens slide-out menu. All links accessible. Layout responsive. Forms properly sized. Touch-friendly (44x44px). No horizontal scroll. | No hamburger menu. Full desktop nav displayed (overlaps). Headers cover >50% screen. Nav links overlap, unusable. Forms extend beyond viewport. Horizontal scrolling required. Touch targets too small. Completely unusable. | `/screenshots/bug-038-mobile-iphone.png`<br>`/screenshots/bug-038-android.png`<br>`/videos/bug-038-unusable.mp4`<br>`/screenshots/bug-038-expected-vs-actual.png` | Open | **CRITICAL**. 50%+ users on mobile. Mobile-first design not implemented. No responsive CSS. Workaround: Use desktop/tablet only. Impact: Excludes mobile users completely. Business impact: Lost users, negative reviews. Blocks: TC-094, TC-095. Related: BUG-037, BUG-036. |
| [BUG-039](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/83) | WCAG 2.1 AA compliance failures - 34 violations | Major | High | Chrome 120.0 with axe DevTools v4.8.0 / Windows 11 / Local dev | FR-071 | 1. Install axe DevTools<br>2. Navigate to home page<br>3. Run axe scan<br>4. Navigate to all pages<br>5. Run scans on each<br>6. Review violations | Zero critical WCAG 2.1 AA violations. Zero serious violations. Application accessible to users with disabilities. | 1 critical violation. 34 total WCAG 2.1 AA violations. Issues: missing form labels, insufficient color contrast, missing alt text, improper heading hierarchy, missing ARIA, non-keyboard accessible elements. | `/screenshots/bug-039-axe-summary.png`<br>`/screenshots/bug-039-violations-list.png`<br>`/videos/bug-039-accessibility-scan.mp4`<br>`/reports/bug-039-axe-full-report.html` | Open | Accessibility compliance failure. Excludes users with disabilities. Legal risk (ADA, Section 508). Workaround: None for affected users. Impact: Discriminates against disabled users, legal exposure. Blocks: TC-096. Fix required: Address all critical and serious violations before production. |
| [BUG-040](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/84) | Screen reader cannot announce dropdown elements | Major | Medium | Chrome 120.0, Firefox 121.0 / NVDA 2023.3, JAWS 2024 / Windows 11 / Local dev | FR-074 | 1. Enable screen reader (NVDA/JAWS)<br>2. Navigate to Blog section<br>3. Navigate to tag dropdown<br>4. Use arrow keys<br>5. Listen to announcements | Screen reader announces dropdown. Options read aloud when navigating. Selected option announced. Dropdown accessible. Proper ARIA labels. | Dropdown for blog tags not announced. Screen reader silent when focused. Options not read aloud. Dropdown inaccessible to screen reader users. Missing ARIA attributes. | `/screenshots/bug-040-dropdown-no-aria.png`<br>`/screenshots/bug-040-missing-attributes.png`<br>`/videos/bug-040-screen-reader-silent.mp4` | Open | Accessibility issue. Screen reader users cannot use blog tags. Workaround: None for screen reader users. Impact: Blog categorization inaccessible to blind users. Blocks: TC-099. Fix: Add ARIA labels: aria-label, role="combobox". |
| [BUG-041](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/85) | Navigation menu and breadcrumbs missing | Critical | High | All browsers / All OS / Local dev | FR-075, FR-076 | 1. Open application<br>2. Login<br>3. Look for navigation menu at top/side<br>4. Navigate to Admin/nested pages<br>5. Look for breadcrumb trail | Nav menu with links: Home, Dashboard, Schedule Pickup, Community, Awareness, Profile, Admin. Current page highlighted. Breadcrumbs on complex pages: Home > Section > Page. Breadcrumbs clickable. | No navigation menu anywhere. Cannot access pages without typing URL. No breadcrumbs on any pages. Navigation completely missing. Users must use browser back or type URLs. | `/screenshots/bug-041-no-navigation.png`<br>`/screenshots/bug-041-no-breadcrumbs.png` | Open | **CRITICAL**. Basic navigation missing. Major usability issue. Users cannot navigate properly. Workaround: Type URLs manually or use browser navigation. Impact: Poor UX, cannot find features. Blocks: TC-100, TC-101. Related: BUG-038 (mobile hamburger also needed). |
| [BUG-042](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/86) | XSS attack prevention not implemented | Critical | High | Chrome 120.0, Firefox 121.0 / Windows 11, macOS 14 / Local dev | FR-082 | 1. Navigate to registration<br>2. In Name field enter: `<script>alert('XSS')</script>`<br>3. Fill valid email and password<br>4. Register<br>5. Navigate to profile<br>6. Observe rendering | Script tags escaped/sanitized. Name displayed as plain text. No JavaScript alert executed. Content rendered safely. | No alert popup (minor positive). However, script tags NOT escaped/sanitized. HTML/JS stored as-is in localStorage. Potential for script execution in different contexts. | `/screenshots/bug-042-xss-vulnerability.png`<br>`/screenshots/bug-042-localstorage-unescaped.png` | Open | **CRITICAL SECURITY VULNERABILITY**. Application vulnerable to XSS attacks. No input sanitization. Malicious scripts can be injected in: name, comments, posts, addresses. Workaround: None - requires code fix. Impact: All users at risk, data theft, session hijacking possible. Fix required before: Any production deployment. Recommended: Implement DOMPurify library. |
| [BUG-043](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/87) | SQL injection prevention not implemented | Critical | High | Chrome 120.0 / Windows 11 / Local dev | FR-082 | 1. Navigate to login<br>2. In Email: `' OR '1'='1`<br>3. In Password: `' OR '1'='1`<br>4. Click Sign In<br>5. Observe result | SQL injection payload treated as literal text. Login fails with error. No unauthorized access. | Unauthorized access granted. User logged in without valid credentials. SQL injection payload bypasses authentication. Access to protected pages obtained. | `/screenshots/bug-043-sql-injection.png`<br>`/videos/bug-043-sql-injection-demo.mp4` | Open | **CRITICAL SECURITY VULNERABILITY**. Application vulnerable to SQL injection. No input validation or parameterized queries. Queries likely using string concatenation. Workaround: None. Impact: Complete database compromise possible, unauthorized access. Related: BUG-005, BUG-006 (auth issues). Note: Even with localStorage, SQL injection patterns work due to improper validation. |
| [BUG-044](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/88) | User content sanitization missing | Major | Medium | All browsers / All OS / Local dev | FR-083 | 1. Login as user<br>2. Navigate to Community<br>3. Create post with HTML: `<strong>Bold text</strong>`<br>4. Submit post<br>5. View rendered content<br>6. Check DevTools | HTML tags escaped or sanitized. Content displayed safely as text. Only safe markdown subset allowed. | HTML does not escape. Content not sanitized. HTML tags stored and rendered as-is. Potential for malicious content injection. | `/screenshots/bug-044-html-not-escaped.png`<br>`/screenshots/bug-044-raw-html.png` | Open | Security issue. Could allow malicious styling, iframes, etc. Workaround: Avoid using HTML in posts. Impact: Security vulnerability, content safety risk. Blocks: TC-111. Related: BUG-042 (XSS). Fix: Implement DOMPurify or escape all HTML. |
| [BUG-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) | Help system features not implemented | Major | Medium | All browsers / All OS / Local dev | FR-093, FR-094, FR-095 | 1. Navigate through application<br>2. Look for help icons (?)<br>3. Hover over form fields<br>4. Navigate to Help/FAQ section<br>5. Look for Contact information | Contextual help tooltips on hover. FAQ section with common questions. Contact info displayed: support email, phone/hotline, website/social media. Help accessible from all pages. | No tooltips or help icons. No FAQ section. No contact information. Help system completely missing. Users cannot get assistance. | `/screenshots/bug-045-no-help-system.png` | Open | Support features missing. Poor UX for confused users. Workaround: External documentation (if available). Impact: Users cannot get help, increased frustration. Blocks: TC-129, TC-130, TC-131. Fix: Add tooltip component, create FAQ page, add contact section. |

---

##  Summary Statistics

### Defects by Severity
| Severity | Count | Percentage |
|----------|-------|------------|
|  Critical | 11 | 24.4% |
|  Major | 30 | 66.7% |
|  Minor | 4 | 8.9% |
| **Total** | **45** | **100%** |

### Defects by Priority
| Priority | Count | Percentage |
|----------|-------|------------|
| High | 23 | 51.1% |
| Medium | 21 | 46.7% |
| Low | 1 | 2.2% |
| **Total** | **45** | **100%** |

### Defects by Module
| Module | Critical | Major | Minor | Total |
|--------|----------|-------|-------|-------|
| Authentication | 3 | 2 | 1 | 6 |
| Waste Management | 2 | 3 | 1 | 6 |
| Dashboard & Analytics | 1 | 3 | 0 | 4 |
| Admin Functions | 3 | 1 | 0 | 4 |
| Community Features | 0 | 5 | 1 | 6 |
| User Interface | 1 | 2 | 0 | 3 |
| Security | 2 | 1 | 0 | 3 |
| Business Rules | 0 | 4 | 0 | 4 |
| Accessibility | 0 | 2 | 0 | 2 |
| Navigation | 1 | 0 | 0 | 1 |
| Support | 0 | 1 | 0 | 1 |
| Gamification/Notifications | 0 | 2 | 0 | 2 |
| Content Management | 0 | 3 | 0 | 3 |

### Defects by Status
| Status | Count | Percentage |
|--------|-------|------------|
| Open | 45 | 100% |
| In Progress | 0 | 0% |
| Fixed | 0 | 0% |
| Closed | 0 | 0% |

---

##  Critical Blockers for Production

| Priority | Bug IDs | Issue | Impact |
|----------|---------|-------|--------|
| **P0** | BUG-005, BUG-006 | Authentication completely bypassed | Complete security breach - any user can access any account |
| **P0** | BUG-042, BUG-043 | XSS and SQL injection vulnerabilities | Application open to attacks, data theft, malicious code injection |
| **P0** | BUG-007, BUG-028, BUG-027 | Data persistence failure | Core feature broken - users cannot track pickup requests |
| **P0** | BUG-038 | Mobile completely unusable | 50%+ of users cannot use application |
| **P0** | BUG-023, BUG-024, BUG-025 | Admin panel non-functional | Admins cannot manage application operations |
| **P0** | BUG-041 | No navigation menu | Users cannot navigate application |

**Status:** Application NOT production-ready. All P0 bugs must be fixed before any deployment.

---

##  Test Case Impact

### Test Cases Blocked by Bugs
| Bug ID | Blocks Test Cases | Count | Impact |
|--------|------------------|-------|--------|
| BUG-028 | TC-021 to TC-027 | 7 | Cannot test request management features |
| BUG-031a/b | TC-038 to TC-042, TC-086 to TC-091 | 11 | Cannot test gamification or notifications |
| BUG-024 | TC-070 to TC-075 | 6 | Cannot test admin request management |
| BUG-025 | TC-076 to TC-080 | 5 | Cannot test admin user management |
| BUG-027 | TC-018, TC-019, TC-020 | 3 | Cannot test duplicate detection |
| BUG-026 | TC-081 to TC-084 | 4 | Cannot test content moderation |
| BUG-022 | TC-065 to TC-068 | 4 | Cannot test social features |
| BUG-029 | TC-028 to TC-032 | 5 | Cannot test dashboard features |
| BUG-030 | TC-033 to TC-037 | 5 | Cannot test analytics |

**Total Test Cases Blocked:** 49 out of 129 (38.0%)

### Test Execution Summary
| Status | Count | Percentage |
|--------|-------|------------|
| Pass | 38 | 29.5% |
| Fail | 39 | 30.2% |
| Blocked | 49 | 38.0% |
| Partial | 3 | 2.3% |
| **Total** | **129** | **100%** |

---

##  Recommended Fix Timeline

### Sprint 1 (Week 1-2) - CRITICAL SECURITY & CORE FEATURES
**Must Fix Before Any Deployment**
-  BUG-005, BUG-006 - Fix authentication validation
-  BUG-042, BUG-043 - Implement XSS and SQL injection prevention
-  BUG-007, BUG-028, BUG-027 - Fix data persistence layer
-  BUG-041 - Add navigation menu and breadcrumbs

**Estimated Effort:** 2 weeks | **Priority:** P0 | **Blockers:** None

---

### Sprint 2 (Week 3-4) - HIGH PRIORITY UX & ADMIN
**Required for Usable Application**
-  BUG-038, BUG-037, BUG-036 - Fix responsive design (mobile, tablet, desktop)
-  BUG-023, BUG-024, BUG-025 - Implement admin panel functionality
-  BUG-039 - Fix accessibility violations (34 WCAG issues)
-  BUG-001, BUG-003, BUG-010 - Fix authentication form validation

**Estimated Effort:** 2 weeks | **Priority:** P1 | **Depends on:** Sprint 1 completion

---

### Sprint 3 (Week 5-6) - BUSINESS RULES & KEY FEATURES
**Required for Business Operations**
- BUG-032, BUG-033, BUG-034, BUG-035 - Enforce business rules (pickup limits, approval)
-  BUG-029, BUG-030 - Implement dashboard analytics and reporting
-  BUG-026 - Implement content moderation features
-  BUG-011b - Add missing pickup form fields (Quantity, Address)

**Estimated Effort:** 2 weeks | **Priority:** P1 | **Depends on:** Sprint 2 completion

---

### Sprint 4+ (Week 7+) - ENGAGEMENT & ENHANCEMENT FEATURES
**Nice to Have for Launch**
-  BUG-031a, BUG-031b - Implement gamification and notifications (11 test cases)
-  BUG-022 - Implement social features (follow, feed, share, challenges)
-  BUG-015, BUG-016, BUG-017 - Complete blog management features
-  BUG-019, BUG-021 - Complete profile achievements and statistics
-  BUG-040, BUG-044, BUG-045 - Remaining accessibility and support features
- BUG-011a, BUG-014b, BUG-018, BUG-020 - Minor validation and features

**Estimated Effort:** 3-4 weeks | **Priority:** P2-P3 | **Can be deferred**

---

##  Testing Notes

**Environment Details:**
- **Testing Period:** November 14, 2025
- **Testing Phase:** Phase 2 - Complete
- **Test Cases Executed:** 129
- **Browsers Tested:** Chrome 120.0, Firefox 121.0, Safari 17.0, Edge 120.0
- **Devices Tested:** Desktop (1920x1080), Tablet (768px-1024px), Mobile (320px-767px)
- **Screen Readers:** NVDA 2023.3, JAWS 2024
- **Accessibility Tool:** axe DevTools v4.8.0
- **Network:** Local development server

**Severity Definitions:**
- **Critical:** Security vulnerability, authentication bypass, core feature completely broken, data loss, application unusable
- **Major:** Important feature not working, significant functionality missing, poor user experience, business operations impacted
- **Minor:** Data quality issue, cosmetic issue, minor feature missing, minimal operational impact

**Priority Definitions:**
- **High (P0-P1):** Must fix before production, blocking multiple features, security risk, affects >50% users
- **Medium (P2):** Should fix soon, affects user experience, missing engagement features
- **Low (P3):** Nice to have, minimal impact, cosmetic improvements


**Prepared By:** Bug Hunters Team  
**Team Members:**
- Lilian Kavengi
- Steven Oyaro
- Rose Kemunto

**Report Date:** November 14, 2025  
**Status:** Phase 2 Testing Complete  
**Next Review:** After Sprint 1 P0 fixes completed


---

*End of Defect Log - All 45 bugs documented with complete details for  action*