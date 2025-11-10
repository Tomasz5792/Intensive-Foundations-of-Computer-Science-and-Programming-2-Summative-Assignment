# Add item to table app Application Documentation

Welcome to the Add item to table app Application repository! This Tkinter-based GUI application allows users to enter a row into a table.

## Table of Contents
- [Introduction](#introduction)
- [Design](#design)
  - [GUI Design](#gui-design)
    - [Screen mockups](#screen-mockups)
  - [Requirements Document](#requirements-document)
    - [Functional Requirements](#functional-requirements)
    - [Non-Functional Requirements](#non-functional-requirements)
  - [Tech Stack Outline](#tech-stack-outline)
  - [Code Design Document](#code-design-document)
- [Testing Strategy](#testing-strategy)
- [References](#references)

# Introduction

I work at DEFRA, the Department for the Environment, Food and Rural Affairs.  DEFRA is a large government department responsible for safeguarding the natural environment, supporting farming and protecting the countryside.  Within DEFRA I work in a small business support team where my role is to use Microsoft power platform tools such as PowerApps, Power BI and Power Automate to improve the efficiency of the teams we support.  One of our teams’ tasks is to find people to be seconded when needed, the problem is that the data is scattered across multiple locations and is inconsistent, the “Add Item to Table App” is designed to solve this problem.

DEFRA’s corporate structure is sprawling, massive and ever changing, it is split into Director General areas, then directorates, then teams.  The organisation is a massive bureaucracy with a heavy emphasis on compliance making it unwieldy and inefficient.  To counter this the Digital Data and Technology Service, DDTS, are pushing a strategy to promote automation, innovation and data integrity.  Currently a lot of processes rely on data in an Excel file on someone’s desktop or data within an external companies database which we aren’t allowed to access.

Our team need to find people with certain skills, location and other variables to be seconded into emergency roles, the problem is that this takes a lot of time and is inefficient.  The data is spread around in different places, in some places the data is duplicated or inconsistent.  This whole process is much more time consuming than it needs to be due to the difficulty finding the data along with the time lost verifying it is correct.  Overall, this is not just a technical issue but also requires people to change how they work.

The proposed solution is a Python- based graphical user interface (GUI) application developed using Tkinter and CustomTkinter.  The application will serve as a centralised platform for data entry and data management, enabling users to input the required information easily and efficiently.  The application will also involve integrated data validation such as pattern checking using regular expressions for formatting names or phone numbers.  Input validation ensures standardised entries such as capitalised names or phone numbers in the correct formats.  This approach supports data integrity while providing an intuitive interface that enhances user experience while minimising input errors.  Attention will also be placed making the application accessible, for example, using a 4.5:1 contrast.

The data validation improves data integrity and saves time that would be spent correcting the data.  It also aligns with DEFRAS data governance and accessibility standards along with DDTS’s strategy to promote automation and data integrity.  There is also potential to integrate the app with other department systems such as Power Automate or Power BI.

On reflection it is important to involve the future users of the application when creating it as early as possible to make sure you are making something they want.  It is also a good idea to keep the code modular as to limit the amount of rework when something is changed.

In conclusion this project demonstrates innovation and aligns with DEFRA’s strategies.  


##  Empathy map

### Says
We are wasting time looking for data.
The date isn't correct or consistent.

### Thinks
If all the data were in one place and correct, it would save time.
Will everyone want to use a new system?

### Does
Spends time searching in different places for information.
Double-checks information for accuracy.

### Feels
Frustrated at the inefficiency of this and the duplication of effort.
Anxious about data accuracy.

### Pain
Frustrations:  Scattered and inconsistent data.
Obstacles:  Resistance to change.

### Gain
Goal:  To create a centralised platform.
Desired Outcome:  Improved accuracy and efficiency.


# Design

## GUI Design

### Screen mockups

The app was prototyped using [Figma](https://www.figma.com/design/PMYPoYa4koSNLf0LBXGbHx/Apps?node-id=4001-2960&p=f&t=P8jyBnSRsRnxKFNO-0).

![mockups](Formative_Figma_Diagram.png)

## Requirements Document

### Functional Requirements

- The application shall display a window titled "Add item to table app".
- The application window shall have dimensions 1200x600 pixels.
- The background color of the application window shall be white or dark grey depending on light mode.
- The application shall display a label with the text "Enter a new item".
- The application shall provide an input field for the user to enter information for 3 rows.
- The application shall provide a "Submit" button. When clicked, the button shall trigger the action to save the item to a table.
- The appliation shall have appropriate data input such as dropdowns or text input.

#### Future Functional Requirements
 - Incluse a day night mode
 - The application shall allow deleting of items.
 - Show and hide add item bar.

#### Future Accessibility Requirements
  - Font and text resizing
  - Colour changes for specific types of colourblind or 

### Non-Functional Requirements

- The application shall have an intuitive and user-friendly interface.
- The application shall respond to user input within 1 second.
- The application shall handle invalid input gracefully without crashing.
- The application code shall be well-structured and documented.
- The application shall run on any system that supports Python and Tkinter.
- The application shall use appropriate font sizes and color contrasts for readability.
- The application design shall allow for easy addition of new features.

#### Accessibility Requirements

 - All text and interactive elements shall maintain a minimum 4.5:1 colour contrast ratio against their background, in accordance with WCAG 2.1 AA standards.
 - All screens shall maintain consistent navigation and layout.

#### Future Non-Functional Requirements
  - I would like this to change when the screen size changes not just on loading the data



## Tech Stack Outline

UI / GUI:
- Python with Tkinter and CustomTkinter
  - [customtkinter documentation](https://customtkinter.tomschimansky.com/documentation/appearancemode)  
  - [Adding a table](https://github.com/TomSchimansky/CustomTkinter/discussions/431)

App logic:
- Python object orientated programming, OOP structure

Data:
- CSV File

Data validation:
- regular expressions (regex)


## Code Design Document

The code design is summarised in the class diagram below.

The `App_Window` class inherits from the `ctk.CTk` class, which provides the foundational GUI window functionality. This inheritance allows `App_Window` to use and extend the methods and attributes of `ctk.CTk` to create a customised application window with specific features.  All the other classes are placed inside this class.

The `Frame` and `Table` class inherits from the `ctk.CTkFrame` class, which provides foundational responsive component functionality. This inheritance allows `Frame` and `Table` to be placed inside themselves in order to create a reponsive app. `Frame` is extended with flaxible layout and colour option and `Table` is extended with an interactive tkinter table.

`InputText` extends `ctk.CTkEntry` by adding reusable methods for retrieving and clearing user input.
`InputName` further extends `InputText` with name-specific validation logic, for example capitalisation and no numbers.
`InputTelephoneNo` also extends `InputText`, adding validation rules for UK telephone formats.

Together these classes provide a modular and maintainable aproach to handling user input and data validation.

![class-diagram](InheritanceDiagram2.png)


# Testing Strategy

This testing strategy will aim to produce a piece of software which is usable, reliable with few bugs and is easy to use.

This testing will be continuous throughout the development of the software.  When I finish a piece of code, I will test to see if it works as intended.

The testing will be split into two different areas, functional testing which makes sure the software does what it is supposed to, for example checks the phone number or adds a person to the csv file, and non-functional testing which is how the software preforms, how secure and how usable it is, for example if colour blind people can see the text in the app and if the app is responsive when resized.

I will employ a combination of manual testing and automated testing, the automated testing I shall do with the unit test framework.  I shall manually test both functional and non-functional requirements as I develop, making sure that when I add a component frame, it resizes correctly, or when I add a button, it’s the correct colour and fits the space properly.  I will also manually test that the software recognises inputs are in the correct layout, for example, British telephone numbers.  I can’t possibly test that many, though, so I will also use the unit test framework to automate the checking of 20 correct and 20 incorrect inputs. Then, if the tests fail, I will update the code so that all the tests pass, removing a bug.

I will use the linting and code quality checks present in Visual Studio Code.  Also, due to the nature of this project, I shall do the user acceptance testing, as there are no users, comparing the app to the planned functional and non-functional requirements.
In conclusion, I will manually test, comparing the app to the requirements, then use unit tests to check the input validation. 
