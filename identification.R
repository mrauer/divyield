data<-read.csv('output.dat')
names(data)[1:4]<-c("symbol", "history", "stdev", "divyield");

head(data)
nrow(data)

# We will only keep 10% percentile for stdev and 90% percentile for divyield.
top_stdev=quantile(data$stdev, 0.10)
top_divyield=quantile(data$divyield, 0.90)

data<-data[which(data$stdev<=top_stdev),]
nrow(data)

data<-data[which(data$divyield>top_divyield),]
nrow(data)

# Ordered by history in descending order.
data <- data[order(-data$history),]
data