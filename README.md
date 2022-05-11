# Large Tether Transfer Agent

## Description

This agent detects high price transaction if swap more 25%

## Supported Chains

- Ethereum

## Alerts

Dectection unsual high price changes

- FORTA-Agent
  - Finding liquid of transaction
  - Process send finding alert for liquid swap more 25%

## TEST
Testing done detect 2 data more than 25% liquid

## Test Data

The agent behaviour can be verified with the following transactions:
```
1 findings for transaction 0x30a0f1cab9c6a26dd99446c3e94760ed7489ae62b28d205178e4dc78f04de62e {
  "name": "Swap value is more than 25% of the liquidity value",
  "description": "A large increase in gas prices from the previous block.",
  "alertId": "LOW-LIQUIDITY  ",
  "protocol": "ethereum",
  "severity": "High",
  "type": "Suspicious",
  "metadata": {
    "token_address": "0x4a7397b0b86bb0f9482a3f4f16de942f04e88702",
    "liquid": "0x96d4f9d8f23eadee78fc6824fc60b8c1ce578443"
  },
  "addresses": [
    "0x7b9d4d8772b8705ddc7456daf821c3022dda0504",
    "0x96d4f9d8f23eadee78fc6824fc60b8c1ce578443",
    "0x4a7397b0b86bb0f9482a3f4f16de942f04e88702",
    "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "0x271544af1f703ac3deb3f12790de83b3b987aa2b"
  ]
}
```

```
2 findings for transaction 0x72a725b48b2c18a0a887bfdc9ee7be1cb839bc146c987e2054856b0751da2bd5 {
  "name": "Swap value is more than 25% of the liquidity value",
  "description": "A large increase in gas prices from the previous block.",
  "alertId": "LOW-LIQUIDITY  ",
  "protocol": "ethereum",
  "severity": "High",
  "type": "Suspicious",
  "metadata": {
    "token_address": "0x6b175474e89094c44da98b954eedeac495271d0f",
    "liquid": "0x2057cfb9fd11837d61b294d514c5bd03e5e7189a"
  },
  "addresses": [
    "0x0d080a3c3290c98e755d8123908498bce2c5620d",
    "0x1111111254fb6c44bac0bed2854e76f90643097d",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "0x6b175474e89094c44da98b954eedeac495271d0f",
    "0x5777d92f208679db4b9778590fa3cab3ac9e2168",
    "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "0x3058ef90929cb8180174d74c507176cca6835d73",
    "0x7d9af957bb728595a9d2405b33b03f7282e91899"
  ]
},{
  "name": "Swap value is more than 25% of the liquidity value",
  "description": "A large increase in gas prices from the previous block.",
  "alertId": "LOW-LIQUIDITY  ",
  "protocol": "ethereum",
  "severity": "High",
  "type": "Suspicious",
  "metadata": {
    "token_address": "0x6b175474e89094c44da98b954eedeac495271d0f",
    "liquid": "0x2057cfb9fd11837d61b294d514c5bd03e5e7189a"
  },
  "addresses": [
    "0x0d080a3c3290c98e755d8123908498bce2c5620d",
    "0x1111111254fb6c44bac0bed2854e76f90643097d",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "0x6b175474e89094c44da98b954eedeac495271d0f",
    "0x5777d92f208679db4b9778590fa3cab3ac9e2168",
    "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "0x3058ef90929cb8180174d74c507176cca6835d73",
    "0x7d9af957bb728595a9d2405b33b03f7282e91899"
  ]
}

```