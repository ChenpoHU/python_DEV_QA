describe('Dashboard', () => {
    beforeEach(() => {
      cy.visit('/dashboard')
    })
  
    it('displays the correct title', () => {
      cy.get('h1').should('contain', 'My Dashboard')
    })
  
    it('displays a widget', () => {
      cy.get('.widget').should('be.visible')
    })
  
    it('displays the correct data in the widget', () => {
      cy.get('.widget').should('contain', 'Widget Data')
    })
  
    it('allows the user to create a new widget', () => {
      cy.get('#new-widget-button').click()
      cy.get('#widget-name-input').type('New Widget')
      cy.get('#widget-type-select').select('Bar Chart')
      cy.get('#create-widget-button').click()
      cy.get('.widget').should('contain', 'New Widget')
    })
  })  