from flask import Flask, jsonify, request
# initialize our Flask application
app= Flask(__name__)
@app.route("/notify", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['ticketDetails']
        print(data["ticketId"])
        import requests
        import json

        url = "https://rimccsupport.teamcomputers.com/sdpapi/request"

        #subject = "Test Alexa Ticket"
        inputdata = {
            "operation": {
                "details": {
                    "Subject": "Test TTL Ebonding ticket_" + str(data["ticketId"]) +"_"+ str(data["description"]),
                    "requesttemplate": "Default Request",
                    "site": "Celebi",
                    "account": "Celebi"
                }
            }
        }

        payload = {"INPUT_DATA": json.dumps(inputdata), "OPERATION_NAME": "ADD_REQUEST",
                   "TECHNICIAN_KEY": "0A139C85-E91E-42C6-80C1-8D37BDE18AD1", "format": "json"}
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=payload)
        print(response.json())
        if response.json()["operation"]["result"]["status"] == "Success":
            ticket_number = response.json()["operation"]["details"]["workorderid"]
            priority = response.json()["operation"]["details"]["priority"]
            sla = response.json()["operation"]["details"]["sla"]
            impact = response.json()["operation"]["details"]["impact"]
            subject = response.json()["operation"]["details"]["subject"]

            print(
                "The following ticket has been created for you:-<br><br>Ticket Number:{}<br>Priority:{}<br>Subject:{}<br>Impact:{"
                "}<br>SLA:{}".format(ticket_number, priority, subject, impact, sla))

        return jsonify(str("Successfully stored  " + str(data)))
'''@app.route("/message", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " +  name + "!!!")'''
#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)
