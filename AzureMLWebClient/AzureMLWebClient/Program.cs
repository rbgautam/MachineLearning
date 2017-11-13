using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Net.Http.Formatting;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
namespace AzureMLWebClient
{


    // This code requires the Nuget package Microsoft.AspNet.WebApi.Client to be installed.
    // Instructions for doing this in Visual Studio:
    // Tools -> Nuget Package Manager -> Package Manager Console
    // Install-Package Microsoft.AspNet.WebApi.Client



    class Program
    {
        static void Main(string[] args)
        {
            InvokeRequestResponseService().Wait();
        }

        static async Task InvokeRequestResponseService()
        {
            using (var client = new HttpClient())
            {
                var scoreRequest = new
                {
                    Inputs = new Dictionary<string, List<Dictionary<string, string>>>() {
                        {
                            "input1",
                            new List<Dictionary<string, string>>(){new Dictionary<string, string>(){
                                            {
                                                "status_checking", "A11"
                                            },
                                            {
                                                "loan_duration", "6"
                                            },
                                            {
                                                "credit_history", "A34"
                                            },
                                            {
                                                "purpose", "A43"
                                            },
                                            {
                                                "credit_amount", "1169"
                                            },
                                            {
                                                "savings_amt", "A65"
                                            },
                                            {
                                                "emp_years", "A75"
                                            },
                                            {
                                                "percent_disp_income", "4"
                                            },
                                            {
                                                "status_sex", "A93"
                                            },
                                            {
                                                "other_debts", "A101"
                                            },
                                            {
                                                "residence_since", "4"
                                            },
                                            {
                                                "property", "A121"
                                            },
                                            {
                                                "age", "67"
                                            },
                                            {
                                                "other_installments", "A143"
                                            },
                                            {
                                                "housing_status", "A152"
                                            },
                                            {
                                                "num_credits", "2"
                                            },
                                            {
                                                "job_type", "A173"
                                            },
                                            {
                                                "num_dependant", "1"
                                            },
                                            {
                                                "own_telephone", "A192"
                                            },
                                            {
                                                "foreign_worker", "A201"
                                            },
                                            {
                                                "credit_risk", "1"
                                            },
                                }
                            }
                        },
                    },
                    GlobalParameters = new Dictionary<string, string>()
                    {
                    }
                };

                const string apiKey = "a6iQKlhRDvQ/U9LSMaA6iCMcgl4YwwjqqlCR3dPQ+2DebYNTpWRhFtgywSGmfMO1Vo2ubP3OqEzx03um1tGsnA=="; // Replace this with the API key for the web service
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);
                client.BaseAddress = new Uri("https://ussouthcentral.services.azureml.net/workspaces/8c68810612b849a994aec53eb470d02d/services/69bd399586ba43a98384b72bd9240b2b/execute?api-version=2.0&format=swagger");

                // WARNING: The 'await' statement below can result in a deadlock
                // if you are calling this code from the UI thread of an ASP.Net application.
                // One way to address this would be to call ConfigureAwait(false)
                // so that the execution does not attempt to resume on the original context.
                // For instance, replace code such as:
                //      result = await DoSomeTask()
                // with the following:
                //      result = await DoSomeTask().ConfigureAwait(false)

                HttpResponseMessage response = await client.PostAsJsonAsync("", scoreRequest);

                if (response.IsSuccessStatusCode)
                {
                    string result = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Result: {0}", result);
                }
                else
                {
                    Console.WriteLine(string.Format("The request failed with status code: {0}", response.StatusCode));

                    // Print the headers - they include the requert ID and the timestamp,
                    // which are useful for debugging the failure
                    Console.WriteLine(response.Headers.ToString());

                    string responseContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine(responseContent);
                }
            }
        }
    }
}