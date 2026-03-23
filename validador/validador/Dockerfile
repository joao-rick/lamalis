FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine AS RUNTIME
LABEL authors="NicoleNogueira"
WORKDIR /app
EXPOSE 8080

COPY --from=build /app/target/*.jar /app/app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]