# python_DEV_QA
Project based python tutorial of development and QA of python based application. 

## 1. Dev Projects
### 1.1 A console game called treasure box
### 1.2 Use Selenium to automate a download task

## 2. QA Projects
### 2.1 Testing Pyramid [1]
![alt text](https://github.com/ChenpoHU/python_DEV_QA/blob/main/Asset/img/testPyramid.png)

### 2.2 QA Tools Setup and Start
#### 2.2.1 Cypress
To install cypress, run:
``` 
cd /{$yourPath}/PYTHON_DEV_QA/QA
npm install cypress --save-dev 
```

To run cypress:
use 
``` 
npx cypress open 
```
to run with builtin browser in cypress

or use 
``` 
npx cypress run 
```
#### 2.2.2 Selenium
To install selenium, run:
``` 
pip install selenium
```
To run the code： 

``` 
python test.py
```

#### 2.2.2 Cypress Good Practices
- https://www.webtips.dev/webtips/cypress/cypress-best-practices
- https://docs.cypress.io/guides/references/best-practices
- https://www.lambdatest.com/blog/cypress-best-practices/

### 2.3 Selenium vs. Cypress

FEATURE | SELENIUM | CYPRESS
------------- | ------------- | -------------
Execution Speed	| Slow	| Fast as Cypress scripts are executed within the browser.
Time Travel| 	Not supported	| Supported
Real time reloads| 	Not supported	| Tests are reloaded when any change is made in the test implementation.
Automatic Waiting	| Not supported	No requirement to add waits or sleep in the tests. | Cypress automatically waits for commands and assertions before moving to the next instruction.
Default Screenshots and Videos| 	Not available by default, developer has to write code to achieve the same. | Available by default
Network Traffic Control	Not supported	| No network lag as tests are executed within the browser. | You can control, stub, and test edge cases without any involvement of the server.
Access to elements outside the DOM	| Access only to the elements in the DOM | A unique DOM manipulation technique helps Cypress in getting access DOM elements, timers, service workers, and more.
Documentation, Community| 	Mature Community with multiple points of support. | Average Documentation	Growing Community, Excellent Documentation
Remote Execution | Supported. Cloud-based Selenium Grid from LambdaTest can be used to expedite cross browser testing and automation testing | Not supported
Spies, stubs, and clocks| 	Not available	| Cypress lets you control the behavior of functions, timers, and server responses with ease.
Mobile Testing	| Mobile Testing with Appium	| Not supported
Test Flakiness| 	Tests can be flaky	| With Cypress, tests are expected to be non-flaky.
Programming Languages| Python, C#, Java, Python, Ruby, JavaScript | JavaScript
Browser Support	| Chrome, Firefox, Internet Explorer, Microsoft Edge, Safari | Brave, Chrome, Edge, Firefox, Electron
Test Frameworks	| PyUnit, JUnit, TestNG, JBehave, Behave, Gauge, Specflow, NUnit, Robot, and more. | Mocha JS
Test Setup | Selenium Grid Server and browser drivers have to be installed in the test machine. Setup is different for a cloud-based Selenium Grid where only browser drivers have to be installed on the test machine. | Node JS, Mocha JS, and Cypress have to be installed on the test machine.
Arena of testing| 	Unit testing, security testing, and integration testing	| Unit testing, security testing, and integration testing
Integrations| 	Wide range of integration options – CI/CD tools, reporting tools, and more.	| Limited integration support with CI/CD tools when compared to Selenium.
Driver Dependencies	| Appropriate browser driver has to be installed so that the test script can talk to the corresponding web browser.	| No driver dependency.
Parallel testing| 	Supported	| Supported
Multi Tabs| 	Supported	| Not supported
Multiple browser instances| 	Supported| 	Not supported [2]

Cypress is preferred over Selenium when one need:
- Single Framework for Component, API, End to End, Visual, Accessibility, Performance testing
- Video recording capability of test execution
- Out of the box retry capability of actions performed over elements, which reduces flaky test for Cypress
- Single Programming language across development (Front end) and Automation
- Capability to Mock/Stub Request and Responses during early stage of development
- Save time building framework from Scratch with Selenium, as Cypress provides stable and ready to use Framework with everything wrapped and ready to use functions
- Test Runner which provides time travel capability to go through individual step with before and after screenshots attached to debug failures
- Meaningful exceptions when any test fails

Selenium is preferred over Cypress when one need:
- When one need flexibility in terms of choosing test script language. Cypress supports on JavaScripts, while Selenium supports several languages like Java, Python, JavaScript, C#, etc.
- When you need to run a test case on different browsers simultaneously then Selenium Grid works the best, since Cypress cannot be used to drive two browsers at the same time.
- Cross browser testing at scale becomes easy with Selenium. Cypress does not support browsers like Safari, which restricts the cross browser testing support, when compared to Selenium.
- Selenium supports NUnit and JUnit that are not supported by [3]

## 3. Others
### 3.1 The commit type can include the following
Type  | Explanation
------------- | -------------
feat | a new feature is introduced with the changes
fix | a bug fix has occurred
chore | changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
refactor | refactored code that neither fixes a bug nor adds a feature
docs | updates to documentation such as a the README or other markdown files
style | changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
test | including new or correcting previous tests
perf | performance improvements
ci | continuous integration related
build | changes that affect the build system or external dependencies
revert | reverts a previous commit
### 3.2 Tree
![alt text](https://github.com/ChenpoHU/python_DEV_QA/blob/main/Asset/img/tree.png)

Sources: 
- [1]https://martinfowler.com/bliki/TestPyramid.html, last accessed on 03.03.2023
- [2]https://www.browserstack.com/guide/cypress-vs-selenium, last accessed on 03.03.2023
- [3]https://www.lambdatest.com/blog/cypress-vs-selenium-comparison/, last accessed on 03.03.2023
