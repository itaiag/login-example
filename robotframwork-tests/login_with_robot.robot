*** Settings ***
Library           Selenium2Library
Resource          pages/loginPage.txt
Resource          pages/webdriver.txt
Resource          pages/registerPage.txt
Resource          pages/dashboardPage.txt

*** Test Cases ***
Test register new user
    [Documentation]    Test simple siginin and login
    [Tags]    itai    regression    signup
    [Setup]    Webdriver.Init webdriver    # Initiliaze the webdriver
    loginPage.Verify location
    loginPage.Click on register lnk
    registerPage.Do register    Itai    Agmon    itaiag    password
    loginPage.Do login    itaiag    password
    dashboardPage.Verify location
    dashboardPage.Click on delete user lnk    itaiag
    dashboardPage.Click on logout btn
    loginPage.Verify location
    [Teardown]    Close Browser

Test login with wrong user name and password
    [Documentation]    Test wrong user name behaviour
    [Tags]    itai    regression    negative    signin
    [Setup]    Webdriver.Init webdriver
    loginPage.Verify location
    loginPage.Type to username tb    Wrong user name
    loginPage.Type to password tb    Wrong password
    loginPage.Click on login btn
    loginPage.Verify location
    ${text}    loginPage.Get alert message text
    Should Be Equal    ${text}    Username or password is incorrect
    [Teardown]    Close Browser
