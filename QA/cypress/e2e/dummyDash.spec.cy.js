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
  
  it('should have an external link pointing to the right domain', () => {
    // Ensure the external link is visible and has the correct attributes
    cy.get('[data-cy="dashboard-external-link"]').should('be.visible')
      .find('a')
      .should('contain', 'webtips.dev')
      .and('have.attr', 'href', 'https://webtips.dev/')
      .and('have.attr', 'target', '_blank');
  });

  it('validates and formats first name', () => {
    // Enter the first name and ensure it is validated and formatted correctly
    cy.get('[data-cy="dashboard-first-name-input"]').type('johnny')
      .should('have.attr', 'data-validation', 'required')
      .and('have.class', 'active')
      .and('have.value', 'Johnny');
  });
});
