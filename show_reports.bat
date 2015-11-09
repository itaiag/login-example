@echo off

echo Opening web server
allure-cli\bin\allure.bat report open -o pytest-tests\reports\allure-reports -p 8090