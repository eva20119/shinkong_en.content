# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s shinkong.content -t test_polyester.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src shinkong.content.testing.SHINKONG_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/shinkong/content/tests/robot/test_polyester.robot
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

Scenario: As a site administrator I can add a polyester
  Given a logged-in site administrator
    and an add polyester form
   When I type 'My polyester' into the title field
    and I submit the form
   Then a polyester with the title 'My polyester' has been created

Scenario: As a site administrator I can view a polyester
  Given a logged-in site administrator
    and a polyester 'My polyester'
   When I go to the polyester view
   Then I can see the polyester title 'My polyester'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add polyester form
  Go To  ${PLONE_URL}/++add++polyester

a polyester 'My polyester'
  Create content  type=polyester  id=my-polyester  title=My polyester

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the polyester view
  Go To  ${PLONE_URL}/my-polyester
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a polyester with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the polyester title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
