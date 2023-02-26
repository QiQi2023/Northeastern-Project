###

### MISM 6210 - 36993 - Spring 2023

### Analysis 01 - Yang QiQi
###Analyzing the Effectiveness of Limited Signal Message
library(stargazer)
library(tidyverse)
library(lfe) 
library(readxl)
library(ggplot2)

file_path <- "/Users/kiki/Downloads/analyis01_data.xlsx"
df <- tibble(read_excel(file_path, sheet = "Sheet 1"))

### summary statistics of variables
##Mean of variables
df %>%
  group_by (signals_allocated) %>%
  dplyr :: summarize(across(c(signals_sent, messages_sent, messages_replies, dates_reported), mean))
##Mode of Left_platform column
find_mode <- function(x) {
  u <- unique(x)
  tab <- tabulate(match(x, u))
  u[tab == max(tab)]
}
data <- df$left_platform
##Count of left platform 
find_mode(data)
df %>% count(left_platform)

### Plots

ggplot(df, aes(y = left_platform, x = as.factor(signals_allocated))) +
  geom_bar(stat="summary", fun="mean") +
  ggtitle("User Retention") + 
  xlab("Group") +
  ylab("Left platform")




