data<-read.csv('output.dat')
names(data)[1:9]<-c("symbol", "history", "stdev", "div_yield",
                    "stock_price", "num_stock", "per_stock",
                    "yearly_gain", "ratio");
head(data)
nrow(data)

"""
We will only keep:
* 20% percentile for stdev
* 85% percentile for the yearly gain
* 75% percentile for the ratio
"""
bottom_stdev=quantile(data$stdev, 0.20)
top_yearly=quantile(data$yearly_gain, 0.85)
top_ratio=quantile(data$ratio, 0.75)
# Bottom stdev.
data<-data[which(data$stdev<=bottom_stdev),]
nrow(data)
# High yearly gain.
data<-data[which(data$yearly_gain>top_yearly),]
nrow(data)
# Close to all time high.
data<-data[which(data$ratio>top_ratio),]
nrow(data)

# Ordered by history in descending order.
data <- data[order(-data$history),]
data.frame(data$symbol,data$history, data$num_stock, data$yearly_gain, data$ratio)
