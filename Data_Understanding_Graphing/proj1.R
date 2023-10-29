#install.packages("ggplot2")
library(ggplot2)
aisles = read.csv("aisles.csv")
departments = read.csv("departments.csv")
products_prior = read.csv("order_products__prior.csv")
products_train = read.csv("order_products__train.csv", sep=";")
orders = read.csv("orders.csv", sep = ";")
products = read.csv("products.csv", sep=";")
sample_submission = read.csv("sample_submission.csv")

products = na.omit(products)

ggplot(data = products, col = "blue", border = "black", aes(x = department_id)) + geom_histogram(bins = 40, fill = "light blue")+labs(title = "Frequency of Departments",
                                                                                                                                      x = "Department ID",
                                                                                                                                      y = "Frequency")
ggplot(data = products, col = "blue", aes(x=aisle_id))+ geom_histogram(bins = 100, fill = "light blue")+labs(title = "Aisle count",
                                                                                                       x = "Aisle ID",
                                                                                                       y = "Count")
ggplot(data = orders, aes(x=user_id))+ geom_histogram(bins = 10000, fill = "light blue")+labs(title = "Histogram of Users frequency",
                                                                        x = "User ID",y = "Frequency")
                                                                        
ggplot(data = orders, aes(x=days_since_prior_order))+ geom_histogram(bins = 60, fill = "light blue")+labs(title = "Histogram of days from last order",
                                                                                    x = "Number of days",
                                                                                    y = "Count")
