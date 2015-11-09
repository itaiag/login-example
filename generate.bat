@echo off
echo Generating HTML reports
allure-cli\bin\allure.bat generate pytest-tests\reports\allure -o pytest-tests\reports\allure-reports

