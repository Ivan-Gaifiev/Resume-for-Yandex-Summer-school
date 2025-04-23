library(shiny)
library(demography)

ui <- fluidPage(

    # Application title
    titlePanel("France deaths in 2001 Data"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("year",
                        "Choose the year:",
                        min = 1950,
                        max = 2000,
                        value = 10)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("Hist")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    output$Hist <- renderPlot({
      france <- extract.ages(fr.mort, 0:110, FALSE)
      france_2001 <- extract.years(france, input$year)
      
      plot(france_2001)
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
