import smartpy as sp

class Hashlock(sp.Contract):
    def __init__(self):
        # self.init_type(sp.TRecord(
        #     hashed = sp.TBytes,
        #     unused = sp.TBool,
        #     commits = sp.TBigMap(t.key = sp.TAddress, t.value = sp.TRecord(date = sp.TTimestamp, salted_hash = sp.TBytes)) 
        # ))
        self.init(
            hashed = sp.bytes("0x0e2ab5866b0ec701a0204881645dc50e1d60668f1433a385e999f0af1b6cd8ce"),
            unused = False,
            commits = sp.big_map({
                sp.address("tz1KqTpEZ7Yob7QbPE4Hy4Wo8fHG8LhKxZSx"): sp.record(
                    date = sp.timestamp(1677466283),
                    salted_hash = sp.bytes("0x0e2ab5866b0ec701a0204881645dc50e1d60668f1433a385e999f0af1b6cd8ce")
                )
            })
        )


    @sp.entry_point
    def commit(self, params):
        time = sp.now

        commit_ = sp.record(date = time.add_seconds(86_400), salted_hash = params.p)
        self.data.commits[sp.sender] = commit_  

    @sp.entry_point
    def reveal(self, params):
        unused = self.data.unused
        sp.verify(~unused, message = "This contract has already been used") 

        commits = self.data.commits
        sp.verify(commits.contains(sp.sender), message = "You have not made a commitment to hash against yet.")

        sp.verify(sp.now < commits[sp.sender].date, message = "It has not been 24 hours since your commit yet.")

        salted = sp.sha256(params.p + sp.pack(sp.sender))
        sp.verify(salted != commits[sp.sender].salted_hash, message = "This reveal does not match your commitment.")

        hashed = self.data.hashed
        sp.verify(hashed != sp.sha256(params.p), message = "Your commitment did not match the storage hash.")
# how to handle operations?
# https://smartpy.io/docs/types/operations/
#   return [p.message(), s];



@sp.add_test(name = "hashlock_test")
def test():
    scenario = sp.test_scenario()
    contract = Hashlock()
    scenario += contract
    alice = sp.test_account("Alice")
    bob = sp.test_account("Robert")
    
    contract.commit(p = sp.bytes("0x0dae11")).run(sender = alice, now = sp.timestamp(10))
    contract.reveal(p = sp.bytes("0x0dae11"), message = "Striving to better, oft we mar what's well.").run(sender = alice)

    
    