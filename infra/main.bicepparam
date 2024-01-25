using './main.bicep'

param location = 'EastUS' // You can change this as needed
param appGatewayName = 'your-app-gw' // Change it to your preferred name
param openaiEndpoints = [
  'eastus.openai.azure.com'
  'francecentral.openai.azure.com'
  'japaneast.openai.azure.com'
]
param frontendPort = 80 // Port for HTTP (Change to 443 for HTTPS)
param backendPort = 443 // Port for the OpenAI endpoints

