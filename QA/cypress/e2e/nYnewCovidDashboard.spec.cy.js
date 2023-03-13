describe('NY Times COVID Cases Interactive Page', () => {
  it('Loads and displays data correctly', () => {
    cy.visit('https://www.nytimes.com/interactive/2021/us/covid-cases.html')

    // Confirm that the map is visible and interactive
    cy.get('h1').invoke('text').should('be.visible')
    cy.get('h1').invoke('text').should('have.length.gt', 0)  // gt == greater than
    cy.get('h1').invoke('text').should('not.be.empty')       // not.be.empty == NOT "" 
    cy.get('h1').should('not.have.text', "")     
    cy.get('h1').should('include.text','Coronavirus')

    // Close the state data popup
    cy.get('.close-btn').click()

    // Confirm that the popup is no longer visible
    cy.get('.state-data').should('not.be.visible')
  })
})