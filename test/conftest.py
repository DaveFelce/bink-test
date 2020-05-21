import pytest


@pytest.fixture
def csv_rows():
    dataset = [
        {"Property Name": "Beecroft Hill", "Property Address [1]": "Broad Lane", "Property  Address [2]": "",
         "Property Address [3]": "", "Property Address [4]": "LS13", "Unit Name": "Beecroft Hill - Telecom App",
         "Tenant Name": "Arqiva Services ltd", "Lease Start Date": "01 Mar 1994",
         "Lease End Date": "28 Feb 2058", "Lease Years": 64, "Current Rent": 23950.0},
        {"Property Name": "Potternewton Crescent", "Property Address [1]": "Potternewton Est Playing Field",
         "Property  Address [2]": "", "Property Address [3]": "", "Property Address [4]": "LS7",
         "Unit Name": "Potternewton Est Playing Field", "Tenant Name": "Arqiva Services ltd",
         "Lease Start Date": "24 Jun 1999", "Lease End Date": "23 Jun 2019", "Lease Years": 20,
         "Current Rent": 6600.0},
        {"Property Name": "Seacroft Gate (Chase) - Block 2", "Property Address [1]": "Telecomms Apparatus",
         "Property  Address [2]": "Leeds", "Property Address [3]": "", "Property Address [4]": "LS14",
         "Unit Name": "Seacroft Gate (Chase) block 2-Telecom App.", "Tenant Name": "Vodafone Ltd",
         "Lease Start Date": "30 Jan 2004", "Lease End Date": "29 Jan 2029", "Lease Years": 25,
         "Current Rent": 12250.0},
        {"Property Name": "Queenswood Heights", "Property Address [1]": "Queenswood Heights",
         "Property  Address [2]": "Queenswood Gardens", "Property Address [3]": "Headingley",
         "Property Address [4]": "Leeds", "Unit Name": "Queenswood Hgt-Telecom App.",
         "Tenant Name": "Vodafone Ltd", "Lease Start Date": "08 Nov 2004", "Lease End Date": "07 Nov 2029",
         "Lease Years": 25, "Current Rent": 9500.0},
        {"Property Name": "Armley - Burnsall Grange", "Property Address [1]": "Armley",
         "Property  Address [2]": "LS13", "Property Address [3]": "", "Property Address [4]": "",
         "Unit Name": "Burnsall Grange CSR 37865", "Tenant Name": "O2 (UK) Ltd",
         "Lease Start Date": "26 Jul 2007", "Lease End Date": "25 Jul 2032", "Lease Years": 25,
         "Current Rent": 12000.0},
        {"Property Name": "Seacroft Gate (Chase) - Block 2", "Property Address [1]": "Telecomms Apparatus",
         "Property  Address [2]": "Leeds", "Property Address [3]": "", "Property Address [4]": "LS14",
         "Unit Name": "Seacroft Gate (Chase) - Block 2, WYK 0414",
         "Tenant Name": "Hutchinson3G Uk Ltd&Everything Everywhere Ltd", "Lease Start Date": "21 Aug 2007",
         "Lease End Date": "20 Aug 2032", "Lease Years": 25, "Current Rent": 12750.0},
    ]

    yield dataset
