javac -classpath `hadoop classpath` -d classes src/WordCount.java
jar -cvf wordcount.jar -C classes/ .
