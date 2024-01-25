param location string = 'EastUS' // You can change this as needed
param appGatewayName string = 'your-app-gw' // Change it to your preferred name
param openaiEndpoints array = [
  'eastus.openai.azure.com'
  'francecentral.openai.azure.com'
  'japaneast.openai.azure.com'
  // Add more endpoints as necessary
]

param frontendPort int = 80 // Port for HTTP (Change to 443 for HTTPS)
param backendPort int = 443 // Port for the OpenAI endpoints

resource vnet 'Microsoft.Network/virtualNetworks@2021-05-01' = {
  name: 'myVnet'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        '10.0.0.0/16'
      ]
    }
    subnets: [
      {
        name: 'mySubnet'
        properties: {
          addressPrefix: '10.0.0.0/24'
        }
      }
    ]
  }
}

resource applicationGateway 'Microsoft.Network/applicationGateways@2021-05-01' = {
  name: appGatewayName
  location: location
  properties: {
    sku: {
      name: 'Standard_v2'
      tier: 'Standard_v2'
    }
    gatewayIPConfigurations: [
      {
        name: 'appGatewayIpConfig'
        properties: {
          subnet: {
            id: vnet.properties.subnets[0].id
          }
        }
      }
    ]
    httpListeners: [
      {
        name: 'appGatewayHttpListener'
        properties: {
          frontendIPConfiguration: { id: resourceId('Microsoft.Network/applicationGateways/frontendIPConfigurations', appGatewayName, 'appGatewayFrontendIp') }
          frontendPort: { id: resourceId('Microsoft.Network/applicationGateways/frontendPorts', appGatewayName, 'appGatewayFrontendPort') }
          protocol: 'Http'
          // Change this to 'Https' and configure SSL certificate if using HTTPS
        }
      }
    ]
    backendAddressPools: [
      {
        name: 'appGatewayBackendPool'
        properties: {
          backendAddresses: [for fqdn in openaiEndpoints: {
            fqdn: fqdn
          }]
        }
      }
    ]
    backendHttpSettingsCollection: [
      {
        name: 'appGatewayBackendHttpSettings'
        properties: {
          cookieBasedAffinity: 'Disabled'
          path: '/status-0123456789abcdef'
          port: backendPort
          protocol: 'Https'
          pickHostNameFromBackendAddress: true
          requestTimeout: 300
          // Other settings as needed
        }
      }
    ]
    urlPathMaps: [] // Customize according to your requirements
    // Define other settings like custom health probes, rewrite rules, etc.
    // Additional elements such as rules, SSL certificates, and more would also need to be included here
  }
}

// Additional configurations and dependencies might need to be added here based on the above setup

output appGatewayId string = applicationGateway.id
