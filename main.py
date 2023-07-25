# Program Description: Insurance Policy Program for One Stop Insurance Company
# Written By: Brandon Butler
# Date: July 18, 2023

#Imports
import datetime
import FormatValues as FV
from tqdm import trange
from time import sleep
CurrDate = datetime.datetime.now()

#Define program constants.

#Define a required functions.

#Main program.
# Open default file and add required values
f = open("OSICDef.dat", "r")
PolNum = int(f.readline())
BasicPrem = float(f.readline())
AddCarDis = float(f.readline())
AddLiabilityCost = float(f.readline())
GlassCovCost = float(f.readline())
LoanCarCovCost = float(f.readline())
HST_RATE = float(f.readline())
ProcFee = float(f.readline())
f.close()

# Loop to input and validate required customer information
while True:
    CustFName = input("Enter customer's first name (End to quit): ").title()
    if CustFName == "End":
        break
    CustLName = input("Enter customer's last name: ").title()
    Address = input("Enter customer's street address: ")
    City = input("Enter customer's city: ").title()
    while True:
        ProvinceList = ["NL", "NB", "NS", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "NT", "NU", "YK"]
        Province = input("Enter customers province: (AA): ")
        if Province in ProvinceList:
            break
        else:
            print("Error - Please enter a valid Province with correct formatting.")

    Postal = input("Enter customer's postal code (A9A9A9): ")
    PhoneNum = input("Enter customer phone number (9999999999): ")
    NumCarIns = int(input("Enter the number of cars being insured (99): "))
    AddLiability = input("Enter additional liability up to $1,000,000 (Y/N): ").upper()
    GlassCov = input("Enter optional glass coverage (Y/N): ").upper()
    LoanerCarCov = input("Enter optional loaner car coverage (Y/N): ").upper()
    while True:
        PaymentMethodList = ["Monthly", "Full"]
        PaymentMethod = input("Enter customer's payment method (Full or Monthly): ").title()
        if PaymentMethod in PaymentMethodList:
            break
        else:
            print("Error - Please enter Full or Monthly for payment method.")

    #Calculations
    BasicPremDis = BasicPrem * 0.25
    BasicPremDSP = 869.00
    if NumCarIns >= 2:
        BasicPremDSP += + ((NumCarIns-1) * (BasicPrem - BasicPremDis))
    else:
        BasicPremDSP = BasicPrem

    if AddLiability == "Y":
        AddLiabilityCostDSP = AddLiabilityCost * NumCarIns
    else:
        AddLiabilityCostDSP = 0

    if GlassCov == "Y":
        GlassCovCostDSP = GlassCovCost * NumCarIns
    else:
        GlassCovCostDSP = 0

    if LoanerCarCov == "Y":
        LoanerCarCovCostDSP = LoanCarCovCost * NumCarIns
    else:
        LoanerCarCovCostDSP = 0

    TotalExtraCosts = AddLiabilityCostDSP + GlassCovCostDSP + LoanerCarCovCostDSP
    TotalInsPrem = BasicPremDSP + TotalExtraCosts
    HST = TotalInsPrem * HST_RATE
    TotalCost = TotalInsPrem + HST
    if PaymentMethod == "Full":
        MonthlyPayment = 0
        YearlyPayment = TotalCost
        ProcFeeDSP = 0
    elif PaymentMethod == "Monthly":
        ProcFeeDSP = ProcFee
        MonthlyPayment = (TotalCost + ProcFee)/8
        YearlyPayment = 0

    InvDate = CurrDate.strftime("%b %d, %Y")
    PaymentDate = (CurrDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    PaymentDate = PaymentDate.strftime("%b %d, %Y")

    # Displaying output
    print()
    print(" =====================================================================")
    print()
    print("                      ONE STOP INSURANCE COMPANY")
    print("                         123 Insurance Street")
    print("                             Paradise, NL")
    print("                                A1A1A1")
    print()
    print()
    print(f" AUTOMOBILE INSURANCE SUMMARY                       Date: {InvDate}")
    print(" =====================================================================")
    print(" CLIENT INFORMATION:")
    print()
    print(f"    {CustFName} {CustLName}")
    print(f"    {Address:<20s}")
    print(f"    {City}, {Postal}")
    print(f"    {PhoneNum}")
    print(" _____________________________________________________________________")
    print(f" POLICY DETAILS - #{PolNum}                     Invoice Date: {InvDate}")
    print()
    print(f"    Cars Insured:                        {NumCarIns}")
    print(f"    Additional Liability:        {FV.FDollar2(AddLiabilityCostDSP):>9s}")
    print(f"    Glass Coverage:              {FV.FDollar2(GlassCovCostDSP):>9s}")
    print(f"    Loaner Car Coverage:         {FV.FDollar2(LoanerCarCovCostDSP):>9s}")
    print(f"    Payment Method:              {PaymentMethod:>9s}")
    print(" _____________________________________________________________________")
    print(f" POLICY COST BREAKDOWN                First Payment Date: {PaymentDate}")
    print()
    print(f"    Insurance Premium:           {FV.FDollar2(BasicPremDSP):>9s}")
    print(f"    Additional Coverage Costs:   {FV.FDollar2(TotalExtraCosts):>9s}")
    print(f"    Total Insurance Premium:     {FV.FDollar2(TotalInsPrem):>9s}")
    print(f"    HST:                         {FV.FDollar2(HST):>9s}")
    print("                                  --------")
    print(f"    Total Cost:                  {FV.FDollar2(TotalCost):>9s}")
    print(f"    Monthly Payment:             {FV.FDollar2(MonthlyPayment):>9s}")
    print()
    print(" =====================================================================")

    print()
    print()
    print("Saving data ...")

    for i in trange(100):
        sleep(0.01)

    f = open("Policies.dat", "a")
    f.write(f"{PolNum}, ")
    f.write(f"{InvDate}, ")
    f.write(f"{CustFName}, ")
    f.write(f"{CustLName}, ")
    f.write(f"{Address}, ")
    f.write(f"{City}, ")
    f.write(f"{Province}, ")
    f.write(f"{Postal}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCarIns}, ")
    f.write(f"{AddLiability}, ")
    f.write(f"{GlassCov}, ")
    f.write(f"{LoanerCarCov}, ")
    f.write(f"{PaymentMethod}, ")
    f.write(f"{TotalInsPrem}\n")
    f.close()

    print()
    print("Policy information processed and saved ...")
    print()

    # update any default values based on the processing
    PolNum += 1

    f = open('OSICDef.dat', 'w')
    f.write(f"{PolNum}\n")
    f.write(f"{BasicPrem}\n")
    f.write(f"{AddCarDis}\n")
    f.write(f"{AddLiabilityCost}\n")
    f.write(f"{GlassCovCost}\n")
    f.write(f"{LoanCarCovCost}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{ProcFee}\n")
    f.close()

    #Housekeeping