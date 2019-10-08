# rbt_webapp
Web app for testing ICU Rule-Based Transliterators

Requires ICU(4C) and Python >=3.6 installed.

# Installation and running instructions

* Clone repo.
* Install dependencies:
  
  `pip3 install -r requirements.txt`

* Run:

  `python3 rbt_webapp.py`

* Navigate to: https://localhost:8000

By default, this will start the webserver at https://localhost:8000

To run on a different IP or port, run:

  `python3 rbt_webapp.py <IP> <port>`

# Basic Usage

* First, input a ruleset into the left-hand textbox. For RBT rule syntax, see [here](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classicu_1_1Transliterator.html#details)

* Next, input a test data string into "Test data" input box. Input expected result into "Expected".
  * To add more test strings, press the "+" button below the input box.
  * Note: Do not leave any of the test data or expected boxes empty, or bad things happen. By default, they are filled with a dash (-)

* Press the "Test" button or press `F5`. Output strings are displayed under "Output".
  * If the output does not match the expected result, it will be highlighted in yellow.
  * If the ruleset contains syntax errors, an alert will pop up with the error returned by ICU.

# Other features

* A rule file can be loaded using the file chooser above the ruleset textbox.

* A rule file can be saved by pressing "Save rule file", or pressing `Ctrl-S`.

* A preexisting ruleset can be selected using the dropdown menu below the rule textbox.
  * Note: Preexisting rulesets are pulled from the locally-installed version of ICU.
  * **CAUTION** By selecting an existing ruleset, whatever is currently in the ruleset textbox will be replaced by the new ruleset. Save your work!

* To run a "reverse" transliteration, check the "Reverse?" checkbox.

* To load test data from a file, use the "Load test data" file chooser above the test data.
  * Test data should be in a two-column Tab-separated Values format, with the first column being the test string and the second column being the expected output.

# Registering rulesets

* Registering a ruleset allows it to be called by ID from within a new ruleset, using the `::<ID>;` syntax (Existing rulesets can be called without needing to register them).

* To register the ruleset in the ruleset textbox, input an ID into the "Register with ID" textbox below the ruleset textbox, and then pressing "Register"

* Ruleset IDs should follow the ID syntax mentioned in the [ICU documentation](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classicu_1_1Transliterator.html#details)

* Ruleset IDs are unique. Attempting to register a ruleset with an ID that has already been used, or belongs to a preexisting ruleset, will result in an error alert.

* Once registered, a ruleset will now show up in the "Load existing ruleset" dropdown.
  * Note: When a preexisting ruleset is selected, the ruleset that ends up in the ruleset textbox is derived from the compiled version of the ruleset. As such, it will lose many details. Do not rely on this as a method to save your rulesets!
  
# TODO

- [ ] Fix the test data/expected textboxes so they don't screw up when empty.
- [ ] Allow registering reverse rulesets.
- [ ] Make rule syntax error alert less incomprehensible.
- [ ] Allow multiline test input.
