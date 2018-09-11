# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s shinkong.content -t test_category.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src shinkong.content.testing.SHINKONG_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/shinkong/content/tests/robot/test_category.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a category
  Given a logged-in site administrator
    and an add category form
   When I type 'My category' into the title field
    and I submit the form
   Then a category with the title 'My category' has been created

Scenario: As a site administrator I can view a category
  Given a logged-in site administrator
    and a category 'My category'
   When I go to the category view
   Then I can see the category title 'My category'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add category form
  Go To  ${PLONE_URL}/++add++category

a category 'My category'
  Create content  type=category  id=my-category  title=My category

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the category view
  Go To  ${PLONE_URL}/my-category
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a category with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the category title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
