## Deployed contract (Ghostnet)
KT1Tgqeh2az5Wodga7tPzqPVeDpuCkm49TdN

# hash_time_locked_contract
A Hash Time Locked Contract (HTLC) is a type of digital agreement or smart contract used in cryptocurrency transactions. It involves two or more parties agreeing to exchange assets (such as cryptocurrencies) at a future date, subject to certain conditions.

The contract is created by one party and includes a secret key. This secret key is hashed (which is a process of turning the key into a string of characters) and the hashed key is shared with the other party. The actual secret key remains private.

The funds are locked up in the contract until a specified time period has elapsed. The funds are then released to the appropriate party once the conditions of the contract are met. If either party fails to meet the conditions, the funds are returned to their respective owners.

Reference: https://tezos.gitlab.io/alpha/timelock.html

## common usage
A cross-chain atomic swap is a type of peer-to-peer exchange between two different cryptocurrencies on separate blockchain networks. It allows for the exchange of one cryptocurrency for another without the need for a trusted third party or centralized exchange. It works by using HTLCs to ensure that both parties fulfill their part of the exchange, so neither party can cheat the other. This allows for more secure and decentralized trading between different cryptocurrencies.

Reference: https://www.coindesk.com/tech/2021/08/20/a-beginners-guide-to-atomic-swaps/

## Practical Example
Suppose you and I want to exchange cryptocurrencies using an atomic swap.

- 1. You deposits your cryptocurrency into an HTCL address, which acts like a virtual safe and can only be unlocked with a special key that she can access.
- 2. You share a cryptographic hash of the special key with me, I deposits my cryptocurrency into an address created using the same cryptographic hash.
- 3. Once I have deposited the cryptocurrency, You can use the currency by “unlocking” the transaction with the special key obtained from your initial deposit.
- 4. After you have used the key to “unlock” the transaction, I can get access to his share of the exchange.
- 5. Once both parties have access to their respective funds, the atomic swap is completed.


## Resources for learning SmartPy:
[B9Lab](https://tezos.b9lab.com/smartpy/intro)

[Smartpy docs](https://smartpy.io/docs/)

[OpenTezos](https://opentezos.com/smartpy/)

[Tacode](https://tacode.dev/courses/dev-starter)

## Original Ligo Contract

[hashlock](https://gitlab.com/ligolang/ligo/-/blob/dev/src/test/examples/jsligo/hashlock.jsligo)
