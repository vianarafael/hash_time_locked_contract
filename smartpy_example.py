# reference: https://smartpy.io/docs/experimental/timelock/#chest
import smartpy as sp

class Timelock(sp.Contract):
    def __init__(self):
        self.init(
            time  = 3456,
            chest = sp.chest(
                "0xbcf89e8a80d99cd49690dda59accc4d381c1a3facbacc1a3f9aab5e7ecdc8db6b0928eed84a7e5d9958e96b5b1f3c8ddd9b98dd394f9bafaafad85a2d7cbffeec1e280d5c6ccbab3caddb5ced3c1d39c82cea0cc99b7f788bbca85eeb1badd91fdc8e1e1e9a6cddca7bdef8faaf6acf2aeef8ccbd3d987f6d0ecf9c8c9818c92eb8a81e385fff9e8c4ad96d6e7bad6a480ec83f3cb84bedeac82baafa1b88bfd90968b9ee7b2d8aabef9d8e0d9a9c8a5a8859a8db5e6d496de95cfd2cfc4dcfae3edf9f1d5faee998694ed8aada2a7d4b88aecc8acda98d6f69cfb8df3a5ca80b48d91aa9bbbf68f918998ddc5d3cc82d3f0ce81869fd9edb8b0989dcfa5e9b59db18dd099c7b8bb848586afc7c8888f86d2c6988eeee5e5fbfc9de8a7f19e84ebc2b687049390ebd5cecb86eecfe2bef994f9a7c3eabeabdda0b4b7b59381a8a4c3d7c1b382bcf6e1adb2e3c6ce9ca5e0c0a0beb999f4eacc89cf858fb282b294d99ec2daccd9cdcc98a98b8cb5b0bbf9ed80b0f6ccd2a994f3a1faafbbacf7eebbec9399bfdfd1f0da9ee4aa9dcb8b9c85fcab87bd86b98fd7cc9a8cb2e3cc93ef86df83e5ce9bbda8c7d4cad0e4b893fde8e18b9cf283f9829f9ab8f48da8b0f1b5c8f3a1d2a1a6e5c1fec0abb09eb9b0c2c3ae9f9df6c6a7bad396f7b3b1fc90e490a4f2a5f599fedbc8b3b297a99db3b285a3f0acefe0c8d4cec08195af8098d0f4b8d488bdacd7e8effea5cdaf8dd1ccdbe4fee59eb7e1cebff2eb839b8f81d598abc798d5bdcea59bfcbaf89fbdbbcb8182a3eea1f4f5dccafcb4ddd4ff83d3879edef5d3ca06d2f1146cf4c25faf0e432bf540b4de74fae3cc68e0bc57c700000021cf744e778f4d5e220d4be7310077e6735795b6c90bbe2bdcdd9b686e3c71f833f2"
            ),
            decrypted = sp.none
        )

    @sp.entry_point
    def ep(self, chest_key):
        sp.set_type(chest_key, sp.TChest_key)

        with sp.open_chest(chest_key, self.data.chest, self.data.time).match_cases() as result:
            with result.match("Left") as success:
                # If the output is "Left" variant, it means that the content was decrypted successfully
                self.data.decrypted = sp.unpack(success, sp.TString) # Unpack the result
            with result.match("Right") as fail_status:
                # If the output is "Right" variant, it means that the content could not be decrypted
                with sp.if_(fail_status):
                    sp.failwith("The ciphertext does not decrypt under the symmetric key that was timelocked.")
                with sp.else_():
                    sp.failwith("The provided symmetric key was not the one timelocked.")

@sp.add_test(name = "timelock_test")
def test():
    scenario = sp.test_scenario()
    timelock = Timelock()
    scenario += timelock
    timelock.ep(
        sp.chest_key(
            "0xf5d3cec5da988edfbee8be85b4919bc7c5a3f7ecebe7a19ac8e0c3f9c3aac5948de9b9dddab88b93c4fee4d094a3a5e48494c0ae80b4ffbcd9a8b7a2c9f3dfc0e2e18082f3d3ceabf9f1a7c8fcd4dec7b7e091a89e83f8a6ab90dea1bdbd95bff9ed8ac89c88ebeecfe5faaeb8f184e5df9298e5aff3bad5bbc1fcefdbb5b2929df9c6ced9aebefbc49decb4d9e085b1a8c39099818d97e0b3dbf287efb99c87c8eeb38f86d9e9c2bdeccec4abb5ce89bce988aba5a0adf59180898697a7e5d1dfa8d5a6aac8f0f5bd87ecb7aeaedec6a4f7f5bfead9e1cbd3a8a88fddcb939198f0ae94cecdc3e9d3d9c2b28ece8ff487a0e983868ef995b3ee90f082adf8aeddbab2efc2b5fcd5aff1a19bb3acff83b08986d0ffa3eec4afabbec280f4d498b1f2e6de01c192a381d3b8c19dd8edb4d6e689cbccb1b5c396c7abda9bc4ed9edf9ecff7c78bab8fadbbd4f4e7d1d289eace839becdfa5e7d1ddc2b0e9e1e88d87a3e3aae8c6dd889cd980e69af8b992d4b5e28cb691de94c0afe0f3fbde8b85e4eced9ec8dcd986d189e4a8bcd3fda2efbce5cde9d68499eef7bda5a782c3adf0cc84abd0c0ec91988b9a81ad819af19e97eefacea9a9b1ffe2d1bcc1e5d8dc87e89d8a92afd3fcf4d4d2e1d9e4f583c5a583ebb6f19dd7abd3f8f5d6a8ee9bf78faa8aedf0d8b0e6a1a6bf95849192b5f8bfef9581deaebef3e6f390ac99ade490e7feb5d0d589cce2e3d4b9ced493e3fac1da83f697e6c0e68f8295ec97f2c0aae7dcaffaedb5fef283d4a5b4f3fdd8e7a0b0f9c4accce9c2f9e9ba8b8391fad3d0db84cbe9f3d003"
        ),
    )

sp.add_compilation_target("timelock_compilation", Timelock())

# usage example: https://github.com/RomarQ/tezos-timelock#generate-chest-and-chest-key
