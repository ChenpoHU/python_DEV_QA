describe('diagrams.net', () => {
  beforeEach(() => {
    cy.visit('https://app.diagrams.net');
  });

  it('should load the app', () => {
    cy.get('#app').should('be.visible');
  });

  it('should create a new diagram', () => {
    // Click the "New Diagram" button
    cy.get('#newDiagramButton').click();

    // Check that the new diagram modal is visible
    cy.get('#newDiagramModal').should('be.visible');

    // Enter a name for the new diagram and click "Create"
    cy.get('#newDiagramNameInput').type('My New Diagram');
    cy.get('#newDiagramCreateButton').click();

    // Check that the diagram canvas is visible
    cy.get('#mxGraph').should('be.visible');
  });

  it('should open an existing diagram', () => {
    // Click the "Open Existing Diagram" button
    cy.get('#openExistingDiagramButton').click();

    // Check that the "Open Diagram" modal is visible
    cy.get('#openExistingDiagramModal').should('be.visible');

    // Select the first diagram in the list and click "Open"
    cy.get('#openExistingDiagramList li').first().click();
    cy.get('#openExistingDiagramOpenButton').click();

    // Check that the diagram canvas is visible
    cy.get('#mxGraph').should('be.visible');
  });

  it('should save a diagram', () => {
    // Create a new diagram
    cy.get('#newDiagramButton').click();
    cy.get('#newDiagramNameInput').type('My New Diagram');
    cy.get('#newDiagramCreateButton').click();
    cy.get('#mxGraph').should('be.visible');

    // Click the "Save" button and check that the "Save Diagram" modal is visible
    cy.get('#saveDiagramButton').click();
    cy.get('#saveDiagramModal').should('be.visible');

    // Enter a name for the diagram and click "Save"
    cy.get('#saveDiagramNameInput').type('My Saved Diagram');
    cy.get('#saveDiagramSaveButton').click();

    // Check that the "Diagram Saved" message is visible
    cy.get('#saveDiagramSuccess').should('be.visible');
  });

  it('should export a diagram as an image', () => {
    // Create a new diagram
    cy.get('#newDiagramButton').click();
    cy.get('#newDiagramNameInput').type('My New Diagram');
    cy.get('#newDiagramCreateButton').click();
    cy.get('#mxGraph').should('be.visible');

    // Click the "Export as Image" button and check that the "Export Diagram as Image" modal is visible
    cy.get('#exportAsImageButton').click();
    cy.get('#exportAsImageModal').should('be.visible');

    // Click the "Export" button and check that the image is downloaded
    cy.get('#exportAsImageExportButton').click();
    cy.wait(5000); // Wait for the download to complete
    cy.readFile('cypress/downloads/My_New_Diagram.png', 'binary')
      .then((file) => {
        expect(file.length).to.be.greaterThan(0);
      });
  });
});