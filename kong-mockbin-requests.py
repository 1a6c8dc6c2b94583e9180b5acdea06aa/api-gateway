

# https://docs.gelato.io/guides/advanced-kong-integration



# Step 1: Create the "loop-back" API
#-----------------------------------------------------------------------------------------------------

curl -X POST http://127.0.0.1:8001/apis \
    -d "name=admin-loop-back" \
    -d "request_path=/admin-loop-back" \
    -d "upstream_url=http://localhost:8001" \
    -d "strip_request_path=true"


#   
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/ \
    --data "name=test.io" \
    --data "request_host=api.test.io" \
    --data "request_path=/api-test" \
    --data "upstream_url=http://mockbin.org/request"
    
    



# test
curl -i -X GET http://127.0.0.1:8000/api-test -H "Host: api.test.io" 



# Step 2: Add API Key Authentication
#-----------------------------------------------------------------------------------------------------

curl -X POST http://localhost:8001/apis/admin-loop-back/plugins \
    -d "name=key-auth"

    
#
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins \
    --data "name=key-auth" \
    --data "config.key_names=X-AUTH"




# Step 3: Create a Consumer
#-----------------------------------------------------------------------------------------------------

curl -X POST http://localhost:8001/consumers \
    -d "username=loop-back-consumer"


#
curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=<USERNAME>" \
    --data "custom_id=<CUSTOM_ID>"


curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/ \
    --data "username=testio" \
    --data "custom_id=123456"


    

# Step 4: Create an API Key for our Consumer
#-----------------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/testio/key-auth \
    --data "key=testkey"
    
    
curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/testio/key-auth \
    --data "key=testkey01"
    
    
    
    
# test
curl -X GET http://127.0.0.1:8001/consumers/testio/key-auth

curl -i -X GET http://127.0.0.1:8000/api-test -H "host: api.test.io" -H "x-auth: testkey"

        
curl -i -X GET -H "host: api.test.io" -H "x-auth: testkey" http://127.0.0.1:8000/api-test
  





# rate-limiting Configuration
#----------------------------------------------------------------------------------------------------------------


curl -i -X POST \
    --url http://127.0.0.1:8001/apis/{api}/plugins \
    --data "name=rate-limiting" \
    --data "config.second=5" \
    --data "config.hour=10000"


#
curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins \
    --data "name=rate-limiting" \
    --data "config.second=2" \
    --data "config.minute=5" \
    --data "config.hour=1000" \
    --data "config.day=50000"
    
    
    
    



# /acl/ Configuration
#----------------------------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/apis/{api}/plugins \
    --data "name=acl" \
    --data "config.whitelist=group1, group2"




curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins \
    --data "name=acl" \
    --data "config.whitelist=group1, group2"
    
    
# curl -X GET http://127.0.0.1:8001/apis/test.io/plugins   



# Associating Consumers:
curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/{consumer}/acls \
    --data "group=group1"


curl -i -X POST \
    --url http://127.0.0.1:8001/consumers/testio/acls \
    --data "group=group1"
    
    
# curl -X GET http://127.0.0.1:8001/consumers/testio/acls  



    
    
# /galileo/ Configuration    
#----------------------------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/apis/{api}/plugins/ \
    --data "name=galileo" \
    --data "config.service_token=YOUR_SERVICE_TOKEN"



curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins/ \
    --data "name=galileo" \
    --data "config.service_token=tokentest"






# /bot-detection/ Configuration    
#----------------------------------------------------------------------------------------------------------------

curl -i -X POST \
    --url http://127.0.0.1:8001/apis/{api}/plugins \
    --data "name=bot-detection"


curl -i -X POST \
    --url http://127.0.0.1:8001/apis/test.io/plugins \
    --data "name=bot-detection"



# User-Agent
# https://github.com/Mashape/kong/blob/master/kong/plugins/bot-detection/rules.lua







