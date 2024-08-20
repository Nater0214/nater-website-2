pipeline {
    agent any
    parameters{
        string(name: "IMAGE_NAME", defaultValue: "nater-website", description: "Docker image name")
        string(name: "IMAGE_TAG", defaultValue: "latest", description: "Docker image tag")
    }
    environment {
        REGISTRY_CREDENTIALS = "NaterRegistryCredentials"
        REGISTRY_URL = "https://docker.nater0214.com"
    }
    stages{
        stage("Build") {
            steps {
                docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}")
            }
        }
        stage("Push") {
            steps {
                docker.withRegistry("${env.REGISTRY_URL}", "${env.REGISTRY_CREDENTIALS}") {
                    docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").push()
                }
            }
        }
    }
}