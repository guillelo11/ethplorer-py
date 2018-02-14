from ethplorer.address import Address


call = Address(address='0x48c80f1f4d53d5951e5d5438b54cba84f29f32a5')
print(call.get_address_info())
print(call.get_address_history())
print(call.get_address_transactions())