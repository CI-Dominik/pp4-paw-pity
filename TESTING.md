# TESTING

In this document, you will find all manual testing procedures that were used when taking all needed conditions of user behaviour into consideration.

## Table of Contents

* [Navigation](#navigation)
* [Registration Page](#registration-page)
* [Login Page](#login-page)
* [Footer](#footer)
* [Starting page](#starting-page)
  * [Hero Section](#hero-section)
  * [Latest Reports](#latest-reports)
* [Lost Animals page](#lost-animals-page)
  * [Overview](#overview)
  * [Animal Details Page](#animal-details)
  * [Edit Animal](#edit-animal)
  * [Report Comment](#report-comment)
* [Your Animals page](#your-animals-page)
  * [Animal List](#animal-list)
  * [Edit Animal](#edit-animal)
* [Complaints page](#complaints-page)
* [Admin Panel](#admin-panel)
  * [General](#general)
  * [Users](#users)
  * [Animals](#animals)
  * [Comments](#comments)
  * [Complaints](#complaints)

* [RESPONSIVENESS](#responsiveness)

## Navigation

![Picture of the navigation bar](docs/testing/navigation.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Loading the page | Navigation should display with the menu buttons Home, Lost Animals, Register and Login | Pass |
| Hovering over each link | Link should be underlined while hovered | Pass |
| Clicking on each link | The current site link should be highlighted | Pass |
| Visiing each link | The corresponding page should be opened | Pass |
| Clicking on register | The registation site should open up | Pass |
| Clicking on login | The login page should open up | Pass |
| Logging in | The register and login link should disappear | Pass |
| Logging in | The Your Animals and Log out link should appear | Pass |
| Logging out | A modal should open and enable logout | Pass |
| Clicking logout on the modal | The user should be safely logged out | Pass |
| Clicking on Your Animals | The Your Animals page should be opened up | Pass |
| Logging in as a superuser | Open Complaints link should be visible | Pass |
| Logging in as a normal user | Open Complaints link should not be visible | Pass |

---

## Registration page

![Picture of the registration page](docs/testing/registration.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Registering with correct data | An account should be registered and the user should be logged in | Pass |
| Entering a name with a space in it | The registration should be blocked | Pass |
| Entering a name that is already registered | The registration should be blocked, regardless of typing | Pass |
| Entering an email address that is already in use | A message should tell the user that the email address is already in use | Pass |
| Entering an email address that does not follow the email format | A message should tell the user that the format is not correct | Pass |
| Entering a password with less than eight letters | A message should tell the user that the password is too short | Pass |
| Entering a common password | A message should tell the user that the password is too common | Pass |
| Entering the second password wrongly | A message should tell the user that the passwords do not match | Pass |
| Entering only numbers for the password | A message should tell the user that the password cannot be completely numeric | Pass |
| Leaving the username, email address or password field empty | A message should tell the user that the content needs to be inserted | Pass |
| Entering a username and email address that exeeds the maximum length | A message should tell the user that the entry is too long | Pass |
| Entering a username and email address that exeeds the maximum length with the max-length value changed in devtools | A message should tell the user that the entry is too long | Pass |

---

## Login Page

![Picture of the login page](docs/testing/login.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Entering correct login information | User should get logged in | Pass |
| Entering false login information | A message should tell the user that the typed information is incorrect | Pass |
| Entering the right username, but the wrong password | A message should tell the user that the typed information is incorrect | Pass |
| Leaving the username field empty | A message should tell the user that it is a required field | Pass |
| Leaving the fields empty and removing the required tag in devools | A message should tell the user that the field is required | Pass |

---

## Footer

![Picture of the footer](docs/testing/footer.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Viewing the content | Information about the company, links and contact data should be visible | Pass |
| Clicking on each link | The corresponding site should be called | Pass |
| Logging in | The register and login link should disappear | Pass |
| Logging out | The modal should be called | Pass |
| Clicking on the phone number | The corresponding phone app should be opened | Pass |
| Clicking on the email address | An email program should popup if one is used | Pass |

---

## Starting page

### Hero Section

![Picture of the hero section](docs/testing/hero-section.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Viewing the content | A text area with a link to the animal reports and a picture should appear | Pass |
| Clicking on the link | The reports page should open up | Pass |

### Latest Reports

![Picture of the latest reports](docs/testing/latest-reports.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Viewing the content | The last three entries in the reports database should appear | Test |
| Erasing all database entries and viewing the content | A message saying that there are no reports should appear | Pass |
| Clicking on an entry | The related animal details page should open up | Pass |

---

## Lost Animals page

### Overview

![Picture of the lost animals page](docs/testing/lost-animals.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Viewing the content | An overview over the last entries in the animal databse should be visible | Pass |
| Viewing which information is displayed | The photo, name, location and if the animal is approachable should be displayed | Pass |
| Increasing the number of entries to nine | Only eight items per page should be visible and a pagination is displayed | Pass |
| Deleting all entries of the database | A message telling that there are currently no animals registered should appear | Pass |
| Clicking on an entry | The corresponding animal details page should open up | Pass |
| Clicking on register animal | The page to add an animal to the reports should open up | Pass |

### Animal Details

![Picture of the animal details page](docs/testing/animal-details.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Viewing the content | A list of the animal's information should be displayed as a table | Pass |
| Adding a comment | The comment should be displayed on the animal's page | Pass |
| Adding a comment that is long than 255 characters to the textfield | The addition of characters should be stopped | Pass |
| Adding a comment that is longer than 255 characters with increasing the limit in devtools | A message should appear that the comment is too long | Pass |
| Deleting a comment | A modal to cancel of delete the comment should appear | Pass |
| Clicking on delete | The comment should be removed | Pass |
| Viewing a comment as another user who is not the author | The comment should only display without the function to edit it | Pass |
| Editing a comment via a URL while not being the author | A 403 page should appear | Pass |
| Deleting a comment via a URL while not being the author | A 403 page should appear | Pass |

### Edit Comment

![Picture of the edit comment page](docs/testing/edit-comment.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Editing a comment | The text should change on the animal page | Pass |
| Editing a comment with more than 255 characters | The addition of characters should be stopped | Pass |
| Editing a comment with more than 255 characters using an increased max-length in devtools | A message should appear that the comment is too long | Pass |

### Report Comment

![Picture of the report comment page](docs/testing/report-comment.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Reporting a comment | The complaint should be visible in the complaints list | Pass |
| Entering a reason with less than ten characters | A message should appear that the reason is too short | Pass |
| Entering a reason with more than 255 characters | The addition of characters should be stopped | Pass |
| Entering a reason with more than 255 characters with removing the required tag in devtools | A message should appear that tells the user that the message is too long | Pass |

---

## Your Animals page

### Animal List

![Picture of the your animals page](docs/testing/your-animals.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Add Animal

![Picture of the add animal page](docs/testing/add-animal.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Edit Animal

![Picture of the your animals edit page](docs/testing/edit-animal.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

---

## Complaints page

![Picture of the complaints list](docs/testing/complaints.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

---

## Admin Panel

### General

![Picture of the admin panel](docs/testing/admin-panel.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Users

![Picture of the admin panel user page](docs/testing/admin-panel-user.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Animals

![Picture of the admin panel animal page](docs/testing/admin-panel-animals.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Comments

![Picture of the admin panel comments page](docs/testing/admin-panel-comments.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

### Complaints

![Picture of the admin panel complaints page](docs/testing/admin-panel-complaints.jpg)

| Testing method | Expected result | Actual result |
|:-------------:|:---------------:|:-------------:|
| Test | Test | Test |

# RESPONSIVENESS

PLACEHOLDER