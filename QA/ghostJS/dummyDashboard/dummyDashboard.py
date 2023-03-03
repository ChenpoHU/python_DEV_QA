const Ghost = require('ghost');
const { expect } = require('chai');

describe('Dashboard', function() {
  let ghost;

  before(async function() {
    ghost = await Ghost.create();
  });

  after(async function() {
    await ghost.exit();
  });

  it('should display the dashboard page', async function() {
    const page = await ghost.openPage('https://dummyDashboard.com');

    // Ensure the dashboard title is displayed
    const dashboardTitle = await page.evaluate(() => document.querySelector('h1').textContent);
    expect(dashboardTitle).to.equal('Dashboard');

    // Check that the number of widgets is greater than 0
    const widgets = await page.evaluate(() => document.querySelectorAll('.widget').length);
    expect(widgets).to.be.greaterThan(0);

    // Verify that the user avatar is displayed
    const userAvatar = await page.evaluate(() => document.querySelector('.user-avatar').src);
    expect(userAvatar).to.include('example.com/images/avatar.png');

    await page.close();
  });

  it('should create a new widget', async function() {
    const page = await ghost.openPage('https://dummyDashboard.com');

    // Click the "Create Widget" button
    await page.click('.create-widget-button');

    // Fill out the widget form
    await page.type('#widget-name', 'My Widget');
    await page.select('#widget-type', 'Bar Chart');
    await page.click('#create-widget-button');

    // Verify that the new widget was added to the dashboard
    const newWidget = await page.evaluate(() => document.querySelector('.widget:last-child .widget-title').textContent);
    expect(newWidget).to.equal('My Widget');

    await page.close();
  });
});
