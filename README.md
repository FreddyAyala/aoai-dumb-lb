
# Azure OpenAI Dumb Load Balancing

aoai-kiss-lb (Azure OpenAI Keep It Simple Stupid Load Balancing) provides two practical solutions for distributing client requests across Azure OpenAI instances, helping to manage workloads and improve service resilience.

## Load Balancing Approaches

### Application Gateway Approach

When using Azure Application Gateway for load balancing Azure OpenAI services, keep in mind that while the intent is to evenly distribute traffic, variations in network latency and endpoint responsiveness may lead to some imbalance.

Configuration includes:

-   **Backend Pool:**  Enter a list of FQDNs of the desired Azure OpenAI endpoints.
-   **HTTP Settings:**  Enable HTTPS protocol with suitable timeouts and disable cookie-based affinity to promote round-robin traffic distribution.
-   **Listeners & Rules:**  Set up listeners for your chosen protocol (HTTP/HTTPS) and create rules to seamlessly direct traffic to the backend pool.
-   **Health Probes:**  Configure a custom health probe with a path that Azure OpenAI considers indicative of a healthy service, such as  `/status-0123456789abcdef`.
-   **Testing:**  Conduct tests with tools like Postman to monitor and verify round-robin behavior.
-   **Keyless Authentication:**  Set up Azure AD roles for keyless authentication to streamline secure access management.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FFreddyAyala%2Faoai-kiss-lb%2Fmain%2Finfra%2Fmain.json)

### Application Side Python Code Approach

This approach involves Python code for application-level request distribution among several OpenAI endpoints. This method is particularly advantageous for scenarios where you need immediate control over the load balancing logic within your application.

The provided Python script initializes a list of endpoints, each with its deployment name and API key if required. These endpoints are then shuffled to ensure random selection, simulating round-robin behavior without a predesigned sequence.

Requests are sent iteratively using  `send_request_to_random_endpoint`, which tries to obtain a response from one of the shuffled endpoints. If a request fails, the function retries up to a specified maximum number of attempts, cycling through the endpoints. This failover mechanism can help maintain service continuity in case of individual endpoint failures.

The  `send_request`  function handles the construction and dispatching of HTTP requests to a chosen endpoint. By incorporating the  `langchain`  package, the code supports interaction with Azure's OpenAI API, abstracting the complexity of direct API calls.

This example illustrates how to incorporate load balancing into your application's logic without deploying additional Azure infrastructure, maintaining flexibility and straightforward error handling.

## Usage

Evaluate your requirements and select the approach that fits best. For a managed, enterprise-level solution, opt for the Application Gateway approach. If you require fine-grained control within your application, consider the Python code method. Both offer distinct benefits and can be implemented as provided or customized for your specific use case.

## Contributing

We encourage contributions to enhance and evolve this project. If you have suggestions or encounter issues, please submit a pull request or raise an issue.

## License

This project is licensed under the MIT license.
## References

- https://www.raffertyuy.com/raztype/azure-openai-load-balancing/#keyless-authentication-for-code-using-microsoft-entra-id-formerly-azure-ad
- https://medium.com/microsoftazure/distribute-requests-to-azure-openai-service-c01784deb1cb
- https://journeyofthegeek.com/2023/05/31/load-balancing-in-azure-openai-service/