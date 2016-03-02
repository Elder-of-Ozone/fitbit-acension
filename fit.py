import fitbit

client_id = '226JVL'
client_secret = '937c03e3a1e9b51c05c33fc0c7471cd8'

a_token = 'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0NTI1OTEwNzEsInNjb3BlcyI6Indsb2Mgd3BybyB3bnV0IHdzbGUgd3NldCB3aHIgd3dlaSB3YWN0IHdzb2MiLCJzdWIiOiIzWEtCMlIiLCJhdWQiOiIyMjdKVkwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJpYXQiOjE0NTI1ODc0NzF9.wf5oj7M3zF-E-90Sm7U-UUZgllywFTuwWsUXSs7hX3w' 
r_token = 'ae07094901c3c00f28d7df0c7871a8188309ec261a2a8287d12026cd0d3294dc'



client = fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token=a_token, refresh_token=r_token)

data = client.sleep()
print data
