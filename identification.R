data<-read.csv('output.dat')
names(data)[1:8]<-c("symbol", "history", "stdev", "div_yield",
                    "stock_price", "num_stock", "per_stock",
                    "yearly_gain");
head(data)
nrow(data)

"""
We will only keep:
* 10% percentile for stdev
* 90% percentile for divyield
* 90% percentile for the yearly gain
"""
bottom_stdev=quantile(data$stdev, 0.10)
top_divyield=quantile(data$div_yield, 0.90)
top_yearly=quantile(data$yearly_gain, 0.90)
# Bottom stdev.
data<-data[which(data$stdev<=bottom_stdev),]
nrow(data)
# High Div Yield.
data<-data[which(data$div_yield>top_divyield),]
nrow(data)
# High yearly gain.
data<-data[which(data$yearly_gain>top_yearly),]
nrow(data)

# Ordered by history in descending order.
data <- data[order(-data$history),]
data.frame(data$symbol,data$history, data$num_stock, data$yearly_gain)