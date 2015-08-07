# login-example

Example for using page object design pattern in the Python language



## Installation

The project dependencies are specified in the requirements.txt file.

~~~~
> pip install -r requirements.txt
~~~~

## Launching the server
Make sure you have Java JRE installed on your machine

~~~~
> cd demo-server\bin
> run.bat
~~~~

## Running the tests
~~~~
> cd LoginExample
> py.test
~~~~

## Generating reports
Download the latest version of the [Allure-cli](https://github.com/allure-framework/allure-cli/releases/tag/allure-cli-2.3), 
and extract it.

~~~
> cd <path>/allure-cli
> bin\allure <login-example-project-path>\LoginExample\reports\allure
~~~

The HTML reports will be generated in the allure folder.

**Notice:** The reports can not be viewed in the Chrome browser. Try Firefox

