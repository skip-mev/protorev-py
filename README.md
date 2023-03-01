# Overview

- This repo contains test scripts to test the functionality of the ProtoRev Module on Osmosis.
- Intended to be used for Testnet testing
- Places that need to be edited are marked with @DEV TODO in the files
- The Main functions in the three scripts are short and commented to guide the tester in the specific functionality being tested per function
- proposal_test.py must be ran first and does the following:
    1. Delegates to a Validator
    2. Submits & votes on a proposal to change the admin account to one the tester has access to
    3. Submits & votes on a proposal to enable protorev
- everything_else_test.py must be ran after the proposals pass, and does the following:
    1. Gives an authz grant from the admin account to another account the tester has access to
    2. Has the grantee execute messages that
        - Sets the developer account
        - Sets pool points per tx
        - Sets pool points per block
        - Sets pool weights
    3. Sets usomo and atom as base denoms for highest liquidity pool method
    4. Sets hot routes based on routes used by searchers across blocks 7400000-7900000
    5. Swaps a large amount on Pool 1, which ProtoRev should backrun succesfully if using mainnet state export
        - Assumes pool 1 is uosmo/ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2 pair
- stress_test.py 
    1. swaps 200 times in a block, ensuring protorev caps out based on its limits and doesn't add any extra block time.
    2. Ensures within tx limits work and are updated correctly
    - Note: The block pool points set in the everything_else_test.py script are the highest they can be (there exists hard-coded limits in protorev that the admin account cannot override), and the pool weights set are the lowest they can be -- so this is the most ProtoRev can do at once.

# Usage

### **Install Python 3.10** ###
```
sudo apt update && sudo apt upgrade -y
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10 python3-pip python3-virtualenv python3.10-distutils 
```

Check your Python 3.10 is functioning:

```
python3.10 --version
```

Clone the repository:
```
git clone https://github.com/skip-mev/protorev-py.git
```

Move into the directory:
```
cd protorev-py
```

Create a virtual environment
```
python3.10 -m venv venv
```

Activate virtual environment, (venv) will show on left-hand side of shell
```
source venv/bin/activate
```

Once you have python 3.10 and are in the directory, install all the dependencies:
```
pip install -r requirements.txt
```

Edit The Necessary Variables In The Following Files (Marked By @DEV TODO In The Files):
```
proposal_test.py & everything_else_test.py
``` 

Let the Tests Rip, Starting With The Proposal Test:
```
python proposal_test.py 
```

We Then Must Wait Until The Proposal Passes Which Gives The Mnemonic's Address We Set Admin Account Status

Once That Address Is The Admin Account, We Can Run The Bulk Of The Functionality Tests:
```
python everything_else_test.py     
```

Finally, run the stress test which swaps swaps 200 times within a block to ensure Protorev caps out at the block limit and doesn't add any extra block time.
```
python stress_test.py
```

