def Temperature(temperature):
    try:
        if temperature >=0 and temperature <16:
            temperature_static='Low'
        elif temperature >=16 and temperature <31:
            temperature_static='Medium'
        elif temperature >=31 and temperature <=45:
            temperature_static='High'
    
        return temperature_static
    except Exception as e:
        print(e)

def Humidity(humidity):
    try:
        if humidity >=0 and humidity <36:
            humidity_static='Good'
        elif humidity >=36 and humidity <71:
            humidity_static='Fair'
        elif humidity >=71 and humidity <= 100:
            humidity_static='Poor'
        return humidity_static
    except Exception as e:
        print(e)

def Co(CO):
    try:
        if CO >=0 and CO <36:
            Co_static='Low'
        elif CO >=36 and CO <71:
            Co_static='Medium'
        elif CO >=71 and CO <= 100:
            Co_static='High'
        return Co_static 
    except Exception as e:
        print(e)
def Co2(CO2):
    try:
        if CO2 >=0 and CO2 <36:
            CO2_static='Low'
        elif CO2 >=36 and CO2 <71:
            CO2_static='Medium'
        elif CO2 >=71 and CO2 <= 100:
            CO2_static='High'
        return CO2_static
    except Exception as e:
        print(e)
def Health_condition(T_s,H_s,C_s,C2_s):
    if T_s =='Low' and H_s =='Good' and C_s=='Low' and C2_s=='Low':
        Health_condition='Good'
    elif T_s =='Medium' and H_s =='Fair' and C_s=='Medium' and C2_s=='Medium':
        Health_condition='Very good'
    elif T_s =='Medium' and H_s =='Fair' and C_s=='Low' and C2_s=='Low':
        Health_condition='Medium'
    elif T_s =='High' and H_s =='Poor' and C_s=='High' and C2_s=='High':
        Health_condition='Bad and Dangerous'
    elif T_s =='High' and H_s =='Fair' and C_s=='Medium' and C2_s=='Medium':
        Health_condition='Medium'
    else:
        Health_condition='this condition not exist'
    return Health_condition
print('''
Temperature_condition :Low    and Humidity_condition : Good and Co_condition: Low and Co_condition:Low       >>>>Health_condition= Good
Temperature_condition :Medium and Humidity_condition : Fair and Co_condition: Medium and Co_condition:Medium >>>>Health_condition= Very good
Temperature_condition :Medium and Humidity_condition : Fair and Co_condition: Low and Co_condition:Low       >>>>Health_condition= Medium
Temperature_condition :High   and Humidity_condition : Poor and Co_condition: High and Co_condition:High     >>>>Health_condition= Bad and Dangerous
Temperature_condition :High   and Humidity_condition : Fair and Co_condition: Medium and Co_condition:Medium >>>>Health_condition= Medium
______________________________________________________________________________________________________________________________________________________
Temperature_condition : Low(0-15) Medium(16-30) High(31-45)
Humidity_condition    : Low(0-35) Medium(36-70) High(71-100)
Co_condition          : Low(0-35) Medium(36-70) High(71-100)
C2o_condition          : Low(0-35) Medium(36-70) High(71-100)
''')
while True:
    temp=input('put temperature range(0-45C) : ')
    try:
        temperature=int(temp)
        break
    except:
        print('plse enter number')

Temperature_static=Temperature(temperature)
print('Temperature_condition : ',Temperature_static)

while True:
    hum=input('put humidity rang(0-100) : ')
    try:
        humidity=int(hum)
        break
    except:
        print('plse enter number')
        
Humidity_static=Humidity(humidity)
print('Humidity_condition : ',Humidity_static)

while True:
    c=input('put CO rang(0-100) : ')
    try:
        co=int(c)
        break
    except:
        print('plse enter number')
Co_static=Co(co)
print('Co_condition : ',Co_static)

while True:
    c2=input('put CO2 rang(0-100) : ')
    try:
        co2=int(c2)
        break
    except:
        print('plse enter number')
Co2_static=Co2(co2)
print('Co2_condition : ',Co2_static)
Health=Health_condition(Temperature_static,Humidity_static,Co_static,Co2_static)
print('Health_condition : ',Health)
