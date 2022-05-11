#import libray used
from forta_agent import Finding, FindingType, FindingSeverity
from web3 import Web3

#using alchemyapi api
alchemyapi = "https://eth-mainnet.alchemyapi.io/v2/SpMdonByBKO9uRrcHJP4WGxaMa82h8q2"
w3 = Web3(Web3.HTTPProvider(alchemyapi))

#set token_abi
token_abi = '[{"name":"Transfer","type":"event","anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}]},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]'


#handler transaction
def handle_transaction(transaction_event):
    #describe variabel used
    findings = []
    group_logs_data = []
    temp_liquid = []
    temp_token = []
    

    #len of transaction logs
    logs_address = len(transaction_event.logs)

    #loop for data
    for posisition in range(logs_address):
        #set data to function logs position
        data = transaction_event.logs[posisition]
        #get metode topics topics with 10 digits first
        get_method_topics = data.topics[0][0:10]

        #statement for topics transfer
        if(get_method_topics == "0xddf252ad"):
            try:
                #hex to decimal
                get_balance_value = int(data.data,16)
                get_balance_value = get_balance_value / 10**9

                #get address
                get_address = data.address
                #get method from array topics 0
                get_method = data.topics[0]
                #get logs_data for liquid prediction
                logs_data_1 = ("0x" + data.topics[1][26::])
                logs_data_2 = ("0x" + data.topics[2][26::])

                #append all want used
                group_logs_data.append([get_address, get_method, logs_data_1, logs_data_2, get_balance_value])
            
            except Exception as e:
                pass

    #loop data on range  list group_logs_data
    for val in range(len(group_logs_data)):
        #statment if val+1 index out range
        if(val+1 == len(group_logs_data)):
                break

        #loop position with list 2(liquid predict 1) and 3 (liquid predict 2) for get prediction liquid on list
        for position_now in range(2,4):
            #liquid predict now on data
            liquid_now = group_logs_data[val][position_now]
            #stement nest loop for checking predick liquid
            for posisition_next in range(2,4):
                #liquid predict next of data
                liquid_next = group_logs_data[val+1][posisition_next]
                #stament if now predict liquid same on next  predict liquid
                if(liquid_now == liquid_next):
                    #set token address
                    token_address_now = group_logs_data[val][0]
                    #set balance data
                    balance_data_now = group_logs_data[val][4]

                    #set 25% for high severity
                    #get token balance from function get_token_balance
                    token_balance_now = get_token_balance(token_address_now, liquid_now)
                    twenty_five_persent_balance_data_now = token_balance_now * (25/100)
                    


                    #stament checking liquid if liquid data balance > 0
                    if(token_balance_now > 0):
                        #get addresess
                        addresses = [] 
                        for address in transaction_event.addresses:
                            addresses.append(address)

                        #statement for high severity 25% swapp
                        if(balance_data_now > twenty_five_persent_balance_data_now):
                            #finding severity
                           findings.append(Finding({
                                'name': f"Swap value is more than 25% of the liquidity value",
                                'description': f'A large increase in gas prices from the previous block.',
                                'alert_id': "LOW-LIQUIDITY  ",
                                'type': FindingType.Suspicious,
                                'severity': FindingSeverity.High,
                                'metadata': {
                                    'token_address': token_address_now,
                                    'liquid': liquid_now,
                                },
                                'addresses': addresses
                            }))
            
    return findings


def get_token_balance(contract_address, address):
    #checksum address from parameter contract_address
    get_token_address = w3.toChecksumAddress(contract_address)
    #get token balance with parameter and token abi
    get_token_balances = w3.eth.contract(address=get_token_address, abi=token_abi)
    #show token balance with balance of
    token_balance = get_token_balances.functions.balanceOf(w3.toChecksumAddress(address)).call()

    return token_balance
