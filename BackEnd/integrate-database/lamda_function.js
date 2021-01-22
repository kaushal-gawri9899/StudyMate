var aws = require('aws-sdk');
var ddb = new aws.DynamoDB({apiVersion: '2012-10-08'});

exports.handler = async (event,context) => {
    // TODO implement
    print(event);
    
    let data = new Date();
    let uni = "None";
    let org = "None";
    const tableName = process.env.TABLE_NAME;
    const region = process.env.REGION;
    
    console.log("table=" + tableName + " -- region=" + region);
    
    aws.config.update({region: region});
    
    if (event.request.userAttributes.sub) {
        
        let ddbParams = {
            Item: {
                'id': {S: event.request.userAttributes.sub},
                'username': {S: event.username},
                'name': {S: event.request.userAttributes.name},
                'email': {S: event.request.userAttributes.email},
                'phoneNumber': {S: event.request.userAttributes.phone_number},
                'university': {S: uni},
                'organization': {S: org},
                'date': {S: data.toISOString()},
                
            },
            TableName: tableName
        };
        
        try {
            await ddb.putItem(ddbParams).promise()
            console.log("Success");
        } catch (err){
            console.log("Error", err);
        }
        
        console.log("Success: Everything executed correctly");
        context.done(null,event);
    }
    else{
        console.log("Error: Nothing written to DataBase");
        context.done(null,event);
    }
};
