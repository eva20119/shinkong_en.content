# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s shinkong.content -t test_product.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src shinkong.content.testing.SHINKONG_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/shinkong/content/tests/robot/test_product.robot
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

Scenario: As a site administrator I can add a product
  Given a logged-in site administrator
    and an add product form
   When I type 'My product' into the title field
    and I submit the form
   Then a product with the title 'My product' has been created

Scenario: As a site administrator I can view a product
  Given a logged-in site administrator
    and a product 'My product'
   When I go to the product view
   Then I can see the product title 'My product'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add product form
  Go To  ${PLONE_URL}/++add++product

a product 'My product'
  Create content  type=product  id=my-product  title=My product

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the product view
  Go To  ${PLONE_URL}/my-product
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a product with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the product title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
