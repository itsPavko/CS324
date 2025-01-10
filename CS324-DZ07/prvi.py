import re


addresses = """
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com

Jennifer Martin-White
714-555-7405
212 Cedar St., Sunnydale CT 74983
jenniferwhite@bogusemail.com

Erick Davis
800-555-6771
519 Washington St., Olympus TN 32425
tomdavis@bogusemail.com

Neil Patterson
783-555-4799
625 Oak St., Dawnstar IL 61914
neilpatterson@bogusemail.com

Laura Jefferson
516-555-4615
890 Main St., Pythonville LA 29947
laurajefferson@bogusemail.com

Maria Johnson
127-555-1867
884 High St., Braavos‎ ME 43597
mariajohnson@bogusemail.com

Michael Arnold
608-555-4938
249 Elm St., Quahog OR 90938
michaelarnold@bogusemail.com

Michael Smith
568-555-6051
619 Park St., Winterfell VA 99000
michaelsmith@bogusemail.com

Erik Stuart
292-555-1875
220 Cedar St., Lakeview NY 87282
robertstuart@bogusemail.com

Laura Martin
900-555-3205
391 High St., Smalltown WY 28362
lauramartin@bogusemail.com

Barbara Martin
614-555-1166
121 Hill St., Braavos‎ UT 92474
barbaramartin@bogusemail.com

Linda Jackson
530-555-2676
433 Elm St., Westworld TX 61967
lindajackson@bogusemail.com

Eric Miller
470-555-2750
838 Main St., Balmora MT 56526
stevemiller@bogusemail.com

Dave Arnold
800-555-6089
732 High St., Valyria KY 97152
davearnold@bogusemail.com

Jennifer Jacobs
880-555-8319
217 High St., Old-town IA 82767
jenniferjacobs@bogusemail.com

Neil Wilson
777-555-8378
191 Main St., Mordor IL 72160
neilwilson@bogusemail.com

Kurt Jackson
998-555-7385
607 Washington St., Blackwater NH 97183
kurtjackson@bogusemail.com

Mary Jacobs
800-555-7100
478 Oak St., Bedrock IA 58176
maryjacobs@bogusemail.com
"""


broj_indeksa = "5133"  


poslednja_cifra = broj_indeksa[-1]

pattern = rf"\b{poslednja_cifra}\d*\s[\w\s.,-]+\s\d{{5}}\b"


matches = re.findall(pattern, addresses)


with open("adrese.txt", "w") as file:
    for address in matches:
        file.write(address + "\n")

print("Adrese koje počinju sa poslednjom cifrom indeksa su uspešno sačuvane u fajl 'adrese.txt'.")
