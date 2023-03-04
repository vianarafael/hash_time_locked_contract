## Deployed contract
KT1Tgqeh2az5Wodga7tPzqPVeDpuCkm49TdN

# hash_time_locked_contract
A Hash Time Locked Contract (HTLC) is a type of digital agreement or smart contract used in cryptocurrency transactions. It involves two or more parties agreeing to exchange assets (such as cryptocurrencies) at a future date, subject to certain conditions.

The contract is created by one party and includes a secret key. This secret key is hashed (which is a process of turning the key into a string of characters) and the hashed key is shared with the other party. The actual secret key remains private.

The funds are locked up in the contract until a specified time period has elapsed. The funds are then released to the appropriate party once the conditions of the contract are met. If either party fails to meet the conditions, the funds are returned to their respective owners.

Reference: https://tezos.gitlab.io/alpha/timelock.html

## common usage
A cross-chain atomic swap is a type of peer-to-peer exchange between two different cryptocurrencies on separate blockchain networks. It allows for the exchange of one cryptocurrency for another without the need for a trusted third party or centralized exchange. It works by using HTLCs to ensure that both parties fulfill their part of the exchange, so neither party can cheat the other. This allows for more secure and decentralized trading between different cryptocurrencies.

Reference: https://www.coindesk.com/tech/2021/08/20/a-beginners-guide-to-atomic-swaps/

## Project
Project Description
Your goal is to take a smart contract in LIGO, then re-write and deploy it in another language – either SmartPy or Archetype. Which one you choose depends on your preference. We suggest first going over the basics of what both of them offer and only making a decision then. It is very useful to get acquainted with both of these, because most likely, if you are going to work in the Tezos ecosystem, sooner or later you will encounter both. Below, we give several guides for each of the languages. It is advisable to start with one tutorial that seems to be the most appropriate for your experience, but then as you go, check the other ones from time to time to ensure that you haven’t missed anything important.

Resources for learning SmartPy:
[B9Lab](https://tezos.b9lab.com/smartpy/intro)

[Smartpy docs](https://smartpy.io/docs/)

[OpenTezos](https://opentezos.com/smartpy/)

[Tacode](https://tacode.dev/courses/dev-starter)

SmartPy has an online IDE, quite a lot of nice examples of contracts (in the online IDE), a custom-made explorer & origination page, and a convenient testing suite. If you are familiar with Python, choosing SmartPy is likely to be a good choice.

Resources for learning Archetype:
Archetype official docs
Completium Archetype tutorial
OpenTezos Archetype Tutorial
Archetype is meant to be a simple and elegant way to create smart contracts. While it doesn’t have such advanced online tools as SmartPy, it is still a good choice for those who have not coded in Python before, since you will not need to learn Python as well.

Project Specifications
You are encouraged to utilize as many possibilities offered by the chosen language as possible in a reasonable amount of time given for this project. For example, if you choose SmartPy and have the time, it’s really recommended that you use SmartPy tests.

The smart contract that you will need to implement is called HashLock. You can find the LIGO implementation of it in the examples at LIGO IDE. You can also read more about them here. During the correction, you will likely be asked to explain the algorithm in your own words, so make sure that you understand it.


[hashlock](https://gitlab.com/ligolang/ligo/-/blob/dev/src/test/examples/jsligo/hashlock.jsligo)


Your implementation can differ slightly from the one in LIGO IDE, for example, if you want to improve it somehow. However, in such cases, during the correction, you should explicitly mention what you did differently (the default expectation is that you will try to create an implementation that is as identical to the LIGO one as possible).

Before scheduling your correction, make sure that you have uploaded your solution to your Turing College repository. Also, add a readme file with the explanation of your smart contract and the address of it (in a testnet).

Note: if you are experienced with Haskell, you may also be interested in looking at the Morley framework. For the sake of this project, however, you should use either SmartPy or Archetype, in order for more peer learners to be able to perform corrections and be familiar with the language you use.

Sample Questions
Here are questions that the reviewer may choose to ask during the correction.

When would someone want to use a HashLock algorithm?
What are some of the main differences between LIGO and the language you chose (SmartPy/Archetype)?
Are there any functionalities that LIGO offers that Smartpy/Archetype does not (or vice versa), leading to a different set of smart contracts that can be implemented?
How does a particular feature of LIGO/SmartPy/Archetype work?
A reviewer is encouraged and expected to think of more questions.

Note: The goal of the corrections is to promote a deeper understanding of learned topics by both learners. The reviewer and the reviewed learner must strive for a cooperative, friendly, and helpful interaction. Remember that both parties will rate each other after the correction on their technical and soft skills.

Project Evaluation Criteria
Core functionality of the HashLock algorithm is implemented in Archetype/LIGO.
The implementation of HashLock follows the implementation of LIGO example, or improves upon it (with the learner being aware of it and explicitly stating that it does so).
The benefits of the particular language chosen are understood, explained and used (e.g. testing in SmartPy).
Code quality. E.g. is the code tidy, variable names chosen well?
The quality of soft skills during presenting, e.g. was the learner engaging, professional & clear?
The smart contract is properly deployed and the learner is able to demonstrate how to use it.
General understanding of the theoretical topics covered in this sprint.


