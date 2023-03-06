describe('Dashboard', () => {
  before(() => {
    // Log in using cy.request
    cy.request('POST', '/login', {
      email: 'test@email.com',
      pass: 'testPass',
    }).as('login');
    cy.wait('@login');
  });

  beforeEach(() => {
    // Visit the dashboard page before each test
    cy.visit('/dashboard');
  });

  it('displays the dashboard page', () => {
    // Ensure the dashboard page is visible and has the correct elements
    cy.get('[data-cy="dashboard-page"]').should('be.visible');
    cy.get('[data-cy="dashboard-title"]').should('be.visible');
    cy.get('[data-cy="dashboard-links"]').should('be.visible');
    cy.get('[data-cy="dashboard-links"]').find('[data-test-id="link"]').should('have.length', 3);
  });

  it('navigates to the correct link when clicked', () => {
    // Click the first link and ensure the user is redirected to the correct page
    cy.get('[data-cy="dashboard-links"]').find('[data-test-id="link"]').first().click();
    cy.url().should('include', '/link1');

    // Go back to the dashboard and click the second link
    cy.go('back');
    cy.get('[data-cy="dashboard-links"]').find('[data-test-id="link"]').eq(1).click();
    cy.url().should('include', '/link2');

    // Go back to the dashboard and click the third link
    cy.go('back');
    cy.get('[data-cy="dashboard-links"]').find('[data-test-id="link"]').eq(2).click();
    cy.url().should('include', '/link3');
  });
});
