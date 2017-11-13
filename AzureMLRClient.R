library("RCurl")
library("rjson")

# Accept SSL certificates issued by public Certificate Authorities
options(RCurlOptions = list(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl")))

h = basicTextGatherer()
hdr = basicHeaderGatherer()

req =  list(
    Inputs = list(
            "input1"= list(
                list(
                        'status_checking' = "A11",
                        'loan_duration' = "6",
                        'credit_history' = "A34",
                        'purpose' = "A43",
                        'credit_amount' = "1169",
                        'savings_amt' = "A65",
                        'emp_years' = "A75",
                        'percent_disp_income' = "4",
                        'status_sex' = "A93",
                        'other_debts' = "A101",
                        'residence_since' = "4",
                        'property' = "A121",
                        'age' = "67",
                        'other_installments' = "A143",
                        'housing_status' = "A152",
                        'num_credits' = "2",
                        'job_type' = "A173",
                        'num_dependant' = "1",
                        'own_telephone' = "A192",
                        'foreign_worker' = "A201",
                        'credit_risk' = "1"
                    )
            )
        ),
        GlobalParameters = setNames(fromJSON('{}'), character(0))
)

body = enc2utf8(toJSON(req))
api_key = "a6iQKlhRDvQ/U9LSMaA6iCMcgl4YwwjqqlCR3dPQ+2DebYNTpWRhFtgywSGmfMO1Vo2ubP3OqEzx03um1tGsnA==" # Replace this with the API key for the web service
authz_hdr = paste('Bearer', api_key, sep=' ')

h$reset()
curlPerform(url = "https://ussouthcentral.services.azureml.net/workspaces/8c68810612b849a994aec53eb470d02d/services/69bd399586ba43a98384b72bd9240b2b/execute?api-version=2.0&format=swagger",
httpheader=c('Content-Type' = "application/json", 'Authorization' = authz_hdr),
postfields=body,
writefunction = h$update,
headerfunction = hdr$update,
verbose = TRUE
)

headers = hdr$value()
httpStatus = headers["status"]
if (httpStatus >= 400)
{
print(paste("The request failed with status code:", httpStatus, sep=" "))

# Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
print(headers)
}

print("Result:")
result = h$value()
print(fromJSON(result))