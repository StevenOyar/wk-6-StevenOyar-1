# Bug Hunters - Test Cases 

---
| **Field** | **Details** |
|-----------|------------|
| **Document Phase** | Phase 2|
| **Document Date** | November 14, 2025 |
| **Project Name** | CleanCity QA Testing Project |
| **Team Name** | Bug Hunters |
| **Prepared By** | All Team membes |
| **Team Members** | Lilian Kavengi, Steven Oyaro, Rose Kemunto |
| **Status** | Phase 2 - Done |

---


## Authentication & User Management

### Registration & Login Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-001 | FR-001 | Valid user registration with all required fields | Browser opened, on registration page | Name: "John Doe", Email: "user1@test.com", Password: "TestPass123", Confirm: "TestPass123" | 1. Navigate to registration page<br>2. Enter valid name<br>3. Enter valid email<br>4. Enter valid password<br>5. Confirm password<br>6. Click Register | User account created successfully, redirected to login page with success message | Form only displays: Name, Email, and Password fields. Missing Confirm Password and Phone fields , no success message| Fail |[Bug-010](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/47) |
| TC-002 | FR-002 | Registration with invalid email format | Browser opened, on registration page | Name: "John Doe", Email: "invalidemail", Password: "TestPass123" | 1. Navigate to registration page<br>2. Enter name<br>3. Enter invalid email<br>4. Enter password<br>5. Click Register | Error message displayed: "Please enter a valid email address" | error message please enter a valid email pop up | Pass | N/A |
| TC-003 | FR-001 | Registration with password less than 8 characters | Browser opened, on registration page | Name: "John Doe", Email: "user1@test.com", Password: "2" | 1. Navigate to registration page<br>2. Enter name<br>3. Enter email<br>4. Enter short password<br>5. Click Register | Error message displayed: "Password must be at least 8 characters long" | Password accepted, user id redirected to login| Fail | [Bug-001](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/36) |
| TC-004 | FR-001 | Registration with mismatched passwords | Browser opened, on registration page | Name: "John Doe", Email: "user1@test.com", Password: "TestPass123", Confirm: "Pass654321" | 1. Navigate to registration page<br>2. Enter valid data<br>3. Enter different password in confirm field<br>4. Click Register | Error message displayed: "Passwords do not match" | cannot do this the confirm password is not available | Blocked | [Bug-001](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/47) |
| TC-005 | FR-001 | Registration with name less than 2 characters | Browser opened, on registration page | Name: "J", Email: "user1@test.com", Password: "TestPass123" | 1. Navigate to registration page<br>2. Enter single character name<br>3. Enter valid email and password<br>4. Click Register | Error message displayed: "Name must be at least 2 characters" |name is accepted , no error message | Fail | Bug-011 |
| TC-006 | FR-002 | Registration with duplicate email | Browser opened, existing user in system | Email: "user@cleancity.com" (existing), Password: "TestPass123" | 1. Navigate to registration page<br>2. Enter existing email<br>3. Enter password<br>4. Click Register | Error message displayed: "User with this email already exists" | Email can be registered twice | Fail |[Bug-003](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/38) |
| TC-007 | FR-004 | Login with valid credentials | Browser opened, user registered | Email: "user@cleancity.com", Password: "password123" | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter valid password<br>4. Click Sign In | User logged in successfully, redirected to dashboard  or profile| User logged in and redirected to the profile | Pass | N/A |
| TC-008 | FR-005 | Login with unregistered email | Browser opened, on login page | Email: "invalid@test.com", Password: "password123" | 1. Navigate to login page<br>2. Enter non-existent email<br>3. Enter any password<br>4. Click Sign In | Error message displayed: "Invalid email or password" | User can be able to login and access protected pages | Fail |[Bug-005](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/40) |
| TC-009 | FR-005 | Login with invalid password | Browser opened, on login page | Email: "user@cleancity.com", Password: "123" | 1. Navigate to login page<br>2. Enter valid email<br>3. Enter wrong password<br>4. Click Sign In | Error message displayed: "Invalid email or password" | No error message, user can login and access protected pages| Fail |[Bug-006](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/41) |
| TC-010 | FR-006 | Session persistence after login | User logged in | Valid user credentials | 1. Login to application<br>2. Close browser tab<br>3. Reopen application URL | User remains logged in, session maintained | User remains logged in | Pass | N/A |
| TC-011 | FR-008 | User logout functionality | User logged in | N/A | 1. Login to application<br>2. Click Logout button | User logged out, session cleared, redirected to login page | User is logged out, session redirects the user to the login page | Pass | N/A |
| TC-012 | FR-010 | User role assignment on registration | None | Valid registration data | 1. Complete registration<br>2. Check user role in localStorage | User assigned "User" role by default | user is assigned the "user" role in json local storage after closing and opening | Pass   | N/A |

---

## Waste Management

### Pickup Scheduling Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-013 | FR-012 | Schedule pickup with all required fields | User logged in, on Schedule Pickup page | Name: "John Doe",Email: "user@cleancity.com", Location: "Nairobi", WasteType: "General",Quantinty: "medium" ,Date: 3 days after today, address:"autofilled" | 1. Navigate to Schedule Pickup page<br>2. Fill all required fields<br>3. Select future date<br>4. Click Submit Request | Pickup request created successfully with "Pending" status |the form lacks some fields like quantity and address | Fail |[Bug-011](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/49) |
| TC-014 | FR-013 | Schedule pickup with the provided fields | User logged in | Name: "John Doe",Email: "user@cleancity.com" Location: "Nairobi", WasteType: "General", Date: Today | 1. Navigate to Schedule Pickup page<br>2. Fill all fields<br>3. Select today's date<br>4. Click Submit Request | Pickup request created successfully with "Pending" status | Pickup created sucessesful message but no request is c reated in the dashboard with pending status | Fail | [Bug-007](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/43) |
| TC-014 | FR-013 | Schedule pickup with date less than 24 hours | User logged in | Name: "John Doe",Email: "user@cleancity.com" Location: "Nairobi", WasteType: "General", Date: Today | 1. Navigate to Schedule Pickup page<br>2. Fill all fields<br>3. Select today's date<br>4. Click Submit Request | Error message: "Pickup date must be at least 24 hours in advance" |the user can schedule the pickup within 24 hours | Fail | [Bug-014](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/50) |
| TC-015 | FR-012 | Schedule pickup without selecting location | User logged in | Name: "John Doe",Email: "user@cleancity.com", Location: None, WasteType: "General" | 1. Navigate to Schedule Pickup page<br>2. Fill name field<br>3. Skip location selection<br>4. Click Submit Request | Error message: "Please select a location" | error message 'please select an item list" | Pass | N/A |
| TC-016 | FR-012 | Schedule pickup without selecting waste type | User logged in | Name: "John Doe", Email: "user@cleancity.com",Location: "Nairobi", WasteType: None | 1. Navigate to Schedule Pickup page<br>2. Fill name and location<br>3. Skip waste type selection<br>4. Click Submit Request | Error message: "Please select a waste type" |error message 'please select an item list" | Pass | N/A |
| TC-017 | FR-012 | Schedule pickup with name less than 2 characters | User logged in | Name: "J",Email: "user@cleancity.com", Location: "Nairobi", WasteType: "General" | 1. Navigate to Schedule Pickup page<br>2. Enter single character name<br>3. Fill other fields<br>4. Click Submit Request | Error message: "Name must be at least 2 characters" | successful message of request schedule | Fail |[Bug-014](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/51) |
| TC-018 | FR-015 | Prevent duplicate pickups on same date | User logged in, existing pickup for tomorrow | Same date as existing pickup | 1. Schedule pickup for tomorrow<br>2. Try to schedule another pickup for same date | Error message: "You already have a pickup scheduled for this date" | this feature cannot be tested since the data is not saved in the dashboard | Blocked | [Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64) |
| TC-019 | FR-012 | Schedule hazardous waste pickup | User logged in | Name: "John Doe", Email: "user@cleancity.com", Location: "Nairobi", WasteType: "Hazardous" | 1. Navigate to Schedule Pickup page<br>2. Fill all fields<br>3. Select "Hazardous" waste type<br>4. Click Submit Request | Request created, marked as requiring approval | Dashboard does not display the created requests| Blocked |[Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64)  |
| TC-020 | FR-012 | Schedule recyclable waste pickup | User logged in | Name: "John Doe", Email: "user@cleancity.com", Location: "Kisumu", WasteType: "Recyclable" | 1. Navigate to Schedule Pickup page<br>2. Fill all fields<br>3. Select "Recyclable" waste type<br>4. Click Submit Request | Request created successfully | Request created successfully | pass partially, blocked |[Bug-027](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/64)  |

### Request Management Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-021 | FR-016 | View pickup request history | User logged in with existing requests | N/A | 1. Login to application<br>2. Navigate to Dashboard<br>3. View requests table | All user's pickup requests displayed with details | No users pickup request, the dashboard does not update | Fail |[Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) |
| TC-022 | FR-017 | Cancel pending pickup request | User logged in, pending request exists | Request ID of pending request | 1. Navigate to Dashboard<br>2. Locate pending request<br>3. Click Cancel button<br>4. Confirm cancellation | Request status changed to "Cancelled" | Dashboard does'nt display the requests| Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) |
| TC-023 | FR-018 | Modify request before 24-hour window | User logged in, request scheduled >24 hours ahead | Request details | 1. Navigate to Dashboard<br>2. Select request >24 hours away<br>3. Click Edit button<br>4. Modify details<br>5. Save changes | Request details updated successfully | Dashboard not upate from TC-022| Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) |
| TC-024 | FR-018 | Attempt to modify request within 24 hours | User logged in, request scheduled <24 hours ahead | Request details | 1. Navigate to Dashboard<br>2. Select request <24 hours away<br>3. Click Edit button | Error message: "Cannot modify request within 24 hours of pickup" |Dashboard not upate from TC-022| Blocked |[Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65)  |
| TC-025 | FR-019 | Display request status correctly | User logged in, requests with different statuses | Multiple requests | 1. Navigate to Dashboard<br>2. View requests table | Each request displays correct status badge (Pending, Confirmed, Completed, Cancelled) |Dashboard not upate from TC-022| Blocked |[Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65)  |
| TC-026 | FR-020 | Real-time status updates | User logged in, admin changes status | N/A | 1. User views dashboard<br>2. Admin changes request status<br>3. User refreshes page | Updated status displayed immediately |Dashboard not upate from TC-022| Blocked | [Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) |
| TC-027 | FR-022 | Add feedback after pickup completion | User logged in, completed pickup exists | Feedback text | 1. Navigate to completed request<br>2. Click Add Feedback<br>3. Enter feedback<br>4. Submit | Feedback added and displayed with request |Dashboard not upate from TC-022| Blocked |[Bug-028](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/65) |

---

## Dashboard & Analytics

### User Dashboard Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-028 | FR-023 | Display recent pickup requests   or created one after logging in| User logged in with request history | N/A | 1. Login to application<br>2. Navigate to Dashboard | Recent pickup requests displayed in table format | The dashboard does notupdate the pickup requests even after creating one | Fail |[Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) |
| TC-029 | FR-023 | Display upcoming scheduled pickups | User logged in with future pickups | N/A | 1. Login to application<br>2. Navigate to Dashboard | Upcoming pickups highlighted separately | Dashboard doesn't update the  logged pickups they are at 0 | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66) |
| TC-030 | FR-024 | Calculate environmental impact metrics | User logged in with completed pickups | Completed pickup data | 1. Navigate to Dashboard<br>2. View environmental impact section | Metrics calculated and displayed: waste diverted, CO2 saved, trees saved | dashboard does not have the enviromental impacts | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66)  |
| TC-031 | FR-023 | Display achievement badges | User logged in with achievements | N/A | 1. Navigate to Dashboard<br>2. View achievements section | Earned badges displayed with descriptions | No such a section likd achievement | Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66)  |
| TC-032 | FR-023 | Quick action buttons functionality | User logged in | N/A | 1. Navigate to Dashboard<br>2. Click quick action buttons | Buttons navigate to correct pages/features | No such a feature in dashboard page| Fail | [Bug-029](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/66)  |

### Analytics & Reports Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-033 | FR-025 | Display visual charts for waste data | User logged in, waste data exists | Multiple pickup records | 1. Navigate to Dashboard<br>2. View analytics section | Charts and graphs display waste management data visually | NO such feature in dashboard  | Fail |[Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) |
| TC-034 | FR-026 | Display community leaderboards | User logged in | Multiple users with activity | 1. Navigate to Dashboard<br>2. View leaderboard section | Users ranked by environmental impact | Feature availble but not populated  | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67)|
| TC-035 | FR-027 | Show monthly waste trends | User logged in, activity spanning months | Monthly pickup data | 1. Navigate to Dashboard<br>2. View trends section<br>3. Select monthly view | Monthly trends displayed in chart format | Feature not availble | Fail | [Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67)|
| TC-036 | FR-027 | Show yearly waste trends | User logged in, activity spanning years | Yearly pickup data | 1. Navigate to Dashboard<br>2. View trends section<br>3. Select yearly view | Yearly trends displayed in chart format | Feature no availble in the dashboard| Fail |[Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67)  |
| TC-037 | FR-028 | Export user data to CSV | User logged in with data | User's pickup history | 1. Navigate to Dashboard<br>2. Click Export button<br>3. Select CSV format | Data downloaded as CSV file with correct information |  No such feature| Fail |[Bug-030](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/67) |

### Gamification Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-038 | FR-029 | Award "First Pickup" badge | New user, first pickup scheduled | N/A | 1. Register new account<br>2. Schedule first pickup<br>3. Check achievements | "First Pickup Scheduled" badge awarded |Lack of the feature |Fail/Blocked|[Bug-31](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) |
| TC-039 | FR-029 | Award "10 Pickups Completed" badge | User with 9 completed pickups | N/A | 1. Complete 10th pickup<br>2. Check achievements | "10 Pickups Completed" badge awarded | Lack of the feature| fail/blocked |[Bug-31](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) |
| TC-040 | FR-029 | Award "Perfect Recycling" badge | User with all recyclable pickups | All recyclable waste type | 1. Complete multiple recyclable pickups<br>2. Check achievements | "Perfect Recycling Score" badge awarded |Lack of the feature and admin functionality| Fail/blocked | [Bug-31](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) |
| TC-041 | FR-030 | User points calculation | User with various activities | Multiple pickups, community posts | 1. Perform various activities<br>2. Check points total | Points calculated correctly based on activities |Lack of the feature | blocked/Fail |[Bug-31](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) |
| TC-042 | FR-030 | User level progression | User earning points | Sufficient points for level up | 1. Earn points through activities<br>2. Check user level | Level increases when point threshold reached |Lack of the feature | Blocked/Fail |[Bug-31](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/68) |

---

## Content Management

### Blog System Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-043 | FR-031 | Display blog posts | User logged in, blog posts exist | N/A | 1. Navigate to Blog section<br>2. View blog posts | Blog posts displayed with title, content, author, date | blog displayed with title, content, author | Pass | N/A |
| TC-044 | FR-032 | Create new blog post | Admin logged in | Title: "Test Post", Content: "Test content" | 1. Login as admin<br>2. Navigate to Blog<br>3. Click Create Post<br>4. Enter details<br>5. Publish | New blog post created and visible | No such feature and user cannot create a blog| Fail/blocked | [Bug-015](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/52) |
| TC-045 | FR-033 | Edit existing blog post | Admin logged in, blog post exists | Updated content | 1. Login as admin<br>2. Navigate to Blog<br>3. Select post<br>4. Click Edit<br>5. Modify content<br>6. Save | Blog post updated with new content | No such a feature since the user cannot even create a blog | Fail/Blocked | [bug-016](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/53)|
| TC-046 | FR-034 | Delete blog post | Admin logged in, blog post exists | Post ID | 1. Login as admin<br>2. Navigate to Blog<br>3. Select post<br>4. Click Delete<br>5. Confirm | Blog post removed from list | No such a feature to delete blog by admin | blocked | [bug-016](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/53) |
| TC-047 | FR-035 | Comment on blog post | User logged in, blog post exists | Comment text | 1. Navigate to blog post<br>2. Scroll to comments section<br>3. Enter comment<br>4. Submit | Comment added and displayed under post, comment should persist | comment added and display next to post and disappear on refresh or navigation to other page | Pass partial | [Bug-017](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/54) |

### Awareness Section Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-048 | FR-036 | Display rotating eco tips | User on awareness page | N/A | 1. Navigate to Awareness page<br>2. Observe eco tips section<br>3. Wait 5 seconds | Eco tips rotate automatic,ally every 5 seconds | eco tips rotate automatic every 5 seconds| Pass | N/A |
| TC-049 | FR-037 | Interactive quiz functionality | User on awareness page | N/A | 1. Navigate to Awareness page<br>2. eco quiz<br>3. Answer questions | Quiz functions with question progression | the question are functioning and they update the score | Pass | N/A |
| TC-050 | FR-038 | Quiz score tracking | User completing quiz | Quiz answers | 1. Complete quiz<br>2. View results | Score calculated and displayed correctly | after every question the score is updated till its 3 out 3  | pass | N/A |
| TC-051 | FR-038 | Quiz answer explanations | User completing quiz | Quiz answers | 1. Complete quiz<br>2. View results<br>3. Check explanations | Explanations provided for correct/incorrect answers |explanation provided for either correct and incorrect | Pass | N/A |
| TC-052 | FR-039 | Display environmental infographics | User on awareness page | N/A | 1. Navigate to Awareness page<br>2. Scroll through content to "did you know" section | Infographics with environmental statistics displayed | Yes we have some statistics from different environment | Pass | N/A |
| TC-053 | FR-040 | Action buttons linking | User on awareness page | N/A | 1. Navigate to Awareness page<br>2. Click action buttons | Buttons link to correct features and pages | yes we have action buttons to the request page, community and report issues | Pass | N/A |

### Community Feed Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-054 | FR-041 | Create community post | User logged in | Post content: "Test community post" | 1. Navigate to Community<br>2. Click Create Post<br>3. Enter content<br>4. Post | New post created and displayed in feed, persist on refresh | created  a post, and it persist on refresh | Pass | N/A |
| TC-055 | FR-042 | Like community post | User logged in, post exists | N/A | 1. Navigate to Community<br>2. Find post from Admin <br>3. Click Like button | Like count increases, button state changes and like persist on refresh | like increases the count, button turns red, and the like persit on refres | Pass | N/A |
| TC-056 | FR-042 | Comment on community post | User logged in, post exists | Comment text | 1. Navigate to Community<br>2. Find post from Admin <br>3. Click Comment<br>4. Enter comment<br>5. click comment button | Comment added to post | comment is added successfully | Pass | N/A |
| TC-057 | FR-043 | Posts display in chronological order | User logged in, multiple posts exist | N/A | 1. Navigate to Community<br>2. View posts | Posts sorted by date, newest first | Post are sorted in the order of the newest first | Pass | N/A |
| TC-058 | FR-044 | Share waste reduction tips | User logged in | Tip content | 1. Navigate to Community<br>2. Create post with tip<br>3. Add tip category tag | Tip shared successfully with proper categorization | The  tip feature is not availble | Blocker/Fail | [Bug-018](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/55)  |

---

## Community Features

### User Profiles Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-059 | FR-045 | View user profile | User logged in | N/A | 1. Navigate to Profile section<br>2. View profile details | Profile information displayed correctly | yes the name and email display correct | Pass | N/A |
| TC-060 | FR-045 | Edit user profile information | User logged in | Updated name preferences | 1. Navigate to Profile<br>2. Click Edit<br>3. Modify information<br>4. Save changes | Profile updated successfully | successful update the name| Pass | N/A |
| TC-061 | FR-046 | Display user achievements | User logged in with badges | N/A | 1. Navigate to Profile<br>2. View achievements section | All earned achievements displayed and statistics | No achievement is displayed or updated | Fail |[Bug-019](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/56) |
| TC-062 | FR-046 | Display user activity history | User logged in with activity | N/A | 1. Navigate to Profile<br>2. View activity section | Activity history displayed chronologically |No activity update even after creating pickup or post in community | Fail |[Bug-019](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/56) |
| TC-063 | FR-047 | Upload profile picture | User logged in | Image file | 1. Navigate to Profile<br>2. Click upload picture<br>3. Select image<br>4. Save | Profile picture updated and displayed | The picture has not room to update, its like permanent | Fail |[Bug-020](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/57) |
| TC-064 | FR-048 | Display user statistics | User logged in with activity | N/A | 1. Navigate to Profile<br>2. View statistics section | Statistics displayed: pickups, points, impact | No user statistics displayed , just features not updated with user activity | Fail | [Bug-021](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/58) |

### Social Features Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-065 | FR-049 | Follow other community members | User logged in | Another user's profile | 1. Navigate to another user's profile<br>2. Click Follow button | User followed successfully, button changes to "Following" | No such feature | Blocked | [Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) |
| TC-066 | FR-050 | View news feed of community activities | User logged in | N/A | 1. Navigate to Community Feed<br>2. View activities | Feed displays activities from followed users |No such feature | Blocked |[Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) |
| TC-067 | FR-051 | Share achievements and milestones | User logged in, new achievement | Achievement data | 1. Unlock achievement<br>2. Click Share<br>3. Post to community | Achievement shared to community feed |No such feature | Blocked |[Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) |
| TC-068 | FR-052 | Participate in community challenges | User logged in, active challenge | N/A | 1. Navigate to Challenges<br>2. Join challenge<br>3. Complete tasks | Progress tracked, points awarded | No such feature | Blocked |[Bug-022](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/59) |

---

## Administrative Functions

### Request Management Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-069 | FR-053 | Admin view all pickup requests | Admin logged in | Email: "admin@cleancity.com", Password: "admin123" | 1. Login as admin<br>2. Navigate to Admin panel<br>3. View requests section | All pickup requests from all users displayed | Admin panel is not updating automatically for the admin to see the pickup update| Fail |[Bug-023](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/60) |
| TC-070 | FR-054 | Admin approve pickup request | Admin logged in, pending request exists | Request ID | 1. Login as admin<br>2. Navigate to Admin panel<br>3. Select pending request<br>4. Click Approve | Request status changed to "Confirmed" | Missing feature | Blocked |[Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |
| TC-071 | FR-054 | Admin reject pickup request | Admin logged in, pending request exists | Request ID, Reason | 1. Login as admin<br>2. Select pending request<br>3. Click Reject<br>4. Enter reason | Request status changed to "Rejected" with reason | missing feature| Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |
| TC-072 | FR-054 | Admin modify pickup request | Admin logged in, request exists | Modified details | 1. Login as admin<br>2. Select request<br>3. Click Edit<br>4. Modify details<br>5. Save | Request details updated by admin | Missing feature| fail/Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |
| TC-073 | FR-055 | Admin assign pickup date and time | Admin logged in, confirmed request exists | Date, Time | 1. Login as admin<br>2. Select confirmed request<br>3. Assign date/time<br>4. Save | Pickup scheduled with assigned date/time |missing feature| Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |
| TC-074 | FR-056 | Filter requests by status | Admin logged in | Status: "Pending" | 1. Login as admin<br>2. Navigate to Admin panel<br>3. Apply status filter | Only requests with selected status displayed |missing feature| Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |
| TC-075 | FR-056 | Search requests by criteria | Admin logged in | Search term | 1. Login as admin<br>2. Navigate to Admin panel<br>3. Enter search criteria<br>4. Execute search | Matching requests displayed | missing feature| Blocked | [Bug-024](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/61) |

### User Management Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-076 | FR-057 | Admin view all registered users | Admin logged in | N/A | 1. Login as admin<br>2. Navigate to User Management | All registered users displayed with details | All admin user management and reporting features are missing; no options available in Admin Panel | Blocked/Fail |[Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) |
| TC-077 | FR-058 | Admin change user role | Admin logged in, user exists | User ID, New Role | 1. Login as admin<br>2. Select user<br>3. Change role to Admin<br>4. Save | User role updated successfully | All admin user management and reporting features are missing; no options available in Admin Panel | Blocked/Fail |[Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) |
| TC-078 | FR-059 | Admin suspend user account | Admin logged in, user exists | User ID | 1. Login as admin<br>2. Select user<br>3. Click Suspend<br>4. Confirm | User account suspended, cannot login | All admin user management and reporting features are missing; no options available in Admin Panel | Blocked/Fail |[Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) |
| TC-079 | FR-059 | Admin delete user account | Admin logged in, non-admin user exists | User ID | 1. Login as admin<br>2. Select user<br>3. Click Delete<br>4. Confirm | User account deleted permanently | All admin user management and reporting features are missing; no options available in Admin Panel | Blocked/Fail |[Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) |
| TC-080 | FR-060 | Generate user activity report | Admin logged in | Date range | 1. Login as admin<br>2. Navigate to Reports<br>3. Select date range<br>4. Generate report | Report generated with user activity statistics | All admin user management and reporting features are missing; no options available in Admin Panel | Blocked/Fail |[Bug-025](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/62) |

### Content Moderation Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-081 | FR-061 | Admin moderate community post | Admin logged in, flagged post exists | Post ID | 1. Login as admin<br>2. View flagged posts<br>3. Review content<br>4. Approve or reject | Post moderation decision applied|Admin panel does not display updates for moderation | Blocked/Fail |[Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63) |
| TC-082 | FR-062 | Admin delete inappropriate content | Admin logged in, inappropriate post exists | Post ID | 1. Login as admin<br>2. Locate inappropriate post<br>3. Click Delete<br>4. Confirm | Post removed from community feed |Admin panel does not display updates for deletion | Blocked/Fail | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63)|
| TC-083 | FR-063 | User flag inappropriate content | User logged in, inappropriate post exists | Post ID, Reason | 1. Login as user<br>2. Find post<br>3. Click Report<br>4. Select reason<br>5. Submit | Content flagged for admin review | Admin panel does not display updates for flaggin inappropiate content | Blocked/Fail | [Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63)|
| TC-084 | FR-064 | Admin create announcement | Admin logged in | Title, Content | 1. Login as admin<br>2. Navigate to Announcements<br>3. Click Create<br>4. Enter details<br>5. Publish | Announcement created and visible to all users |Admin panel does not display the create announcement | Blocked/Fail |[Bug-026](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/63)|

---

## Notification System

### Notification Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-085 | FR-065 | Notification bell display | User logged in | N/A | 1. Login to application<br>2. View notification bell | Notification bell visible with unread count |notification bell is visible and has no unread count | PAss |N/A |
| TC-086 | FR-066 | Pickup confirmation notification | User logged in | New pickup request | 1. Schedule pickup<br>2. Admin confirms<br>3. Check notifications | Notification received for pickup confirmation |admin page is not working and the  notification are not showing up. | Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |
| TC-087 | FR-066 | New blog post notification | User logged in | Admin publishes blog | 1. Admin creates blog post<br>2. User checks notifications | Notification received for new blog post | Missing feature the user cannot create a blog post|  Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |
| TC-088 | FR-066 | Community interaction notification | User logged in | Another user likes post | 1. Create community post<br>2. Another user interacts<br>3. Check notifications | Notification received for interaction |No update of the notification after interaction with community | Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |
| TC-089 | FR-066 | Achievement unlock notification | User logged in | Achievement criteria met | 1. Complete achievement requirement<br>2. Check notifications | Notification received for badge unlock |Feature is missing to test| Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |
| TC-090 | FR-067 | Mark notification as read | User logged in, unread notifications | Notification ID | 1. View notifications<br>2. Click on notification<br>3. Mark as read | Notification marked as read, count decreases |no update of the notifcation to see the read and unread notification| Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |
| TC-091 | FR-068 | Notification history view | User logged in | Multiple notifications | 1. Click notification bell<br>2. View history | All notifications displayed in chronological order |missing functionality feature|  Blocked/Fail |[Bug-031](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/69) |

---
## User Interface Requirements

### Responsive Design Test Cases
### Responsive Design Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-092 | FR-069 | Desktop responsiveness (1920x1080+) | Browser opened | N/A | 1. Set browser resolution to 1920x1080<br>2. Navigate through all pages<br>3. Test forms and interactions | All features display correctly, no layout issues | Layout issues on all browsers | Fail | [Bug-036](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/80) |
| TC-093 | FR-069 | Tablet responsiveness (768px-1024px) | Browser opened | N/A | 1. Resize browser to 768px width<br>2. Navigate through all pages<br>3. Test forms and interactions | Layout adapts properly, all features accessible | Layout is not adpative to tablet, the element headers overlap on tablet mode| Fail |[Bug-037](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/81) |
| TC-094 | FR-069 | Mobile responsiveness (320px-767px) | Browser opened | N/A | 1. Resize browser to 375px width<br>2. Navigate through all pages<br>3. Test forms and mobile menu | Mobile layout displays correctly, hamburger menu works | No hambuger menu, the headers cover more than half of the screen , tha layout is not displaying correct  | Fail |[Bug-038](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/82) |
| TC-095 | FR-070 | Functionality across all screen sizes | Browser opened | Test data from TC-013 | 1. Test pickup scheduling at 1920px<br>2. Test same at 768px<br>3. Test same at 375px | All functionality works identically across sizes | the scheduling is working well on destop part but the tablet the user will face difficulty of navigation the headers are covering the whole screen| Fail |[Bug-038](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/82),[Bug-037](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/81) |

### Accessibility Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-096 | FR-071 | WCAG 2.1 AA compliance check | Browser with axe DevTools | N/A | 1. Install axe DevTools extension<br>2. Run scan on all pages<br>3. Review violations | No critical WCAG 2.1 AA violations found |one critical and 34 WCAG 2.1 AA violations found | FAil |[Bug-039](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/83) |
| TC-097 | FR-072 | Keyboard navigation - Tab key | Browser opened | N/A | 1. Start on home page<br>2. Use Tab key to navigate<br>3. Test all interactive elements | All elements accessible via Tab, logical order | All top element are acessible via tab key | Pass | N/A |
| TC-098 | FR-073 | Alt text for images | Browser opened | N/A | 1. Navigate to Awareness page<br>2. Inspect all images<br>3. Check alt attributes | All images have descriptive alt text | only avatar is the picture has an alt avatar | pass partially/blocked | n/a |
| TC-99 | FR-074 | Screen reader compatibility | NVDA or JAWS installed | N/A | 1. Enable screen reader<br>2. Navigate through application<br>3. Test form filling | All content properly announced, forms usable | drop down for choosing the blog tages are not announced | Fail  |[Bug-040](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/84) |

### Navigation Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-100 | FR-075 | Clear navigation menu | Browser opened | N/A | 1. View navigation bar<br>2. Check all menu items<br>3. Test each link | Menu clearly labeled, all links functional | Navigation menu is missing, cannot access any menu items.| Fail/Blocked |[Bug-041](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/85) |
| TC-101 | FR-076 | Breadcrumbs on complex pages | User logged in | N/A | 1. Navigate to Admin panel<br>2. Go to nested section<br>3. Check breadcrumb trail | Breadcrumbs show path: Home > Admin > Section |Breadcrumbs are not present on the page | Fail/Blocked |[Bug-041](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/85) |
| TC-102 | FR-077 | Search functionality | Browser opened, content exists | Search term: "recycling" | 1. Locate search box<br>2. Enter "recycling" in the blog page search section <br>3. Submit search | Relevant results are filtered | some blogs are filterd in the blog page| Pass | N/a|

---

## Data Management Requirements

### Data Persistence Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-103 | FR-078 | localStorage stores user data | Browser opened | Registration data from TC-001 | 1. Register new account<br>2. Open browser DevTools<br>3. Check Application > localStorage | User data stored with correct keys and format | all user data is stored corectly | Pass | N/a |
| TC-104 | FR-078 | localStorage stores pickup requests | User logged in | Pickup data from TC-013 | 1. Schedule pickup request<br>2. Check localStorage<br>3. Verify data structure | Pickup request stored in localStorage correctly |stored correctly but no new pickup request is updated to the local storage | Partially pass/fail | n/a |
| TC-105 | FR-079 | Data persists across sessions | User logged in | Valid credentials | 1. Login and create data<br>2. Close browser completely<br>3. Reopen and check data | All data persists correctly after browser restart | Login does persit and data does persit| Pass | |
| TC-106 | FR-080 | localStorage limit handling | Browser opened | Large amount of test data | 1. Fill localStorage near 5MB limit<br>2. Attempt to add more data<br>3. Observe error handling | Graceful error message displayed to user | error"Failed to execute 'setItem' on 'Storage': Setting the value.."   | Pass | 

### Data Validation Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-107 | FR-082 | XSS attack prevention | Browser opened | `<script>alert('XSS')</script>` | 1. Enter XSS payload in name field<br>2. Submit form<br>3. Check rendered output | Script tags escaped, no alert executed | No alert but scripts do not escape | Fail |[Bug-042](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/86) |
| TC-110 | FR-082 | SQL injection prevention | Browser opened | `' OR '1'='1` | 1. Enter SQL injection in login<br>2. Submit form<br>3. Verify behavior | Payload treated as text, no unauthorized access |authorized access with the sql injection | Fail |[Bug-043](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/87) |
| TC-111 | FR-083 | User content sanitization | User logged in | HTML: `<strong>Bold</strong>` | 1. Post community content with HTML<br>2. Submit post<br>3. View rendered content | HTML escaped or sanitized safely |Html does not escape and get sanitized | Fail |[Bug-044](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/88) |

---

## Performance Requirements

### Response Time Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-112 | FR-084 | Page load time - Home page | Browser opened, cache cleared | N/A | 1. Clear browser cache<br>2. Navigate to home page<br>3. Use DevTools Performance tab | Page loads within 3 seconds |page loads withing 3 seconds | Pass | |
| TC-113 | FR-084 | Page load time - Dashboard | User logged in, cache cleared | N/A | 1. Clear browser cache<br>2. Navigate to dashboard<br>3. Measure load time | Dashboard loads within 3 seconds | Dashboard loads in 3 seconds | Pass | |
| TC-114 | FR-085 | Button click response time | User logged in | N/A | 1. Click "Schedule Pickup" button<br>2. Measure response time<br>3. Repeat for other buttons | All interactions respond within 1 second | responds in 1 second | Pass | |
| TC-115 | FR-085 | Form submission response time | User logged in | Valid pickup data | 1. Fill pickup form completely<br>2. Submit form<br>3. Measure response time | Form processes and confirms within 1 second  with success message | form clear almost immediately | Pass | |

### Browser Compatibility Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-116 | FR-086 | Chrome compatibility | Chrome latest version | Pickup data from TC-013 | 1. Open application in Chrome<br>2. Test registration and login<br>3. Test pickup scheduling | All features work correctly in Chrome | All features work correctly| Pass | |
| TC-117 | FR-086 | Firefox compatibility | Firefox latest version | Pickup data from TC-013 | 1. Open application in Firefox<br>2. Test registration and login<br>3. Test pickup scheduling | All features work correctly in Firefox | All features work correctly| Pass | |
| TC-118 | FR-086 | Safari compatibility | Safari latest version | Pickup data from TC-013 | 1. Open application in Safari<br>2. Test registration and login<br>3. Test pickup scheduling | All features work correctly in Safari | All features work correctly| Pass | |
| TC-119 | FR-086 | Edge compatibility | Edge latest version | Pickup data from TC-013 | 1. Open application in Edge<br>2. Test registration and login<br>3. Test pickup scheduling | All features work correctly in Edge | All features work correctly| Pass | |

---

## Error Handling Requirements

### User-Friendly Errors Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-120 | FR-087 | Clear error messages | Browser opened | Invalid login email "admincleancity.com | 1. Enter wrong email <br>2. Submit login form<br>3. Read error message | Message is clear: "Invalid email" | error message display when I try to submit | Pass | |
| TC-121 | FR-088 | Error resolution guidance | Browser opened | Empty required field | 1. Skip required field<br>2. Submit form<br>3. Read error guidance | Error explains what to be filled| error message pop up if I try to submitt the form | Pass | |
| TC-122 | FR-089 | Network error handling | Browser opened | N/A | 1. Disable network connection<br>2. Try to submit form<br>3. Observe error handling | User-friendly message: "Network error. Check connection." | on deployed  web application  the errrors appear in the network devtools | Pass | |

### Form Validation Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-123 | FR-091 | Prevent invalid form submission | Browser opened | All fields empty | 1. Leave all fields blank<br>2. Click Submit button<br>3. Check behavior | Form not submitted, validation errors displayed | erro message fill in the blank spaces| pass | N/A |
| TC-124 | FR-092 | Validation error highlighting | Browser opened | Invalid data in multiple fields | 1. Enter invalid email and short password<br>2. Submit form<br>3. Check visual indicators | Fields with errors highlighted in red with icons | No it only  highlight the firt part and others are not highlited | Partially Pass/Fail | |

FR-090 has been perfomed 
---

## Business Rules Validation

### Pickup Scheduling Rules Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-125 | BR-001 | 30-day advance booking limit | User logged in | Date: 31 days from today | 1. Select date 31 days ahead<br>2. Fill other fields<br>3. Submit request | Error: "Cannot schedule more than 30 days in advance" | the request can be submitted  | Fail |[Bg-032](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/75) |
| TC-126 | BR-001 | 24-hour minimum notice | User logged in | Date: Today | 1. Select today's date<br>2. Fill other fields<br>3. Submit request | Error: "Minimum 24-hour notice required" | request can be submtitted same day | Fail |[Bug-033](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/76) |
| TC-127 | BR-001 | Maximum 3 pickups per week | User logged in, 3 pickups this week | 4th pickup this week | 1. Schedule 3 pickups in current week<br>2. Attempt 4th pickup same week<br>3. Submit | Error: "Maximum 3 pickups per week reached" |more than 4 pickup ca be  created | Fail/blocked |[Bug-034](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/77) |
| TC-128 | BR-001 | Hazardous waste approval requirement | User logged in | WasteType: "Hazardous" | 1. Schedule hazardous waste pickup<br>2. Submit request<br>3. Check status | Status shows "Pending Approval" instead of "Pending" | blocked lack of the admin panel to confirm | Fail/blocked |[Bug-035](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/78) |


### Content Rules Test Cases

*BR-001 and Br-003 already applied on other test cases*

---

## Support and Maintenance

### Help System Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-129 | FR-093 | Contextual help tooltips | Browser opened | N/A | 1. Navigate to registration page<br>2. Hover over help icons (?) <br>3. Read tooltip content | Tooltips appear with helpful information |Feature not available | fail/blocked |[Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) |
| TC-130| FR-094 | FAQ section accessibility | Browser opened | N/A | 1. Navigate to Help/FAQ section<br>2. Browse questions<br>3. Test expandable answers | FAQ section accessible, questions organized by category |Feature not available | fail/blocked |[Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) |
| TC-131 | FR-095 | Contact information display | Browser opened | N/A | 1. Navigate to Awareness page<br>2. Scroll to contact section<br>3. Check information | Contact info clearly displayed: email, phone, website |Feature not available | fail/blocked |[Bug-045](https://github.com/StevenOyar/wk-6-StevenOyar-1/issues/89) |

### System Monitoring Test Cases

| Test ID | FRS ID | Test Case Name | Prerequisites | Test Data | Steps to Reproduce | Expected Result | Actual Result | Status | Bug ID |
|---------|--------|----------------|---------------|-----------|-------------------|-----------------|---------------|--------|---------|
| TC-132| FR-096 | User activity logging | User logged in | Various user actions | 1. Perform login<br>2. Schedule pickup<br>3. Check browser console logs | Activities logged in console for debugging | activites are being logged into the console part of the devtools | Pass | |
| TC-133 | FR-097 | Error logging functionality | Browser opened | Action causing error | 1. Trigger an error (invalid input)<br>2. Check browser console<br>3. Verify error details | Errors logged with details: timestamp, type, message | activities logged with timestamp ,size,name and message | Pass | |

---

## Test Execution Summary

### Summary Statistics

| Section | Pass | Fail | Blocked | Partial | Total |
|---------|------|------|---------|---------|-------|
| Authentication & User Management | 4 | 6 | 2 | 0 | 12 |
| Waste Management | 2 | 6 | 7 | 0 | 15 |
| Dashboard & Analytics | 1 | 9 | 5 | 0 | 15 |
| Content Management | 6 | 3 | 7 | 1 | 17 |
| Community Features | 7 | 1 | 2 | 0 | 10 |
| Administrative Functions | 0 | 1 | 15 | 0 | 16 |
| Notification System | 1 | 0 | 6 | 0 | 7 |
| User Interface Requirements | 1 | 5 | 2 | 0 | 8 |
| Data Management Requirements | 5 | 3 | 0 | 1 | 9 |
| Performance Requirements | 8 | 0 | 0 | 0 | 8 |
| Error Handling Requirements | 3 | 1 | 0 | 1 | 5 |
| Business Rules Validation | 0 | 4 | 0 | 0 | 4 |
| Support and Maintenance | 0 | 0 | 3 | 0 | 3 |
| **TOTAL** | **38** | **39** | **49** | **3** | **129** |

---
