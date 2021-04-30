import json
#------------------------------------------------#
# Claves
#
# 'CustomerID', 'CompanyName', 'ContactName',
# 'ContactTitle', 'Address', 'City', 'Region',
# 'PostalCode', 'Country', 'Phone', 'Fax'
#


def pintarCliente(client):

    print(f"CustomerID: {client['CustomerID']},\n"
          f"CompanyName: {client['CompanyName']},\n"
          f"ContactName: {client['ContactName']},\n"
          f"ContactTitle: {client['ContactTitle']},\n"
          f"Address: {client['Address']},\n"
          f"City: {client['City']},\n"
          f"PostalCode: {client['PostalCode']},\n"
          f"Country: {client['Country']},\n"
          f"Phone: {client['Phone']},\n"
          f"Fax: {client['Fax']}")


file = open('modulo05\\clientes.json', encoding='UTF-8')
data = file.read()
file.close()

clientes = json.loads(data)


print(len(clientes))
# Cod ANATR ANTON
cod = input("Dime el código del cliente: ").upper()
cliente = list(filter(lambda c: c['CustomerID'] == cod, clientes))

if len(cliente) == 0:
    print("No hay clientes.")
else:
    pintarCliente(cliente[0])
