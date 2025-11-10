
##  Document Information
*Team name*: Bug Hunters 

*Project*: CleanCity - Waste Pickup Scheduler  

*Version:*
*Date:* 10/11/2025
*Status:* In Progress

---

## Table of Contents

1. [Authentication Module (TC-001 to TC-015)](#authentication-module)


# CleanCity Test Cases 

## Authentication Module

| Test ID | Test Case Name | Priority | Severity | Prerequisites | Test Data | Steps to reproduce| Expected Result | Actual Result | Status | Bug ID |
|---------|-------------|----------|----------|---------|-----------|-------|-----------------|---------------|--------|---------|
| TC-001 | Valid User Registration | High | Critical | None | Name: "John Doe"<br>Email: "user1@test.com"<br>Password: "TestPass123" | 1. Open CleanCity<br>2. Click "Register"<br>3. Enter full name<br>4. Enter email<br>5. Enter password<br>6. Click "Create Account" | - Registration success message<br>- User redirected/can login<br>- User data in localStorage<br>- Account created with 'user' role | - No success message<br>- User redirected/can login<br>- NO user data in localStorage<br>- Account NOT created with 'user' role | Fail | Bug-002 |
| TC-002 | Registration with Existing Email | High | Major | User "user1@test.com" registered | Email: "user1@test.com" | 1. Open CleanCity<br>2. Click "Register"<br>3. Enter full name<br>4. Enter existing email<br>5. Enter password<br>6. Click "Create Account" | - Error: "User with this email already exists"<br>- Form not submitted<br>- User stays on registration page<br>- No duplicate user | - No error message<br>- Form submitted<br>- Data not stored in localStorage | Fail | Bug-003 |
| TC-003 | Registration with Invalid Email | High | Major | None | Email: "usertests.com" (no @) | 1. Open CleanCity<br>2. Click "Register"<br>3. Enter full name<br>4. Enter invalid email<br>5. Enter password<br>6. Click "Create Account" | - Error message about '@'<br>- Form validation prevents submission<br>- Email field highlighted<br>- User stays on page | - Error: "Please include an '@'..."<br>- No form submission<br>- Email area highlighted<br>- User stays on page | Pass | N/A |
| TC-004 | Registration with Weak Passwords | High | Major | None | Password: "2" (1 character) | 1. Open CleanCity<br>2. Click "Register"<br>3. Enter name<br>4. Enter email<br>5. Enter weak password<br>6. Click Create Account | - Error: "Password must be at least 8 characters"<br>- Account not created<br>- Per FR-001 requirement | - User can submit with 1 char password<br>- Redirected to login<br>- Can login with 1 character | Fail | BG-001 |
| TC-005 | Registration with Special Characters in Name | Medium | Minor | None | Name: "O'oyaro-steven Jr." | 1. Open CleanCity<br>2. Click "Register"<br>3. Enter name with special chars<br>4. Enter email<br>5. Enter password<br>6. Click Create Account | - Valid characters accepted<br>- Registration successful<br>- Name stored correctly | - Valid characters accepted<br>- Registration successful | Pass | N/A |
| TC-006 | Valid User Login | High | Critical | User "user@cleancity.com" exists<br>Password: "password123" | Email: "user@cleancity.com"<br>Password: "password123" | 1. Open CleanCity<br>2. Click Login<br>3. Enter email<br>4. Enter password<br>5. Click "Sign In"<br>6. Observe redirect | - Login successful<br>- Redirected to dashboard/home<br>- Navigation updates<br>- Logout button displayed<br>- Session stored in localStorage | - Login successful<br>- Redirected to profile<br>- Navigation updates<br>- NO Session in localStorage | Fail | Bg-004 |
| TC-007 | Login with Unregistered Email | High | Major | None | Email: "user4@gmail.com"<br>Password: "password123" | 1. Open CleanCity<br>2. Click Login<br>3. Enter unregistered email<br>4. Enter password<br>5. Click Sign In<br>6. Observe | - Error: "Invalid email or password"<br>- User stays on login page<br>- No redirect | - User able to login<br>- Redirected to profile<br>- Logout button appears | Fail | Bug-005 |
| TC-008 | Login with Wrong Password | High | Major | User "user@cleancity.com" exists | Email: "user@cleancity.com"<br>Password: "234" (incorrect) | 1. Open CleanCity<br>2. Navigate to login<br>3. Enter email<br>4. Enter wrong password<br>5. Click "Sign In" | - Error: "Invalid email or password"<br>- User stays on login page<br>- No session created | - User able to login<br>- Can access protected pages<br>- No session created | Fail | Bug-006 |
| TC-010 | Login with Empty Input Fields | Medium | Major | None | Empty email and password | 1. Open CleanCity<br>2. Navigate to login<br>3. Leave email empty<br>4. Leave password empty<br>5. Click Sign In | - HTML5 validation prevents submission<br>- "Please fill in this field" message<br>- Form not submitted | - HTML5 validation prevents submission<br>- "Please fill in this field" shown<br>- Form not submitted | Pass | N/A |
| TC-011 | Successful user logout | High | Major | User logged in with correct credentials | Email: "user@cleancity.com"<br>Password: "password123" | 1. Open CleanCity<br>2. Login as user<br>3. Verify Logout button visible<br>4. Click Logout<br>5. Observe | - User logged out<br>- Redirected to home<br>- Login/Register shown<br>- Logout button hidden<br>- Profile nav hidden<br>- Cannot access protected pages | - User logged out<br>- Redirected to home<br>- Login/Register shown<br>- Logout hidden<br>- Session cleared<br>- Cannot access protected pages | Pass | N/A |
| TC-012 | Access protected page without login | High | Major | User NOT logged in | N/A | 1. Ensure no user logged in<br>2. Navigate to Dashboard directly<br>3. Navigate to Feedback directly | - Redirected to login page<br>- Cannot access protected content<br>- User prompted to login | - Redirected to login<br>- Cannot access protected content<br>- User prompted to login | Pass | N/A |
| TC-013 | Session persistence after browser restart | Medium | Minor | User logged in | N/A | 1. Login as user<br>2. Close browser completely<br>3. Reopen browser<br>4. Navigate to CleanCity<br>5. Check login status | - User remains logged in<br>- No need to login again<br>- Session data intact<br>- User info displays correctly | user remains logged in<br> - local storage holds th euser infomation | Pass | N/A |
| TC-014 | Admin Login and Access | High | Critical | Admin user exists | Email: "admin@cleancity.com"<br>Password: "admin123" | 1. Navigate to login<br>2. Enter admin email<br>3. Enter admin password<br>4. Click "Sign In"<br>5. Check navigation menu | - Login successful<br>- "Admin" navigation link visible<br>- "Admin" badge displayed<br>- Can access admin panel<br>- All user features available | - successful login<br> -navigation link for admin is created<br> admin can access the admin section the requests.<br> - all the user features are available | Pass | NA |
| TC-015 | SQL Injection Attempt in Login | Medium | Critical | None | Email: "' OR '1'='1"<br>Password: "' OR '1'='1" | 1. Navigate to login<br>2. Enter SQL injection in email<br>3. Enter SQL injection in password<br>4. Click "Sign In" | - Login fails<br>- Treated as invalid credentials<br>- Error: "Invalid email or password"<br>- No unexpected behavior | Login failed<br> - pop up message requesting valid email, no unexpected behavior | Pass | N/A |
