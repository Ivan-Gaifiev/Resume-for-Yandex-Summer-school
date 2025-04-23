# # ctrl+shift+c - comment code
# library(skimr)
# table <- read.csv("C://Users/Evanshow/Downloads/anti_pro_2021_v2_cities.csv")
# # str(table)
# # skim(table)
# # table[table==999.0] <- NA
# # count<-sum(is.na(table[[14]]))
# # print(count/nrow(table))
# # table <- as.Date(table$ДАТА.РОЖДЕНИЯ)
# # class(table$ДАТА.РОЖДЕНИЯ)
# table(table$РЕЛИГИЯ)/nrow(table)*100

# library(haven)
# library(psych)
# table <- read_sav("C:/Users/Evanshow/OneDrive/Рабочий стол/table.sav")
# # describe(table$NAS_VOZR)
# str(table)

# library(labeling)
# library(haven)
# library(ggplot2)
# data <- read_sav("C:/Users/Evanshow/OneDrive/Рабочий стол/table.sav")
# ggplot()+geom_histogram(data = data, aes(x=str_r), binwidth=1, fill="#69b3a2", color="#e9ecef", alpha=0.9 ) + theme_minimal() +
#   ggtitle("Countries of birth") +
#   labs(y = "Population", x = "Countries") +
#   theme( 
#     title = element_text(size = 12),
#     axis.title.x = element_text(size=12) 
#   )

# library(plotly)     
# library(ggplot2)
# data <- read.csv("C:/Users/Evanshow/OneDrive/Рабочий стол/Krupnie_goroda-RF_1985-2019_187_09.12.21/data.csv", sep = ";")
# graph <- plot_ly(data, x = ~wage, y = ~crimes)
# print(graph)

# library(ggthemes)
# library(readxl)
# library(tidyverse)
# 
# mean_fert <- read_excel("C:/Users/Evanshow/OneDrive/Рабочий стол/Rus_CMAB 1932-1984.xlsx", skip = 2)
# completed_fert <- read_excel("C:/Users/Evanshow/OneDrive/Рабочий стол/Rus_CCF 1932-1984.xlsx", skip = 2)
# 
# View(mean_fert)
# View(completed_fert)
# 
# df <- right_join(mean_fert, completed_fert, by = "Cohort")
# View(df)
# 
# ggplot(data = df, aes(x ='Cohort', y = 'CMAB40')) + geom_line()


# library(shiny)
# library(HMDHFDplus)
# library(dplyr)
# library(tidyr)
# library(ggpllot2)
# 
# ui <- navbarPage(
#   titlePanel("HMD vizualization tool"),
#   theme = bslib::bs_theme(bootswatch = "sandstone"),
#   
#   tabPanel("Data", 
#   sidebarLayout(
#     sidebarPanel(selectInput("state",
#                              "select the population",
#                              choices = getHMDcountries()$Country),
#                  selectInput("year",
#                              "Select the year",
#                              choices = NULL)),
#     mainPanel(h4("Population data"),
#               tableOutput(outputId = "pop_table"))
#   )
#   tabPanel("Population",
#            plotOutput("pop_pyramid", width = "800px", height = "600px"))
# )
# 
# server <- function(input, output){
#   
#   logdass <- read.table("logpass.txt")
#   login <- logpass[1,]
#   pass <- logpass[2,]
#   
#   code <- reactive(getHMDcountries()$CNTRY [getHMDCountries()$Country == input$state])
#   
#   string <- reactive(paste0("the country is ", input$state, "The code is ", code()))
#   
#   output$sel_cntry <- renderText(string()) # string as function
#   
#   pop_data <- reactive(readHMDweb(code(), "Exposures_1x1", username = login, password = pass))
#   
#   observeEvent(pop_data(), {
#     req(pop_data())
#     years <- unique(pop_data()&Year)
#     updateSelectInput(session, "year", choices = sort(years))
#   })
#   
#   pop_data_fil <- reactive({
#     req(pop_data(), input$year)
#     pop_data() %>%
#       filter(Year == as.numeric(input$year))
#   })
#   
#   output$pop_table <- renderTable(head(pop_data()))
#   
#   # тут много кода для отрисовки пирамиды
# }
# 
# shineApps(ui=ui, server=server)


library(demography)

france <- extract.ages(fr.mort, 0:110, FALSE)
france_2001 <- extract.years(france, 2001)

plot(france_2001)


