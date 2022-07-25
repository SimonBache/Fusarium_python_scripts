library('stringr')
library("ggplot2")

data <- read.csv("CAV3049_SMARTDENOVO_STEP_CORRECTION_MEDAKA_effector_per_contig.txt")
data$chromosome <- factor(data$chromosome, levels = data$chromosome)
data$effector_prop = as.numeric(data$effector_prop)

ggplot(data) + geom_bar(aes(x = chromosome, y = effector_prop), stat = "identity", fill = "goldenrod3")+
  ggtitle("D")+
  theme_bw()+
  ylim(0,8)+
  ylab("effector proportion (%)")+
  xlab("contig")+
  theme(axis.text = element_text(size = 10),
        axis.title = element_text(size = 14, face = "bold"),
        plot.title = element_text(size = 21, face = "bold"))
