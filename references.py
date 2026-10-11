references = {
    "R01": (
        "R01 means Insufficient Funds. "
        "The available balance and/or cash reserve balance "
        "is not sufficient to cover the dollar value "
        "of the ACH debit entry."
    ),
    "R02": (
        "R02 means Account Closed. "
        "An account that was previously active has been closed "
        "by the customer or the receiving bank."
    ),
    "R03": (
        "R03 means No Account/Unable to Locate Account. "
        "The account number has a valid structure, but it does "
        "not match the individual identified in the entry, "
        "or it does not identify an open account."
    ),
    "R04": (
        "R04 means Invalid Account Number Structure. "
        "The account number has an invalid structure, such as "
        "an incorrect number of digits or a failed check digit validation."
    ),
}
wire_references = {
    "INTERNATIONAL WIRE DELAY": (
        "Bank of America's international wire guidance identifies "
        "several factors that may delay delivery: the selected currency, "
        "the receiving bank's processing time, local bank holidays, "
        "intermediary-bank delays, and other local conditions. "
        "These are possible delay factors; this reference does not "
        "establish the cause or completion time of a particular transfer."
    ),
}

wire_source = {
    "title": "Bank of America — Wire Transfers",
    "url": "https://info.bankofamerica.com/en/digital-banking/wire-transfers",
}